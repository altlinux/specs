%define oname python-networkmanager

Name: python3-module-networkmanager
Version: 2.2
Release: alt1

License: zlib/libpng License
Group: Development/Python3
Url: https://github.com/seveas/python-networkmanager

Summary: Easy communication with NetworkManager

# Source-url: %__pypi_url %oname
Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-python3 rpm-build-intro

%description
python-networkmanager wraps NetworkManagers D-Bus interface so you can be less
verbose when talking to NetworkManager from python. All interfaces have been
wrapped in classes, properties are exposed as python properties and function
calls are forwarded to the correct interface.

%prep
%setup

%build
%python3_build

%install
%python3_install

%files
%python3_sitelibdir/*

%changelog
* Mon Apr 19 2021 Vitaly Lipatov <lav@altlinux.ru> 2.2-alt1
- initial build for ALT Sisyphus
