%define _unpackaged_files_terminate_build 1
%define oname shortuuid

%def_with python3

Name: python-module-%oname
Version: 0.4.3
Release: alt1.1
Summary: A generator library for concise, unambiguous and URL-safe UUIDs
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/shortuuid/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/stochastic-technologies/shortuuid.git
Source0: https://pypi.python.org/packages/e9/41/d867be1470af87dd8af1b3462e5eae44f78ffd33cec54630d40ca6b2d0bd/%{oname}-%{version}.tar.gz
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools
BuildPreReq: python-tools-pep8
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python3-tools-pep8
%endif

%py_provides %oname

%description
A library that generates short, pretty, unambiguous unique IDs by using
an extensive, case-sensitive alphabet and omitting similar-looking
letters and numbers.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
A library that generates short, pretty, unambiguous unique IDs by using
an extensive, case-sensitive alphabet and omitting similar-looking
letters and numbers.

This package contains tests for %oname.

%package -n python3-module-%oname
Summary: A generator library for concise, unambiguous and URL-safe UUIDs
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
A library that generates short, pretty, unambiguous unique IDs by using
an extensive, case-sensitive alphabet and omitting similar-looking
letters and numbers.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
A library that generates short, pretty, unambiguous unique IDs by using
an extensive, case-sensitive alphabet and omitting similar-looking
letters and numbers.

This package contains tests for %oname.

%prep
%setup -q -n %{oname}-%{version}

%if_with python3
cp -fR . ../python3
%endif

%build
%python_build_debug

%if_with python3
pushd ../python3
%python3_build_debug
popd
%endif

%install
%python_install

%if_with python3
pushd ../python3
%python3_install
popd
%endif

%check
python setup.py test
%if_with python3
pushd ../python3
python3 setup.py test
popd
%endif

%files
%doc *.rst
%python_sitelibdir/*
%exclude %python_sitelibdir/*/tests.*

%files tests
%python_sitelibdir/*/tests.*

%if_with python3
%files -n python3-module-%oname
%doc *.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests.*
%exclude %python3_sitelibdir/*/*/tests.*

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/tests.*
%python3_sitelibdir/*/*/tests.*
%endif

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.4.3-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 0.4.3-alt1
- automated PyPI update

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.4.2-alt2.git20140426.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Fri Mar 06 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.2-alt2.git20140426
- Disabled test_pep8 (broken with new pep8)

* Mon Nov 10 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.2-alt1.git20140426
- Initial build for Sisyphus

