%define oname SQLAlchemy-Utils

%def_with python3

Name: python-module-%oname
Version: 0.32.1
Release: alt1

Summary: Various utility functions for SQLAlchemy.
License: BSD
Group: Development/Python
Url: https://github.com/kvesteri/sqlalchemy-utils

Source: %oname-%version.tar
BuildArch: noarch
%py_provides %oname

BuildRequires: python-devel python-module-setuptools
BuildRequires: python-module-six
BuildRequires: python-module-SQLAlchemy >= 1.0

%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools
BuildRequires: python3-module-six
BuildRequires: python3-module-SQLAlchemy >= 1.0
%endif

%description
%summary

%if_with python3
%package -n python3-module-%oname
Summary: Python 3 Various utility functions for SQLAlchemy.
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
%summary

%package -n python3-module-%oname-tests
Summary: Tests for %oname (Python 3)
Group: Development/Python3
Requires: python3-module-%oname = %version-%release

%description -n python3-module-%oname-tests
%summary

%endif

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %version-%release

%description tests
%summary

%prep
%setup -n %oname-%version
%if_with python3
rm -rf ../python3
cp -a . ../python3
%endif

%build
%python_build

%if_with python3
pushd ../python3
%python3_build
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
%python_sitelibdir/*
#%exclude %python_sitelibdir/*/tests

#%files tests
#%python_sitelibdir/*/tests

%if_with python3
%files -n python3-module-%oname
%python3_sitelibdir/*
#%exclude %python3_sitelibdir/*/tests

#%files -n python3-module-%oname-tests
#%python3_sitelibdir/*/tests
%endif

%changelog
* Wed Apr 13 2016 Alexey Shabalin <shaba@altlinux.ru> 0.32.1-alt1
- Initial build for Sisyphus.

