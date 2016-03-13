%define oname dj-queryset-manager

%def_with python3

Name: python-module-%oname
Version: 0.1.3
Release: alt1.git20140628.1
Summary: Stop writing Django querysets
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/dj-queryset-manager/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/nosamanuel/dj-queryset-manager.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
%endif

%description
A Django utility that makes it simple to write DRY queryset methods.

Warning:

dj-queryset-manager only works with Django versions 1.2 through 1.6.

In Django 1.7 it has been superseded by QuerySet.as_manager().

%package -n python3-module-%oname
Summary: Stop writing Django querysets
Group: Development/Python3

%description -n python3-module-%oname
A Django utility that makes it simple to write DRY queryset methods.

Warning:

dj-queryset-manager only works with Django versions 1.2 through 1.6.

In Django 1.7 it has been superseded by QuerySet.as_manager().

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
%doc *.rst
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.rst
%python3_sitelibdir/*
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.1.3-alt1.git20140628.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Tue Sep 30 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.3-alt1.git20140628
- Initial build for Sisyphus

