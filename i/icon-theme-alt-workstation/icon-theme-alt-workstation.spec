%define _unpackaged_files_terminate_build 1
Name: icon-theme-alt-workstation
Version: 0.3
Release: alt1

Summary: ALT Workstation icon theme
Group: Graphics
URL: https://altlinux.org
License: GPL-3.0

Source: icon-theme-alt-workstation-%version.tar

BuildArch: noarch

Provides: alt-workstation-icon-theme = %EVR
Obsoletes: alt-workstation-icon-theme < %EVR

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson icon-naming-utils gtk4-update-icon-cache

%description
ALT Workstation icon for Alterator and other ALT app icons.

%prep
%setup

%build
%meson
%meson_build

%install
%meson_install
cp -r scalable %buildroot/%_iconsdir/AltWorkstation/
# cleanup from meson.build files
find %buildroot/%_iconsdir/AltWorkstation/ -name meson.build -exec rm -v {} \;

%files
%_iconsdir/AltWorkstation/

%changelog
* Sat Mar 01 2025 Semen Fomchenkov <armatik@altlinux.org> 0.3-alt1
- Removed images for basealt and altlinux icon (Closes: 53154)

* Mon Feb 10 2025 Semen Fomchenkov <armatik@altlinux.org> 0.2-alt1
- Fix overlap of a package with a different name (Closes: 52846)
- Complies with icon theme standards

* Mon Jan 27 2025 Semen Fomchenkov <armatik@altlinux.org> 0.1-alt1
- Initial build
