## Models.
  **Patient's Model**
  Patient's Table
    * Name
    * Date of Birth
    * Phone Number
    * Gender
    * id_Number
    * Status
    * Email
    * Location
    * NHIF Number
    * Blood Group
    * Profile Photo
    * Doctor(Foreign Key to Doctor)
  # With Foreign Key to Other Tables
    * Next of Kin
    * Medications
    * Allergies and Directives
    * Medical Cover
  Next of Kin Table
    * Name
    * Relationship
    * Phone Number
    * Email
  Medications Table
    * Name of Medication,
    * Date Given
    * Status of Medication
    * Doctor that Administered(Foreign Key to Doctors Table)
  Allergies and Directives
    * Name of Allergy or Directive.
    * Level of Severity
  Medical Cover
    * Name of Insurer
    * Email of Insurer
    * Name of Cover

  **Doctor's Model**
    * Name
    * License Number
    * Specialty
    * Hospital(Foreign Key to Hospital)
    * Profile Photo

## User Specifications
* As a doctor you will be able to create an account and login.
* You will be able to search for patients based on their NHIF numbers.
* View patient's medical records.
* Administer treatment to the patients.
* Checkout to the patient's insurer or their selected mode of payment.
