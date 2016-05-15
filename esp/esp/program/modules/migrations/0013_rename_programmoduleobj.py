# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('program', '0006_classsubject_timestamp'),
        ('modules', '0012_auto_20160212_1903'),
    ]

    operations = [
        migrations.DeleteModel(name='AdminClass'),
        migrations.DeleteModel(name='AdminCore'),
        migrations.DeleteModel(name='AdminMaterials'),
        migrations.DeleteModel(name='AdminMorph'),
        migrations.DeleteModel(name='AdminReviewApps'),
        migrations.DeleteModel(name='AdminVitals'),
        migrations.DeleteModel(name='AdmissionsDashboard'),
        migrations.DeleteModel(name='AJAXSchedulingModule'),
        migrations.DeleteModel(name='AvailabilityModule'),
        migrations.DeleteModel(name='BigBoardModule'),
        migrations.DeleteModel(name='ClassChangeRequestModule'),
        migrations.DeleteModel(name='ClassFlagModule'),
        migrations.DeleteModel(name='ClassSearchModule'),
        migrations.DeleteModel(name='CommModule'),
        migrations.DeleteModel(name='CreditCardModule_Cybersource'),
        migrations.DeleteModel(name='CreditCardModule_Stripe'),
        migrations.DeleteModel(name='CreditCardViewer_Cybersource'),
        migrations.DeleteModel(name='CustomFormModule'),
        migrations.DeleteModel(name='DonationModule'),
        migrations.DeleteModel(name='FinancialAidAppModule'),
        migrations.DeleteModel(name='FormstackAppModule'),
        migrations.DeleteModel(name='FormstackMedliabModule'),
        migrations.DeleteModel(name='GroupTextModule'),
        migrations.DeleteModel(name='JSONDataModule'),
        migrations.DeleteModel(name='ListGenModule'),
        migrations.DeleteModel(name='LotteryStudentRegModule'),
        migrations.DeleteModel(name='MailingLabels'),
        migrations.DeleteModel(name='NameTagModule'),
        migrations.DeleteModel(name='OnSiteCheckinModule'),
        migrations.DeleteModel(name='OnSiteClassList'),
        migrations.DeleteModel(name='OnsiteClassSchedule'),
        migrations.DeleteModel(name='OnsiteCore'),
        migrations.DeleteModel(name='OnsitePaidItemsModule'),
        migrations.DeleteModel(name='OnsitePrintSchedules'),
        migrations.DeleteModel(name='OnSiteRegister'),
        migrations.DeleteModel(name='ProgramPrintables'),
        migrations.DeleteModel(name='RegProfileModule'),
        migrations.DeleteModel(name='ResourceModule'),
        migrations.DeleteModel(name='SchedulingCheckModule'),
        migrations.DeleteModel(name='SplashInfoModule'),
        migrations.DeleteModel(name='StudentClassRegModule'),
        migrations.DeleteModel(name='StudentExtraCosts'),
        migrations.DeleteModel(name='StudentJunctionAppModule'),
        migrations.DeleteModel(name='StudentLunchSelection'),
        migrations.DeleteModel(name='StudentRegConfirm'),
        migrations.DeleteModel(name='StudentRegCore'),
        migrations.DeleteModel(name='StudentRegTwoPhase'),
        migrations.DeleteModel(name='SurveyManagement'),
        migrations.DeleteModel(name='SurveyModule'),
        migrations.DeleteModel(name='TeacherAcknowledgementModule'),
        migrations.DeleteModel(name='TeacherBioModule'),
        migrations.DeleteModel(name='TeacherCheckinModule'),
        migrations.DeleteModel(name='TeacherClassRegModule'),
        migrations.DeleteModel(name='TeacherEventsModule'),
        migrations.DeleteModel(name='TeacherPreviewModule'),
        migrations.DeleteModel(name='TeacherQuizModule'),
        migrations.DeleteModel(name='TeacherRegCore'),
        migrations.DeleteModel(name='TeacherReviewApps'),
        migrations.DeleteModel(name='TextMessageModule'),
        migrations.DeleteModel(name='VolunteerManage'),
        migrations.DeleteModel(name='VolunteerSignup'),
        migrations.RenameModel('ProgramModuleObj', 'ProgramModuleSettings'),
    ]
