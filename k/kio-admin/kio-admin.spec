%define rname kio-admin

Name: %rname
Version: 26.04.2
Release: alt1
%K6init

Group: Graphical desktop/KDE
Summary: Manage files as administrator using the admin:/ KIO protocol
License: (GPL-2.0-only or GPL-3.0-only) and BSD-3-Clause and CC0-1.0 and FSFAP
Url: https://invent.kde.org/system/kio-admin
Vcs: https://invent.kde.org/system/kio-admin.git

Source: %rname-%version.tar

BuildRequires(pre): rpm-build-kf6
BuildRequires: extra-cmake-modules
BuildRequires: kf6-ki18n-devel
BuildRequires: kf6-kio-devel
BuildRequires: qt6-declarative-devel
BuildRequires: libpolkitqt6-qt6-devel
BuildRequires: libvulkan-devel

%description
kio-admin implements a new protocol "admin:///" which gives administrative access
to the entire system. This is achieved by talking, over dbus, with a root-level
helper binary that in turn uses existing KIO infrastructure to run file://
operations in root-scope.

%prep
%setup

%build
%K6cmake -DQT_MAJOR_VERSION=6
%K6build

%install
%K6install
%find_lang %name --with-kde --all-name

%files -f %name.lang
%doc README.* LICENSES/*
%_K6plug/kf6/kfileitemaction/*admin*.so
%_K6plug/kf6/kio/*admin*.so
%_K6exec/%name-helper
%_K6dbus/system.d/*admin*.conf
%_K6dbus_sys_srv/*admin*.service
%_datadir/metainfo/*admin*.xml
%_datadir/polkit-1/actions/*admin*.policy

%changelog
* Thu Jun 04 2026 Sergey V Turchin <zerg@altlinux.org> 26.04.2-alt1
- new version

* Fri May 08 2026 Sergey V Turchin <zerg@altlinux.org> 26.04.1-alt1
- new version

* Fri Mar 06 2026 Sergey V Turchin <zerg@altlinux.org> 25.12.3-alt1
- new version

* Fri Feb 06 2026 Sergey V Turchin <zerg@altlinux.org> 25.12.2-alt1
- new version

* Mon Jan 19 2026 Sergey V Turchin <zerg@altlinux.org> 25.12.1-alt1
- new version

* Tue Nov 18 2025 Sergey V Turchin <zerg@altlinux.org> 25.08.3-alt1
- new version

* Mon Oct 13 2025 Sergey V Turchin <zerg@altlinux.org> 25.08.2-alt1
- new version

* Mon Sep 22 2025 Sergey V Turchin <zerg@altlinux.org> 25.08.1-alt1
- new version

* Thu Jul 24 2025 Sergey V Turchin <zerg@altlinux.org> 25.04.3-alt1
- new version

* Tue Jun 10 2025 Sergey V Turchin <zerg@altlinux.org> 25.04.2-alt1
- new version

* Mon May 12 2025 Sergey V Turchin <zerg@altlinux.org> 25.04.1-alt1
- new version

* Mon Apr 21 2025 Sergey V Turchin <zerg@altlinux.org> 25.04.0-alt1
- new version

* Sun Mar 16 2025 Anton Kurachenko <srebrov@altlinux.org> 25.03.80-alt1
- New version 25.03.80.

* Tue Feb 11 2025 Anton Kurachenko <srebrov@altlinux.org> 24.12.2-alt1
- New version 24.12.2.

* Sun Jan 19 2025 Anton Kurachenko <srebrov@altlinux.org> 24.12.1-alt1
- New version 24.12.1.

* Mon Dec 23 2024 Anton Kurachenko <srebrov@altlinux.org> 24.12.0-alt1
- New version 24.12.0.

* Mon Nov 18 2024 Anton Kurachenko <srebrov@altlinux.org> 24.11.80-alt1
- Initial build for Sisyphus.
