%def_disable clang

%define repo dde-session-ui

Name: deepin-session-ui
Version: 5.4.29
Release: alt1
Summary: Deepin desktop-environment - Session UI module
License: GPL-3.0+
Group: Graphical desktop/Other
Url: https://github.com/linuxdeepin/dde-session-ui
Packager: Leontiy Volodin <lvol@altlinux.org>

Source: %url/archive/%version/%repo-%version.tar.gz

%if_enabled clang
BuildRequires(pre): clang12.0-devel
%else
BuildRequires(pre): gcc-c++
%endif
BuildRequires: deepin-gettext-tools
BuildRequires: dtk5-widget-devel
BuildRequires: deepin-qt-dbus-factory-devel
BuildRequires: gsettings-qt-devel
BuildRequires: libgtk+2-devel
BuildRequires: lightdm-devel
BuildRequires: libsystemd-devel
BuildRequires: qt5-base-devel
BuildRequires: qt5-tools
BuildRequires: qt5-svg-devel
BuildRequires: qt5-x11extras-devel
BuildRequires: qt5-multimedia-devel
BuildRequires: libxcbutil-icccm-devel
BuildRequires: libXcursor-devel
BuildRequires: libXtst-devel
BuildRequires: libpam0-devel
BuildRequires: qt5-linguist
BuildRequires: deepin-dock-devel
BuildRequires: libgio-qt-devel
BuildRequires: libgtest-devel

%description
This project include those sub-project:
- dde-switchtogreeter: The tools to switch the user to login in.
- dde-license-dialog.
- dde-pixmix.
- dde-wm-chooser.
- dmemory-warning-dialog.

%prep
%setup -n %repo-%version
# sed -i 's|lrelease|lrelease-qt5|' translate_generation.sh
# sed -i 's|lupdate|lupdate-qt5|' lupdate.sh
#sed -i 's|default_background.jpg|deepin/desktop.jpg|' \
#    widgets/fullscreenbackground.cpp \
#    lightdm-deepin-greeter/logintheme.qrc \
#    dde-lock/logintheme.qrc
sed -i 's|/lib/deepin-daemon|/libexec/deepin-daemon|' \
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
sed -i 's|/usr/lib/dde-dock|%_libdir/dde-dock|' dde-notification-plugin/notifications/notifications.pro

%build
export PATH=%_qt5_bindir:$PATH
%qmake_qt5 \
%if_enabled clang
    QMAKE_STRIP= -spec linux-clang \
%endif
    CONFIG+=nostrip \
    PREFIX=%_prefix \
    PKGTYPE=rpm \
#     SYSTYPE=Desktop \
%ifarch mipsel mips64el sw_64
    SHUTDOWN_NO_QUIT=YES \
    LOCK_NO_QUIT=YES \
    DISABLE_DEMO_VIDEO=YES \
    DISABLE_TEXT_SHADOW=YES \
    DISABLE_ANIMATIONS=YES \
    USE_CURSOR_LOADING_ANI=YES \
%endif
#
    
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
* Fri Aug 20 2021 Leontiy Volodin <lvol@altlinux.org> 5.4.29-alt1
- New version (5.4.29).

* Wed Jul 14 2021 Leontiy Volodin <lvol@altlinux.org> 5.4.20-alt1
- New version (5.4.20).

* Tue May 18 2021 Leontiy Volodin <lvol@altlinux.org> 5.4.7-alt1
- New version (5.4.7) with rpmgs script.

* Fri Apr 09 2021 Leontiy Volodin <lvol@altlinux.org> 5.4.6-alt1
- New version (5.4.6) with rpmgs script.

* Thu Mar 25 2021 Leontiy Volodin <lvol@altlinux.org> 5.4.5-alt1
- New version (5.4.5) with rpmgs script.

* Tue Jan 26 2021 Leontiy Volodin <lvol@altlinux.org> 5.3.35-alt1
- New version (5.3.35) with rpmgs script.

* Tue Jan 12 2021 Leontiy Volodin <lvol@altlinux.org> 5.3.0.30-alt1
- New version (5.3.0.30) with rpmgs script.

* Fri Dec 04 2020 Leontiy Volodin <lvol@altlinux.org> 5.3.0.26-alt1
- New version (5.3.0.26) with rpmgs script.

* Wed Nov 18 2020 Leontiy Volodin <lvol@altlinux.org> 5.3.0.22-alt1
- New version (5.3.0.22) with rpmgs script.

* Thu Nov 05 2020 Leontiy Volodin <lvol@altlinux.org> 5.3.0.18-alt1
- New version (5.3.0.18) with rpmgs script.

* Wed Oct 07 2020 Leontiy Volodin <lvol@altlinux.org> 5.3.0.17-alt1
- New version (5.3.0.17) with rpmgs script.

* Mon Aug 17 2020 Leontiy Volodin <lvol@altlinux.org> 5.3.0.2-alt1
- Initial build for ALT Sisyphus (thanks fedora for this spec).
