%define oname Flask-Versioned
Name: python3-module-flask-versioned
Version: 0.9.4.git
Release: alt2

Summary: Flask plugin to rewrite file paths to add version info.

License: BSD
Group: Development/Python
Url: https://github.com/pilt/flask-versioned

# Source-url: %__pypi_url %oname
Source: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-python3 rpm-build-intro

#py3_use setuptools
%py3_use flask

%description
Add version info to file paths. The default configuration will prefix a
timestamp to and make the path absolute. Paths must be files, if a path is
unexisting or is a directory, an exception will be raised.

Typically used in templates to allow for really long expiration dates of
static content.

%prep
%setup

%build
%python3_build

%install
%python3_install

#check
#python3_test

%files
%python3_sitelibdir/*

%changelog
* Sun Nov 08 2020 Vitaly Lipatov <lav@altlinux.ru> 0.9.4.git-alt2
- drop setuptools requires

* Tue Nov 03 2020 Vitaly Lipatov <lav@altlinux.ru> 0.9.4.git-alt1
- cleanup spec

* Tue Apr 14 2020 Eugene Omelyanovich <regatio@etersoft.ru> 0.9.4.git-alt0
- initial build
