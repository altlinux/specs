# If you want to suggest changes, please send PR on
# https://altlinux.space/alt-atomic/plymouth-theme to altlinux branch 

%define _unpackaged_files_terminate_build 1
%define theme_name atomic

Name: plymouth-theme-%theme_name
Version: 0.2
Release: alt1

Summary: Plymouth theme with Atomic animataed logo
License: GPL-2.0-only
Group: System/Base
Url: https://altlinux.space/alt-atomic/plymouth-theme
Vcs: https://altlinux.space/alt-atomic/plymouth-theme.git

Source: %name-%version.tar

Requires: plymouth-plugin-two-step
Requires: plymouth-plugin-script

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson

BuildArch: noarch

%description
%summary.

%prep
%setup

%build
%meson
%meson_build

%install
%meson_install

%files
%_datadir/plymouth/themes/%theme_name
%doc README.md

%changelog
* Thu May 14 2026 Vladimir Romanov <rirusha@altlinux.org> 0.2-alt1
- New version: 0.2.
- Fixed logo for ultra-wide resolutions.

* Mon Sep 15 2025 Vladimir Vaskov <rirusha@altlinux.org> 0.1-alt1
- Initial build.
