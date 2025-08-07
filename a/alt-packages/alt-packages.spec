%define _unpackaged_files_terminate_build 1

Name: alt-packages
Version: 0.3.5
Release: alt1

Summary: ALT Packages - Alterator application for managing system packages and package repositories
License: GPLv2+
Group: System/Configuration/Other
URL: https://altlinux.space/alterator/alt-packages

Source0: %name-%version.tar

BuildRequires(pre): rpm-macros-alterator
BuildRequires(pre): rpm-macros-cmake

BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: qt6-base-common qt6-base-devel qt6-tools-devel
BuildRequires: nlohmann-json-devel

Requires: alterator-backend-packages >= 0.2.7
Requires: alterator-manager >= 0.1.25
Requires: alterator-module-executor >= 0.1.14

Provides: alterator-application-packages = %version-%release
Obsoletes: alterator-application-packages < 0.3.3

%description
ALT Packages - Alterator application for managing system packages
and package repositories through apt and rpm.

%prep
%setup

%build
%cmake
%cmake_build

%install
%cmakeinstall_std

%files
%doc LICENSE CHANGELOG.md
%_bindir/*
%dir %_alterator_datadir/backends
%dir %_alterator_datadir/applications
%_alterator_datadir/backends/*.backend
%_alterator_datadir/applications/*.application
%_desktopdir/*.desktop

%changelog
* Tue Aug 05 2025 Kirill Sharov <sheriffkorov@altlinux.org> 0.3.5-alt1
- Add progress indicator while waiting (thx Oleg Chagaev).

* Wed Jul 23 2025 Kirill Sharov <sheriffkorov@altlinux.org> 0.3.4-alt1
- Fix lack of removal of packages.
- Add option to disable safe mode.

* Fri Jul 11 2025 Kirill Sharov <sheriffkorov@altlinux.org> 0.3.3-alt1
- Added:
  + Safe mode from newest backend (APT).
  + Hiding empty package views in applying dialog (closes: #53759).
- Changed:
  + APT Transaction applying dialog replaced to dialog with scrollable
    package list (closes: #54034).
- Fixed:
  + Suggestion when upgrading if package list on transaction is empty.
    In this case, user gets a notification.
- Spec:
  + Fix description.
  + Remove unused build requirements.
  + Rename package to alt-packages with providing.

* Fri Apr 25 2025 Aleksey Saprunov <sav@altlinux.org> 0.3.2-alt1
- Fix deletion of update sources
- Fix dialog closing after package list update
- Bump required backend version
- Add rpm action messages

* Fri Apr 25 2025 Evgeny Sinelnikov <sin@altlinux.org> 0.3.1-alt1
- Clean not needed BuildRequires.
- Fix APT check for last update from /var/log/alterator/apt/updates.log
  (got from LastUpdate method on org.altlinux.alterator.apt1 interface)

* Fri Apr 18 2025 Kirill Sharov <sheriffkorov@altlinux.org> 0.3.0-alt1
- Added:
  + Filter by Group (RPM).
  + Filter by Arch (RPM).
- Changed:
  + Version & Release columns has been merged to Version-Release
    single column (RPM).
  + Repo Type column has been renamed to Type (Repo).
  + Branch column has been renamed to Sign (Repo).
  + Upgrade All button has been retranslated (APT).
- Fixed:
  + Alignment of packages list on applying transaction (APT).

* Mon Apr 14 2025 Kirill Sharov <sheriffkorov@altlinux.org> 0.2.0-alt1
- Add APT transaction progress.
- Add suggestion to update if last update date is not found.
- Add displaying an actual packages list of APT transaction.
- Add Upgrade All button for upgrading an all obsoleted packages.
- Change application name to ALT Packages.
- Fix broken Update.
- Fix selection resetting if filter is changed.

* Tue Feb 25 2025 Kirill Sharov <sheriffkorov@altlinux.org> 0.1.5-alt1
- New version.

* Mon Dec 09 2024 Aleksey Saprunov <sav@altlinux.org> 0.1.4-alt1
- Fix broken updating of packages list.
- Add waiting dialog.
- Change alterator entries format from ini to toml.

* Tue Oct 22 2024 Michael Chernigin <chernigin@altlinux.org> 0.1.3-alt1
- Change prefix from ru.basealt to org.altlinux.

* Wed Sep 25 2024 Michael Chernigin <chernigin@altlinux.org> 0.1.2-alt1
- Add dialog if update has not been done for a while.
- Fixed incorrect package selection in on apt page.
- Make search field snappier by doing search only on button press.
- Remove exit button in favor of window decorations button.
- Improve translations.

* Thu Jul 11 2024 Michael Chernigin <chernigin@altlinux.org> 0.1.1-alt1
- Cache apt page, so it takes less time to load after first try.
- Show package info as a table instead of plain text.

* Mon Feb 26 2024 Michael Chernigin <chernigin@altlinux.org> 0.1.0-alt1
- Initial build.
