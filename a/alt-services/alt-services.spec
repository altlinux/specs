%define _unpackaged_files_terminate_build 1

Name: alt-services
Version: 0.1.11
Release: alt1
Provides: alterator-application-services
Obsoletes: alterator-application-services

Summary: Alterator application for managing services
License: GPLv2+
Group: System/Configuration/Other
URL: https://altlinux.space/alterator/alt-services

Source0: %name-%version.tar

BuildRequires(pre): rpm-macros-cmake
BuildRequires(pre): rpm-macros-alterator
BuildRequires(pre): rpm-build-kf6
BuildRequires: cmake extra-cmake-modules
BuildRequires: gcc-c++
BuildRequires: qt6-base-devel
BuildRequires: qt6-tools-devel
BuildRequires: qt6-base-common
BuildRequires: libtoml11-devel
BuildRequires: boost-devel-headers
BuildRequires: kf6-kwidgetsaddons-devel
BuildRequires: kf6-kitemmodels-devel
BuildRequires: kf6-kdbusaddons-devel
BuildRequires: kf6-kwindowsystem-devel
BuildRequires: librange-v3-devel

Requires: alterator-interface-service >= 0.2.1
Requires: alterator-interface-diag >= 0.1.4
Requires: alterator-manager >= 0.1.25
Requires: alterator-module-executor >= 0.1.14
Requires: alterator-entry >= 0.4.5

%description
GUI utility for alterator service management.

%prep
%setup

%build
%cmake
%cmake_build

%install
%cmakeinstall_std
install -v -p -m 644 -D data/org.altlinux.alt-services.desktop %buildroot%_desktopdir/org.altlinux.alt-services.desktop

mkdir -p %buildroot%_iconsdir/hicolor/scalable/apps
install -v -p -m 644 -D data/icons/org.altlinux.alt-services.svg %buildroot%_iconsdir/hicolor/scalable/apps

mkdir -p %buildroot%_datadir/alterator/applications
install -v -p -m 644 -D alterator/alt-services.application %buildroot%_datadir/alterator/applications

mkdir -p %buildroot%_datadir/alterator/backends
install -v -p -m 644 -D alterator/alt-services.backend %buildroot%_datadir/alterator/backends

%files
%_bindir/alt-services
%_desktopdir/org.altlinux.alt-services.desktop
%_datadir/alterator/applications/alt-services.application
%_datadir/alterator/backends/alt-services.backend
%doc *.md
%_K6dbus_srv/*.service
%_iconsdir/hicolor/*/*/*.svg

%changelog
* Thu Jan 15 2026 Maria Alexeeva <alxvmr@altlinux.org> 0.1.11-alt1
- Added:
  + app icon

* Fri Dec 26 2025 Maria Alexeeva <alxvmr@altlinux.org> 0.1.10-alt1
- Changed (thx Andrey Alekseev):
  + tables are now compact by default
  + resource values are now top-aligned
  + added word-wrap for tooltips
- Fixed (thx Andrey Alekseev):
  + html journal displayed with wrong encoding in some browsers
  + brought back forgotten menu items in mainwindow
  + validation messages blinking while changing enum parameters
  + application coud not raise its window on Wayland
  + process could continue when window is closed by user immediately after start
  + minor memory leaks
- Added (thx Andrey Alekseev):
  + --replace commandline option for replacing existing window

* Thu Dec 04 2025 Maria Alexeeva <alxvmr@altlinux.org> 0.1.9-alt1
- Added (thx Andrey Alekseev):
  + password confirmation
  + an ability of selectively ignoring diagnostic test errors
  + a text message, representing operation result, on the "Progress" page
- Changed (thx Andrey Alekseev):
  + improved wizard appearance and navigation
  + text log entries on "Progress" page are now collapsed by default
- Fixed (thx Andrey Alekseev):
  + handling diagnostic "warning" result
  + log entries on the "Progress" had their own scrollbars on gtk3
  + tool/test names were not localized inside log on "Progress" page

* Wed Nov 26 2025 Maria Alexeeva <alxvmr@altlinux.org> 0.1.8-alt1
- Fixed (thx Andrey Alekseev):
  + segmentation fault while editing parameters in table mode
  + "Copy"/"Select All" default actions not being displayed in Log Page context menu
  + "table mode" parameter editor was losing its scroll position while adding/removing parameters
  + optional parameter selection was only possible outside of table checkboxes

* Wed Oct 01 2025 Maria Alexeeva <alxvmr@altlinux.org> 0.1.7-alt1
- Fixed (thx Andrey Alekseev):
  + editors being opened on disabled items
  + margins in table mode
  + missing translations
  + "remove" button position in table mode
  + parameters selection page being skipped when parameters are incorrect
  + wizard could be closed during operation
  + missing icon on the start page of wizard
  + highlighting of disabled parameters
  + incorrect application name & icon in Gnome
  + incorrect text/background colors in some table cells
  + disabled checkboxes were drawn as active in "compact mode
  + "word wrap" option did not affect some table cells
  + "select all" & "clear" buttons were not working
  + diagnostic tools selection was not possible in keyboard-only naviggation
  + incorrect enum parameters processing
  + "Refresh" action not working
  + all actions are now properly disabled while another operation in progress
  + diagnostic will run all selected tests, even if some of them failed
- Changed (thx Andrey Alekseev and Oleg Chagaev):
  + updated to latest alterator-entry changes
  + preserve initial parameters order
  + text is no more elided inside table
  + error messages are now tracked for all actions
  + unified look and behaviour of all selectable items inside tables
  + important messages now have background color depending on message type
  + "force deploy" now allowes to ignore resource conflicts
  + "refresh all" option position in services table context menu
  + start & stop actions are now blocked until prefious call is finished
  + import/export file format
  + improved keyboard navigation
  + wizard's log page now displays entries hierarchically
- Added (thx Andrey Alekseev and Oleg Chagaev):
  + an option to put non-required parameters at the end of the list
  + an option to configure word wrap in tables
  + service's Status() debug output
  + service, diagnostic tools and test icons
  + overridable resource highlighting
  + array item prefixes
  + a table of resources with current owners on the start wizard page
  + check for unresolvable resource conflicts on the start wizard page
  + check for resource conflicts while validating parameters that are linked to resources
  + a warning message, when Status() returns a non-zero exit code
  + a search bar on the Parameters page of a wizard
  + ability to export journals
- Removed (thx Andrey Alekseev):
  + Start() & Stop() calls during Configure()
  + old resource conflict message

* Thu Jul 24 2025 Maria Alexeeva <alxvmr@altlinux.org> 0.1.6-alt1
- build with qt < 6.9 (thx Andrey Alekseev)

* Wed Jul 23 2025 Andrey Limachko <liannnix@altlinux.org> 0.1.5-alt1
- new version (thx Andrey Alekseev)

* Tue Jul 22 2025 Andrey Limachko <liannnix@altlinux.org> 0.1.4-alt1
- new version (thx Andrey Alekseev)

* Wed May 14 2025 Aleksey Saprunov <sav@altlinux.org> 0.1.3-alt1
- add tooltip in service table header
- service will not be displayed if any errors were encountered during parsing
- add role icons
- implement composite parameters and arrays
- implement deployment/configuration dialog
- implement start/stop methods
- add desktop file
- add force_deploy parameter
- changed parameter icon
- improved properties table
- resources are now displayed in groups
- various UI improvements

* Mon Mar 24 2025 Aleksey Saprunov <sav@altlinux.org> 0.1.2-alt1
- update interface by Andrey Alekseev <parovoz@altlinux.org>
- add search bar by Andrey Alekseev <parovoz@altlinux.org>

* Tue Mar 11 2025 Aleksey Saprunov <sav@altlinux.org> 0.1.1-alt1
- fix missing icon on some environments by Andrey Alekseev <parovoz@altlinux.org>
- small ui improvements by Andrey Alekseev <parovoz@altlinux.org>

* Sun Mar 09 2025 Aleksey Saprunov <sav@altlinux.org> 0.1.0-alt2
- fix main window title
- add .gitingnore

* Fri Mar 7 2025 Andrey Alekseev <parovoz@altlinux.org> 0.1.0-alt1
- initial build
