%add_findpackage_path %_kde4_bindir

Name: quick-usb-formatter
Version: 0.6
Release: alt3

Group: Graphical desktop/KDE
Summary: A small KDE4 application to format usb sticks and devices
License: LGPLv2+
Url: http://kde-apps.org/content/show.php?content=137493
# git://git.chakraos.org/quick-usb-formatter.git

#Requires: dosfstools e2fsprog ntfs-3g
Requires: /sbin/mkfs.ntfs /sbin/mkfs.fat /sbin/mke2fs /sbin/mkfs.exfat /usr/sbin/mkfs.f2fs

Source: quick-usb-formatter-%version.tar
Patch1: alt-path.patch
Patch2: alt-ru-po.patch
Patch3: alt-desktopfile.patch

BuildRequires: cmake gcc-c++ kde4libs-devel gettext kde-common-devel

%description
Quick Usb Formatter is a tiny app designed for enhance the usability of the
device notifier, an additional option for quick format usb sticks.

%prep
%setup -q
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
%K4build

%install
%K4install
mkdir -p %buildroot/%_bindir
mv %buildroot/%_kde4_bindir/* %buildroot/%_bindir/
%K4find_lang quickusbformatter

%files -f quickusbformatter.lang
%doc README.txt
%_K4bindir/quickusbformatter
%_K4exec/helper
%_K4apps/solid/actions/quickusbformatter_solid.desktop
%_K4xdg_apps/quickusbformatter.desktop
%_K4dbus_system/org.kde.auth.quf.conf
%_K4dbus_sys_services/org.kde.auth.quf.service
%_datadir/polkit-1/actions/org.kde.auth.quf.policy


%changelog
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
