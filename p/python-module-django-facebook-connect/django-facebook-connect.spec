%define oname django-facebook-connect

%def_with python3

Name: python-module-%oname
Version: 1.0.2
Release: alt1.git20121127.1
Summary: Add facebook connect authentication to your Django website
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/django-facebook-connect/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/noamsu/django-facebook-connect.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python-tools-2to3
%endif

%description
This package adds facebook connect authentication to a Django web site.
Many of the existing packages are either out of date, using soon to be
deprecated facebook apis (along with out of date documentation), or
simply do not work quite right.

This package is small, does not have external dependencies, and should
"just work".

%package -n python3-module-%oname
Summary: Add facebook connect authentication to your Django website
Group: Development/Python3

%description -n python3-module-%oname
This package adds facebook connect authentication to a Django web site.
Many of the existing packages are either out of date, using soon to be
deprecated facebook apis (along with out of date documentation), or
simply do not work quite right.

This package is small, does not have external dependencies, and should
"just work".

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

%if_with python3
%files -n python3-module-%oname
%doc *.md
%python3_sitelibdir/*
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.0.2-alt1.git20121127.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Mon Sep 29 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.2-alt1.git20121127
- Initial build for Sisyphus

