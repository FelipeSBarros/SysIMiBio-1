from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.test import TestCase

from sysimibio.imibio_tree_ecological_data.models import FieldWork, Tree, PermanentParcel, TreeMeasurement


class TreeMeasurementTest(TestCase):
    def setUp(self):
        self.coordinator = User.objects.create_user('Florencia', 'flor@imibio.com', 'florpassword')
        self.staff = User.objects.create_user('Francisco', 'fran@imibio.com', 'fanpassword')
        self.parcel1 = PermanentParcel.objects.create(name='Nombre test',
                                                      coordinator=self.coordinator,
                                                      province='Misiones',
                                                      municipality='Puerto Iguazu',
                                                      locality='600 ha', obs='Observacion', latitude=-26, longitude=-56,
                                                      geom='')
        self.field = FieldWork.objects.create(
            date='2020-12-30',
            start_time='0:0',
            end_time='0:30',
            temperature=35.9,
            humidity=80,
            coordinator=self.coordinator,
            parcel_id=self.parcel1
        )
        self.field.staff.add(self.staff)

        self.tree = Tree.objects.create(
            field=self.field,
            subplot='A1',
            tree_number=3,
            specie='Solanaceae',
            latitude=-26,
            longitude=-54,
            obs='Teste 1')

        self.valid_measurement = TreeMeasurement(
            field=self.field,
            tree=self.tree,
            dap=11,
            dab=20,
            tree_height=3,
            phytosanitary_status='Bueno',
            sociological_classification='Emergente'
        )

    def test_tree_measurement_exists(self):
        self.valid_measurement.save()
        self.assertTrue(TreeMeasurement.objects.exists())

    def test_sociologicalclassification_Dominante(self):
        self.valid_measurement.sociological_classification = 'Dominante'
        self.assertEqual(None, self.valid_measurement.clean_fields())

    def test_sociologicalclassification_Codominante(self):
        self.valid_measurement.sociological_classification = 'Codominante'
        self.assertEqual(None, self.valid_measurement.clean_fields())

    def test_sociologicalclassification_Intermedia(self):
        self.valid_measurement.sociological_classification = 'Intermedia'
        self.assertEqual(None, self.valid_measurement.clean_fields())

    def test_sociologicalclassification_Inferior_suprimido(self):
        self.valid_measurement.sociological_classification = 'Inferior suprimido'
        self.assertEqual(None, self.valid_measurement.clean_fields())

    def test_sociologicalclassification_Inferior_sumergido(self):
        self.valid_measurement.sociological_classification = 'Inferior sumergido'
        self.assertEqual(None, self.valid_measurement.clean_fields())

    def test_sociologicalclassification_CHOICES(self):
        self.valid_measurement.phytosanitary_status = 'Bad sociological classification'
        msg = "Valor 'Bad sociological classification' no es una opción válida"
        with self.assertRaisesMessage(ValidationError, msg):
            self.valid_measurement.full_clean()

    def test_phytosanitary_Regular(self):
        self.valid_measurement.phytosanitary_status = 'Regular'
        self.assertEqual(None, self.valid_measurement.clean_fields())

    def test_phytosanitary_Malo(self):
        self.valid_measurement.phytosanitary_status = 'Malo'
        self.assertEqual(None, self.valid_measurement.clean_fields())

    def test_phytosanitary_Muerto(self):
        self.valid_measurement.phytosanitary_status = 'Muerto'
        self.assertEqual(None, self.valid_measurement.clean_fields())

    def test_phytosanitary_CHOICES(self):
        """"Sociological classification mus be limited by choices"""
        self.valid_measurement.phytosanitary_status = 'BAD phytosanitary classification'
        msg = "Valor 'BAD phytosanitary classification' no es una opción válida"
        with self.assertRaisesMessage(ValidationError, msg):
            self.valid_measurement.full_clean()

    def test_min_tree_height(self):
        self.valid_measurement.tree_height = 1.29
        msg = "Altura del árbol no puede ser menor a 1.3 metros"
        with self.assertRaisesMessage(ValidationError, msg):
            self.valid_measurement.full_clean()

    def test_min_tree_dap(self):
        self.valid_measurement.dap = 9
        msg = "DAP del árbol debe ser mayor a 10 cm"
        with self.assertRaisesMessage(ValidationError, msg):
            self.valid_measurement.full_clean()

    def test_str(self):
        """measurement string must be tree_id + field work date"""
        self.assertEqual('NTA13; 2020-12-30', str(self.valid_measurement))
