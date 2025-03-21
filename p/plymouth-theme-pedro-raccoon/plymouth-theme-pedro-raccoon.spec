%define _unpackaged_files_terminate_build 1
%define theme_name pedro-raccoon

Name: plymouth-theme-%theme_name
Version: 1.1
Release: alt1

Summary: This is a simple Plymouth theme with Pedro racoon meme
License: MIT
Group: System/Base

Url: https://github.com/FilaCo/pedro-raccoon-plymouth
Vcs: https://github.com/FilaCo/pedro-raccoon-plymouth
Source: %name-%version.tar

Requires: plymouth

BuildArch: noarch

%description
%summary.

%prep
%setup

%install
mkdir -p %buildroot%_datadir/plymouth/themes
mv %theme_name %buildroot%_datadir/plymouth/themes

%files
%_datadir/plymouth/themes/%theme_name
%doc README.md

%changelog
* Thu Mar 13 2025 David Sultaniiazov <x1z53@altlinux.org> 1.1-alt1
- Initial build
