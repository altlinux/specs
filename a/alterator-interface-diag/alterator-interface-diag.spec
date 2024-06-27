Name: alterator-interface-diag
Version: 0.1.3
Release: alt1

Summary: XML files for ru.basealt.alterator.diag interface
License: GPLv2+
Group: Other
Obsoletes: alterator-interface-diag1
URL: https://gitlab.basealt.space/alt/altrerator-interface-diag

BuildArch: noarch

Source0: %name-%version.tar

%description
XML files describing D-Bus interface ru.basealt.alterator.diag for ADT (Alt Diagnostic Tool).

%prep
%setup

%install
install -p -m 644 -D ru.basealt.alterator.diag1.xml %buildroot%_datadir/dbus-1/interfaces/ru.basealt.alterator.diag1.xml
install -p -m 644 -D ru.basealt.alterator.diag1.policy %buildroot%_datadir/polkit-1/actions/ru.basealt.alterator.diag1.policy

%files
%_datadir/dbus-1/interfaces/ru.basealt.alterator.diag1.xml
%_datadir/polkit-1/actions/ru.basealt.alterator.diag1.policy

%changelog
* Wed Jun 26 2024 Aleksey Saprunov <sav@altlinux.org> 0.1.3-alt1
- add interface spec

* Thu Mar 14 2024 Aleksey Saprunov <sav@altlinux.org> 0.1.2-alt2
- aligned with specification

* Thu Feb 15 2024 Aleksey Saprunov <sav@altlinux.org> 0.1.2-alt1
- add Report method

* Tue Nov 14 2023 Aleksey Saprunov <sav@altlinux.org> 0.1.1-alt2
- initial build
