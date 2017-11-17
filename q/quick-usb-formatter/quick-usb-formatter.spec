Name: quick-usb-formatter
Version: 0.6
Release: alt4%ubt
%K5init no_altplace

Group: Graphical desktop/KDE
Summary: A small KDE4 application to format usb sticks and devices
License: LGPLv2+
Url: http://kde-apps.org/content/show.php?content=137493
# git://git.chakraos.org/quick-usb-formatter.git

#Requires: dosfstools e2fsprog ntfs-3g
Requires: /sbin/mkfs.ntfs /sbin/mkfs.fat /sbin/mke2fs /sbin/mkfs.exfat /usr/sbin/mkfs.f2fs

Source: quick-usb-formatter-%version.tar
Source10: ru.po
Patch1: alt-path.patch
Patch2: alt-desktopfile.patch
Patch3: alt-shell.patch
Patch4: alt-kf5.patch

# Automatically added by buildreq on Thu Oct 06 2016 (-bi)
# optimized out: cmake cmake-modules elfutils gcc-c++ kf5-karchive-devel kf5-kauth-devel kf5-kbookmarks-devel kf5-kcodecs-devel kf5-kcompletion-devel kf5-kconfig-devel kf5-kconfigwidgets-devel kf5-kcoreaddons-devel kf5-kcrash-devel kf5-kdbusaddons-devel kf5-kdelibs4support kf5-kdesignerplugin-devel kf5-kdoctools kf5-kdoctools-devel kf5-kemoticons-devel kf5-kguiaddons-devel kf5-ki18n-devel kf5-kiconthemes-devel kf5-kinit-devel kf5-kitemmodels-devel kf5-kitemviews-devel kf5-kjobwidgets-devel kf5-knotifications-devel kf5-kparts-devel kf5-kservice-devel kf5-ktextwidgets-devel kf5-kunitconversion-devel kf5-kwidgetsaddons-devel kf5-kwindowsystem-devel kf5-kxmlgui-devel kf5-solid-devel kf5-sonnet-devel libEGL-devel libGL-devel libdbusmenu-qt52 libgpg-error libjson-c libqt5-core libqt5-dbus libqt5-gui libqt5-network libqt5-printsupport libqt5-svg libqt5-widgets libqt5-x11extras libqt5-xml libstdc++-devel libxcbutil-keysyms perl python-base python-modules python3 python3-base qt5-base-devel rpm-build-python3
#BuildRequires: extra-cmake-modules kf5-kdelibs4support-devel kf5-kdoctools-devel-static kf5-kio-devel python-module-google python3-dev ruby ruby-stdlibs
BuildRequires(pre): rpm-build-kf5 rpm-build-ubt
BuildRequires: extra-cmake-modules gettext qt5-base-devel
BuildRequires: kf5-kdelibs4support-devel kf5-kdoctools-devel-static kf5-kio-devel

%description
Quick Usb Formatter is a tiny app designed for enhance the usability of the
device notifier, an additional option for quick format usb sticks.

%prep
%setup -q
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1 -b .kf5

install -m 0644 %SOURCE10 translations/

%build
%K5build

%install
%K5install
%K5install_move data solid
%find_lang --with-kde quickusbformatter

%files -f quickusbformatter.lang
%doc README.txt
%_K5bin/quickusbformatter
%_K5libexecdir/kauth/qufhelper
%_K5data/solid/actions/*quickusbformatter*.desktop
%_K5xdgapp/quickusbformatter.desktop
%_K5conf_dbus_sysd/org.kde.auth.quf.conf
%_K5dbus_sys_srv/org.kde.auth.quf.service
%_datadir/polkit-1/actions/org.kde.auth.quf.policy


%changelog
* Fri Nov 17 2017 Sergey V Turchin <zerg@altlinux.org> 0.6-alt4%ubt
- port to KF5

* Thu Oct 06 2016 Sergey V Turchin <zerg@altlinux.org> 0.6-alt3
- update code from master branch

* Fri Jun 10 2016 Anton Farygin <rider@altlinux.ru> 0.6-alt2
- adapted for dostfstools-4.0

* Wed Nov 18 2015 Sergey V Turchin <zerg@altlinux.org> 0.6-alt1
- new version

* Tue Dec 17 2013 Sergey V Turchin <zerg@altlinux.org> 0.5-alt0.M70P.1
- built for M70P

* Tue Dec 17 2013 Sergey V Turchin <zerg@altlinux.org> 0.5-alt1
- initial build
