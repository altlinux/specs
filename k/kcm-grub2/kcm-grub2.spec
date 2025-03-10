%define rname kcm-grub2

%def_disable packagekit

%define liquidshell_sover 5
%define libliquidshell liquidshell%liquidshell_sover

Name: %rname
Version: 0.6.4
Release: alt20
%K6init

Group: Graphical desktop/KDE
Summary:  Configuring the GRUB2
Url: https://cgit.kde.org/kcm-grub2.git
License: GPLv3

Source: %rname-%version.tar
Source1: po.tar
Patch1: alt-no-details-btn.patch
Patch2: alt-wallpaper.patch

BuildRequires(pre): rpm-build-kf6
BuildRequires: extra-cmake-modules
BuildRequires: libImageMagick-devel
BuildRequires: qt6-declarative-devel
BuildRequires: kf6-kcmutils-devel kf6-ki18n-devel kf6-kio-devel

%description
A KDE Control Module for configuring the GRUB2 bootloader.


%prep
%setup -n %rname-%version -a1
%patch1 -p1
%patch2 -p1

%build
%K6build \
    -DQT_MAJOR_VERSION=6 \
    -DGRUB_INSTALL_EXE=/usr/sbin/grub-install \
    -DGRUB_MKCONFIG_EXE=/usr/sbin/grub-mkconfig \
    -DGRUB_PROBE_EXE=/usr/sbin/grub-probe \
    -DGRUB_SET_DEFAULT_EXE=/usr/sbin/grub-set-default \
    -DGRUB_MENU=/boot/grub/grub.cfg \
    -DGRUB_CONFIG=/etc/sysconfig/grub2 \
    -DGRUB_ENV=/boot/grub/grubenv \
    -DGRUB_MEMTEST=/etc/grub.d/39_memtest \
    #

%install
%K6install

#K6install_move data doc

%find_lang %name --with-kde --all-name

%files -f %name.lang
%doc README
%_K6exec/kauth/kcmgrub2helper
%_K6plug/plasma/kcms/systemsettings_qwidgets/*grub*.so
%_K6xdgapp/*grub*.desktop
%_datadir/polkit-1/actions/org.kde.kcontrol.kcmgrub2.policy
%_K6dbus_sys_srv/org.kde.kcontrol.kcmgrub2.service
%_K6dbus/system.d/org.kde.kcontrol.kcmgrub2.conf


%changelog
* Mon Mar 10 2025 Sergey V Turchin <zerg@altlinux.org> 0.6.4-alt20
- update from work/nico/qt6
- build with KF6

* Wed Nov 08 2023 Sergey V Turchin <zerg@altlinux.org> 0.6.4-alt9
- don't hardcode alternate placement

* Wed Apr 26 2023 Sergey V Turchin <zerg@altlinux.org> 0.6.4-alt8
- update to master branch 25898367

* Mon Oct 31 2022 Sergey V Turchin <zerg@altlinux.org> 0.6.4-alt7
- update to master branch bdb458c9

* Mon Mar 14 2022 Slava Aseev <ptrnine@altlinux.org> 0.6.4-alt6
- fix combobox colors

* Tue Mar 01 2022 Slava Aseev <ptrnine@altlinux.org> 0.6.4-alt5
- fix the inability to run from the System Settings

* Wed Sep 22 2021 Sergey V Turchin <zerg@altlinux.org> 0.6.4-alt4
- update from upstream/master

* Thu Nov 21 2019 Sergey V Turchin <zerg@altlinux.org> 0.6.4-alt3
- add GRUB_WALLPAPER support

* Thu Nov 14 2019 Sergey V Turchin <zerg@altlinux.org> 0.6.4-alt2
- remove Details button from info dialogs

* Mon Oct 28 2019 Sergey V Turchin <zerg@altlinux.org> 0.6.4-alt1
- initial build
