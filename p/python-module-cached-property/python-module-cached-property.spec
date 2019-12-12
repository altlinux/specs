%define oname cached-property
%define modname cached_property
%def_with python3

Name: python-module-%oname
Version: 1.5.1
Release: alt2

Summary: A decorator for caching properties in classes.

License: BSD-3-Clause
Group: Development/Python
Url: https://github.com/pydanny/cached-property

Source: %oname-%version.tar
BuildArch: noarch

BuildPreReq: rpm-build-python
BuildRequires: python-devel python-module-distribute
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-distribute
%endif

%setup_python_module %oname

%description
A decorator for caching properties in classes.

%if_with python3
%package -n python3-module-%oname
Summary: A decorator for caching properties in classes (Python 3)
Group: Development/Python3

%description -n python3-module-%oname
A decorator for caching properties in classes.
%endif


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
%doc LICENSE AUTHORS.rst README.rst HISTORY.rst CONTRIBUTING.rst
%python_sitelibdir/%modname.*
%python_sitelibdir/*.egg-info

%if_with python3
%files -n python3-module-%oname
%python3_sitelibdir/%modname.*
%python3_sitelibdir/*.egg-*
%python3_sitelibdir/__pycache__/*
%endif

%changelog
* Thu Dec 12 2019 Grigory Ustinov <grenka@altlinux.org> 1.5.1-alt2
- NMU: Fix license.

* Tue Dec 4 2018 Vladimir Didenko <cow@altlinux.ru> 1.5.1-alt1
- 1.5.1

* Fri Apr 08 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.3.0-alt1.1.1
- (NMU) Rebuild with python3-3.5.1-alt3 to get rid of the meaningless __pycache__/ dep
  (it is meaningless because arbitrary packages package that dir).

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.3.0-alt1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Mon Feb 8 2016 Vladimir Didenko <cow@altlinux.ru> 1.3.0-alt1
- 1.3.0
