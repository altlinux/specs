%define oname cached-property
%define modname cached_property
%def_with python3

Name: python-module-%oname
Version: 1.3.0
Release: alt1.1

Summary: A decorator for caching properties in classes.

License: %bsd
Group: Development/Python
Url: https://github.com/pydanny/cached-property

Source: %oname-%version.tar
BuildArch: noarch

BuildRequires(pre): rpm-build-licenses
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
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.3.0-alt1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Mon Feb 8 2016 Vladimir Didenko <cow@altlinux.ru> 1.3.0-alt1
- 1.3.0
