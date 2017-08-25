# Lists of all tags used anywhere in the codebase
# Populated by hand, so don't be too surprised if something
# is missing

# Format: 'key': (is tag used with getBooleanTag, "some help text for admins")

# Any tag used with Tag.getTag(),
# or Tag.getBooleanTag() with no program argument
all_global_tags = {
    'teacherreg_custom_forms': (False, ""),
    'allow_global_restypes': (False, "Include global resource types in the options shown"),
    'splashinfo_choices': (False, ""),
    'full_group_name': (False, ""),
    'nearly_full_threshold': (False, ""),
    'splashinfo_siblingdiscount': (True, ""),
    'splashinfo_lunchsat': (True, ""),
    'splashinfo_lunchsun': (True, ""),
    'use_class_size_optimal': (True, ""),
    'teacherreg_difficulty_choices': (False, ""),
    'volunteer_tshirt_options': (False, ""),
    'volunteer_tshirt_type_selection': (False, ""),
    'volunteer_allow_comments': (False, ""),
    'min_available_timeslots': (False, ""),
    'availability_group_timeslots': (True, "Group timeslots into contiguous blocks in the availability interface (enabled by default, set to 'False' to disable)"),
    'group_phone_number': (False, ""),
    'finaid_form_fields': (False, ""),
    'onsite_classlist_min_refresh': (False, ""),
    'oktimes_collapse': (False, ""),
    'qsd_display_date_author': (False, ""),
    'current_theme_name': (False, ""),
    'prev_theme_customization': (False, ""),
    'current_theme_params': (False, ""),
    'theme_template_control': (False, ""),
    'current_theme_palette': (False, ""),
    'request_student_phonenum': (True, ""),
    'allow_change_grade_level': (False, ""),
    'show_studentrep_application': (False, ""),
    'show_student_tshirt_size_options': (False, ""),
    'show_student_vegetarianism_options': (False, ""),
    'show_student_graduation_years_not_grades': (True, ""),
    'ask_student_about_transportation_to_program': (False, ""),
    'student_medical_needs': (False, ""),
    'require_school_field': (True, ""),
    'teacherinfo_shirt_options': (False, ""),
    'teacherinfo_shirt_type_selection': (False, ""),
    'teacher_profile_hide_fields': (False, ""),
    'student_grade_options': (False, ""),
    'user_types': (False, ""),
    'studentinfo_shirt_options': (False, ""),
    'studentinfo_food_options': (False, ""),
    'student_profile_gender_field': (True, "Ask about student gender in profile"),
    'ask_about_duplicate_accounts': (True, "Before creating an account for an email address already in the database, ask if the user wants to log into an existing account instead"),
    'require_email_validation': (True, ""),
    'automatic_registration_redirect': (True, "If student/teacher registration is open for exactly one program, redirect to student registration after student account creation (enabled by default)"),
    'text_messages_to_students': (True, ""),
    'local_state': (False, ""),
    'grade_ranges': (False, "Replaces min and max grade options in teacher class reg with grade ranges, as specified by tag"),
}

# Any tag used with Tag.getProgramTag(),
# or Tag.getBooleanTag() with a program argument
all_program_tags = {
    'increment_default_grade_levels': (True, "Consider all students to be one grade level higher (useful for summer programs)"),
    'open_class_category': (False, "Class category used for open classes (classes for which students don't register in advance)"),
    'sibling_discount': (False, ""),
    'splashinfo_costs': (False, ""),
    'catalog_sort_fields': (False, ""),
    'teacherreg_hide_fields': (False, ""),
    'teacherreg_default_min_grade': (False, ""),
    'teacherreg_default_max_grade': (False, ""),
    'teacherreg_default_class_size_max': (False, ""),
    'stripe_settings': (False, ""),
    'learn_extraform_id': (False, ""),
    'teach_extraform_id': (False, ""),
    'donation_settings': (False, ""),
    'splashinfo_choices': (False, ""),
    'no_overlap_classes': (False, ""),
    'special_classroom_types': (False, ""),
    'collapse_full_classes': (True, ""),
    'friendly_times_with_date': (True, ""),
    'grade_range_popup': (True, ""),
    'quiz_form_id': (False, ""),
    'default_restypes': (False, ""),
    'cc_redirect': (False, ""),
    'teacherreg_help_text_duration': (False, ""),
    'teacherreg_help_text_class_size_max': (False, ""),
    'teacherreg_help_text_num_sections': (False, ""),
    'teacherreg_help_text_requested_room': (False, ""),
    'teacherreg_help_text_message_for_directors': (False, ""),
    'teacherreg_help_text_purchase_requests': (False, ""),
    'teacherreg_help_text_class_info': (False, ""),
    'teacherreg_label_duration': (False, ""),
    'teacherreg_label_class_size_max': (False, ""),
    'teacherreg_label_num_sections': (False, ""),
    'teacherreg_label_requested_room': (False, ""),
    'teacherreg_label_message_for_directors': (False, ""),
    'teacherreg_label_purchase_requests': (False, ""),
    'teacherreg_label_class_info': (False, ""),
    'display_registration_names': (False, ""),
    'program_size_by_grade': (False, ""),
    'studentschedule_show_empty_blocks': (True, ""),
    'student_lottery_run': (False, ""),
    'formstack_id': (False, ""),
    'formstack_viewkey': (False, ""),
    'num_stars': (False, "The preferred number of starred classes per timeslot for student two-phase registration"),
}
