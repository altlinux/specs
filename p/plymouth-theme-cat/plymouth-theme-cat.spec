%define _unpackaged_files_terminate_build 1
%define theme_name PlymouthTheme-Cat

Name: plymouth-theme-cat
Version: 20250109
Release: alt1

Summary: This is a Plymouth theme created that can be used in Linux Distributions
License: GPL-3.0-only
Group: System/Base

Url: https://github.com/krishnan793/PlymouthTheme-Cat
Vcs: https://github.com/krishnan793/PlymouthTheme-Cat
Source: %name-%version.tar

Requires: plymouth

BuildArch: noarch

%description
%summary.

%prep
%setup

%install
mkdir -p %buildroot%_datadir/plymouth/themes/%theme_name
mv *.script *.plymouth *.png %buildroot%_datadir/plymouth/themes/%theme_name

%files
%_datadir/plymouth/themes/%theme_name
%doc README.md

%changelog
* Fri Mar 21 2025 David Sultaniiazov <x1z53@altlinux.org> 20250109-alt1
- Initial build
