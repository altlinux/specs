%define _unpackaged_files_terminate_build 1
%define oname trytond

%def_enable check

Name: python3-module-%oname
Version: 6.4.5
Release: alt2

Summary: Tryton server
License: GPL-3
Group: Development/Python3
Url: https://www.tryton.org

Source0: https://files.pythonhosted.org/packages/4e/43/b565c06310a2c00bc09ee676c07f71bd40290353a03bc84c5c458a765f99/%{oname}-%{version}.tar.gz
BuildArch: noarch

BuildRequires(pre): rpm-build-python3
%if_enabled check
BuildRequires: python3-module-werkzeug
BuildRequires: python3-module-lxml
BuildRequires: python3-modules-sqlite3
BuildRequires: python3-module-sql
BuildRequires: python3-module-dateutil
BuildRequires: python3-module-polib
BuildRequires: python3-module-defusedxml
BuildRequires: python3-module-relatorio
BuildRequires: python3-module-wrapt
BuildRequires: python3-module-passlib
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
%python3_build

%install
%python3_install

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

