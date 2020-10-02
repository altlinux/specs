%global repo dde-session-ui

Name: deepin-session-ui
Version: 5.3.0.2
Release: alt1
Summary: Deepin desktop-environment - Session UI module
License: GPL-3.0+
Group: Graphical desktop/Other
Url: https://github.com/linuxdeepin/dde-session-ui
Packager: Leontiy Volodin <lvol@altlinux.org>

Source: %url/archive/%version/%repo-%version.tar.gz

BuildRequires: gcc-c++ deepin-gettext-tools dtk5-widget-devel deepin-qt-dbus-factory-devel gsettings-qt-devel libgtk+2-devel lightdm-devel libsystemd-devel qt5-base-devel qt5-svg-devel qt5-x11extras-devel qt5-multimedia-devel libxcbutil-icccm-devel libXcursor-devel libXtst-devel libpam0-devel qt5-linguist deepin-dock-devel

%description
This project include those sub-project:

- dde-switchtogreeter: The tools to switch the user to login in.
- dde-license-dialog.
- dde-pixmix.
- dde-wm-chooser.
- dmemory-warning-dialog.

%prep
%setup -n %repo-%version
%__subst 's|lrelease|lrelease-qt5|' translate_generation.sh

%build
%qmake_qt5 PREFIX=%_prefix
%make_build

%install
%makeinstall INSTALL_ROOT=%buildroot

%files
%doc README.md
%doc LICENSE
%_bindir/dde-license-dialog
%_bindir/dde-pixmix
%_bindir/dde-switchtogreeter
%_bindir/dde-wm-chooser
%_bindir/dmemory-warning-dialog
%dir %_libexecdir/deepin-daemon
%_libexecdir/deepin-daemon/dde-bluetooth-dialog
%_libexecdir/deepin-daemon/dde-lowpower
%_libexecdir/deepin-daemon/dde-osd
%_libexecdir/deepin-daemon/dde-suspend-dialog
%_libexecdir/deepin-daemon/dde-warning-dialog
%_libexecdir/deepin-daemon/dde-touchscreen-dialog
%_libexecdir/deepin-daemon/dde-welcome
%_libexecdir/deepin-daemon/dnetwork-secret-dialog
%_datadir/%repo/
%_iconsdir/hicolor/*/apps/deepin-*
%_datadir/dbus-1/services/*.service
%_datadir/glib-2.0/schemas/com.deepin.dde.dock.module.notifications.gschema.xml
# Maybe deepin-dock-devel?
%dir %_libexecdir/dde-dock
%dir %_libexecdir/dde-dock/plugins
%_libexecdir/dde-dock/plugins/libnotifications.so

%changelog
* Mon Aug 17 2020 Leontiy Volodin <lvol@altlinux.org> 5.3.0.2-alt1
- Initial build for ALT Sisyphus (thanks fedora for this spec).
