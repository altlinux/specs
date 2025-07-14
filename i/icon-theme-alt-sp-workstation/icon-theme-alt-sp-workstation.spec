%define _unpackaged_files_terminate_build 1
Name: icon-theme-alt-sp-workstation
Version: 0.2
Release: alt1

Summary: ALT SP Workstation icon theme
Group: Graphics
URL: https://altlinux.org
License: GPL-3.0

Source: icon-theme-alt-sp-workstation-%version.tar

BuildArch: noarch

Requires: icon-theme-morewaita
Requires: icon-theme-adwaita

%description
ALT Workstation icon for Alterator and other ALT app icons.

%prep
%setup

%install
mkdir -p %buildroot/%_iconsdir/ALT_SP_Workstation
cp -r index.theme scalable %buildroot/%_iconsdir/ALT_SP_Workstation/

%files
%_iconsdir/ALT_SP_Workstation/

%changelog
* Mon Jul 14 2025 Anton Midyukov <antohami@altlinux.org> 0.2-alt1
- Update alt-distro-logo.

* Tue Jul 08 2025 Anton Midyukov <antohami@altlinux.org> 0.1-alt1
- Initial build.
