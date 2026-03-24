%define _unpackaged_files_terminate_build 1
%define oname trytond

%def_enable check

Name: python3-module-%oname
Version: 7.8.6
Release: alt1

Summary: Tryton server
License: GPL-3
Group: Development/Python3
Url: https://www.tryton.org

Source0: %oname-%version.tar
BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel
%if_enabled check
BuildRequires: python3-module-werkzeug
BuildRequires: python3-module-lxml
BuildRequires: python3-modules-sqlite3
BuildRequires: python3-module-sql
BuildRequires: python3-module-dateutil
BuildRequires: python3-module-polib
BuildRequires: python3-module-defusedxml
BuildRequires: python3-module-relatorio
BuildRequires: python3-module-passlib
BuildRequires: python3-module-simpleeval
BuildRequires: python3-module-pwdlib
BuildRequires: python3-module-argon2-cffi
BuildRequires: python3-module-html2text
%endif

%py_provides %oname
%add_python3_req_skip __main__

%description
The server of the Tryton application platform. A three-tiers high-level
general purpose application platform written in Python and use
Postgresql as main database engine. It is the core base of an Open
Source ERP. It provides modularity, scalability and security.

%package tests
Summary: Tests for %oname
Group: Development/Python3
Requires: %name = %EVR
Requires: python3-module-trytond_country

%description tests
The server of the Tryton application platform. A three-tiers high-level
general purpose application platform written in Python and use
Postgresql as main database engine. It is the core base of an Open
Source ERP. It provides modularity, scalability and security.

This package contains tests for %oname.

%prep
%setup -q -n %{oname}-%{version}

%build
%pyproject_build

%install
%pyproject_install

%check
export PYTHONPATH=%buildroot%python3_sitelibdir/
python3 -m unittest discover -s trytond.tests -v

%files
%doc CHANGELOG LICENSE README.rst COPYRIGHT
%_bindir/*
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/test*

%files tests
%python3_sitelibdir/*/test*


%changelog
* Tue Mar 24 2026 Nikita Panov <nexxy@altlinux.org> 7.8.6-alt1
- new version 7.8.6

* Wed Mar 04 2026 Nikita Panov <nexxy@altlinux.org> 7.8.5-alt1
- new version 7.8.5

* Thu Feb 12 2026 Nikita Panov <nexxy@altlinux.org> 7.8.4-alt1
- new version 7.8.4

* Mon Jan 26 2026 Nikita Panov <nexxy@altlinux.org> 7.8.3-alt1
- new version 7.8.3

* Tue Dec 16 2025 Nikita Panov <nexxy@altlinux.org> 7.8.0-alt1
- new version 7.8.0

* Fri Nov 14 2025 Nikita Panov <nexxy@altlinux.org> 7.6.10-alt1
- new version 7.6.10

* Thu Oct 30 2025 Nikita Panov <nexxy@altlinux.org> 7.6.9-alt1
- new version 7.6.9

* Thu Oct 16 2025 Nikita Panov <nexxy@altlinux.org> 7.6.8-alt1
- new version 7.6.8

* Tue Sep 16 2025 Anton Vyatkin <toni@altlinux.org> 7.6.7-alt1
- new version 7.6.7

* Tue Sep 09 2025 Anton Vyatkin <toni@altlinux.org> 7.6.6-alt1
- new version 7.6.6

* Thu Aug 14 2025 Anton Vyatkin <toni@altlinux.org> 7.6.5-alt1
- new version 7.6.5

* Wed Jul 16 2025 Anton Vyatkin <toni@altlinux.org> 7.6.4-alt1
- new version 7.6.4

* Wed Jul 02 2025 Anton Vyatkin <toni@altlinux.org> 7.6.3-alt1
- new version 7.6.3

* Thu Jun 05 2025 Anton Vyatkin <toni@altlinux.org> 7.6.2-alt1
- new version 7.6.2

* Wed May 21 2025 Anton Vyatkin <toni@altlinux.org> 7.6.1-alt1
- new version 7.6.1

* Tue Apr 29 2025 Anton Vyatkin <toni@altlinux.org> 7.6.0-alt1
- new version 7.6.0

* Sun Apr 27 2025 Anton Vyatkin <toni@altlinux.org> 7.4.10-alt1
- new version 7.4.10

* Thu Apr 03 2025 Anton Vyatkin <toni@altlinux.org> 7.4.9-alt1
- new version 7.4.9

* Thu Mar 20 2025 Anton Vyatkin <toni@altlinux.org> 7.4.8-alt1
- new version 7.4.8

* Wed Mar 05 2025 Anton Vyatkin <toni@altlinux.org> 7.4.7-alt1
- new version 7.4.7

* Mon Feb 17 2025 Anton Vyatkin <toni@altlinux.org> 7.4.6-alt1
- new version 7.4.6

* Sun Feb 02 2025 Anton Vyatkin <toni@altlinux.org> 7.4.5-alt1
- new version 7.4.5

* Fri Jan 17 2025 Anton Vyatkin <toni@altlinux.org> 7.4.4-alt1
- new version 7.4.4

* Wed Jan 15 2025 Anton Vyatkin <toni@altlinux.org> 7.4.3-alt1
- new version 7.4.3

* Mon Jan 29 2024 Grigory Ustinov <grenka@altlinux.org> 6.4.5-alt2.1
- NMU: fixed FTBFS.

* Mon Dec 18 2023 Anton Zhukharev <ancieg@altlinux.org> 6.4.5-alt2
- Applied patches from upstream for compatibility with werkzeug 3.0.

* Tue Sep 20 2022 Danil Shein <dshein@altlinux.org> 6.4.5-alt1
- version updated to 6.4.5

* Fri Mar 25 2022 Danil Shein <dshein@altlinux.org> 6.2.6-alt1
- version updated to 6.2.6
- tests enabled

* Tue Mar 31 2020 Andrey Bychkov <mrdrew@altlinux.org> 5.4.6-alt1
- Version updated to 5.4.6.

* Thu Oct 17 2019 Andrey Bychkov <mrdrew@altlinux.org> 5.2.7-alt1
- version updated to 5.2.7
- disable python2, enable python3

* Fri May 10 2019 Vitaly Lipatov <lav@altlinux.ru> 4.2.1-alt1.2
- NMU: fix MySQLdb require

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 4.2.1-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Tue Jan 17 2017 Igor Vlasenko <viy@altlinux.ru> 4.2.1-alt1
- automated PyPI update

* Fri Mar 06 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.4.2-alt1
- Version 3.4.2

* Tue Oct 21 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.4.0-alt1
- Version 3.4.0

* Tue Oct 21 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.2.3-alt1
- Initial build for Sisyphus

