%define oname tgming

%def_with python3

Name: python-module-%oname
Version: 0.0.8
Release: alt2.1
Summary: TurboGears2 Support for Ming MongoDB ORM
License: MIT
Group: Development/Python
Url: http://pypi.python.org/pypi/tgming/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python-tools-2to3
%endif

%description
tgming is used by TurboGears2 to support ming backend. To create a ming
project just use quickstart command with --ming option it will
automatically setup tgming and all the required dependencies.

%package -n python3-module-%oname
Summary: TurboGears2 Support for Ming MongoDB ORM
Group: Development/Python3

%description -n python3-module-%oname
tgming is used by TurboGears2 to support ming backend. To create a ming
project just use quickstart command with --ming option it will
automatically setup tgming and all the required dependencies.

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

%build
%python_build_debug

%if_with python3
pushd ../python3
find -type f -name '*.py' -exec 2to3 -w -n '{}' +
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
%doc PKG-INFO *.rst
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc PKG-INFO *.rst
%python3_sitelibdir/*
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.0.8-alt2.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Tue Jul 22 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.8-alt2
- Added module for Python 3

* Wed Apr 03 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.8-alt1
- Version 0.0.8

* Wed Sep 26 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.7-alt1
- Initial build for Sisyphus

