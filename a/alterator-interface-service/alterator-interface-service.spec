Name: alterator-interface-service
Version: 0.2.1
Release: alt2

Summary: XML files for org.altlinux.alterator.service interface
License: GPLv2+
Group: Other
Obsoletes: alterator-interface-service1
URL: https://altlinux.space/alterator/alterator-interface-service

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
* Mon Jul 07 2025 Evgenii Sozonov <arzdez@altlinux.org> 0.2.1-alt2
- Change URL

* Wed Jun 04 2025 Evgenii Sozonov <arzdez@altlinux.org> 0.2.1-alt1
- Removed stdout_strings from deploy and undeploy methods
- Edit docs

* Fri Apr 11 2025 Evgenii Sozonov <arzdez@altlinux.org> 0.2-alt1
- Supplemented the description of methods
- Add Configure method
- Add Stop method
- Add Start method
- Add signals
- Add interface description

* Tue Mar 24 2025 Aleksey Saprunov <sav@altlinux.org> 0.1.3-alt1
- fix CHANGELOG.md
- fix policy (thx Andrey Alekseev)

* Thu Mar 13 2025 Aleksey Saprunov <sav@altlinux.org> 0.1.2-alt1
- correct interface

* Mon Mar 10 2025 Aleksey Saprunov <sav@altlinux.org> 0.1.1-alt1
- add license and changelog

* Thu Dec 12 2024 Evgenii Sozonov <arzdez@altlinux.org> 0.1-alt1
- Initial build
