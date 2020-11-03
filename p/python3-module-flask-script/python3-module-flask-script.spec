%define oname Flask-Script
Name: python3-module-flask-script
Version: 2.0.6
Release: alt2

Summary: Flask extension to help writing external scripts for Flask applications

License: BSD
Group: Development/Python
Url: https://github.com/smurfix/flask-script

# Source-url: %__pypi_url %oname
Source: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-python3 rpm-build-intro

# for test
#py3_use flask
%py3_buildrequires pytest

%description
A set of utilities for use with the Flask framework
which provide decorators, classes and helpers for writing your own script commands.

Useful for creating command-line scripts, cronjobs etc outside your web application.

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
* Tue Nov 03 2020 Vitaly Lipatov <lav@altlinux.ru> 2.0.6-alt2
- cleanup spec

* Mon Apr 13 2020 Eugene Omelyanovich <regatio@etersoft.ru> 2.0.6-alt1
- new version (2.0.6) with rpmgs script
