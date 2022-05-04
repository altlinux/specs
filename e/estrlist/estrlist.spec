Name: estrlist
Version: 0.5
Release: alt1

Summary: estrlist - string operation utility

License: Public domain
Group: Development/Other
Url: http://www.altlinux.org/Etersoft-build-utils

Packager: Vitaly Lipatov <lav@altlinux.ru>

# Source-git: http://git.altlinux.org/people/lav/packages/estrlist.git
Source: ftp://updates.etersoft.ru/pub/Etersoft/Sisyphus/sources/tarball/%name-%version.tar

BuildArchitectures: noarch

Conflicts: etersoft-build-utils < 3.0.0

%description
String operation utility.

%prep
%setup

%install
install -D bin/%name %buildroot%_bindir/%name

%files
%_bindir/%name

%changelog
* Wed May 04 2022 Vitaly Lipatov <lav@altlinux.ru> 0.5-alt1
- egrep -> grep -E

* Sun Sep 05 2021 Vitaly Lipatov <lav@altlinux.ru> 0.4-alt1
- turn off wildcard expansion

* Mon Aug 30 2021 Vitaly Lipatov <lav@altlinux.ru> 0.3-alt1
- estrlist: add is_empty alias
- estrlist: add has_space
- estrlist: add -- support

* Sat Oct 10 2020 Vitaly Lipatov <lav@altlinux.ru> 0.2-alt1
- estrlist: fix exclude, fix exclude tests

* Wed Oct 07 2020 Vitaly Lipatov <lav@altlinux.ru> 0.1-alt1
- initial build for ALT Sisyphus (separated from etersoft-build-utils)
