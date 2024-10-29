%define rname liquidshell

%def_enable packagekit

%define liquidshell_sover 5
%define libliquidshell liquidshell%liquidshell_sover

Name: %rname
Version: 1.10.0
Release: alt1
%K6init no_altplace appdata

Group: Graphical desktop/KDE
Summary: KDE plasma dekstop shell alternative
Url: https://cgit.kde.org/liquidshell.git/
License: GPL-3.0

Requires: polkit-kde-plasma-desktop
Provides:  kde5-liquidshell = %EVR
Obsoletes: kde5-liquidshell < %EVR

Source: %rname-%version.tar
Patch2: alt-def-quicklaunch.patch
Patch3: alt-def-date-format.patch
Patch4: alt-panel-minimum-rows.patch
Patch5: alt-widgets-order.patch
Patch6: alt-def-wallpaper.patch
Patch7: alt-clean-device-notifier.patch
Patch8: alt-start-menu-icon.patch
Patch9: alt-start_liquidshell.patch

BuildRequires(pre): rpm-build-kf6
BuildRequires: desktop-file-utils
BuildRequires: libvulkan-devel
BuildRequires: extra-cmake-modules qt6-declarative-devel
BuildRequires: kf6-bluez-qt-devel kf6-karchive-devel kf6-kcmutils-devel kf6-kcrash-devel kf6-kdbusaddons-devel
BuildRequires: kf6-ki18n-devel kf6-kiconthemes-devel kf6-kio-devel kf6-knewstuff-devel kf6-knotifications-devel
BuildRequires: kf6-kwindowsystem-devel kf6-networkmanager-qt-devel kf6-kstatusnotifieritem-devel
%if_enabled packagekit
BuildRequires: libappstream-qt6-devel packagekit-qt6-devel
%endif

%description
Alternative desktop replacement for Plasma, using QtWidgets instead of QtQuick to ensure hardware acceleration is not required.

%prep
%setup -n %rname-%version
%patch2 -p1
%patch3 -p1
#%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1 -b .start

sed -i 's|@CMAKE_INSTALL_FULL_BINDIR@|%_bindir|' liquidshell-session.desktop
sed -i 's|@ALT_KDE_XDG_APPS_INSTALL_DIR@|%_K6xdgapp|' start_liquidshell

%build
%K6build

%install
%K6install

# install session
mkdir -p %buildroot/%_x11sysconfdir/wmsession.d/
cat <<__EOF__ >%buildroot/%_x11sysconfdir/wmsession.d/02LIQUIDSHELL
NAME=Liquidshell
DESC=Liquid Desktop Workspace
ICON=%_K6icon/hicolor/48x48/apps/liquidshell.png
EXEC=/usr/bin/start_liquidshell
SCRIPT:
exec /usr/bin/start_liquidshell
__EOF__
#install -Dm 0755 org.kde.liquidshell.desktop %buildroot/%_kf6_xdgapp/
install -Dm 0644 liquidshell-session.desktop %buildroot/%_datadir/xsessions/liquidshell-session.desktop
mkdir -p %buildroot/%_bindir/
[ -e %buildroot/%_bindir/start_liquidshell ] \
    || mv %buildroot/%_kf6_bin/start_liquidshell %buildroot/%_bindir/start_liquidshell

desktop-file-install --mode=0644 --dir %buildroot/%_datadir/xsessions/ \
	--set-key=Type \
	--set-value=Application \
	--set-icon=liquidshell \
	%buildroot/%_datadir/xsessions/liquidshell-session.desktop
sed -i 's|^Type=.*|Type=XSession|' %buildroot/%_datadir/xsessions/liquidshell-session.desktop

%find_lang %name --with-kde --all-name

%files -f %name.lang
%doc README stylesheet.css
%_K6bin/liquidshell
%_K6icon/*/*/apps/liquidshell.*
%_K6xdgapp/*liquidshell*.desktop
%_K6notif/*liquidshell*
%_x11sysconfdir/wmsession.d/02LIQUIDSHELL
%_bindir/start_liquidshell
%_datadir/xsessions/liquidshell-session.desktop
%_datadir/metainfo/*liquidshell*

%changelog
* Tue Oct 29 2024 Sergey V Turchin <zerg@altlinux.org> 1.10.0-alt1
- initial build
