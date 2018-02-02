%define _unpackaged_files_terminate_build 1
%define oname affine

%def_with python3

Name: python-module-%oname
Version: 2.0.0.post1
Release: alt2.1
Summary: Affine transformation matrices
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/affine/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/sgillies/affine.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools
BuildPreReq: python-module-nose
BuildPreReq: python-module-pytest
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python3-module-nose
BuildPreReq: python3-module-pytest
%endif

%py_provides %oname

%description
Matrices describing affine transformation of the plane.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
Matrices describing affine transformation of the plane.

This package contains tests for %oname.

%if_with python3
%package -n python3-module-%oname
Summary: Affine transformation matrices
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
Matrices describing affine transformation of the plane.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
Matrices describing affine transformation of the plane.

This package contains tests for %oname.
%endif

%prep
%setup

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
rm -fR build
py.test -vv
%if_with python3
pushd ../python3
python3 setup.py test
rm -fR build
py.test3 -vv
popd
%endif

%files
%doc *.txt *.rst
%python_sitelibdir/*
%exclude %python_sitelibdir/*/tests

%files tests
%python_sitelibdir/*/tests

%if_with python3
%files -n python3-module-%oname
%doc *.txt *.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/tests
%endif

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 2.0.0.post1-alt2.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Wed Jun 28 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 2.0.0.post1-alt2
- Import upstream sources and updated spec
- Fix build with new python3-module-pytest

* Tue Jan 17 2017 Igor Vlasenko <viy@altlinux.ru> 2.0.0.post1-alt1
- automated PyPI update

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.2.0-alt1.git20150601.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Wed Aug 12 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.0-alt1.git20150601
- Version 1.2.0

* Wed Jan 21 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.0-alt1.git20141113
- Initial build for Sisyphus

