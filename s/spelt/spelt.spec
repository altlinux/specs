Name: spelt
Version: 0.1.20170307
Release: alt2

Summary: Backup photo from VKontakte to local storage

Group: File tools
Url: https://github.com/amka/Spelt
License: MIT

Packager: Vitaly Lipatov <lav@altlinux.ru>

# Source-git: https://github.com/amka/Spelt.git
Source: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools

BuildRequires: python3-module-requests >= 2.9.1
BuildRequires: python3-module-vk_api >= 7.0

BuildRequires: python-tools-2to3

Requires: python3-module-requests >= 2.9.1

%description
Spelt is a small python application aimed to allow users
to backup their photo from https://vk.com to local storage.

%prep
%setup

%build
2to3 -w spelt
%python3_build_debug

%install
%python3_install
#mkdir -p %buildroot%_bindir/
#cat <<EOF  >%buildroot%_bindir/%name
##!/bin/sh
#python %python_sitelibdir/%name/
#EOF
#chmod 755 %buildroot%_bindir/%name


%files
%doc readme.md
%_bindir/%name
%python3_sitelibdir/*

%changelog
* Sat Jun 17 2017 Vitaly Lipatov <lav@altlinux.ru> 0.1.20170307-alt2
- build as python3 program

* Fri Jun 16 2017 Vitaly Lipatov <lav@altlinux.ru> 0.1.20170307-alt1
- initial build for ALT Sisyphus
