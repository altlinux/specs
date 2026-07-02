%define rname plasma-login-manager

Name: %rname
Version: 6.7.2
Release: alt1

Group: Graphical desktop/KDE
Summary: QML based login manager from KDE
License: BSD-3-Clause and CC0-1.0 and (GPL-2.0-only or GPL-3.0-only) and GPL-2.0-or-later and LGPL-2.0-or-later and LGPL-2.1-or-later
Url: https://invent.kde.org/plasma/plasma-login-manager

Provides: service(graphical-login) = plasmalogin
Requires: xinitrc >= 2.4.43 xauth /usr/share/design/current
# for jxl support
Requires: kf6-kimageformats
Requires: kf6-filesystem
Requires: kf6-kauth-common
Requires(pre): shadow-utils
Requires: kwin

Source: %rname-%version.tar
Source10: alt.tar
Source11: plasmalogin.sysconfig
# sysusers config file. note these are shipped in the upstream tarball
# but we cannot use the files from the tarball for %pre scriptlet
# generation, so we duplicate them as source files for that purpose;
# this is an ugly hack that should be removed if it becomes possible.
# see https://lists.fedoraproject.org/archives/list/devel@lists.fedoraproject.org/thread/TFDMAU7KLMSQTKPJELHSM6PFVXIZ56GK/
Source12: plasmalogin.sysusers
Source13: plasmalogin.conf
Source14: Xsetup

Patch1001: plasmalogin-environment_file.patch
## Workaround for https://pagure.io/fedora-kde/SIG/issue/87
Patch1002: plasmalogin-rpmostree-tmpfiles-hack.patch

BuildRequires(pre): rpm-build-kf6
BuildRequires: extra-cmake-modules
BuildRequires: libpam-devel
BuildRequires: libXau-devel
BuildRequires: pkgconfig(libsystemd)
BuildRequires: pkgconfig(systemd)
BuildRequires: pkgconfig(xcb)
BuildRequires: pkgconfig(xcb-xkb)
BuildRequires: qt6-declarative-devel qt6-tools-devel qt6-shadertools-devel
BuildRequires: kf6-kconfig-devel kf6-kdbusaddons-devel kf6-kpackage-devel kf6-kwindowsystem-devel kf6-ki18n-devel 
BuildRequires: kf6-kconfig-devel kf6-kcmutils-devel kf6-kpackage-devel kf6-kwindowsystem-devel kf6-ki18n-devel 
BuildRequires: kf6-kauth-devel kf6-kio-devel kf6-kirigami-devel
BuildRequires: plasma6-lib-devel plasma6-layer-shell-qt-devel plasma-workspace-devel plasma6-libkscreen-devel
# verify presence to pull defaults from /etc/login.defs
BuildRequires: shadow-utils

%description
Plasma Login provides a display manager for KDE Plasma
and with an new frontend providing a greeter,
wallpaper plugin integration and a System Settings module (KCM).

%package -n kcm-plasmalogin
Group: Graphical desktop/KDE
Summary: KDE KCM for %name
Requires: systemsettings
Requires: polkit
%description -n kcm-plasmalogin
%summary.

%prep
%setup -n %rname-%version
pushd data/pam
tar xvf %SOURCE10
popd
cat %SOURCE14 >data/scripts/Xsetup
%patch1001 -p1
%patch1002 -p1

%build
%K6cmake \
    -DDATA_INSTALL_DIR:PATH=%_K6data/plasmalogin \
    -DUID_MIN=1000 \
    -DUID_MAX=32000 \
    -DPAM_OS_CONFIGURATION:STRING="alt" \
    -DPAM_CONFIG_DIR:STRING=%_sysconfdir/pam.d \
    -DLOGIN_DEFS_PATH:PATH=/dev/null \
    -DSESSION_COMMAND:PATH=/etc/X11/Xsession \
    -DWAYLAND_SESSION_COMMAND:PATH=/etc/plasmalogin/wayland-session \
    #
%K6make

%install
%K6install

%find_lang --with-kde plasma_login
%find_lang --with-kde kcm_plasmalogin

mkdir -p %buildroot/%_sysconfdir/plasmalogin.conf.d
mkdir -p %buildroot/%prefix/lib/plasmalogin/plasmalogin.conf.d

install -Dpm 644 %SOURCE11 %buildroot/%_sysconfdir/sysconfig/plasmalogin
install -Dpm 644 %SOURCE13 %buildroot/%_sysconfdir/plasmalogin.conf

mkdir -p %buildroot/run/plasmalogin
mkdir -p %buildroot/%_localstatedir/plasmalogin
mkdir -p %buildroot/%_sysconfdir/plasmalogin/

rm -r %buildroot/%_datadir/plasmalogin/scripts/Xsession
cp -a %buildroot/%_datadir/plasmalogin/scripts/* \
      %buildroot/%_sysconfdir/plasmalogin/
rm -rf %buildroot/%_datadir/plasmalogin/scripts/*

# conflict with lightdm
mv %buildroot/%_datadir/dbus-1/system.d/org.freedesktop.DisplayManager.conf \
   %buildroot/%_datadir/dbus-1/system.d/org.freedesktop.DisplayManager-plasmalogin.conf

mkdir -p -m 0755 %buildroot/%_presetdir
cat >%buildroot/%_presetdir/84-plasmalogin.preset <<__EOF__
enable plasmalogin.service
__EOF__

%pre
/usr/sbin/useradd -c 'PLASMALOGIN Greeter Account' -s /sbin/nologin -d %_localstatedir/plasmalogin -r plasmalogin 2> /dev/null ||:

%post
if [ $1 -eq 1 ] ; then
        SYSTEMCTL=/usr/bin/systemctl
        # Initial installation
        $SYSTEMCTL preset plasmalogin.service > /dev/null 2>&1 ||:
fi

%preun
if [ $1 -eq 0 ] ; then
        SYSTEMCTL=/usr/bin/systemctl
        # Package removal, not upgrade
        $SYSTEMCTL --no-reload disable plasmalogin.service > /dev/null 2>&1 ||:
        #$SYSTEMCTL stop plasmalogin.service > /dev/null 2>&1 ||:
fi

%files -f plasma_login.lang
%doc README.md LICENSE* LICENSES/*
%dir %_sysconfdir/plasmalogin/
%dir %_sysconfdir/plasmalogin.conf.d
%dir %prefix/lib/plasmalogin
%dir %prefix/lib/plasmalogin/plasmalogin.conf.d
%config(noreplace) %_sysconfdir/plasmalogin/*
%config(noreplace) %_sysconfdir/plasmalogin.conf
%config(noreplace) %_sysconfdir/sysconfig/plasmalogin
%config(noreplace) %_sysconfdir/pam.d/plasmalogin*
%_datadir/dbus-1/system.d/org.freedesktop.DisplayManager-plasmalogin.conf
%_K6bin/plasmalogin
%_K6bin/startplasma-login-wayland
%_bindir/plasma-login-wallpaper
%_K6libexecdir/plasmalogin-helper
%_K6libexecdir/plasmalogin-helper-start-x11user
%_K6libexecdir/plasma-login-greeter
%_tmpfilesdir/plasmalogin.conf
%_sysusersdir/plasmalogin.conf
%attr(0711, root, plasmalogin) %dir /run/plasmalogin
%attr(1770, plasmalogin, plasmalogin) %dir %_localstatedir/plasmalogin
%_unitdir/plasmalogin.service
%_presetdir/??-plasmalogin.preset
%_userunitdir/plasma-login.service
%_userunitdir/plasma-login-kwin_wayland.service
%_userunitdir/plasma-login-wayland.target
%_userunitdir/plasma-wallpaper.service
%_K6data/plasmalogin/

%files -n kcm-plasmalogin -f kcm_plasmalogin.lang
%_K6exec/kauth/kcmplasmalogin_authhelper
%_K6plug/plasma/kcms/systemsettings/kcm_plasmalogin.so
%_K6xdgapp/kcm_plasmalogin.desktop
%_datadir/dbus-1/system-services/org.kde.kcontrol.kcmplasmalogin.service
%_datadir/dbus-1/system.d/org.kde.kcontrol.kcmplasmalogin.conf
%_datadir/polkit-1/actions/org.kde.kcontrol.kcmplasmalogin.policy

%changelog
* Wed Jul 01 2026 Sergey V Turchin <zerg@altlinux.org> 6.7.2-alt1
- new version

* Mon Jun 29 2026 Sergey V Turchin <zerg@altlinux.org> 6.7.1-alt1
- new version

* Tue May 12 2026 Sergey V Turchin <zerg@altlinux.org> 6.6.5-alt1
- new version

* Mon Apr 20 2026 Sergey V Turchin <zerg@altlinux.org> 6.6.4-alt1
- initial build
