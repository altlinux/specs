Name: psi-plus-l10n
Version: 0.16.287
Release: alt1

Summary: Translations for Psi+
License: GPLv2
Group: Networking/Instant messaging

Url: http://www.psi-plus.com/
Packager: Nazarov Denis <nenderus@altlinux.org>

# https://github.com/psi-plus/%name/archive/%version.tar.gz
Source: %name-%version.tar.gz

BuildArch: noarch

BuildPreReq: libqt4-devel

%description
Translations for Psi+

%prep
%setup

%build
lrelease-qt4 translations/*.ts

%install
%__mkdir_p %buildroot%_datadir/psi-plus
%__install -Dp -m 0644 translations/*.qm %buildroot%_datadir/psi-plus

%files
%doc AUTHORS COPYING ChangeLog README
%_datadir/psi-plus/*.qm

%changelog
* Mon Mar 03 2014 Nazarov Denis <nenderus@altlinux.org> 0.16.287-alt1
- Initial release for ALT Linux
