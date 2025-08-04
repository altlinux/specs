%define _unpackaged_files_terminate_build 1
%define theme_name spinner-alt

Name: plymouth-theme-%theme_name
Version: 0.2
Release: alt1

Summary: Simple Plymouth theme with ADW Spinner
License: GPL-2.0-only
Group: System/Base

Url: https://altlinux.space/x1z53/plymouth-theme-spinner-alt
Vcs: https://altlinux.space/x1z53/plymouth-theme-spinner-alt
Source: %name-%version.tar

Requires: plymouth-plugin-two-step

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
* Sat Aug 02 2025 x1z53 <x1z53@altlinux.org> 0.2-alt1
- Initial build
