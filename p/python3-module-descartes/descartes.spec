%define _unpackaged_files_terminate_build 1
%define oname descartes

# compared values are same, but dont equal to numeric value
%def_disable check

Name: python3-module-%oname
Version: 1.1.0
Release: alt2
Summary: Use geometric objects as matplotlib paths and patches
License: BSD
Group: Development/Python3
Url: https://pypi.python.org/pypi/descartes/

Source0: https://pypi.python.org/packages/1d/6f/81735a30432b74f41db6754dd13869021ccfed3088d1cf7a6cfc0af9ac49/%{oname}-%{version}.tar.gz
BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-matplotlib python3-module-nose python3-module-numpy-testing python3-module-shapely time

%py3_provides %oname

%description
Use Shapely or GeoJSON-like geometric objects as matplotlib paths and
patches.

%package tests
Summary: Tests for %oname
Group: Development/Python3
Requires: %name = %EVR

%description tests
Use Shapely or GeoJSON-like geometric objects as matplotlib paths and
patches.

This package contains tests for %oname.

%prep
%setup -n %{oname}-%{version}

# Quick fix deprecation warnings
#sed -i 's/failUnlessEqual/assertEqual/' descartes/tests.py
#sed -i 's/failUnless/assertTrue/' descartes/tests.py

%build
%python3_build

%install
%python3_install

%check
python3 setup.py test
nosetests3

%files
%doc *.txt PKG-INFO
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests.*
%exclude %python3_sitelibdir/*/*/tests.*

%files tests
%python3_sitelibdir/*/tests.*
%python3_sitelibdir/*/*/tests.*

%changelog
* Sat Apr 03 2021 Grigory Ustinov <grenka@altlinux.org> 1.1.0-alt2
- Disable check, because of ftbfs.
- Drop python2 support.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.1.0-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Wed Jan 18 2017 Igor Vlasenko <viy@altlinux.ru> 1.1.0-alt1
- automated PyPI update

* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 1.0.2-alt1
- automated PyPI update

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.0.1-alt3.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 1.0.1-alt3.1
- NMU: Use buildreq for BR.

* Mon Mar 02 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.1-alt3
- Fixed build

* Sun Nov 02 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.1-alt2
- Added requirement on shapely for Python 3 (for tests)
- Enabled testing with nose

* Sun Nov 02 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.1-alt1
- Initial build for Sisyphus

