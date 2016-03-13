%define oname django-setuptest

%def_with python3

Name: python-module-%oname
Version: 0.1.5
Release: alt1.git20140911.1
Summary: Simple test suite enabling Django app testing via $ python setup.py test
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/django-setuptest/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/praekelt/django-setuptest.git 
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
%endif

%description
Simple test suite enabling Django app testing via $ python setup.py
test.

%package -n python3-module-%oname
Summary: Simple test suite enabling Django app testing via $ python setup.py test
Group: Development/Python3

%description -n python3-module-%oname
Simple test suite enabling Django app testing via $ python setup.py
test.

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
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.1.5-alt1.git20140911.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Tue Sep 30 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.5-alt1.git20140911
- Initial build for Sisyphus

