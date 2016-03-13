%define oname betterpath

%def_with python3

Name: python-module-%oname
Version: 0.2.2
Release: alt1.1
Summary: Path manipulation library
License: MIT/X11
Group: Development/Python
Url: https://pypi.python.org/pypi/betterpath/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-vcversioner python-module-zope.interface
BuildPreReq: python-module-twisted-core-test
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-vcversioner python3-module-zope.interface
BuildPreReq: python3-module-twisted-core-test
BuildPreReq: python-tools-2to3
%endif

%py_provides %oname bp
%py_requires zope.interface

%description
betterpath, or "bp", is an adaptation of the classic Twisted FilePath
type and interface. bp provides a simple, robust, well-tested object
abstraction over file paths, generalizing the concept of file paths
beyond filesystems.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
betterpath, or "bp", is an adaptation of the classic Twisted FilePath
type and interface. bp provides a simple, robust, well-tested object
abstraction over file paths, generalizing the concept of file paths
beyond filesystems.

This package contains tests for %oname.

%package -n python3-module-%oname
Summary: Path manipulation library
Group: Development/Python3
%py3_provides %oname bp
%py3_requires zope.interface

%description -n python3-module-%oname
betterpath, or "bp", is an adaptation of the classic Twisted FilePath
type and interface. bp provides a simple, robust, well-tested object
abstraction over file paths, generalizing the concept of file paths
beyond filesystems.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
betterpath, or "bp", is an adaptation of the classic Twisted FilePath
type and interface. bp provides a simple, robust, well-tested object
abstraction over file paths, generalizing the concept of file paths
beyond filesystems.

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
rm -fR build
py.test -vv
%if_with python3
pushd ../python3
python3 setup.py test
#rm -fR build
#py.test-%_python3_version -vv
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
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.2.2-alt1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Tue Feb 10 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.2-alt1
- Initial build for Sisyphus

