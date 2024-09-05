%global repo dde-device-formatter

Name: deepin-device-formatter
Version: 0.0.1.16
Release: alt1
Summary: Device formatter for Deepin Desktop Environment
License: GPL-3.0+
Group: Graphical desktop/Other
Url: https://github.com/linuxdeepin/dde-device-formatter
Packager: Leontiy Volodin <lvol@altlinux.org>

Source: %url/archive/%version/%repo-%version.tar.gz

BuildRequires: gcc-c++ dqt5-base-devel dqt5-tools deepin-gettext-tools udisks2-qt5-devel dtk5-widget-devel dqt5-x11extras-devel
#Requires: icon-theme-hicolor

%description
%summary.

%prep
%setup -n %repo-%version

%build
export PATH=%_dqt5_bindir:$PATH
%qmake_dqt5 \
  DEFINES+="VERSION=%version" \
  CONFIG+=nostrip \
  VERSION=%version \
  LIB_INSTALL_DIR=%_libdir \
  QMAKE_RPATHDIR=%_dqt5_libdir \
  #
%make_build

%install
%makeinstall INSTALL_ROOT=%buildroot
%find_lang --with-qt %repo

%files -f %repo.lang
%doc README.md LICENSE
%_bindir/%repo
%_desktopdir/%repo.desktop
%dir %_datadir/%repo/
%dir %_datadir/%repo/translations/
%_datadir/%repo/translations/%repo.qm

%changelog
* Fri May 31 2024 Leontiy Volodin <lvol@altlinux.org> 0.0.1.16-alt1
- New version 0.0.1.16.
- Built via separate qt5 instead system (ALT #48138).

* Thu Mar 18 2021 Leontiy Volodin <lvol@altlinux.org> 0.0.1.6-alt1
- Initial build for ALT Sisyphus.
