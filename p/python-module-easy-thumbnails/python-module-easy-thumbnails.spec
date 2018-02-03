
%global pypi_name easy-thumbnails

Name: python-module-%pypi_name
Version: 2.3
Release: alt1.1
Summary: Easy thumbnails for Django
Group: Development/Python
License: BSD
Url: https://pypi.python.org/pypi/easy-thumbnails
Source: %name-%version.tar

BuildArch: noarch

BuildRequires: python-devel
BuildRequires: python-module-setuptools
BuildRequires: python-module-setuptools

%description
A powerful, yet easy to implement thumbnailing
application for Django 1.4+

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
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 2.3-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Wed Mar 15 2017 Lenar Shakirov <snejok@altlinux.ru> 2.3-alt1
- Initial build for ALT


