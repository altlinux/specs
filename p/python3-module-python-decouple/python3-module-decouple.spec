%define oname python-decouple

%def_with check

Name: python3-module-%oname
Version: 3.8
Release: alt1

Summary: Strict separation of config from code.

License: MIT
Group: Development/Python
Url: https://pypi.org/project/python-decouple/

# Source-url: %__pypi_url %oname
Source: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-python3 rpm-build-intro
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel
%if_with check
BuildRequires: python3-module-pytest
BuildRequires: python3-module-mock
%endif

%description
Decouple helps you to organize your settings
so that you can change parameters without having to redeploy your app.

It also makes it easy for you to:

store parameters in ini or .env files;
define comprehensive default values;
properly convert values to the correct data type;
have only one configuration module to rule all your instances.
It was originally designed for Django,
but became an independent generic tool for separating settings from code.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -v

%files
%doc README.*
%python3_sitelibdir/__pycache__/decouple.*
%python3_sitelibdir/decouple.py
%python3_sitelibdir/python_decouple-%version.dist-info

%changelog
* Mon Oct 23 2023 Anton Vyatkin <toni@altlinux.org> 3.8-alt1
- NMU: new version 3.8 (build with check)

* Tue Nov 03 2020 Vitaly Lipatov <lav@altlinux.ru> 3.3-alt2
- cleanup build

* Fri Jul 10 2020 Eugene Omelyanovich <regatio@etersoft.ru> 3.3-alt1
- new version (3.3) with rpmgs script

