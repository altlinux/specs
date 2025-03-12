%define _unpackaged_files_terminate_build 1
%def_without check

Name: minegrub-theme
Version: 3.1.0
Release: alt1

Summary: A Grub Theme in the style of Minecraft!
License: MIT
Group: System/Configuration/Boot and Init
Url: https://github.com/Lxtharia/minegrub-theme
Vcs: https://github.com/Lxtharia/minegrub-theme
BuildArch: noarch

Source: %name-%version.tar

Requires: grub-common

%description
%summary

To use this theme it is better to install grub customiser otherwise
install it manually following developer's instructions which is not
recommended for security reasons.

%prep
%setup

%install
mkdir -pv %buildroot/boot/grub/themes/
mv -v ./minegrub %buildroot/boot/grub/themes/

%files
%doc LICENSE README.md
/boot/grub/themes/minegrub/

%changelog
* Mon Mar 10 2025 Sergey Zhidkih <rx1513@altlinux.org> 3.1.0-alt1
- Initial build.
