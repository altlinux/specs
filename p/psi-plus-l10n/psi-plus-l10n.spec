Name: psi-plus-l10n
Version: 1.2.107
Release: alt1

Summary: Translations for Psi+
License: GPLv2
Group: Networking/Instant messaging

Url: http://www.psi-plus.com/
Packager: Nazarov Denis <nenderus@altlinux.org>

# https://github.com/psi-plus/%name/archive/%version.tar.gz
Source: %name-%version.tar.gz

BuildArch: noarch

BuildPreReq: qt5-tools

Requires: psi-plus >= %version

%description
Translations for Psi+

%prep
%setup

%build
lrelease-qt5 translations/*.ts

%install
%__mkdir_p %buildroot%_datadir/psi-plus
%__install -Dp -m 0644 translations/*.qm %buildroot%_datadir/psi-plus

%files
%doc AUTHORS COPYING ChangeLog README
%dir %_datadir/psi-plus
%_datadir/psi-plus/*.qm

%changelog
* Tue Dec 05 2017 Oleg Solovyov <mcpain@altlinux.org> 1.2.107-alt1
- Version 1.2.107

* Tue Oct 17 2017 Oleg Solovyov <mcpain@altlinux.org> 1.2.98-alt1
- Version 1.2.98

* Mon Sep 25 2017 Oleg Solovyov <mcpain@altlinux.org> 1.2.79-alt1
- Version 1.2.79

* Mon Sep 11 2017 Oleg Solovyov <mcpain@altlinux.org> 1.2.71-alt1
- Version 1.2.71

* Wed Aug 30 2017 Oleg Solovyov <mcpain@altlinux.org> 1.2.39-alt1
- Version 1.2.39

* Mon Aug 07 2017 Oleg Solovyov <mcpain@altlinux.org> 1.2.28-alt1
- Version 1.2.28

* Thu Aug 03 2017 Oleg Solovyov <mcpain@altlinux.org> 1.2.27-alt1
- Version 1.2.27

* Fri Jul 28 2017 Oleg Solovyov <mcpain@altlinux.org> 1.2.12-alt3
- Version 1.2.12

* Tue Jul 25 2017 Oleg Solovyov <mcpain@altlinux.org> 1.0.133-alt3
- Update translations

* Tue Jul 18 2017 Oleg Solovyov <mcpain@altlinux.org> 1.0.133-alt2
- Build with Qt5

* Thu Jul 14 2017 Oleg Solovyov <mcpain@altlinux.org> 1.0.133-alt1
- Version 1.0.133

* Thu Jun 29 2017 Oleg Solovyov <mcpain@altlinux.org> 1.0.116-alt1
- Version 1.0.116

* Fri Dec 04 2015 Nazarov Denis <nenderus@altlinux.org> 0.16.475.1-alt0.M70T.1
- Build for branch t7

* Fri Dec 04 2015 Nazarov Denis <nenderus@altlinux.org> 0.16.475.1-alt1
- Version 0.16.475.1

* Fri Mar 07 2014 Nazarov Denis <nenderus@altlinux.org> 0.16.289-alt0.M70T.1
- Build for branch t7

* Fri Mar 07 2014 Nazarov Denis <nenderus@altlinux.org> 0.16.289-alt1
- Version 0.16.289

* Tue Mar 04 2014 Nazarov Denis <nenderus@altlinux.org> 0.16.287-alt0.M70T.1
- Build for branch t7

* Mon Mar 03 2014 Nazarov Denis <nenderus@altlinux.org> 0.16.287-alt1
- Initial release for ALT Linux
