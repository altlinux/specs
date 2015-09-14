
%global pypi_name django-pyscss

Name: python-module-%pypi_name
Version: 2.0.2
Release: alt1
Summary: Makes it easier to use PySCSS in Django
Group: Development/Python
License: BSD
Url: https://github.com/fusionbox/django-pyscss
Source: %name-%version.tar

BuildArch: noarch

BuildRequires: python-devel
BuildRequires: python-module-setuptools
BuildRequires: python-module-django
BuildRequires: python-module-pyScss

Requires: python-module-pyScss

%description
A collection of tools for making it easier to use
pyScss within Django.

%prep
%setup

# Remove bundled egg-info
#rm -rf %pypi_name.egg-info

%build
%python_build

%install
%python_install

%files
%doc README.rst LICENSE
%python_sitelibdir/*

%changelog
* Mon Sep 14 2015 Lenar Shakirov <snejok@altlinux.ru> 2.0.2-alt1
- New version

* Tue Mar 17 2015 Alexey Shabalin <shaba@altlinux.ru> 1.0.6-alt1
- Initial package.
