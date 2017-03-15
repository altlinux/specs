
%global pypi_name django-tools

Name: python-module-%pypi_name
Version: 0.32.7
Release: alt1
Summary: Miscellaneous tools for django
Group: Development/Python
License: GPL
Url: https://pypi.python.org/pypi/django-tools
Source: %name-%version.tar

BuildArch: noarch

BuildRequires: python-devel
BuildRequires: python-module-setuptools
BuildRequires: python-module-django

%description
Miscellaneous tools for django

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
* Wed Mar 15 2017 Lenar Shakirov <snejok@altlinux.ru> 0.32.7-alt1
- Initial build for ALT


