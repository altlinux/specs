%define oname django_factory

%def_with python3

Name: python-module-%oname
Version: 0.11
Release: alt1.1
Summary: Generic factory for creating instances of Django models in tests
License: ASL v2.0
Group: Development/Python
Url: https://pypi.python.org/pypi/django_factory/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
%endif

%description
django_factory is a generic implementation of `Creation Methods` for
Django models.

Using django_factory in your tests means that each test can create
instances of the models, but only has to specify the model attributes
that are germane to that particular test.

Using creation methods usually leads to tests that are easier to read,
and makes it easier to avoid convoluted test setup methods that are
shared, as the pre-conditions for each test are easier to establish.

%package -n python3-module-%oname
Summary: Generic factory for creating instances of Django models in tests
Group: Development/Python3

%description -n python3-module-%oname
django_factory is a generic implementation of `Creation Methods` for
Django models.

Using django_factory in your tests means that each test can create
instances of the models, but only has to specify the model attributes
that are germane to that particular test.

Using creation methods usually leads to tests that are easier to read,
and makes it easier to avoid convoluted test setup methods that are
shared, as the pre-conditions for each test are easier to establish.

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
%doc HACKING README
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc HACKING README
%python3_sitelibdir/*
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.11-alt1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Mon Sep 29 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.11-alt1
- Initial build for Sisyphus

