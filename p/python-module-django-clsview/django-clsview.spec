%define oname django-clsview

%def_with python3

Name: python-module-%oname
Version: 0.0.3
Release: alt1.git20100818.1
Summary: Yet another class-based view system for Django
License: Free
Group: Development/Python
Url: https://pypi.python.org/pypi/django-clsview/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/zacharyvoase/django-clsview.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
%endif

%description
django-clsview is a library with yet another solution to the problem of
class-based views in Django.

%package -n python3-module-%oname
Summary: Yet another class-based view system for Django
Group: Development/Python3

%description -n python3-module-%oname
django-clsview is a library with yet another solution to the problem of
class-based views in Django.

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

%files
%doc *.md UNLICENSE
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.md UNLICENSE
%python3_sitelibdir/*
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.0.3-alt1.git20100818.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Mon Sep 29 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.3-alt1.git20100818
- Initial build for Sisyphus

