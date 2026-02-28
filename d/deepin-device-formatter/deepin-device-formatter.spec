%global repo dde-device-formatter

Name: deepin-device-formatter
Version: 1.5.11
Release: alt2

Summary: Device formatter for Deepin Desktop Environment

License: GPL-3.0+
Group: Graphical desktop/Other
Url: https://github.com/linuxdeepin/dde-device-formatter
VCS: https://github.com/linuxdeepin/dde-device-formatter

Packager: Leontiy Volodin <lvol@altlinux.org>

# Source-url: https://github.com/linuxdeepin/dde-device-formatter/archive/%version/%repo-%version.tar.gz
Source: %repo-%version.tar
Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-macros-dqt6
BuildRequires: gcc-c++ cmake dqt6-base-devel dqt6-tools-devel deepin-gettext-tools dtk6-common-devel libdtk6widget-devel libudisks2-qt6-devel libwayland-client-devel
BuildRequires: libdqt6-concurrent vulkan-headers libcups-devel

Requires: libdqt6-gui = %_dqt6_version
#Requires: icon-theme-hicolor

%description
%summary.

%prep
%setup -n %repo-%version
%patch -p1

%build
export LC_ALL=C.UTF-8
%DQ6build \
  -DVERSION=%version \
  -DLIB_INSTALL_DIR=%_libdir \
#

%install
%DQ6install
%find_lang --with-qt %repo

%files -f %repo.lang
%doc README.md LICENSE
%_bindir/%repo
%_desktopdir/%repo.desktop
%dir %_datadir/%repo/
%dir %_datadir/%repo/translations/
%_datadir/%repo/translations/%repo.qm

%changelog
* Sat Feb 28 2026 Leontiy Volodin <lvol@altlinux.org> 1.5.11-alt2
- Fixed build on shrinked dqt6.10.

* Mon Jan 26 2026 Leontiy Volodin <lvol@altlinux.org> 1.5.11-alt1
- New version 1.5.11.
- Fixed build on dtk 6.7.31.

* Thu Jan 23 2025 Leontiy Volodin <lvol@altlinux.org> 1.5.2-alt1
- New version 1.5.2.
- Added vcs tag.
- Switched to dqt6.

* Fri May 31 2024 Leontiy Volodin <lvol@altlinux.org> 0.0.1.16-alt1
- New version 0.0.1.16.
- Built via separate qt5 instead system (ALT #48138).

* Thu Mar 18 2021 Leontiy Volodin <lvol@altlinux.org> 0.0.1.6-alt1
- Initial build for ALT Sisyphus.
