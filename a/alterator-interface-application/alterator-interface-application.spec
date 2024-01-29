%define _unpackaged_files_terminate_build 1

Name: alterator-interface-application
Version: 0.1.1
Release: alt1

Summary: Local applications interface for alterator browser.
License: GPLv2+
Group: System/Configuration/Other
URL: https://gitlab.basealt.space/alt/alterator-interface-application

BuildArch: noarch

Source0: %name-%version.tar

%description
Local applications interface for alterator browser.

%prep
%setup

%install
mkdir -p %buildroot%_datadir/dbus-1/interfaces
mkdir -p %buildroot%_datadir/polkit-1/actions

install -v -p -m 644 -D ru.basealt.alterator.application.xml %buildroot%_datadir/dbus-1/interfaces
install -v -p -m 644 -D ru.basealt.alterator.application.policy %buildroot%_datadir/polkit-1/actions

%files
%_datadir/polkit-1/actions/ru.basealt.alterator.application.policy
%_datadir/dbus-1/interfaces/ru.basealt.alterator.application.xml

%changelog
* Mon Jan 29 2024 Evgeny Sinelnikov <sin@altlinux.org> 0.1.1-alt1
- first build for Sisyphus

* Tue Oct 24 2023 Aleksey Saprunov <sav@altlinux.org> 0.1.0-alt1
- initial build
