Name: alterator-interface-service
Version: 0.1.1
Release: alt1

Summary: XML files for org.altlinux.alterator.service interface
License: GPLv2+
Group: Other
Obsoletes: alterator-interface-service1
URL: https://gitlab.basealt.space/alt/altrerator-interface-service

BuildArch: noarch

Source0: %name-%version.tar


%description
XML files describing D-Bus interface org.altlinux.alterator.service.

%prep
%setup

%install
install -p -m 644 -D org.altlinux.alterator.service1.xml %buildroot%_datadir/dbus-1/interfaces/org.altlinux.alterator.service1.xml
install -p -m 644 -D org.altlinux.alterator.service1.policy %buildroot%_datadir/polkit-1/actions/org.altlinux.alterator.service1.policy

%files
%_datadir/dbus-1/interfaces/org.altlinux.alterator.service1.xml
%_datadir/polkit-1/actions/org.altlinux.alterator.service1.policy

%changelog
* Mon Mar 10 2025 Aleksey Saprunov <sav@altlinux.org> 0.1.1-alt1
- add license and changelog

* Thu Dec 12 2024 Evgenii Sozonov <arzdez@altlinux.org> 0.1-alt1
- Initial build
