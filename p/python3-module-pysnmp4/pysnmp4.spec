%define oname pysnmp

Name: python3-module-%{oname}4
Version: 4.4.12
Release: alt1

Summary: SNMP v1/v2c/v3 engine

License: BSD-2-Clause
Group: Development/Python3
Url: https://pypi.org/project/pysnmp

Source: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-python3

%description
This is an alpha-quality revision of pure-Python, open source and free
implementation of v1/v2c/v3 SNMP engine.

%prep
%setup

%build
%python3_build

%install
%python3_install

%check
# syntax error in runtests

%files
%doc docs/* *.txt *.rst *.md
%python3_sitelibdir/%oname
%python3_sitelibdir/%oname-%version-py%_python3_version.egg-info

%changelog
* Thu Jun 02 2022 Grigory Ustinov <grenka@altlinux.org> 4.4.12-alt1
- Build new version.

* Mon Jul 26 2021 Grigory Ustinov <grenka@altlinux.org> 4.4.9-alt2
- Drop python2 support.

* Mon Jun 03 2019 Vitaly Lipatov <lav@altlinux.ru> 4.4.9-alt1
- new version 4.4.9 (with rpmrb script)

* Wed May 16 2018 Andrey Bychkov <mrdrew@altlinux.org> 4.3.1-alt1.2
- (NMU) rebuild with python3.6

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 4.3.1-alt1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Fri Jan 29 2016 Sergey Alembekov <rt@altlinux.ru> 4.3.1-alt1
- Build version 4.3.1

* Fri Mar 06 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.2.6-alt1.rc1
- Version 4.2.6rc1

* Mon Aug 25 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.2.5-alt1
- Version 4.2.5
- Added module for Python 3

* Mon Sep 09 2013 Alexey Shabalin <shaba@altlinux.ru> 4.2.4-alt1
- 4.2.4

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 4.1.14a-alt3.1
- Rebuild with Python-2.7

* Wed Aug 04 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.1.14a-alt3
- Added explicit conflict with python-module-pysnmp

* Tue Aug 03 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.1.14a-alt2
- Added url

* Tue Aug 03 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.1.14a-alt1
- Version 4.1.14a

* Sat Nov 21 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.1.8a-alt2
- Rebuilt with python 2.6

* Thu Jan 24 2008 Grigory Batalov <bga@altlinux.ru> 4.1.8a-alt1.1
- Rebuilt with python-2.5.

* Tue Oct 16 2007 Peter V. Saveliev <peet@altlinux.org> 4.1.8a-alt1
- initial build

