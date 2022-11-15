%define oname pycparser

Name: python3-module-pycparser
Version: 2.21
Release: alt1.1

Summary: C parser in Python

Group: Development/Python3
License: BSD
Url: https://github.com/eliben/pycparser

Packager: Vitaly Lipatov <lav@altlinux.ru>

# Source-url: %__pypi_url %oname
Source: %name-%version.tar

BuildRequires(pre): rpm-build-intro >= 2.2.5
BuildRequires(pre): rpm-build-python3

BuildArch: noarch

%add_python3_self_prov_path %buildroot%python3_sitelibdir/%oname/

%description
pycparser is a complete parser of the C language, written in pure Python
using the PLY parsing library.
It parses C code into an AST and can serve as a front-end for C compilers or analysis tools.


%prep
%setup

%build
%python3_build

%install
%python3_install

%files
%python3_sitelibdir/%oname/
%python3_sitelibdir/%oname-%version-*.egg-info

%changelog
* Sun Nov 13 2022 Daniel Zagaynov <kotopesutility@altlinux.org> 2.21-alt1.1
- NMU: used %%add_python3_self_prov_path macro to skip self-provides from dependencies.

* Mon Jul 18 2022 Vitaly Lipatov <lav@altlinux.ru> 2.21-alt1
- new version 2.21 (with rpmrb script)

* Tue Jul 13 2021 Vitaly Lipatov <lav@altlinux.ru> 2.20-alt2
- build python3 separately, cleanup spec

* Thu Nov 05 2020 Vitaly Lipatov <lav@altlinux.ru> 2.20-alt1
- new version 2.20 (with rpmrb script)

* Sat Feb 08 2020 Vitaly Lipatov <lav@altlinux.ru> 2.19-alt2
- drop mwlib buildrequire

* Sun Nov 04 2018 Vitaly Lipatov <lav@altlinux.ru> 2.19-alt1
- new version 2.19 (with rpmrb script)

* Sat Jun 09 2018 Vitaly Lipatov <lav@altlinux.ru> 2.18-alt1
- new version 2.18 (with rpmrb script)

* Fri Feb 03 2017 Michael Shigorin <mike@altlinux.org> 2.14-alt1.1.1
- BOOTSTRAP: avoid python-module-mwlib -> gevent -> greenlet (!e2k)

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 2.14-alt1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Mon Aug 03 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.14-alt1
- Version 2.14

* Wed Apr 22 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.12-alt1
- Version 2.12

* Tue Jul 29 2014 Vladimir Didenko <cow@altlinux.org> 2.10-alt1
- 2.10
- add python3 version

* Mon Apr 08 2013 Vitaly Lipatov <lav@altlinux.ru> 2.09.1-alt1
- initial build for ALT Linux Sisyphus
