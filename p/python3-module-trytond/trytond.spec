%define _unpackaged_files_terminate_build 1
%define oname trytond

Name: python3-module-%oname
Version: 5.2.7
Release: alt1

Summary: Tryton server
License: GPL
Group: Development/Python3
Url: https://pypi.python.org/pypi/trytond/

Source0: https://pypi.python.org/packages/17/f7/c7981ea71084c8dc4adf61627bd9265716407bc7cedf13bc746dd51cde76/%{oname}-%{version}.tar.gz
BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools
BuildRequires: python3-module-sphinx

%py_provides %oname

%description
The server of the Tryton application platform. A three-tiers high-level
general purpose application platform written in Python and use
Postgresql as main database engine. It is the core base of an Open
Source ERP. It provides modularity, scalability and security.

%package tests
Summary: Tests for %oname
Group: Development/Python3
Requires: %name = %EVR

%description tests
The server of the Tryton application platform. A three-tiers high-level
general purpose application platform written in Python and use
Postgresql as main database engine. It is the core base of an Open
Source ERP. It provides modularity, scalability and security.

This package contains tests for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
The server of the Tryton application platform. A three-tiers high-level
general purpose application platform written in Python and use
Postgresql as main database engine. It is the core base of an Open
Source ERP. It provides modularity, scalability and security.

This package contains documentation for %oname.

%prep
%setup -q -n %{oname}-%{version}

# `alt` sphinx-build name in python3 package sphinx-build-3
sed -i 's/sphinx-build/&-3/' doc/Makefile

%build
%python3_build_debug

export PYTHONPATH=$PWD
%make -C doc html

%install
%python3_install

%files
%doc CHANGELOG README.rst COPYRIGHT
%_bindir/*
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/test*

%files tests
%python3_sitelibdir/*/test*

%files docs
%doc doc/_build/html/*


%changelog
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

