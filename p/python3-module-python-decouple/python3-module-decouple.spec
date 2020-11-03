%define oname python-decouple
Name: python3-module-%oname
Version: 3.3
Release: alt2

Summary: Strict separation of config from code.

License: MIT License
Group: Development/Python
Url: https://pypi.org/project/python-decouple/

# Source-url: %__pypi_url %oname
Source: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-python3 rpm-build-intro

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
%python3_build

%install
%python3_install

%files
%python3_sitelibdir/*

%changelog
* Tue Nov 03 2020 Vitaly Lipatov <lav@altlinux.ru> 3.3-alt2
- cleanup build

* Fri Jul 10 2020 Eugene Omelyanovich <regatio@etersoft.ru> 3.3-alt1
- new version (3.3) with rpmgs script

