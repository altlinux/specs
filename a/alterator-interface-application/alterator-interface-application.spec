%define _unpackaged_files_terminate_build 1

Name: alterator-interface-application
Version: 0.1.1
Release: alt4

Summary: Local applications interface for alterator browser.
License: GPLv2+
Group: System/Configuration/Other
URL: https://altlinux.space/alterator/alterator-interface-application

BuildArch: noarch

Source0: %name-%version.tar

%description
Local applications interface for alterator browser.

%prep
%setup

%install
mkdir -p %buildroot%_datadir/dbus-1/interfaces
mkdir -p %buildroot%_datadir/polkit-1/actions

install -v -p -m 644 -D org.altlinux.alterator.application.xml %buildroot%_datadir/dbus-1/interfaces
install -v -p -m 644 -D org.altlinux.alterator.application.policy %buildroot%_datadir/polkit-1/actions

%files
%_datadir/polkit-1/actions/org.altlinux.alterator.application.policy
%_datadir/dbus-1/interfaces/org.altlinux.alterator.application.xml

%changelog
* Mon Jul 07 2025 Kirill Sharov <sheriffkorov@altlinux.org> 0.1.1-alt4
- actualize URL of repository

* Mon Oct 21 2024 Aleksey Saprunov <sav@altlinux.org> 0.1.1-alt3
- change prefix from ru.basealt to org.altlinux

* Tue Apr 02 2024 Aleksey Saprunov <sav@altlinux.org> 0.1.1-alt2
- added versions to interfaces

* Mon Jan 29 2024 Evgeny Sinelnikov <sin@altlinux.org> 0.1.1-alt1
- first build for Sisyphus

* Tue Oct 24 2023 Aleksey Saprunov <sav@altlinux.org> 0.1.0-alt1
- initial build
