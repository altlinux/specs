%define _unpackaged_files_terminate_build 1

Name: alt-components
Version: 0.6.3
Release: alt1

Summary: Alterator application for managing system components
License: GPLv2+
Group: System/Configuration/Other
URL: https://altlinux.space/alterator/alt-components

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake
BuildRequires: cmake-modules
BuildRequires: gcc-c++
BuildRequires: qt6-base-common
BuildRequires: qt6-base-devel
BuildRequires: qt6-declarative-devel
BuildRequires: qt6-tools-devel
BuildRequires: boost-devel-headers
BuildRequires: libqbase-devel >= 0.1.0-alt3
BuildRequires: libtomlplusplus-devel
BuildRequires: nlohmann-json-devel
BuildRequires: libexpected-devel
BuildRequires: alterator-entry >= 0.3.1

Requires: alterator-backend-packages >= 0.2.9-alt1
Requires: alterator-backend-component >= 0.3.0-alt1
Requires: alterator-backend-systeminfo
Requires: libqbase
Requires: alt-components-base >= 0.7.12-alt1

Provides: alterator-application-components = %version-%release
Obsoletes: alterator-application-components < 0.4.0

%description
Alterator application for managing system components.

%prep
%setup

%build
%cmake
%cmake_build

%install
%cmakeinstall_std

%check
find ./alterator/*.{object,application,backend} -type f -exec alterator-entry validate {} \+

%files
%_datadir/alterator/applications/*.application
%_datadir/alterator/backends/*.backend
%_datadir/alterator/objects/*.object
%_datadir/polkit-1/actions/*.policy
%_datadir/dbus-1/interfaces/*.xml
%_bindir/alt-components
%_desktopdir/*.desktop

%changelog
* Tue Oct 28 2025 Kirill Sharov <sheriffkorov@altlinux.org> 0.6.3-alt1
- Fix incorrect number of components after filtering for description,
  status bar and section/tag item of tree.
- Fix incorrect check state of category with filtered components.
- Fix filtered components included in transaction when clicking on
  a category.
- Change option for filtering components that not included in the
  edition in any view mode (instead "Other components" section in
  "By sections" view mode).

* Mon Oct 13 2025 Kirill Sharov <sheriffkorov@altlinux.org> 0.6.2-alt1
- Fix crash via date of last update initialization.

* Fri Oct 03 2025 Kirill Sharov <sheriffkorov@altlinux.org> 0.6.1-alt1
- Fix launch wihout displaying because of user locale.

* Fri Oct 03 2025 Kirill Sharov <sheriffkorov@altlinux.org> 0.6.0-alt1
- Add ability to sync with software sources (such as apt-get update)
  using application.
- Add option for hiding of "Other components" section with non edition
  components (thx Maria Alexeeva).
- Fix warnings when clicking on category in component tree.
- Fix missing display of kernel module components and packages in
  transaction.
- Fix crash after view mode switching if edition is not selected.
- Fix zero counter of components of edition when Plain view mode selected
  (thx Maria Alexeeva).
- Add desktop entry (thx Andrey Alekseev).

* Wed Sep 10 2025 Evgeny Sinelnikov <sin@altlinux.org> 0.5.4-alt2
- Fixed dependency on supported version of alt-components-base.

* Fri Aug 22 2025 Kirill Sharov <sheriffkorov@altlinux.org> 0.5.4-alt1
- Use alterator-interface-component 0.3.0.

* Wed Aug 20 2025 Kirill Sharov <sheriffkorov@altlinux.org> 0.5.3-alt1
- Fix setting of locale in D-Bus connection when starting.

* Fri Aug 08 2025 Kirill Sharov <sheriffkorov@altlinux.org> 0.5.2-alt1
- Fix build: add missing includings.

* Tue Jul 29 2025 Kirill Sharov <sheriffkorov@altlinux.org> 0.5.1-alt1
- Add caching of content of unapplied resolved transaction if content is
  not changed.
- Fix incorrect display of states of kernel module packages.
- Fix incorrect display of check boxes in tree after switching safe mode
  for base components.

* Wed Jul 23 2025 Kirill Sharov <sheriffkorov@altlinux.org> 0.5.0-alt1
- Change design for dialog of transaction like wizard.
- Add display of requested and resolved components and packages during
  application.
- Add display of specifical error if transaction contains manually installed
  packages or base components in safe mode.
- Add ability to retry a transaction in case of failure.
- Add name and ID combined view mode (Menu Bar -> View).
- Set safe mode for base section by default.
- Change display component display-names in wizard instead their
  identifiers.
- Fix updating the model if auth is failure.
- Fix incorrect checking date of last update.
- Fix expanding of top level after filtering.
- Fix opening transaction log before auth checking.
- Fix display of wrong number of installed components for categories
  during preparation of transaction.
- Fix reset of view mode after transaction.
- Fix graphical margins in windows.
- Fix background color for items in component tree (KDE).
- Fix l10n of log levels when language is changed (thx Oleg Chagaev).

* Tue Jul 01 2025 Maria Alexeeva <alxvmr@altlinux.org> 0.4.0-alt1
- Implement integrity preservation (Closes: #52837)
  By default, the ban on deleting packages installed manually is enabled.
  If the edition is installed on the system, you can optionally prohibit
  the removal of packages related to the basic components.
  Even if the ban on manually deleting installed packages is lifted, manually
  deleted packages will be highlighted in the transaction application window
- Add display progressbar during transaction (thx Andrey Alekseev).
- Rename package: alterator-application-components to alt-components.

* Tue Jun 17 2025 Kirill Sharov <sheriffkorov@altlinux.org> 0.3.1-alt1
- Fix incomplete package list in transaction.
- Add preprocessing of transactions with error indication.
- Add package and component count display after applying.
- Add hiding of empty views of packages and components.
- Merge views in one page separated by tabs after applying.
- Change brush of selection for categories to green/red diag pattern.
- Fix margin between views.
- Add clear button to search line.
- Disable package list in component content.
- Add hide/display content panel (thx Maria Alexeeva).

* Thu Jun 05 2025 Michael Chernigin <chernigin@altlinux.org> 0.3.0-alt1
- Add support for tags in components and editions.
- New view mode menu in view menu.
- Add icons to buttons in main window.
- Show components which will be installed and uninstalled.
- Keep sections and tags expanded after "Collapse all".

* Fri May 23 2025 Michael Chernigin <chernigin@altlinux.org> 0.2.10-alt1
- Update tree item background color based on check state.
- Add edition component count to status bar.
- Add component count to section item display name.
- Prepend description with a title.
- Show categories and sections components count in the description.
- Display description for categories.
- Show categories content on the right.

* Tue May 13 2025 Michael Chernigin <chernigin@altlinux.org> 0.2.9-alt1
- Show content of selected categories and sections instead of empty description.
- Display apply diff in columns.

* Tue May 06 2025 Michael Chernigin <chernigin@altlinux.org> 0.2.8-alt2
- Change URL to altlinux.space.

* Mon May 05 2025 Michael Chernigin <chernigin@altlinux.org> 0.2.8-alt1
- Merge two dialogs shown during the apply process into one.
- Go back to remove and install in separate apt transactions. This fixes some
  conflicts then trying to install and remove components at the same time.
- Add ctrl+f shortcut to focus search box.
- Fix duplicate error messages on apply.

* Sun Apr 20 2025 Michael Chernigin <chernigin@altlinux.org> 0.2.7-alt1
- Remove and install packages in a single apt transaciton.
- Show apt logs from backend on apply.
- Don't allow to close wait dialog mid apply.

* Mon Apr 07 2025 Michael Chernigin <chernigin@altlinux.org> 0.2.6-alt1
- Filter by DE, language and arch from systeminfo backend.

* Sun Mar 30 2025 Michael Chernigin <chernigin@altlinux.org> 0.2.5-alt1
- Add option to show/hide sections in View menu.
- Add exit action in File menu.

* Tue Mar 25 2025 Michael Chernigin <chernigin@altlinux.org> 0.2.4-alt1
- Rename Debug menu to Tools.
- Add option to show drafts in Tools menu.
- Add reload components action in File menu.
- Fix status for categories with only partially checked children.
- Get kernel flavour using systeminfo backend.

* Sun Mar 23 2025 Michael Chernigin <chernigin@altlinux.org> 0.2.3-alt1
- Filter packages in components by arch.
- Add kflavour as a suffix for packages marked with kernel_module.

* Mon Mar 17 2025 Michael Chernigin <chernigin@altlinux.org> 0.2.2-alt1
- Hide checkboxes of components with no packages.
- Rename binary to alt-components.
- Make links in descriptions clickable.
- Add support for draft components and categories.

* Thu Mar 08 2025 Michael Chernigin <chernigin@altlinux.org> 0.2.1-alt1
- Switch to sync batch dbus calls which reduces model build time.
- Enable window decorations for WaitDialog.
- Fix translation warnings when using english.

* Mon Feb 24 2025 Michael Chernigin <chernigin@altlinux.org> 0.2.0-alt1
- Move to qt6.
- Add sections. Use sections from edition if one is selected.
- Show current edition in status bar if selected.

* Mon Feb 17 2025 Michael Chernigin <chernigin@altlinux.org> 0.1.12-alt1
- Add UI warnings (thx Kozyrev Yuri)
- Add debug menu (thx Kozyrev Yuri)

* Wed Feb 05 2025 Michael Chernigin <chernigin@altlinux.org> 0.1.11-alt1
- Fix DBus timeout when applying changes.

* Mon Feb 03 2025 Michael Chernigin <chernigin@altlinux.org> 0.1.10-alt3
- Add alterator-backend-component and alterator-backend-component_categories to
  dependencies.

* Fri Jan 24 2025 Michael Chernigin <chernigin@altlinux.org> 0.1.10-alt2
- Enable %check on all arches.
- Add alt-components-base to dependencies.

* Fri Dec 27 2024 Michael Chernigin <chernigin@altlinux.org> 0.1.10-alt1
- Add welcome screen in description text box.
- Show packages install status in packages list.

* Mon Dec 23 2024 Michael Chernigin <chernigin@altlinux.org> 0.1.9-alt1
- Status bar now shows current build status.
- Add context menus for components tree and packages list.
- Display icons for components and categories.

* Thu Dec 19 2024 Michael Chernigin <chernigin@altlinux.org> 0.1.8-alt2
- Fixes for p10 build.

* Mon Dec 16 2024 Michael Chernigin <chernigin@altlinux.org> 0.1.8-alt1
- Fix tree sorting to work correctly while using translations.
- Add search for components and categories.
- Add packages list on the right side.
- Improve startup time.
- Fix showing nested categories.

* Fri Dec 13 2024 Michael Chernigin <chernigin@altlinux.org> 0.1.7-alt1
- Improve launching time by building model async.
- Add menubar and ability to change language at runtime (thx Kirill Sharov)

* Wed Dec 11 2024 Michael Chernigin <chernigin@altlinux.org> 0.1.6-alt1
- Switch components from ini to toml format.

* Fri Nov 15 2024 Michael Chernigin <chernigin@altlinux.org> 0.1.5-alt1
- Don't show default category if it's empty.
- Sort components and component categories in a given tree.
- Fix translations in components install dialog and enable qtbase translations.

* Tue Oct 22 2024 Michael Chernigin <chernigin@altlinux.org> 0.1.4-alt1
- Change prefix from ru.basealt to org.altlinux.

* Wed Sep 25 2024 Michael Chernigin <chernigin@altlinux.org> 0.1.3-alt1
- Now component description desappears on click on category.
- Remove redundant buttons.
- Improve logging.

* Mon Jul 23 2024 Michael Chernigin <chernigin@altlinux.org> 0.1.2-alt1
- Fix build on older gcc.

* Thu Mar 21 2024 Michael Chernigin <chernigin@altlinux.org> 0.1.1-alt1
- Add support for nested categories of components.
- Update logic to comply with new component status API.

* Thu Mar 21 2024 Michael Chernigin <chernigin@altlinux.org> 0.1.0-alt1
- Initial build.

