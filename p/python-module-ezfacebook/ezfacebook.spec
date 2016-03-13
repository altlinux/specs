%define oname ezfacebook

%def_with python3

Name: python-module-%oname
Version: 0.87.0
Release: alt1.git20140107.1
Summary: Django Tools to use facebook seamlessly without having to build around it
License: ASL
Group: Development/Python
Url: https://pypi.python.org/pypi/ezfacebook/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/explodes/ezfacebook.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python-tools-2to3
%endif

%description
The purpose of this package is to make facebook integration easy WITHOUT
having to make your whole app depend on this package.

This package makes facebook integration easy for all kinds of web sites:

* Web Applications
* Facebook Page Tabs
* Facebook Applications

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
The purpose of this package is to make facebook integration easy WITHOUT
having to make your whole app depend on this package.

This package contains tests for %oname.

%package -n python3-module-%oname
Summary: Django Tools to use facebook seamlessly without having to build around it
Group: Development/Python3

%description -n python3-module-%oname
The purpose of this package is to make facebook integration easy WITHOUT
having to make your whole app depend on this package.

This package makes facebook integration easy for all kinds of web sites:

* Web Applications
* Facebook Page Tabs
* Facebook Applications

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
The purpose of this package is to make facebook integration easy WITHOUT
having to make your whole app depend on this package.

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

%files
%doc *.md
%python_sitelibdir/*
%exclude %python_sitelibdir/*/tests

%files tests
%python_sitelibdir/*/tests

%if_with python3
%files -n python3-module-%oname
%doc *.md
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/tests
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.87.0-alt1.git20140107.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Tue Sep 30 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.87.0-alt1.git20140107
- Initial build for Sisyphus

