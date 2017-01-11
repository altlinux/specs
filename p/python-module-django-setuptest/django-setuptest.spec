%define _unpackaged_files_terminate_build 1
%define oname django-setuptest

%def_with python3

Name: python-module-%oname
Version: 0.2.1
Release: alt1
Summary: Simple test suite enabling Django app testing via $ python setup.py test
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/django-setuptest/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/praekelt/django-setuptest.git 
Source0: https://pypi.python.org/packages/93/5c/0a76e83e066942ca8caed6382095f218f14ae49b1631d16b262e4ce4ae89/%{oname}-%{version}.tar.gz
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
%setup -q -n %{oname}-%{version}

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
* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 0.2.1-alt1
- automated PyPI update

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.1.5-alt1.git20140911.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Tue Sep 30 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.5-alt1.git20140911
- Initial build for Sisyphus

