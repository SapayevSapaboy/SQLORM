from django.contrib import admin
from .models import *

admin.site.register(EAcademicInformation)
admin.site.register(EAcademicInformationData)
admin.site.register(EAcademicInformationDataSubject)
admin.site.register(EAcademicRecord)
admin.site.register(EAdmin)
admin.site.register(EAdminGroup)
admin.site.register(EAdminMessage)
admin.site.register(EAdminMessageContact)
admin.site.register(EAdminMessageContactUser)
admin.site.register(EAdminMessageFolder)
admin.site.register(EAdminMessageItem)
admin.site.register(EAdminResource)
admin.site.register(EAdminRole)
admin.site.register(EAdminRoleResource)
admin.site.register(EAdminRoles)
admin.site.register(EAdmissionQuota)
admin.site.register(EAttendance)
admin.site.register(EAttendanceActivity)
admin.site.register(EAttendanceControl)

admin.site.register(EAttendanceSettingBorder)
admin.site.register(EAuditorium)
admin.site.register(EBankDetails)
admin.site.register(ECallSheet)
admin.site.register(ECertificateCommittee)
admin.site.register(ECertificateCommitteeMember)
admin.site.register(ECertificateCommitteeResult)
admin.site.register(ECirculationSheet)
admin.site.register(ECirculationSheetMeta)

admin.site.register(EContractPrice)
admin.site.register(EContractType)
admin.site.register(ECounter)

admin.site.register(ECriteriaTemplate)

admin.site.register(ECurriculum)
admin.site.register(ECurriculumSubject)
admin.site.register(ECurriculumSubjectDetail)
admin.site.register(ECurriculumSubjectExamType)
admin.site.register(ECurriculumSubjectResponsible)

admin.site.register(ECurriculumSubjectTopic)
admin.site.register(ECurriculumWeek)
admin.site.register(EDecree)

admin.site.register(EDecreeStudent)
admin.site.register(EDepartment)

admin.site.register(EDiplomaBlank)
admin.site.register(EDissertationDefense)
admin.site.register(EDoctorateStudent)

admin.site.register(EEducationYear)
admin.site.register(EEmployee)

admin.site.register(EEmployeeAcademicDegree)
admin.site.register(EEmployeeCompetition)
admin.site.register(EEmployeeForeign)

admin.site.register(EEmployeeMeta)

admin.site.register(EEmployeeProfessionalDevelopment)
admin.site.register(EEmployeeTraining)
admin.site.register(EExam)
admin.site.register(EExamExclude)

admin.site.register(EExamGroup)
admin.site.register(EExamQuestion)
admin.site.register(EExamStudent)
admin.site.register(EGraduateQualifyingWork)

admin.site.register(EGroup)

admin.site.register(EIncreasedContractCoefficient)


admin.site.register(EIndividualTrainingSubjectSchedule)
admin.site.register(EIndividualTrainingSubjectStudent)
admin.site.register(EIndividualTrainingSubjectTeacher)

admin.site.register(EInventory)
admin.site.register(EInventoryCategory)
admin.site.register(EMinimumWage)
admin.site.register(EPaidContractFee)
admin.site.register(EPerformance)
admin.site.register(EPerformanceControl)
admin.site.register(EProject)
admin.site.register(EProjectExecutor)
admin.site.register(EProjectMeta)
admin.site.register(EPublicationAuthorMeta)
admin.site.register(EPublicationCriteria)
admin.site.register(EPublicationMethodical)
admin.site.register(EPublicationProperty)
admin.site.register(EPublicationScientific)
admin.site.register(EQualification)
admin.site.register(ERetraining)

admin.site.register(ERetrainingExamSchedule)
admin.site.register(ERetrainingPerformance)
admin.site.register(ERetrainingPerformanceControl)
admin.site.register(ERetrainingStudent)
admin.site.register(ERetrainingSubject)
admin.site.register(ERetrainingSubjectGroup)
admin.site.register(ERetrainingSubjectGroupStudent)
admin.site.register(ERetrainingSubjectSchedule)

admin.site.register(EScientificPlatformCriteria)
admin.site.register(EScientificPlatformProfile)
admin.site.register(ESmsLog)
admin.site.register(ESpecialty)

admin.site.register(EStipendValue)
admin.site.register(EStudent)

admin.site.register(EStudentApiToken)
admin.site.register(EStudentAward)

admin.site.register(EStudentContract)
admin.site.register(EStudentContractInvoice)
admin.site.register(EStudentContractTemplate)
admin.site.register(EStudentContractType)

admin.site.register(EStudentData)
admin.site.register(EStudentDiploma)

admin.site.register(EStudentEmployment)
admin.site.register(EStudentExchange)

admin.site.register(EStudentGpa)
admin.site.register(EStudentGrade)
admin.site.register(EStudentMeta)

admin.site.register(EStudentOlympiad)

admin.site.register(EStudentPtt)
admin.site.register(EStudentPttSubject)

admin.site.register(EStudentReference)
admin.site.register(EStudentRefreshToken)

admin.site.register(EStudentScholarship)
admin.site.register(EStudentScholarshipMonth)
admin.site.register(EStudentSport)
admin.site.register(EStudentSubject)

admin.site.register(EStudentSubjectChoice)

admin.site.register(EStudentTaskActivity)
admin.site.register(ESubgroup)
admin.site.register(ESubjectExamSchedule)

admin.site.register(ESubjectFileResource)

admin.site.register(ESubjectResource)

admin.site.register(ESubjectResourceQuestion)

admin.site.register(ESubjectSchedule)

admin.site.register(ESubjectTask)
admin.site.register(ESubjectTaskStudent)

admin.site.register(ESystemClassifier)
admin.site.register(ESystemConfig)
admin.site.register(ESystemLog)
admin.site.register(ESystemLogin)
admin.site.register(ESystemMessage)
admin.site.register(ESystemMessageTranslation)
admin.site.register(ESystemSyncLog)
admin.site.register(ESystemSyncModel)
admin.site.register(ETranscriptSubject)
admin.site.register(EUniversity)

#hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh

admin.site.register(HAcademicDegree)
admin.site.register(HAcademicMobileType)
admin.site.register(HAcademicRank)
admin.site.register(HAcademicReason)
admin.site.register(HAccommodation)



admin.site.register(HAttendanceSetting)
admin.site.register(HAuditoriumType)
admin.site.register(HBachelorSpeciality)

admin.site.register(HBuilding)
admin.site.register(HCitizenshipType)
admin.site.register(HContractClass)
admin.site.register(HContractSummaType)
admin.site.register(HContractType)

admin.site.register(HCountry)
admin.site.register(HCourse)
admin.site.register(HDecreeType)
admin.site.register(HDeviceType)
admin.site.register(HDiplomBlankCategory)
admin.site.register(HDiplomBlankStatus)

admin.site.register(HDoctoralStudentType)
admin.site.register(HDoctorateStudentStatus)



admin.site.register(HEducationForm)
admin.site.register(HEducationType)
admin.site.register(HEducationWeekType)
admin.site.register(HEducationYear)


admin.site.register(HEmployeeType)
admin.site.register(HEmploymentForm)

admin.site.register(HEmploymentStaff)

admin.site.register(HExamFinish)
admin.site.register(HExamType)
admin.site.register(HExpelReason)

admin.site.register(HFinalExamType)
admin.site.register(HGender)

admin.site.register(HGradeType)
admin.site.register(HGraduateFieldsType)


admin.site.register(HGraduateInactiveType)
admin.site.register(HLanguage)
admin.site.register(HLessonPair)
admin.site.register(HLocality)
admin.site.register(HLocalityType)
admin.site.register(HMarkingSystem)



admin.site.register(HMasterSpeciality)
admin.site.register(HMethodicalPublicationType)
admin.site.register(HNationality)


admin.site.register(HOwnership)
admin.site.register(HPatientType)

admin.site.register(HPaymentForm)
admin.site.register(HProjectCurrency)

admin.site.register(HProjectExecutorType)
admin.site.register(HProjectType)
admin.site.register(HPublicationDatabase)
admin.site.register(HQualification)

admin.site.register(HRatingGrade)
admin.site.register(HScienceBranch)

admin.site.register(HScientificPlatform)
admin.site.register(HScientificPublicationType)
admin.site.register(HSemester)
admin.site.register(HSemestr)

admin.site.register(HSemestrType)
admin.site.register(HSoato)

admin.site.register(HSocialCategory)
admin.site.register(HSpecialityOrdinatura)

admin.site.register(HSportType)

admin.site.register(HStipendRate)

admin.site.register(HStructureType)


admin.site.register(HStudentLivingStatus)

admin.site.register(HStudentRoommateType)
admin.site.register(HStudentStatus)

admin.site.register(HStudentSuccess)

admin.site.register(HStudentType)

admin.site.register(HSubjectBlock)
admin.site.register(HSubjectGroup)
admin.site.register(HSubjectType)

admin.site.register(HTeacherPositionType)
admin.site.register(HTeacherStatus)
admin.site.register(HTeacherSuccess)
admin.site.register(HTrainingType)


admin.site.register(HUniversity)
admin.site.register(HUniversityForm)

admin.site.register(Migration)

admin.site.register(RContract)
admin.site.register(REmployment)

