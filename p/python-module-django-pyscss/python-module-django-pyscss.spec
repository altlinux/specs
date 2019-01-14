
%global pypi_name django-pyscss

Name: python-module-%pypi_name
Version: 2.0.2
Release: alt2
Summary: Makes it easier to use PySCSS in Django
Group: Development/Python
License: BSD
Url: https://github.com/fusionbox/django-pyscss
Source: %pypi_name-%version.tar.gz

BuildArch: noarch

Requires: python-module-pyScss

BuildRequires: python-devel
BuildRequires: python-module-setuptools
BuildRequires: python-module-django
BuildRequires: python-module-pyScss

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-django
BuildRequires: python3-module-pyScss

%description
A collection of tools for making it easier to use
pyScss within Django.

%package -n python3-module-%pypi_name
Summary: Makes it easier to use PySCSS in Django
Group: Development/Python3
Requires: python3-module-pyScss

%description -n python3-module-%pypi_name
A collection of tools for making it easier to use
pyScss within Django.

%prep
%setup -n %pypi_name-%version

# Remove bundled egg-info
#rm -rf %pypi_name.egg-info

rm -rf ../python3
cp -a . ../python3

%build
%python_build

pushd ../python3
%python3_build
popd

%install
%python_install

pushd ../python3
%python3_install
popd

%files
%doc README.rst LICENSE
%python_sitelibdir/*

%files -n python3-module-%pypi_name
%doc README.rst LICENSE
%python3_sitelibdir/*

%changelog
* Mon Jan 14 2019 Alexey Shabalin <shaba@altlinux.org> 2.0.2-alt2
- add python3 package

* Mon Sep 14 2015 Lenar Shakirov <snejok@altlinux.ru> 2.0.2-alt1
- New version

* Tue Mar 17 2015 Alexey Shabalin <shaba@altlinux.ru> 1.0.6-alt1
- Initial package.
