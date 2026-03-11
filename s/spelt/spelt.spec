Name: spelt
Version: 0.3.1
Release: alt1

Summary: Backup photo from VKontakte to local storage

Group: File tools
Url: https://github.com/amka/Spelt
License: MIT

Packager: Vitaly Lipatov <lav@altlinux.ru>

# Source-git: https://github.com/amka/Spelt.git
Source: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools python3-module-wheel

%description
Spelt is a small python application aimed to allow users
to backup their photo from https://vk.com to local storage.

%prep
%setup
ln -sf readme.md README.md

%build
%pyproject_build

%install
%pyproject_install


%files
%doc readme.md
%_bindir/%name
%python3_sitelibdir/*

%changelog
* Wed Mar 11 2026 Vitaly Lipatov <lav@altlinux.ru> 0.3.1-alt1
- new version 0.3.1
- migrate to pyproject_build

* Sat Jun 17 2017 Vitaly Lipatov <lav@altlinux.ru> 0.1.20170307-alt2
- build as python3 program

* Fri Jun 16 2017 Vitaly Lipatov <lav@altlinux.ru> 0.1.20170307-alt1
- initial build for ALT Sisyphus
