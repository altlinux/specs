
%define _libexecdir %prefix/libexec
%add_findreq_skiplist %_datadir/sddm/scripts/Xsession

%define sddm_user sddm
%define x11confdir %_sysconfdir/X11
%define sddm_confdir %x11confdir/sddm

Name: sddm
Version: 0.13.0
Release: alt3
%K5init no_altplace man

Group: Graphical desktop/KDE
Summary: Lightweight QML-based display manager
Url: https://github.com/sddm/sddm
License: GPLv2+

Requires: xinitrc >= 2.4.43 xauth design-graphics

Source: %name-%version.tar
Source1: sddm.conf
Source2: tmpfiles-sddm.conf
Source10: sddm.pam
Source11: sddm-autologin.pam
Source12: sddm-greeter.pam
Source20: Xsetup
# SuSE
Patch1: create_pid_file.patch
# ALT
Patch100: alt-defaults.patch
Patch101: alt-branding.patch
Patch102: alt-wmsession.patch
Patch103: alt-systemctl-path.patch
Patch104: alt-fix-desktop-session-name.patch
Patch105: alt-fix-crash-configreader.patch

# Automatically added by buildreq on Thu Apr 02 2015 (-bi)
# optimized out: cmake-modules elfutils libEGL-devel libGL-devel libcloog-isl4 libqt5-core libqt5-dbus libqt5-gui libqt5-network libqt5-qml libqt5-quick libqt5-test libqt5-xml libstdc++-devel libxcb-devel pkg-config python-base python-module-BeautifulSoup python-module-PyStemmer python-module-Pygments python-module-google python-module-google-apputils python-module-matplotlib python-module-numpy python-module-pyExcelerator python-module-pyparsing python-module-pytz python-module-setuptools python-module-snowballstemmer python-module-zope.interface python-modules python-modules-compiler python-modules-email python-modules-encodings qt5-base-devel qt5-tools
#BuildRequires: cmake gcc-c++ glibc-devel-static libpam-devel libsystemd-devel nss-ldapd python-module-Reportlab python-module-cssselect python-module-docutils python-module-ecdsa python-module-ed25519 python-module-html5lib python-module-nss python-module-polib python-module-protobuf python-module-pycparser python-module-pycrypto python-module-pygobject3 python-module-pygraphviz python-module-xlwt qt5-declarative-devel qt5-tools-devel ruby ruby-stdlibs time xsetroot
BuildRequires(pre): rpm-build-kf5
BuildRequires: cmake gcc-c++ glibc-devel
BuildRequires: libpam-devel libsystemd-devel
BuildRequires: libxcb-devel libXau-devel libXdmcp-devel
BuildRequires: qt5-declarative-devel qt5-tools-devel
BuildRequires: python-module-docutils

%description
SDDM is a modern display manager for X11 aiming to be fast, simple and beatiful.
It uses modern technologies like QtQuick, which in turn gives the designer the
ability to create smooth, animated user interfaces.


%prep
%setup -n %name-%version
%patch1 -p1
%patch100 -p1 -b .defaults
%patch101 -p1
%patch102 -p1 -b .wmsession
%patch103 -p1
%patch104 -p1
%patch105 -p1

%build
%K5build \
    -DDATA_INSTALL_DIR=%_datadir/sddm \
    -DCMAKE_INSTALL_LIBEXECDIR=%_libexecdir/sddm \
    -DLIBEXEC_INSTALL_DIR=%_libexecdir/sddm \
    -DSYSTEMD_SYSTEM_UNIT_DIR=%_unitdir \
    -DENABLE_PAM:BOOL=ON \
    -DENABLE_JOURNALD=ON \
    -DMINIMUM_VT=1 \
    -DSESSION_COMMAND="/etc/X11/Xsession" \
    -DBUILD_MAN_PAGES=ON \
    -DSTATE_DIR="%_localstatedir/sddm" \
    -DRUNTIME_DIR="%_runtimedir/sddm" \
    -DPID_FILE="%_runtimedir/sddm.pid" \
    -DCONFIG_FILE="%sddm_confdir/sddm.conf" \
    -DQT_IMPORTS_DIR="%_qt5_qmldir" \
    -DDBUS_CONFIG_FILENAME="sddm_org.freedesktop.DisplayManager.conf" \
    -DUID_MIN=500 \
    -DUID_MAX=60000 \
    #

%install
%K5install

install -Dm 0644 %SOURCE1 %buildroot/%sddm_confdir/sddm.conf
install -Dpm 0644 %SOURCE2 %buildroot/lib/tmpfiles.d/sddm.conf
install -d %buildroot/%_runtimedir/sddm
install -d %buildroot/%_localstatedir/sddm

install -m 0755 %SOURCE20 %buildroot/%sddm_confdir/

install -p -m 0644 %SOURCE10 %buildroot%_sysconfdir/pam.d/sddm
install -p -m 0644 %SOURCE11 %buildroot%_sysconfdir/pam.d/sddm-autologin
#install -p -m 0644 %SOURCE12 %buildroot%_sysconfdir/pam.d/sddm-greeter

# create default theme
cp -ar %buildroot/%_datadir/sddm/themes/maui %buildroot/%_datadir/sddm/themes/default
sed -i 's|^background=.*|background=%_datadir/design/current/backgrounds/xdm.png|' %buildroot/%_datadir/sddm/themes/default/theme.conf
sed -i 's|^\(Name=.*\)|\1 Default|' %buildroot/%_datadir/sddm/themes/default/metadata.desktop
sed -i 's|^\(Description=.*\)|\1 Default|' %buildroot/%_datadir/sddm/themes/default/metadata.desktop

%pre
/usr/sbin/useradd -c 'SDDM User' -s /sbin/nologin -d %_localstatedir/sddm -r %sddm_user 2> /dev/null || :

%files
%doc COPYING* README*
%dir %sddm_confdir
%config(noreplace) %sddm_confdir/*
%config(noreplace) %_sysconfdir/pam.d/sddm*
%config(noreplace) %_sysconfdir/dbus-1/system.d/sddm_org.freedesktop.DisplayManager.conf
%_libexecdir/sddm/
%_bindir/sddm
%_bindir/sddm-greeter
%_K5qml/*
%_datadir/sddm/
%_man1dir/*.*
%_man5dir/*.*
%attr(0711,root,%sddm_user) %dir %_runtimedir/sddm
%attr(0775,%sddm_user,root) %dir %_localstatedir/sddm
%_unitdir/sddm.service
/lib/tmpfiles.d/sddm.conf

%changelog
* Thu Jan 28 2016 Sergey V Turchin <zerg@altlinux.org> 0.13.0-alt3
- add upstream fix for config reader (ALT#31737)

* Wed Jan 27 2016 Sergey V Turchin <zerg@altlinux.org> 0.13.0-alt2
- fix crash on read config

* Mon Jan 25 2016 Sergey V Turchin <zerg@altlinux.org> 0.13.0-alt1
- new version

* Mon Sep 07 2015 Sergey V Turchin <zerg@altlinux.org> 0.12.0-alt1
- new version
- using /usr/share/xsessions

* Thu Sep 03 2015 Sergey V Turchin <zerg@altlinux.org> 0.11.0-alt7
- fix wm sessions list

* Thu Aug 27 2015 Sergey V Turchin <zerg@altlinux.org> 0.11.0-alt6
- fix pam KWallet support

* Thu Aug 27 2015 Sergey V Turchin <zerg@altlinux.org> 0.11.0-alt5
- fix pam KWallet support

* Fri Aug 07 2015 Sergey V Turchin <zerg@altlinux.org> 0.11.0-alt4
- fix path to systemctl
- setup default theme
- hide nologin users
- don't setup initial backgroung color

* Mon Apr 20 2015 Sergey V Turchin <zerg@altlinux.org> 0.11.0-alt3
- don't uppercase xdg session name

* Fri Apr 03 2015 Sergey V Turchin <zerg@altlinux.org> 0.11.0-alt2
- fix apply patch

* Thu Apr 02 2015 Sergey V Turchin <zerg@altlinux.org> 0.11.0-alt1
- inittial build
