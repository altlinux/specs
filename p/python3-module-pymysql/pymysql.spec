%define _unpackaged_files_terminate_build 1
%define modulename pymysql

Name: python3-module-%modulename
Version: 1.0.3
Release: alt1

Summary: This pure Python MySQL client provides a DB-API to a MySQL database.

License: MIT
Group: Development/Python3
Url: http://code.google.com/p/pymysql/

BuildArch: noarch

# https://github.com/PyMySQL/PyMySQL.git
Source0: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel

%description
This pure Python MySQL client provides a DB-API to a MySQL database by
talking directly to the server via the binary client/server protocol.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%files
%doc *.md example.py
%python3_sitelibdir/%modulename
%python3_sitelibdir/PyMySQL-%version.dist-info

%changelog
* Tue Mar 28 2023 Grigory Ustinov <grenka@altlinux.org> 1.0.3-alt1
- Automatically updated to 1.0.3.

* Thu May 26 2022 Grigory Ustinov <grenka@altlinux.org> 1.0.2-alt1
- Automatically updated to 1.0.2.

* Wed Jul 28 2021 Grigory Ustinov <grenka@altlinux.org> 0.9.3-alt2
- Drop python2 support.

* Fri Jul 24 2020 Anton Farygin <rider@altlinux.ru> 0.9.3-alt1
- 0.9.3

* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 0.7.9-alt1
- automated PyPI update

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.6.6-alt1.git20150727.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.6.6-alt1.git20150727.1
- NMU: Use buildreq for BR.

* Wed Jul 29 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.6-alt1.git20150727
- Version 0.6.6

* Sat Jan 17 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.3-alt1.git20150114
- Version 0.6.3

* Wed Sep 03 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.2-alt1.git20140901
- Version 0.6.2
- Added module for Python 3

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.3-alt1.svn35.1
- Rebuild with Python-2.7

* Tue Oct 12 2010 Alexey Morsov <swi@altlinux.ru> 0.3-alt1.svn35
- new version

* Tue Mar 16 2010 Alexey Morsov <swi@altlinux.ru> 0.2-alt1.svn4
- initial build

