%global repo dde-session-ui

Name: deepin-session-ui
Version: 5.3.0.18
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
%__subst 's|default_background.jpg|default.png|' widgets/fullscreenbackground.cpp
%__subst 's|lib|libexec|' \
    misc/applications/deepin-toggle-desktop.desktop* \
    dde-osd/dde-osd_autostart.desktop \
    dde-osd/com.deepin.dde.osd.service \
    dde-osd/notification/files/com.deepin.dde.*.service* \
    dde-osd/dde-osd.pro \
    dde-welcome/com.deepin.dde.welcome.service \
    dde-welcome/dde-welcome.pro \
    dde-bluetooth-dialog/dde-bluetooth-dialog.pro \
    dde-touchscreen-dialog/dde-touchscreen-dialog.pro \
    dde-warning-dialog/com.deepin.dde.WarningDialog.service \
    dde-warning-dialog/dde-warning-dialog.pro \
    dde-offline-upgrader/dde-offline-upgrader.pro \
    dde-suspend-dialog/dde-suspend-dialog.pro \
    dnetwork-secret-dialog/dnetwork-secret-dialog.pro \
    dde-lowpower/dde-lowpower.pro
%__subst 's|%_libexecdir/dde-dock|%_libdir/dde-dock|' dde-notification-plugin/notifications/notifications.pro

%build
%qmake_qt5 \
    CONFIG+=nostrip \
    PREFIX=%prefix \
    PKGTYPE=rpm
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
%dir %_prefix/libexec/deepin-daemon
%_prefix/libexec/deepin-daemon/dde-bluetooth-dialog
%_prefix/libexec/deepin-daemon/dde-lowpower
%_prefix/libexec/deepin-daemon/dde-osd
%_prefix/libexec/deepin-daemon/dde-suspend-dialog
%_prefix/libexec/deepin-daemon/dde-warning-dialog
%_prefix/libexec/deepin-daemon/dde-touchscreen-dialog
%_prefix/libexec/deepin-daemon/dde-welcome
%_prefix/libexec/deepin-daemon/dnetwork-secret-dialog
%_datadir/%repo/
%_iconsdir/hicolor/*/apps/deepin-*
%_datadir/dbus-1/services/*.service
%_datadir/glib-2.0/schemas/com.deepin.dde.dock.module.notifications.gschema.xml
%dir %_libdir/dde-dock
%dir %_libdir/dde-dock/plugins
%_libdir/dde-dock/plugins/libnotifications.so

%changelog
* Thu Nov 05 2020 Leontiy Volodin <lvol@altlinux.org> 5.3.0.18-alt1
- New version (5.3.0.18) with rpmgs script.

* Wed Oct 07 2020 Leontiy Volodin <lvol@altlinux.org> 5.3.0.17-alt1
- New version (5.3.0.17) with rpmgs script.

* Mon Aug 17 2020 Leontiy Volodin <lvol@altlinux.org> 5.3.0.2-alt1
- Initial build for ALT Sisyphus (thanks fedora for this spec).
