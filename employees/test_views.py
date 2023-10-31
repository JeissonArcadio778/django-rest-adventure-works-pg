from rest_framework.test import APITestCase
from rest_framework import status
from employees.models import Employee


class EmployeeViewsTestCase(APITestCase):
    @classmethod
    def setUpTestData(cls):
        Employee.objects.create(
            businessentityid=1,
            nationalidnumber="295847284",
            loginid="adventure-works\\ken0",
            jobtitle="Chief Executive Officer",
            birthdate="1969-01-29",
            maritalstatus="S",
            gender="M",
            hiredate="2009-01-14",
            salariedflag=True,
            vacationhours=99,
            sickleavehours=69,
            currentflag=True,
            rowguid="f01251e5-96a3-448d-981e-0f99d789110d",
            modifieddate="2014-06-30 00:00:00",
            organizationnode="/",
        )

        Employee.objects.create(
            businessentityid=2,
            nationalidnumber="295847281",
            loginid="adventure-works\\terri0",
            jobtitle="Chief Executive SubOfficer",
            birthdate="1969-01-29",
            maritalstatus="S",
            gender="M",
            hiredate="2009-01-14",
            salariedflag=True,
            vacationhours=99,
            sickleavehours=69,
            currentflag=True,
            rowguid="f01251e5-96a3-448d-981e-0f99d789110d",
            modifieddate="2014-06-30 00:00:00",
            organizationnode="/1/",
        )

        Employee.objects.create(
            businessentityid=3,
            nationalidnumber="295847282",
            loginid="adventure-works\\roberto0",
            jobtitle="Chief Executive SubSubOfficer",
            birthdate="1969-01-29",
            maritalstatus="S",
            gender="M",
            hiredate="2009-01-14",
            salariedflag=True,
            vacationhours=99,
            sickleavehours=69,
            currentflag=True,
            rowguid="f01251e5-96a3-448d-981e-0f99d789110d",
            modifieddate="2014-06-30 00:00:00",
            organizationnode="/1/1/",
        )

    def test_list_managers(self):
        response = self.client.get("/api/managers/")

        self.assertEqual(response.status_code, status.HTTP_200_OK, response.data)

        # Verificar que ken0 (CEO) y terri0 (VP de Ingeniería) están en la lista de managers
        managers_logins = [employee["loginid"] for employee in response.data]
        self.assertIn("adventure-works\\ken0", managers_logins)
        self.assertIn("adventure-works\\terri0", managers_logins)

    def test_list_subordinates_of_terri0(self):
        # terri0 (VP de Ingeniería) tiene businessentityid = 2
        response = self.client.get("/api/managers/2/subordinates/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        subordinates_logins = [employee["loginid"] for employee in response.data]
        self.assertIn("adventure-works\\roberto0", subordinates_logins)

    def test_manager_without_subordinates(self):
        # Imagina que el empleado con ID 10 es un manager sin subordinados
        response = self.client.get("/api/managers/10/subordinates/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 0)  # Asegurar que la respuesta está vacía

    def test_invalid_manager_id(self):
        # Imagina que no hay empleado con ID 9999
        response = self.client.get("/api/managers/9999/subordinates/")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
