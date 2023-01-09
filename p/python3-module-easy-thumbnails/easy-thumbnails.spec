%global pypi_name easy-thumbnails

%def_with check

Name: python3-module-%pypi_name
Version: 2.8.5
Release: alt1

Summary: Easy thumbnails for Django

Group: Development/Python3
License: BSD-3-Clause
Url: https://pypi.python.org/pypi/easy-thumbnails

Source: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-python3

%if_with check
BuildRequires: python3-module-django
BuildRequires: python3-module-django-dbbackend-sqlite3
BuildRequires: python3-module-Pillow
BuildRequires: python3-module-Reportlab
BuildRequires: python3-module-svglib
%endif

%description
A powerful, yet easy to implement thumbnailing
application for Django 1.8+

%prep
%setup

%build
%python3_build

%install
%python3_install

%check
# this runs 119 tests, which pyunittest or pytest won't make
export DJANGO_SETTINGS_MODULE='easy_thumbnails.tests.settings'
export PYTHONPATH=$PWD
%__python3 -m django test -v 2

%files
%python3_sitelibdir/easy_thumbnails
%python3_sitelibdir/easy_thumbnails-%version-py%_python3_version.egg-info

%changelog
* Mon Jan 09 2023 Grigory Ustinov <grenka@altlinux.org> 2.8.5-alt1
- Automatically updated to 2.8.5.

* Tue Dec 20 2022 Grigory Ustinov <grenka@altlinux.org> 2.8.4-alt1
- Automatically updated to 2.8.4.

* Wed Aug 03 2022 Grigory Ustinov <grenka@altlinux.org> 2.8.3-alt1
- Automatically updated to 2.8.3.

* Wed Apr 27 2022 Grigory Ustinov <grenka@altlinux.org> 2.8.1-alt1
- Build new version.
- Build with check.

* Thu Jul 15 2021 Grigory Ustinov <grenka@altlinux.org> 2.7-alt2
- Transferred on python3.

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
