%define repo dde-session-shell

Name: deepin-session-shell
Version: 5.3.0.22
Release: alt1
Summary: Deepin desktop-environment - Session shell module
License: GPL-3.0+
Group: Graphical desktop/Other
Url: https://github.com/linuxdeepin/dde-session-shell
Packager: Leontiy Volodin <lvol@altlinux.org>

Source: %url/archive/%version/%repo-%version.tar.gz
Patch: deepin-session-shell_5.3_fix-build.patch

BuildRequires(pre): rpm-build-ninja
BuildRequires: gcc-c++ cmake qt5-tools qt5-base-devel deepin-qt-dbus-factory-devel libpam0-devel dtk5-widget-devel qt5-x11extras-devel qt5-multimedia-devel qt5-svg-devel libxcbutil-icccm-devel gsettings-qt-devel lightdm-devel
# deepin-gettext-tools dtk5-widget-devel deepin-qt-dbus-factory-devel gsettings-qt-devel libgtk+2-devel lightdm-devel libsystemd-devel qt5-base-devel qt5-svg-devel qt5-x11extras-devel qt5-multimedia-devel libxcbutil-icccm-devel libXcursor-devel libXtst-devel libpam0-devel qt5-linguist

%description
%summary.

%prep
%setup -n %repo-%version
%patch -p2
%__subst 's|lrelease|lrelease-qt5|' translate_generation.sh

%build
%cmake_insource -GNinja -DCMAKE_INSTALL_PREFIX=%_prefix
# warning: out of memory
ninja -j1
# %%ninja_build

%install
%ninja_install

%files
%config(noreplace) %_sysconfdir/deepin/greeters.d/00-xrandr
%config(noreplace) %_sysconfdir/deepin/greeters.d/lightdm-deepin-greeter
%_bindir/deepin-greeter
%_bindir/lightdm-deepin-greeter
%_bindir/dde-lock
%_bindir/dde-shutdown
%_datadir/%repo/
%_datadir/dbus-1/services/*.service
%_datadir/xgreeters/lightdm-deepin-greeter.desktop

%changelog
* Wed Oct 07 2020 Leontiy Volodin <lvol@altlinux.org> 5.3.0.22-alt1
- New version (5.3.0.22) with rpmgs script.

* Mon Aug 17 2020 Leontiy Volodin <lvol@altlinux.org> 5.3.0.5-alt1
- Initial build for ALT Sisyphus.
