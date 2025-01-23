%global repo dde-device-formatter

Name: deepin-device-formatter
Version: 1.5.2
Release: alt1

Summary: Device formatter for Deepin Desktop Environment

License: GPL-3.0+
Group: Graphical desktop/Other
Url: https://github.com/linuxdeepin/dde-device-formatter
Vcs: git://github.com/linuxdeepin/dde-device-formatter.git

Packager: Leontiy Volodin <lvol@altlinux.org>

Source: %url/archive/%version/%repo-%version.tar.gz

BuildRequires: gcc-c++ cmake dqt6-base-devel dqt6-tools-devel deepin-gettext-tools dtk6-common-devel libdtk6widget-devel libudisks2-qt6-devel
#Requires: icon-theme-hicolor

%description
%summary.

%prep
%setup -n %repo-%version

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
* Thu Jan 23 2025 Leontiy Volodin <lvol@altlinux.org> 1.5.2-alt1
- New version 1.5.2.
- Added vcs tag.
- Switched to dqt6.

* Fri May 31 2024 Leontiy Volodin <lvol@altlinux.org> 0.0.1.16-alt1
- New version 0.0.1.16.
- Built via separate qt5 instead system (ALT #48138).

* Thu Mar 18 2021 Leontiy Volodin <lvol@altlinux.org> 0.0.1.6-alt1
- Initial build for ALT Sisyphus.
