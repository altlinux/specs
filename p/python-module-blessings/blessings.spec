%define oname blessings

%def_with python3
%def_disable check

Name: python-module-%oname
Version: 1.6
Release: alt1.git20140520.1.1
Summary: A thin, practical wrapper around terminal capabilities in Python
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/blessings/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/erikrose/blessings.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools /dev/pts
BuildPreReq: python-module-nose
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python3-module-nose python3-modules-curses
BuildPreReq: python-tools-2to3
%endif

%py_provides %oname

%description
A thin, practical wrapper around terminal coloring, styling, and
positioning.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
A thin, practical wrapper around terminal coloring, styling, and
positioning.

This package contains tests for %oname.

%package -n python3-module-%oname
Summary: A thin, practical wrapper around terminal capabilities in Python
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
A thin, practical wrapper around terminal coloring, styling, and
positioning.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
A thin, practical wrapper around terminal coloring, styling, and
positioning.

This package contains tests for %oname.

%prep
%setup

%if_with python3
cp -fR . ../python3
find ../python3 -type f -name '*.py' -exec 2to3 -w -n '{}' +
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
%doc *.rst docs/*.rst
%python_sitelibdir/*
%exclude %python_sitelibdir/*/tests.*

%files tests
%python_sitelibdir/*/tests.*

%if_with python3
%files -n python3-module-%oname
%doc *.rst docs/*.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests.*
%exclude %python3_sitelibdir/*/*/tests.*

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/tests.*
%python3_sitelibdir/*/*/tests.*
%endif

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.6-alt1.git20140520.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.6-alt1.git20140520.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Fri Nov 28 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.6-alt1.git20140520
- Initial build for Sisyphus

