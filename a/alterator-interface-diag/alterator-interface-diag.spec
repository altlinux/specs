Name: alterator-interface-diag
Version: 0.1.4
Release: alt1

Summary: XML files for org.altlinux.alterator.diag interface
License: GPLv2+
Group: Other
Obsoletes: alterator-interface-diag1
URL: https://gitlab.basealt.space/alt/altrerator-interface-diag

BuildArch: noarch

Source0: %name-%version.tar

%description
XML files describing D-Bus interface org.altlinux.alterator.diag for ADT (Alt Diagnostic Tool).

%prep
%setup

%install
install -p -m 644 -D org.altlinux.alterator.diag1.xml %buildroot%_datadir/dbus-1/interfaces/org.altlinux.alterator.diag1.xml
install -p -m 644 -D org.altlinux.alterator.diag1.policy %buildroot%_datadir/polkit-1/actions/org.altlinux.alterator.diag1.policy

%files
%_datadir/dbus-1/interfaces/org.altlinux.alterator.diag1.xml
%_datadir/polkit-1/actions/org.altlinux.alterator.diag1.policy

%changelog
* Mon Oct 21 2024 Aleksey Saprunov <sav@altlinux.org> 0.1.4-alt1
- change prefix from ru.basealt to org.altlinux

* Wed Jun 26 2024 Aleksey Saprunov <sav@altlinux.org> 0.1.3-alt1
- add interface spec

* Thu Mar 14 2024 Aleksey Saprunov <sav@altlinux.org> 0.1.2-alt2
- aligned with specification

* Thu Feb 15 2024 Aleksey Saprunov <sav@altlinux.org> 0.1.2-alt1
- add Report method

* Tue Nov 14 2023 Aleksey Saprunov <sav@altlinux.org> 0.1.1-alt2
- initial build
