Name: icon-theme-qogir
Version: 2025.11.04
Release: alt1
Epoch: 1

Summary: Qogir icon theme

License: GPL-3.0-only
Group: Graphical desktop/GNOME
Url: https://github.com/vinceliuice/Qogir-icon-theme
VCS: https://github.com/vinceliuice/Qogir-icon-theme

Packager: Leontiy Volodin <lvol@altlinux.org>

Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildArch: noarch

Conflicts: %name = 20190407

BuildRequires: gtk-update-icon-cache

%description
A flat colorful design icon theme for Qogir theme

%prep
%setup
%patch -p1

%install
mkdir -p %buildroot%_datadir/icons
./install.sh -d %buildroot%_datadir/icons
# fix unmets
# %%_datadir/icons/Qogir*/symbolic/status/audio-input-microphone-symbolic.svg
find %buildroot%_datadir/icons/Qogir*/symbolic/status/ \
  -maxdepth 0 -type d -exec cp -n \
  src/symbolic/devices/audio-input-microphone-symbolic.svg {} \;

%files
%doc AUTHORS COPYING README.md
%_datadir/icons/Qogir*

%changelog
* Fri May 15 2026 Leontiy Volodin <lvol@altlinux.org> 1:2025.11.04-alt1
- New version 2025.11.04.

* Mon Sep 08 2025 Leontiy Volodin <lvol@altlinux.org> 1:2025.02.15-alt1
- New version 2025.02.15.
- Conflicts with 20190407 version (ALT #45549).
- Fixed url tag.
- Added VCS tag.

* Sun Mar 12 2023 Artyom Bystrov <arbars@altlinux.org> 20230223-alt1
- update to new version

* Thu Apr 11 2019 Leontiy Volodin <lvol@altlinux.org> 20190407-alt1
- Initial build for ALT Sysiphus

