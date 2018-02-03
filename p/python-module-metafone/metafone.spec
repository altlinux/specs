%define oname metafone

%def_with python3

Name: python-module-%oname
Version: 0.5
Release: alt1.git20150216.1.1
Summary: A Python implementation of the double metaphone algorithms
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/Metafone/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/al45tair/metaphone.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools
BuildPreReq: python-module-nose python-module-six
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python3-module-nose python3-module-six
%endif

%py_provides %oname

%description
A Python implementation of the double metaphone algorithms.

This is a fork of the Metaphone package, with added Unicode support.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires six

%description tests
A Python implementation of the double metaphone algorithms.

This is a fork of the Metaphone package, with added Unicode support.

This package contains tests for %oname.

%if_with python3
%package -n python3-module-%oname
Summary: A Python implementation of the double metaphone algorithms
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
A Python implementation of the double metaphone algorithms.

This is a fork of the Metaphone package, with added Unicode support.
%endif

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR
%py3_requires six

%description -n python3-module-%oname-tests
A Python implementation of the double metaphone algorithms.

This is a fork of the Metaphone package, with added Unicode support.

This package contains tests for %oname.

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

%build
export LC_ALL=en_US.UTF-8
%python_build_debug

%if_with python3
pushd ../python3
%python3_build_debug
popd
%endif

%install
export LC_ALL=en_US.UTF-8
%python_install

%if_with python3
pushd ../python3
%python3_install
popd
%endif

%check
export LC_ALL=en_US.UTF-8
python setup.py test
%if_with python3
pushd ../python3
python3 setup.py test
popd
%endif

%files
%doc *.rst
%python_sitelibdir/*
%exclude %python_sitelibdir/*/tests

%files tests
%python_sitelibdir/*/tests

%if_with python3
%files -n python3-module-%oname
%doc *.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/tests
%endif

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.5-alt1.git20150216.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.5-alt1.git20150216.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Mon Mar 02 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5-alt1.git20150216
- Initial build for Sisyphus

