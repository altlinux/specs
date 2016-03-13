%define oname django-secretballot

%def_with python3

Name: python-module-%oname
Version: 0.2.4
Release: alt1.git20140519.1.1
Summary: Django anonymous voting application
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/django-secretballot/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/sunlightlabs/django-secretballot.git
Source: %name-%version.tar
BuildArch: noarch

#BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools
%endif

# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: python-base python-modules python-modules-compiler python-modules-email python3 python3-base
BuildRequires: python-devel rpm-build-python3

%description
Django voting application that allows voting without a logged in user.

Provides abstract base model for types that the user wishes to allow
voting on as well as related utilities including generic views to ease
the addition of 'anonymous' voting to a Django project.

%package -n python3-module-%oname
Summary: Django anonymous voting application
Group: Development/Python3

%description -n python3-module-%oname
Django voting application that allows voting without a logged in user.

Provides abstract base model for types that the user wishes to allow
voting on as well as related utilities including generic views to ease
the addition of 'anonymous' voting to a Django project.

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
%doc CHANGELOG *.rst
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc CHANGELOG *.rst
%python3_sitelibdir/*
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.2.4-alt1.git20140519.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.2.4-alt1.git20140519.1
- NMU: Use buildreq for BR.

* Tue Sep 30 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.4-alt1.git20140519
- Initial build for Sisyphus

