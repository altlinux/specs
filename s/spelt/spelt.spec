Name: spelt
Version: 0.1.20170307
Release: alt1

Summary: Backup photo from VKontakte to local storage

Group: File tools
Url: https://github.com/amka/Spelt
License: MIT

Packager: Vitaly Lipatov <lav@altlinux.ru>

# Source-git: https://github.com/amka/Spelt.git
Source: %name-%version.tar

BuildRequires: python-module-requests >= 2.9.1
BuildRequires: python-module-vk_api >= 7.0

BuildArch: noarch

%description
Spelt is a small python application aimed to allow users
to backup their photo from https://vk.com to local storage.

%prep
%setup

%build
%python_build_debug

%install
%python_install
#mkdir -p %buildroot%_bindir/
#cat <<EOF  >%buildroot%_bindir/%name
##!/bin/sh
#python %python_sitelibdir/%name/
#EOF
#chmod 755 %buildroot%_bindir/%name


%files
%doc readme.md
%_bindir/%name
%python_sitelibdir/*

%changelog
* Fri Jun 16 2017 Vitaly Lipatov <lav@altlinux.ru> 0.1.20170307-alt1
- initial build for ALT Sisyphus
