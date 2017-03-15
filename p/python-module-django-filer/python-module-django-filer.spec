
%global pypi_name django-filer

Name: python-module-%pypi_name
Version: 1.2.7
Release: alt1
Summary: A file management application for django
Group: Development/Python
License: BSD
Url: http://github.com/divio/django-filer
Source: %name-%version.tar

BuildArch: noarch

BuildRequires: python-devel
BuildRequires: python-module-setuptools
BuildRequires: python-module-django

%description
A file management application for django that makes
handling of files and images a breeze.

%prep
%setup

# Remove bundled egg-info
#rm -rf %pypi_name.egg-info

%build
%python_build

%install
%python_install

%files
%python_sitelibdir/*

%changelog
* Wed Mar 15 2017 Lenar Shakirov <snejok@altlinux.ru> 1.2.7-alt1
- Initial build for ALT


