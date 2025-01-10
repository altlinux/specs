%define rname kwrited

Name: %rname
Version: 6.2.5
Release: alt1
%K6init

Group: Graphical desktop/KDE
Summary: KDE Frameworks 6 Write Daemon
Url: http://www.kde.org
License: GPL-2.0-or-later

Provides: plasma5-kwrited = %EVR
Obsoletes: plasma5-kwrited < %EVR

Source: %rname-%version.tar

BuildRequires(pre): rpm-build-kf6
BuildRequires: libvulkan-devel
BuildRequires: extra-cmake-modules qt6-base-devel
BuildRequires: kf6-kcoreaddons-devel kf6-ki18n-devel kf6-knotifications-devel
BuildRequires: kf6-kpty-devel kf6-kwindowsystem-devel kf6-kdbusaddons-devel

%description
Watch for messages from local users sent with write(1) or wall(1)

%prep
%setup -n %rname-%version

%build
%K6build \
    -DBUILD_AS_EXECUTABLE:BOOT=ON \
    #
%install
%K6install
%find_lang %name --all-name

%files -f %name.lang
%doc LICENSES/*
%attr(2711,root,utempter) %_K6bin/kwrited
%_K6start/kwrited-autostart.desktop
%_K6notif/*writed*

%changelog
* Thu Jan 09 2025 Sergey V Turchin <zerg@altlinux.org> 6.2.5-alt1
- new version

* Tue Nov 26 2024 Sergey V Turchin <zerg@altlinux.org> 6.2.4-alt1
- new version

* Wed Nov 06 2024 Sergey V Turchin <zerg@altlinux.org> 6.2.3-alt1
- new version

* Mon Oct 28 2024 Sergey V Turchin <zerg@altlinux.org> 6.2.2-alt1
- new version

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

