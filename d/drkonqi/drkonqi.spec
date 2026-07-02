%define rname drkonqi
%define _sysd_unitdir /usr/lib/systemd/system
%define _sysd_userunitdir /usr/lib/systemd/user
%add_python3_path %_K6data/drkonqi/gdb/python/gdb_preamble/
%add_python3_req_skip gdb gdb.FrameDecorator

Name: %rname
Version: 6.7.2
Release: alt1
#Epoch: 1
%K6init

Group: Graphical desktop/KDE
Summary: KDE Crash Handler
Url: http://www.kde.org
License: GPL-2.0-or-later

Requires: kf6-kirigami
Requires: /usr/bin/coredumpctl
#Requires: python3(psutil) python3(pygdbmi) python3(sentry_sdk)

#Provides: plasma5-drkonqi = 1:%version-%release
#Obsoletes: plasma5-drkonqi < 1:%version-%release

Source: %rname-%version.tar
Patch1: alt-enable-debuginfod-support.patch

BuildRequires(pre): rpm-build-kf6 rpm-macros-systemd
BuildRequires: rpm-build-python3
BuildRequires: extra-cmake-modules qt6-base-devel qt6-declarative-devel
BuildRequires: libvulkan-devel
BuildRequires: libssl-devel libsystemd-devel
BuildRequires: pkgconfig(polkit-qt6-1)
BuildRequires: kf6-kcrash-devel kf6-ki18n-devel kf6-kidletime-devel kf6-kio-devel kf6-knotifications-devel
BuildRequires: kf6-kwallet-devel kf6-kwindowsystem-devel kf6-syntax-highlighting-devel kf6-kitemmodels-devel
BuildRequires: kf6-kpackage-devel kf6-kdeclarative-devel kf6-kstatusnotifieritem-devel

%description
The KDE Crash Handler.

%package -n plasma5-drkonqi
Group: Graphical desktop/KDE
Summary: Compatibility package
Epoch: 1
Requires: drkonqi >= %version-%release
%description -n plasma5-drkonqi
Compatibility package.

%prep
%setup -n %rname-%version
%autopatch -p1

%build
%K6build \
    -DWITH_PYTHON_VENDORING:BOOL=OFF \
    -DWITH_GLOBAL_NOTIFIER:BOOL=OFF \
    #

%install
%K6install
%K6install_move data drkonqi
%find_lang %name --all-name

%files -n plasma5-drkonqi

%files -f %name.lang
%doc LICENSES/*
%_K6bin/drkonqi*
%_K6exec/drkonqi*
%_K6libexecdir/drkonqi*
#%_K6plug/drkonqi/
%_K6data/drkonqi/
%_K6xdgapp/*drkonqi*.desktop
%_sysd_unitdir/*drkonqi*
%_sysd_unitdir/*.wants/*drkonqi*
%_sysd_userunitdir/*drkonqi*
%_sysd_userunitdir/*.wants/*drkonqi*
%_datadir/qlogging-categories6/*.*categories
%_datadir/polkit-1/actions/*drkonqi*.policy
%_K6dbus_sys_srv/*drkonqi*.service
%_K6dbus/system.d/*drkonqi*.conf
%_K6notif/*drkonqi*.notifyrc

%changelog
* Wed Jul 01 2026 Sergey V Turchin <zerg@altlinux.org> 6.7.2-alt1
- new version

* Mon Jun 29 2026 Sergey V Turchin <zerg@altlinux.org> 6.7.1-alt1
- new version

* Tue May 19 2026 Sergey V Turchin <zerg@altlinux.org> 6.6.5-alt3
- clean deps

* Mon May 18 2026 Sergey V Turchin <zerg@altlinux.org> 6.6.5-alt2
- build without global notifier

* Tue May 12 2026 Sergey V Turchin <zerg@altlinux.org> 6.6.5-alt1
- new version

* Thu Apr 09 2026 Sergey V Turchin <zerg@altlinux.org> 6.6.4-alt1
- new version

* Mon Mar 30 2026 Sergey V Turchin <zerg@altlinux.org> 6.6.3-alt1
- new version

* Wed Mar 11 2026 Sergey V Turchin <zerg@altlinux.org> 6.5.6-alt1
- new version

* Thu Jan 15 2026 Sergey V Turchin <zerg@altlinux.org> 6.5.5-alt1
- new version

* Wed Dec 10 2025 Sergey V Turchin <zerg@altlinux.org> 6.5.4-alt1
- new version

* Tue Nov 18 2025 Sergey V Turchin <zerg@altlinux.org> 6.5.3-alt1
- new version

* Thu Nov 13 2025 Sergey V Turchin <zerg@altlinux.org> 6.5.2-alt1
- new version

* Wed Nov 12 2025 Sergey V Turchin <zerg@altlinux.org> 6.4.6-alt1
- new version

* Tue Sep 16 2025 Sergey V Turchin <zerg@altlinux.org> 6.4.5-alt1
- new version

* Fri Aug 22 2025 Sergey V Turchin <zerg@altlinux.org> 6.4.4-alt1
- new version

* Tue Jul 15 2025 Sergey V Turchin <zerg@altlinux.org> 6.4.3-alt1
- new version

* Tue Jul 08 2025 Sergey V Turchin <zerg@altlinux.org> 6.4.2-alt1
- new version

* Wed May 07 2025 Sergey V Turchin <zerg@altlinux.org> 6.3.5-alt1
- new version

* Wed Apr 02 2025 Sergey V Turchin <zerg@altlinux.org> 6.3.4-alt1
- new version

* Wed Mar 12 2025 Sergey V Turchin <zerg@altlinux.org> 6.3.3-alt1
- new version

* Wed Feb 26 2025 Sergey V Turchin <zerg@altlinux.org> 6.3.2-alt1
- new version

* Wed Feb 19 2025 Sergey V Turchin <zerg@altlinux.org> 6.3.1-alt1
- new version

* Fri Feb 14 2025 Sergey V Turchin <zerg@altlinux.org> 6.3.0-alt1
- new version

* Thu Jan 09 2025 Sergey V Turchin <zerg@altlinux.org> 6.2.5-alt1
- new version

* Tue Nov 26 2024 Sergey V Turchin <zerg@altlinux.org> 6.2.4-alt1
- new version

* Tue Nov 12 2024 Ajrat Makhmutov <rauty@altlinux.org> 6.2.3-alt2
- Enable ALT debuginfod server support for character resolution in KCrash.

* Wed Nov 06 2024 Sergey V Turchin <zerg@altlinux.org> 6.2.3-alt1
- new version

* Mon Oct 28 2024 Sergey V Turchin <zerg@altlinux.org> 6.2.2-alt1
- new version

* Mon Oct 21 2024 Sergey V Turchin <zerg@altlinux.org> 6.1.5-alt2
- workaround against broken systemd.pc

* Tue Sep 10 2024 Sergey V Turchin <zerg@altlinux.org> 6.1.5-alt1
- new version

* Thu Aug 15 2024 Sergey V Turchin <zerg@altlinux.org> 6.1.4-alt1
- new version

* Thu Jul 11 2024 Sergey V Turchin <zerg@altlinux.org> 6.1.2-alt1
- new version

* Wed Jun 26 2024 Sergey V Turchin <zerg@altlinux.org> 6.1.1-alt1
- new version

* Tue Jun 25 2024 Sergey V Turchin <zerg@altlinux.org> 6.1.0-alt1
- initial build

