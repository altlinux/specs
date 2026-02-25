%define _unpackaged_files_terminate_build 1

%ifdef _priority_distbranch
%define altbranch %_priority_distbranch
%else
%define altbranch %(rpm --eval %%_priority_distbranch)
%endif
%if "%altbranch" == "%nil"
%define altbranch sisyphus
%endif

Name: admc
Version: 0.22.3
Release: alt2

Summary: Active Directory Management Center
License: GPLv3+
Group: Other
Url: https://github.com/altlinux/admc

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

%if "%altbranch" == "sisyphus" || "%altbranch" == "p11"
BuildRequires: libcng-dpapi-devel
BuildRequires: libgkdi-devel
%endif

Requires: libsasl2
Requires: libsasl2-plugin-gssapi
Requires: ad-integration-themes >= 3.0

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
%_bindir/admc_test_find_object_dialog
%_bindir/admc_test_rename_object_dialog
%_bindir/admc_test_create_object_dialog
%_bindir/admc_test_select_classes_widget
%_bindir/admc_test_sam_name_edit
%_bindir/admc_test_dn_edit
%_bindir/admc_test_find_policy_dialog

%changelog
* Sat Feb 21 2026 Evgeny Sinelnikov <sin@altlinux.org> 0.22.3-alt2
- Samba 4.22 compatibility update.
- Fixed project URL.

* Thu Nov 13 2025 Semyon Knyazev <samael@altlinux.org> 0.22.3-alt1
- Changed lockoutTime attribute from datetime to integer format. (closes: 49829)
- Disabled critical domain GPO deletion, remove warning dialog in favor
  of message logging, and update multi-policy deletion confirmation. (closes: 42235)
- Fixed blocked computer icon. (closes: 56740)

* Wed Oct 29 2025 Semyon Knyazev <samael@altlinux.org> 0.22.2-alt1
- Fixed "Telephones" tab Russian translations spelling. (closes: 54430)
- Fixed computer account reset confirmation Russian translations spelling.
  (closes: 54429)
- Fixed modal dialogs appearing behind main window on start. (closes: 54939)
- Changed selection behaviour in security permissions table. (closes: 54504)
- Added sAMAccountName filter to simple object search: the search will take
  the sAMAccountName into account.
- Added spaces check (required fields) for objects creation. (closes: 54372)
- Added FSMO capture table to domain info widget. Role can be captured by
  current domain controller with corresponding button in the table.

* Fri Oct 17 2025 Semyon Knyazev <samael@altlinux.org> 0.22.1-alt1
- Fixed frozen permission checkboxes in security tab.
- Fixed mixing of log message and principal in the status bar
  (log message length is limited).
- Fixed crash on LAPS tab usage.

* Wed Sep 03 2025 Semyon Knyazev <samael@altlinux.org> 0.22.0-alt1
- Fixed ADMC desktop icon view on GNOME.
- Changed domain info and computer icons in custom theme (AD-integration).
- Fixed empty custom icons theme on GNOME: GNOME theme is set as parent
  theme and will be displayed instead of custom theme.
- Set custom icon theme search in standard directories for themes.
- Icon search supplemented with symbolic names.
- Added logout for current user.
- Added credentials save option to authentication dialog. Credentials are
  located in /tmp/admc_uid*/ccaches/ directory.
- Added temporary credentials cleanup on application crash.
- Added "Show login window on startup" option. If this option is enabled,
  system/last credentials won't be used on startup.
- "Use system credentials" option has been moved from main window preferences
  to authentication dialog.
- Disabled main window closing when auth dialog closes on failed startup.
- Fixed broken column view restoration.
- Fixed broken "Action" main window menu.

* Fri Jun 20 2025 Semyon Knyazev <samael@altlinux.org> 0.21.0-alt1
- Added Kerberos authentication. Changing the principal (user) is available 
  via the "Change user" action in the "File" menu or by right-clicking the 
  current user in the bottom right corner. The connection error dialog at 
  startup has been replaced with an authentication dialog.
- Added the name of the applied password settings object to the "Account" tab
  in the user properties.
- Fixed missing policy links in the "Group Policy" tab of organizational units
  in the object tree. The redundant "Status" column has been removed.
- The password settings container has been duplicated at the top level of the tree
  for convenience.
- Increased the size of the toolbar icons.
- Removed the "Set Primary Group..." button from the "Groups" tab for group objects
  (not applicable to groups).
- Fixed an empty list of linked organizational units for newly created policies.
- Removed the ad-integration-line/duotone/color icon themes (they did not cover 
  some objects).
- Renamed the "AD-integration Kora" theme to "AD-integration".
- Redesigned the AD-integration theme.
- Fixed issues with displaying icons in the toolbar and the tree view.
- If core icons are missing in the system theme at startup, the AD-integration theme
  is selected by default.

* Tue Apr 08 2025 Semyon Knyazev <samael@altlinux.org> 0.20.0-alt2
- Update CMake version (thx to Vladimir Rubanov).

* Mon Mar 17 2025 Semyon Knyazev <samael@altlinux.org> 0.20.0-alt1
- Native LAPS (Local administrator password solution) 2023 has been implemented.
  The corresponding tab has been added to the properties of computer class
  objects where LAPS is enabled.

* Tue Mar 4 2025 Semyon Knyazev <samael@altlinux.org> 0.19.0-alt1
- Add action "Show descriptor in SDDL" in the "More" button menu in the
  security tab. Allows to display a security descriptor in SDDL format.
- Add a rollback of the previously applied security descriptor. The action
  "Rollback to the previous descriptor" is available in the menu of the "More"
  button in the security tab.
- Freezing was minimized when interacting with objects of group policy in a tree.
- Fixed changelog errors. (closes: 45839)
- Add middle name to the editable properties and dialogues of user creation.
  The middle name field can be displayed when creating with action "Settings"->
  "Show the middle name when creating."
- Add the copy action for the attribute's display values.
- Fixed optional attributes disappearance after "Reset" action in the attributes
  tab.
- Fixed the display of optional attributes msDS-User-Account-Control-Computed and
  msDS-User-Password-Expire-Time-Computed.

* Wed Dec 5 2024 Semyon Knyazev <samael@altlinux.org> 0.18.0-alt1
- Add custom permissions to security tab: create/delete child objects
  and read/write properties.
- Add delegation tasks to security tab. Delegation tasks represent
  common tasks from RSAT's delegation dialog.
- Extended rights are placed in a separate permissions tab.
- Generic and standard permissions are placed in the common permissions
  tab. Common permissions are supplemented by following: list contents,
  read/write all properties, delete, delete subtree, read permissions,
  modify permissions, modify owner, all validated writes and all extended
  rights.
- Add permissions scope selection to the security tab. Corresponding
  permissions can be applied to the target object, target and child objects,
  only to the child objects or to the child object with specific class.
  Delegation tasks are appliable only to target object.
- Changed permissions unsetting behavior: superior permission unsetting
  unsets all subordinate permissions too. For example, "Full control"
  unsetting unsets all other permissions.
- Fixed test fails, which were caused by arbitrary invalid domain controller
  selection.
- Add "Set/unset all" and "Edit" actions to the links tab in the policy OU
  widget. "Set/unset all" actions set/unset state (enforced/disabled, depending
  on column) for all linked policies. "Edit" action opens GPUI for policy editing.
  These actions can be triggered via context menu.

* Thu Dec 5 2024 Semyon Knyazev <samael@altlinux.org> 0.17.2-alt1
- Fixed lost site and DC info in domain info widget (child domain).
  (closes:52329)

* Wed Nov 6 2024 Semyon Knyazev <samael@altlinux.org> 0.17.1-alt1
- Fix crashing on child domains after context menu request.

* Wed Aug 21 2024 Semyon Knyazev <samael@altlinux.org> 0.17.0-alt1
- Add password settings object's creation/deletion/edition. Password
  Settings Container contains these objects and located in the System
  container (objects tree).
- Fix empty parentheses display in the domain info widget for undefined domain
  controller's version.
- Add the ability to view which groups a group is a member of.

* Mon Jul 30 2024 Semyon Knyazev <samael@altlinux.org> 0.16.4-alt1
- Samba 4.20 compatibility update. Fixed related errors with security
  descriptor manipulations. (closes: 50776)
- Fixed user creation incapability after Samba dependencies
  update. (closes: 50096)

* Tue May 15 2024 Semyon Knyazev <samael@altlinux.org> 0.16.3-alt1
- Fix crashes after OU/user creation attempts by users with
  corresponding delegated rights.

* Fri May 3 2024 Semyon Knyazev <samael@altlinux.org> 0.16.2-alt1
- Fix OU insufficient access for users with delegation. Users with
  delegated OU rights can do corresponding allowed actions. In particular,
  user/group creation/deletion, OU creation and policy (un)link.

* Tue Apr 16 2024 Semyon Knyazev <samael@altlinux.org> 0.16.1-alt1
- Fixed policy link deletion: OU's child link items are deleted from
tree after removal from policy widget. (closes: 49670)
- Update backend files for Samba 4.20 compatibility.
- Fix admin domain definition method.
- Fix crash after optional attributes load.
- Fix optional attribute display bugs with enabled LAPS.
- Fix crashing after domain object properties apply changes.

* Tue Feb 20 2024 Semyon Knyazev <samael@altlinux.org> 0.16.0-alt1
- Add drag&drop policy link order changing to links tab in the policy OU
  widget.
- Domain info widget: "Servers" items are removed from the tree and
  domain controller version is added.
- Add link state icons (enforced/disabled) to the links tab from the
  policy OU widget.
- Domain policy link broken deletion is fixed (the same links in other
  OUs were deleted instead of domain's link). (closes: 49385)
- Fix broken domain policy link icon changing: enforcing/disabling
  from policy widget changed another OU's the same policy link icon.
- Fix links duplication in policy OU widget's inheritance tab.
- Fixed user properties window resize.
- Add optional attributes loading. It can be performed via "Load
  optional attribute values" option checking (in the preferences menu)
  or with corresponding button in the attributes tab. (closes: 48817)
- Fixed not selected of any theme after ADMC start.

* Tue Jan 16 2024 Semyon Knyazev <samael@altlinux.org> 0.15.2-alt1
- Removed missing theme error log on first launch. (closes: 49043)

* Wed Dec 13 2023 Semyon Knyazev <samael@altlinux.org> 0.15.1-alt1
- Add icon theme selection. System theme is taken from /usr/share/icons
  dir, custom themes are taken from /usr/share/ad-integration dir
  by default. Theme dirs must have index.theme file to be included.
  Theme dirs can also be symlinks.
- Object creation and disabling bugs in 0.15.0 version are
  fixed. (closes: 48780)

* Fri Nov 17 2023 Valery Sinelnikov <greh@altlinux.org> 0.15.0-alt1
- Domain info root item is added to console tree. Its results widget
  contains tree with sites, domain controllers and FSMO role items. It
  also contains number of sites and domain controllers, forest and domain
  functional levels, domain schema version.
- Fixed bug with remaining failed connection options. Now after a failed
  connection attempt, the old connection settings are returned and
  connection options dialog doesnt close.
- GPO creation/renaming with only spaces bug fixed. (closes: 44684)
- Add group rename sam account name autofill. (closes: 47082)
- Add disabled computer icon. (closes: 47551)
- Add warning message for multiple object deletion and non-empty OU
  deletion.

* Tue Sep 05 2023 Valery Sinelnikov <greh@altlinux.org> 0.14.0-alt1
- Possible errors due to domain controller switching are fixed
  (revealed with failed tests).
- Disabled user icon is added to icon manager. Now user item icon
  changes after user disabling in the object tree and in the
  organizational unit results widget.
- User domain admin perms check for GPO add is fixed. User should no
  longer be in a group named only "Domain Admins" to be able add GPO
  (domain admins group is defined by sid now).
- Fixed group policy link dissapearence after applying enforce/disable
  action in context menu. (closes: 47122)
- Test admc_test_gplink is fixed.
- Test admc_test_policy_ou_results_widget is temporarily removed.
- Added connectivity to another domain's host.

* Mon Jul 17 2023 Valery Sinelnikov <greh@altlinux.org> 0.13.0-alt1
- PDC-Emulator check option is added. If option is enabled, GPT-related
  moves like policy editing/creation/deletion will be prevented under
  non-PDC-Emulator DC connection.
- Fixed group policy link order value in organizational unit's
  results widget: order was sorted as string number earlier.
  It is sorted as a number now.
- Organizational unit's inherited policies are added to corresponing
  tab in organizational unit's result widget. Also inherited policies
  list is added to organizational unit's properties group tab.
- Enforce and disable checkable actions are added to policy link item
  context menu (group policy objects).
- Fixed organizational unit and user rename ok buttons availability
  with spaces only.
- Crashing after drag and drop attempt in organizational unit's results
  widget is fixed: drag and drop is disabled.
- User and group general tab read-only widgets are added as results
  widgets for corresponding group and user items.
- creationTime attribute's value display/edit fixed.
- Time span attribute value display fixed. Also time span attribute
  edit is added.forceLogoff and lockOutObservationWindow attributes
  are added as time span.
- Attribute userAccountControl, msDs-Supported and systemFlags values
  are displayed as hexadecimal.
- Fixed group policy link appearing after an unauthorized creation
  attempt.

* Wed Mar 22 2023 Evgeny Sinelnikov <sin@altlinux.org> 0.12.0-alt1
- Indents at selected OU's widget with policies list are minimized.
- Ellipsis for too long names in description bar is added. Label is located to
  the right of the tree with chosen object. Tool tip for that label is added.
  Tool tip contains full object name.
- Attribute groupType display and edit are changed from decimal to hexadecimal.
  Attribute value also contains flag names that were set.
- Error dialog after critical policy selection is removed. Error is displayed
  in log now. Dialog error messages after critical policy deletion attempt are
  clarified.
- Russian language is removed from english logs and vice versa.
- Block inheritance indicator is added to OU's icon from group policy objects.
- Enforced link indicator is added to policy icon from group policy objects.
- Disabled policies appearence changing is added to policies from group policy
  objects. Policy item icon changes appearance (fades) after group policy link
  disabling.
- Policy link indicator is added to policy icon from group policy objects.
  Indicator is located in left bottom policy icon corner.
- Policies that are linked to domain is visible in group policy objects now.
- Group policy objects order is changed. Policies is placed higher than OUs now.

* Tue Jan 10 2023 Evgeny Sinelnikov <sin@altlinux.org> 0.11.2-alt1
- Fix race condition problems with AdInterface.

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
