%global pypi_name easy-thumbnails

Name: python-module-%pypi_name
Version: 2.7
Release: alt1
Summary: Easy thumbnails for Django
Group: Development/Python
License: BSD-3-Clause
Url: https://pypi.python.org/pypi/easy-thumbnails
Source: %name-%version.tar

BuildArch: noarch

BuildRequires: python-devel
BuildRequires: python-module-setuptools

%description
A powerful, yet easy to implement thumbnailing
application for Django 1.8+

%prep
%setup

%build
%python_build

%install
%python_install

%files
%python_sitelibdir/*

%changelog
* Thu Jan 09 2020 Grigory Ustinov <grenka@altlinux.org> 2.7-alt1
- Build new version.
- Fix license.

* Tue Mar 05 2019 Grigory Ustinov <grenka@altlinux.org> 2.6-alt1
- Build new version.

* Wed Dec 26 2018 Grigory Ustinov <grenka@altlinux.org> 2.5-alt1
- Build new version.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 2.3-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Wed Mar 15 2017 Lenar Shakirov <snejok@altlinux.ru> 2.3-alt1
- Initial build for ALT
