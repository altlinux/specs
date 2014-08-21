%define oname htmlgen

%def_with python3

Name: python-module-%oname
Version: 0.4
Release: alt1.git20140517
Summary: HTML 5 Generator
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/htmlgen/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
%endif

%description
Python HTML 5 Generator.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
Python HTML 5 Generator.

This package contains tests for %oname.

%package -n python3-module-%oname
Summary: HTML 5 Generator
Group: Development/Python3

%description -n python3-module-%oname
Python HTML 5 Generator.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
Python HTML 5 Generator.

This package contains tests for %oname.

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
%if_with python3
pushd ../python3
python3 setup.py test
popd
%endif

%files
%doc *.rst
%python_sitelibdir/*
%exclude %python_sitelibdir/test_htmlgen

%files tests
%python_sitelibdir/test_htmlgen

%if_with python3
%files -n python3-module-%oname
%doc *.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/test_htmlgen

%files -n python3-module-%oname-tests
%python3_sitelibdir/test_htmlgen
%endif

%changelog
* Thu Aug 21 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4-alt1.git20140517
- Initial build for Sisyphus

