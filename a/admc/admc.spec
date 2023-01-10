%define _unpackaged_files_terminate_build 1

Name: admc
Version: 0.11.1
Release: alt1

Summary: Active Directory Management Center
License: GPLv3+
Group: Other
Url: https://github.com/altlinuxteam/admc

BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: qt5-base-devel
BuildRequires: qt5-tools-devel
#BuildRequires: catch2-devel
BuildRequires: cmake-modules

BuildRequires: samba-devel
BuildRequires: libldap-devel
BuildRequires: libsasl2-devel
BuildRequires: libsmbclient-devel
BuildRequires: qt5-base-common
BuildRequires: doxygen
BuildRequires: libuuid-devel
BuildRequires: libkrb5-devel

Requires: libsasl2
Requires: libsasl2-plugin-gssapi

Source0: %name-%version.tar

%package test
Summary: Tests for ADMC
Group: Other

%description
Active Directory Management Center (ADMC) is integrated complex tool implements
User and Computers and Group Policy Manager modules of Microsoft Remote Server
Administration Tools (RSAT).

%description test
Tests for ADMC

%prep
%setup -q

%build
%cmake -DCMAKE_INSTALL_LIBDIR=%_libdir
%cmake_build

%install
%cmake_install

%files
%doc README.md
%doc CHANGELOG.txt
%doc CHANGELOG_ru.txt
%_bindir/admc
%_libdir/libadldap.so
%_man1dir/admc*
%_datadir/applications/admc.desktop
%_iconsdir/hicolor/scalable/apps/admc.svg

%files test
%_libdir/libadmctest.so
%_bindir/admc_test_ad_interface
%_bindir/admc_test_ad_security
%_bindir/admc_test_unlock_edit
%_bindir/admc_test_upn_edit
%_bindir/admc_test_string_edit
%_bindir/admc_test_string_large_edit
%_bindir/admc_test_country_edit
%_bindir/admc_test_gplink
%_bindir/admc_test_select_base_widget
%_bindir/admc_test_filter_widget
%_bindir/admc_test_attributes_tab
%_bindir/admc_test_members_tab
%_bindir/admc_test_member_of_tab
%_bindir/admc_test_select_object_dialog
%_bindir/admc_test_logon_hours_dialog
%_bindir/admc_test_logon_computers_edit
%_bindir/admc_test_expiry_edit
%_bindir/admc_test_password_edit
%_bindir/admc_test_group_scope_edit
%_bindir/admc_test_group_type_edit
%_bindir/admc_test_datetime_edit
%_bindir/admc_test_manager_edit
%_bindir/admc_test_delegation_edit
%_bindir/admc_test_string_other_edit
%_bindir/admc_test_account_option_edit
%_bindir/admc_test_gpoptions_edit
%_bindir/admc_test_protect_deletion_edit
%_bindir/admc_test_octet_attribute_dialog
%_bindir/admc_test_bool_attribute_dialog
%_bindir/admc_test_datetime_attribute_dialog
%_bindir/admc_test_string_attribute_dialog
%_bindir/admc_test_number_attribute_dialog
%_bindir/admc_test_list_attribute_dialog
%_bindir/admc_test_edit_query_item_widget
%_bindir/admc_test_policy_results_widget
%_bindir/admc_test_policy_ou_results_widget
%_bindir/admc_test_find_object_dialog
%_bindir/admc_test_rename_object_dialog
%_bindir/admc_test_create_object_dialog
%_bindir/admc_test_select_classes_widget
%_bindir/admc_test_sam_name_edit
%_bindir/admc_test_dn_edit
%_bindir/admc_test_find_policy_dialog

%changelog
* Tue Jan 10 2023 Evgeny Sinelnikov <sin@altlinux.org> 0.11.1-alt1
- Fix property tabs size policy to looks more pretty.
- Enable both user and machine attributes during GPO creating.
- Fix availability of the Ok button when:
 + a policy name is missing in the policy create dialog;
 + group name is missing in the renaming ou dialog;
 + user name is missing in rename user dialog.

* Tue Dec 13 2022 Evgeny Sinelnikov <sin@altlinux.org> 0.11.0-alt1
- Action menu: Block inheritance feature is added to organizational
  unit context menu. Also limited group policy tab is returned.
- Console: Bug with empty group policy object crushing is fixed.
- Console: Non-deletable group policy containers dont dissapear
  from GUI after deletion attempt now. Warning message popups instead
  of error log dialog.
- Misc: "Order" column is added to policy organizational unit results.
  Sort is performed with this column by default.
- Console: Fix crash in policy tree after changing properties
  for organizational units.
- Misc: Fix description bar squishing scope pane, when selected
  item's name is too long and description bar needs to display it.
- Toolbar: Fix icons for "create" actions for organizational units,
  users and groups in toolbar.
- Misc: Add trimming to full name autofill.
- Misc: Add trimming to attribute sAMAccountName edit in create
  dialog for computers.
- Misc: Add "find gpo" action to policy tree. It implements group
  policy objects search functional.
- Misc: Improve "Import Query" action. So it's possible to
  import multiple queries at the same time.

* Mon Sep 12 2022 Alexey Shabalin <shaba@altlinux.org> 0.10.0-alt3
- Cleanup Requires and BuidRequires.

* Wed Sep 07 2022 Evgeny Sinelnikov <sin@altlinux.org> 0.10.0-alt2
- Build latest tested release.
- Adjust package summary and description.

* Thu Jun 30 2022 Dmitry Degtyarev <kevl@altlinux.org> 0.10.0-alt1
- Properties: Removed "Group tab". Not necessary because
  policy tree replaces it.
- Policies: Improved policy tree. Tree now contains OU's in
  addition to policies. OU's display their child OU's and
  linked policies. Viewing all policies is still possible in
  "All policies" folder.
- Misc: Fixed eliding of long items in scope view. Scope
  view now correctly displays a scroll bar so that long
  items can be viewed fully.
- Misc: Added trimming of spaces from names when creating or
  renaming policies, query folders and query items.
- Misc: Fixed a bug where object became unloaded if during
  rename character '?' was added to it's name.
- Misc: Increased size of editor for string attributes,
  which is available in "Attributes" tab. Long strings are
  now easier to view and edit.
- Misc: Removed ability to drag and drop policies onto OU's
  in object tree. This action now can be performed inside
  policy tree.

* Fri Apr 01 2022 Dmitry Degtyarev <kevl@altlinux.org> 0.9.0-alt1
- 0.9.0 (See CHANGELOG.txt for details)

* Thu Mar 31 2022 Dmitry Degtyarev <kevl@altlinux.org> 0.8.3-alt1
- 0.8.3 (See CHANGELOG.txt for details)
- Removed auto-generated changelog entry in .spec

* Thu Aug 05 2021 Dmitry Degtyarev <kevl@altlinux.org> 0.6.4-alt1
- 0.6.4
- closes: 40653
- closes: 40654

* Mon Aug 02 2021 Dmitry Degtyarev <kevl@altlinux.org> 0.6.3-alt1
- 0.6.3

* Thu Jul 29 2021 Dmitry Degtyarev <kevl@altlinux.org> 0.6.2-alt1
- 0.6.2 (closes: 40562)

* Tue Jul 20 2021 Dmitry Degtyarev <kevl@altlinux.org> 0.6.1-alt1
- 0.6.1

* Fri Jul 09 2021 Dmitry Degtyarev <kevl@altlinux.org> 0.6.0-alt1
- 0.6.0

* Mon Jun 21 2021 Dmitry Degtyarev <kevl@altlinux.org> 0.5.3-alt1
- 0.5.3

* Sun May 30 2021 Arseny Maslennikov <arseny@altlinux.org> 0.5.2-alt1.1
- NMU: spec: adapted to new cmake macros.

* Wed May 12 2021 Dmitry Degtyarev <kevl@altlinux.org> 0.5.2-alt1
- 0.5.2

* Fri Apr 23 2021 Dmitry Degtyarev <kevl@altlinux.org> 0.5.1-alt1
- 0.5.1

* Thu Apr 22 2021 Dmitry Degtyarev <kevl@altlinux.org> 0.5.0-alt1
- 0.5.0

* Tue Mar 02 2021 Dmitry Degtyarev <kevl@altlinux.org> 0.4.1-alt1
- 0.4.1

* Mon Feb 15 2021 Dmitry Degtyarev <kevl@altlinux.org> 0.4.0-alt1
- 0.4.0

* Sun Dec 27 2020 Alexey Shabalin <shaba@altlinux.org> 0.3.1-alt2
- Delete openldap package from requires.

* Tue Jul 28 2020 Dmitry Degtyarev <kevl@altlinux.org> 0.3.1-alt1
- Fixed login dialog closing app
- Fixed app sometimes segfaulting when reading ber format attributes

* Fri Jul 24 2020 Igor Chudov <nir@altlinux.org> 0.3.0-alt1
- Build ADMC for all architectures

* Fri Jul 24 2020 Igor Chudov <nir@altlinux.org> 0.2.0-alt1
- Translations added
- Logon dialog implemented
- libadldap improved
- Various UI improvements added

* Thu May 21 2020 Igor Chudov <nir@altlinux.org> 0.1.0-alt1
- Initial build
