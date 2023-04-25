from . import domainresource

class AtHomeInVitroTestReport(domainresource.DomainResource):
    """ Information about an At-Home In-Vitro Test Report """

    resource_type = "At-Home In-Vitro Test Report"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties. 
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.sending_system_namespace = None
        self.sending_system_oid = None
        self.sending_facility_name = None
        self.sending_facilty_id = None
        self.sending_facility_id_type = None
        self.recieving_system_namespace = None
        self.recieving_system_oid = None
        self.recieving_facility_name = None
        self.recieving_facility_id = None

        self.datetimeofmessage = None
        self.software_vendor_oragnization = None
        self.software_certificate_version = None
        self.software_product_name = None
        self.software_binary_id = None
        self.software_install_date = None

        self.patient_id = None
        self.patient_id_assigner = None
        self.patient_last_name = None
        self.patient_first_name = None
        self.patient_middle_name = None
        self.patient_dob = None
        self.patient_sex = None
        self.patient_race_code = None
        self.patient_race_description = None
        self.patient_race_code_system = None
        self.patient_race_code_system_version = None
        self.patient_street_address = None
        self.patient_street_address_2 = None
        self.patient_city = None
        self.patient_zip_code = None
        self.patient_county = None
        self.patient_phone_telecom_equipment_code = None
        self.patient_email = None
        self.patient_phone_area_code = None
        self.patient_local_phone = None
        self.patient_ethnicity_code = None
        self.patient_ethnicity_description = None
        self.patient_ethnicity_code_system = None
        self.patient_ethnicity_code_system_version = None

        self.observation_result_date = None
        self.test_result_date_released = None
        self.result_status = None
        self.test_performed_code = None
        self.test_performed_description = None
        self.test_performed_system_version = None
        self.test_performed_code_system_version = None
        self.test_result_code = None
        self.test_result_description = None
        self.test_result_code_system = None
        self.test_result_status = None
        self.test_producer_id = None
        self.device_identifier = None
        self.test_analysis_date = None
        self.test_performing_organization_name = None

        self.test_performed_description = None
        self.test_performed_code_system = None
        self.test_performed_code_system_version = None
        self.test_result_code = None
        self.test_result_description = None
        self.test_result_code_system = None
        self.test_result_status = None
        self.test_producer_id = None
        self.device_identifier = None
        self.test_analysis_date = None
        self.test_performing_organization_name = None

        self.symptomatic_assessment_code = None
        self.symptomatic_assessment_code_description = None
        self.symptomatic_assessment_code_system = None
        self.symptomatic_assessment_code_system_version = None
        self.symptomatic_assessment_result = None
        self.symptomatic_assessment_performing_organization_name = None
        self.symptomatic_assessment_performing_organization_id_assigner_oid = None
        self.symptomatic_assessment_performing_organization_assigner_id_type = None
        self.symptomatic_assessment_performing_organization_id_type = None
        self.symptomatic_assessment_performing_organization_identifier = None
        self.symptomatic_assessment_performing_organization_street_address = None
        self.symptomatic_assessment_performing_organization_city = None
        self.symptomatic_assessment_performing_organization_state = None
        self.symptomatic_assessment_performing_organization_zip_code = None
        self.symptomatic_assessment_performing_organization_county = None
        self.symptomatic_assessment_observation_type = None

        self.set_id = None
        self.illness_onset_date_value_type = None
        self.illness_onset_date_code = None
        self.illness_onset_date_code_description = None
        self.illness_onset_date_code_system = None
        self.illness_onset_date_code_system_version = None
        self.illness_onset_date_result = None
        self.unit_code_system_version = None
        self.illness_onset_date_result_status = None
        self.specimen_id = None
        self.specimen_id_assigner_oid = None
        self.specimen_id_assigner_id_type = None
        self.specimen_type_code = None
        self.specimen_type_description = None
        self.specimen_type_code_system = None
        self.specimen_type_code_system_version = None
        self.specimen_collected_date = None
        
        self.organization_that_issues_the_udi_for_this_test = None
        self.expiration_date_of_the_test_kit = None
        self.lot_number_of_the_test_kit = None
        self.serial_number_of_the_test_kit = None

        def elementProperties(self):
            # TODO map all properties to acceptable values
            js = super(AtHomeInVitroTestReport).elementProperties()
            js.extend([
                ("sending_system_namespace", "sending_system_namespace", str, False, None, False),
                ("sending_system_oid", "sending_system_oid", str, False, None, False),
                ("sending_facility_name", "sending_facility_name", str, False, None, False),
                ("sending_facilty_id", "sending_facilty_id", str, False, None, False),
                ("sending_facility_id_type", "sending_facility_id_type", str, False, None, False),
                ("recieving_system_namespace", "recieving_system_namespace", str, False, None, False),
                ("recieving_system_oid", "recieving_system_oid", str, False, None, False),
                ("recieving_facility_name", "recieving_facility_name", str, False, None, False),
                ("recieving_facility_id", "recieving_facility_id", str, False, None, False),

                ("datetimeofmessage", "datetimeofmessage", str, False, None, False),
                ("software_vendor_oragnization", "software_vendor_oragnization", str, False, None, False),
                ("software_certificate_version", "software_certificate_version", str, False, None, False),
                ("software_product_name", "software_product_name", str, False, None, False),
                ("software_binary_id", "software_binary_id", str, False, None, False),
                ("software_install_date", "software_install_date", str, False, None, False),

                ("patient_id", "patient_id", str, False, None, False),
                ("patient_id_assigner", "patient_id_assigner", str, False, None, False),
                ("patient_last_name", "patient_last_name", str, False, None, False),
                ("patient_first_name", "patient_first_name", str, False, None, False),
                ("patient_middle_name", "patient_middle_name", str, False, None, False),
                ("patient_dob", "patient_dob", str, False, None, False),
                ("patient_sex", "patient_sex", str, False, None, False),
                ("patient_race_code", "patient_race_code", str, False, None, False),
                ("patient_race_description", "patient_race_description", str, False, None, False),
                ("patient_race_code_system", "patient_race_code_system", str, False, None, False),
                ("patient_race_code_system_version", "patient_race_code_system_version", str, False, None, False),
                ("patient_street_address", "patient_street_address", str, False, None, False),
                ("patient_street_address_2", "patient_street_address_2", str, False, None, False),
                ("patient_city", "patient_city", str, False, None, False),
                ("patient_zip_code", "patient_zip_code", str, False, None, False),
                ("patient_county", "patient_county", str, False, None, False),
                ("patient_phone_telecom_equipment_code", "patient_phone_telecom_equipment_code", str, False, None, False),
                ("patient_email", "patient_email", str, False, None, False),
                ("patient_phone_area_code", "patient_phone_area_code", str, False, None, False),
                ("patient_local_phone", "patient_local_phone", str, False, None, False),
                ("patient_ethnicity_code", "patient_ethnicity_code", str, False, None, False),
                ("patient_ethnicity_description", "patient_ethnicity_description", str, False, None, False),
                ("patient_ethnicity_code_system", "patient_ethnicity_code_system", str, False, None, False),
                ("patient_ethnicity_code_system_version", "patient_ethnicity_code_system_version", str, False, None, False),

                ("observation_result_date", "observation_result_date", str, False, None, False),
                ("test_result_date_released", "test_result_date_released", str, False, None, False),
                ("result_status", "result_status", str, False, None, False),
                ("test_performed_code", "test_performed_code", str, False, None, False),
                ("test_performed_description", "test_performed_description", str, False, None, False),
                ("test_performed_system_version", "test_performed_system_version", str, False, None, False),
                ("test_performed_code_system_version", "test_performed_code_system_version", str, False, None, False),
                ("test_result_code", "test_result_code", str, False, None, False),
                ("test_result_description", "test_result_description", str, False, None, False),
                ("test_result_code_system", "test_result_code_system", str, False, None, False),
                ("test_result_status", "test_result_status", str, False, None, False),
                ("test_producer_id", "test_producer_id", str, False, None, False),
                ("device_identifier", "device_identifier", str, False, None, False),
                ("test_analysis_date", "test_analysis_date", str, False, None, False),
                ("test_performing_organization_name", "test_performing_organization_name", str, False, None, False),

                ("symptomatic_assessment_code", "symptomatic_assessment_code", str, False, None, False),
                ("symptomatic_assessment_code_description", "symptomatic_assessment_code_description", str, False, None, False),
                ("symptomatic_assessment_code_system", "symptomatic_assessment_code_system", str, False, None, False),
                ("symptomatic_assessment_code_system_version", "symptomatic_assessment_code_system_version", str, False, None, False),
                ("symptomatic_assessment_result", "symptomatic_assessment_result", str, False, None, False),
                ("symptomatic_assessment_performing_organization_name", "symptomatic_assessment_performing_organization_name", str, False, None, False),
                ("symptomatic_assessment_performing_organization_id_assigner_oid", "symptomatic_assessment_performing_organization_id_assigner_oid", str, False, None, False),
                ("symptomatic_assessment_performing_organization_assigner_id_type", "symptomatic_assessment_performing_organization_assigner_id_type", str, False, None, False),
                ("symptomatic_assessment_performing_organization_id_type", "symptomatic_assessment_performing_organization_id_type", str, False, None, False),
                ("symptomatic_assessment_performing_organization_identifier", "symptomatic_assessment_performing_organization_identifier", str, False, None, False),
                ("symptomatic_assessment_performing_organization_street_address", "symptomatic_assessment_performing_organization_street_address", str, False, None, False),
                ("symptomatic_assessment_performing_organization_city", "symptomatic_assessment_performing_organization_city", str, False, None, False),
                ("symptomatic_assessment_performing_organization_state", "symptomatic_assessment_performing_organization_state", str, False, None, False),
                ("symptomatic_assessment_performing_organization_zip_code", "symptomatic_assessment_performing_organization_zip_code", str, False, None, False),
                ("symptomatic_assessment_performing_organization_county", "symptomatic_assessment_performing_organization_County", str, False, None, False),
                ("symptomatic_assessment_observation_type", "symptomatic_assessment_observation_type", str, False, None, False),

                ("set_id", "set_id", str, False, None, False),
                ("illness_onset_date_value_type", "illness_onset_date_value_type", str, False, None, False),
                ("illness_onset_date_code", "illness_onset_date_code", str, False, None, False),
                ("illness_onset_date_code_description", "illness_onset_date_code_description", str, False, None, False),
                ("illness_onset_date_code_system", "illness_onset_date_code_system", str, False, None, False),
                ("illness_onset_date_code_system_version", "illness_onset_date_code_system_version", str, False, None, False),
                ("illness_onset_date_result", "illness_onset_date_result", str, False, None, False),
                ("unit_code_system_version", "unit_code_system_version", str, False, None, False),
                ("illness_onset_date_result_status", "illness_onset_date_result_status", str, False, None, False),
                ("specimen_id", "specimen_id", str, False, None, False),
                ("specimen_id_assigner_oid", "specimen_id_assigner_oid", str, False, None, False),
                ("specimen_id_assigner_id_type", "specimen_id_assigner_id_type", str, False, None, False),
                ("specimen_type_code", "specimen_type_code", str, False, None, False),
                ("specimen_type_description", "specimen_type_description", str, False, None, False),
                ("specimen_type_code_system", "specimen_type_code_system", str, False, None, False),
                ("specimen_type_code_system_version", "specimen_type_code_system_version", str, False, None, False),
                ("specimen_collected_date", "specimen_collected_date", str, False, None, False),

                ("organization_that_issues_the_udi_for_this_test", "organization_that_issues_the_udi_for_this_test", str, False, None, False),
                ("expiration_date_of_the_test_kit", "expiration_date_of_the_test_kit", str, False, None, False),
                ("lot_number_of_the_test_kit", "lot_number_of_the_test_kit", str, False, None, False),
                ("serial_number_of_the_test_kit", "serial_number_of_the_test_kit", str, False, None, False)
            ])
            return js