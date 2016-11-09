%def_with python3
%define oname django-redis

Name: python-module-%oname
Version: 4.6.0
Release: alt1
Summary: Full featured redis cache backend for Django
License: BSD
Group: Development/Python
Url: https://github.com/niwibe/django-redis

Source: %name-%version.tar

BuildArch: noarch
BuildRequires: python-devel
BuildRequires: python-module-setuptools
BuildRequires: python-module-django
BuildRequires: python-module-redis-py
Requires: python-module-django python-module-redis-py

%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools python3-module-django
BuildRequires: python3-module-redis-py
%endif

%description
Full featured redis cache backend for Django.

%package -n python3-module-%oname
Summary: Full featured redis cache backend for Django
Group: Development/Python3
Requires: python3-module-django python3-module-redis-py

%description -n python3-module-%oname
Full featured redis cache backend for Django.

%prep
%setup

%if_with python3
cp -fR . ../python3
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
%doc AUTHORS.rst LICENSE README.rst
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc AUTHORS.rst LICENSE README.rst
%python3_sitelibdir/*
%endif

%changelog
* Wed Nov 09 2016 Alexey Shabalin <shaba@altlinux.ru> 4.6.0-alt1
- Initial build for ALT Linux


