%define _unpackaged_files_terminate_build 1
%define oname django-preferences

%def_with python3

Name: python-module-%oname
Version: 0.1
Release: alt1
Summary: Django app allowing users to set app specific preferences through the admin interface
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/django-preferences/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/praekelt/django-preferences.git
Source0: https://pypi.python.org/packages/1f/a0/0063d210b980cff110c57562fc1c15ff97e74968123c1f1d139af1b387a2/%{oname}-%{version}.tar.gz
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
%endif

%description
Provides singleton admin views for Preferences objects and a simple
interface to preference values. Singleton views ensure only one
preference intance per site is available for each Preferences class.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
Provides singleton admin views for Preferences objects and a simple
interface to preference values. Singleton views ensure only one
preference intance per site is available for each Preferences class.

This package contains tests for %oname.

%package -n python3-module-%oname
Summary: Django app allowing users to set app specific preferences through the admin interface
Group: Development/Python3

%description -n python3-module-%oname
Provides singleton admin views for Preferences objects and a simple
interface to preference values. Singleton views ensure only one
preference intance per site is available for each Preferences class.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
Provides singleton admin views for Preferences objects and a simple
interface to preference values. Singleton views ensure only one
preference intance per site is available for each Preferences class.

This package contains tests for %oname.

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
%exclude %python_sitelibdir/*/tests

%files tests
%python_sitelibdir/*/tests

%if_with python3
%files -n python3-module-%oname
%doc *.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/tests
%endif

%changelog
* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 0.1-alt1
- automated PyPI update

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.0.6-alt1.git20120612.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Tue Sep 30 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.6-alt1.git20120612
- Initial build for Sisyphus

