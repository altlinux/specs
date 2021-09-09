Name: rpm-build-pear
Version: 0.6
Release: alt2

Summary: RPM helper scripts for build PEAR packages

License: GPL
Group: Development/Other
Url: https://www.altlinux.org/Pear_Policy

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: %name-%version.tar

BuildArch: noarch

BuildRequires: rpm-build-php
Requires: rpm-build-php
Requires: /usr/bin/php

%description
RPM helper scripts for build PEAR packages.
You can build PEAR rpm package with
pear make-rpm-spec <package> command from pear-PEAR_Command_Packaging package.
See %url for detailed PEAR packaging policy.

%prep
%setup

%install
install -D -m644 macros %buildroot/%_rpmmacrosdir/pear
install -D -m644 xml2changelog %buildroot/%php_peardir/xml2changelog
install -D -m644 PHP-LICENSE-3.01 %buildroot/%php_peardir/PHP-LICENSE-3.01

%files
%doc README
%_rpmmacrosdir/pear
%php_peardir/xml2changelog
%php_peardir/PHP-LICENSE-3.01

%changelog
* Thu Sep 09 2021 Vitaly Lipatov <lav@altlinux.ru> 0.6-alt2
- use /usr/bin/php instead of php7

* Thu Jul 08 2021 Dmitry V. Levin <ldv@altlinux.org> 0.6-alt1
- Fixed build.

* Thu Jul 08 2021 Anton Farygin <rider@altlinux.ru> 0.6-alt1
- switched to universal version-independent macros for php

* Wed Feb 13 2019 Vitaly Lipatov <lav@altlinux.ru> 0.5-alt1
- switch to php7

* Tue Jul 01 2008 Vitaly Lipatov <lav@altlinux.ru> 0.4-alt2
- cleanup spec, move to build from git

* Mon Mar 24 2008 Denis Klimov <zver@altlinux.ru> 0.4-alt1
- Modify condition exist %%{pear_name}-%%{version} directory in macros file

* Wed Jan 09 2008 Vitaly Lipatov <lav@altlinux.ru> 0.3-alt1
- new names for pear service macroses (see README)
- hide cd from install section in pear_install_std macros

* Sat Jan 05 2008 Vitaly Lipatov <lav@altlinux.ru> 0.2-alt1
- add rpm-build-php5 (build)requires
- change macros' names to RH compatible
- add php5, php5-simplexml requires

* Fri Jan 04 2008 Vitaly Lipatov <lav@altlinux.ru> 0.1-alt1
- initial build for ALT Linux Sisyphus
