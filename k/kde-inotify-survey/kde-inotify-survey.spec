%define rname kde-inotify-survey

Name: %rname
Version: 26.04.2
Release: alt1
%K6init man

Group: Development/Tools
Summary: Inotify state of the user
Url: http://www.kde.org
License: GPL-2.0-or-later

Provides: kde5-inotify-survey = %EVR
Obsoletes: kde5-inotify-survey < %EVR

Source: %rname-%version.tar
Patch1: alt-reduce-cmake-requires.patch

BuildRequires(pre): rpm-build-kf6
BuildRequires: qt6-declarative-devel
BuildRequires: extra-cmake-modules
BuildRequires: kf6-kauth-devel kf6-kcoreaddons-devel kf6-kdbusaddons-devel kf6-ki18n-devel kf6-knotifications-devel

%description
Have you ever wondered why dolphin or any other application stopped noticing file changes?
Chances are you ran out of inotify resources. kde-inotify-survey to the rescue!
Sporting a kded module to tell you when things are getting dicey and a CLI tool to inspect the state of affairs.

%prep
%setup -n %rname-%version
%patch1 -p1

%build
%K6build \
    #

%install
%K6install
%find_lang %name --with-kde --all-name

%files -f %name.lang
%doc LICENSES/*
%_K6bin/*
%_K6plug/kf6/kded/*inotify*.so
%_K6exec/kauth/kded-inotify-helper
%_K6notif/*inotify*.notifyrc
%_K6dbus_sys_srv/*inotify*.service
%_K6dbus/system.d/*inotify*.conf
%_datadir/polkit-1/actions/*inotify*.policy
%_datadir/metainfo/*.xml


%changelog
* Fri Jun 05 2026 Sergey V Turchin <zerg@altlinux.org> 26.04.2-alt1
- new version

* Sun May 10 2026 Sergey V Turchin <zerg@altlinux.org> 26.04.1-alt1
- new version

* Fri Mar 06 2026 Sergey V Turchin <zerg@altlinux.org> 25.12.3-alt1
- new version

* Fri Feb 06 2026 Sergey V Turchin <zerg@altlinux.org> 25.12.2-alt1
- new version

* Mon Jan 19 2026 Sergey V Turchin <zerg@altlinux.org> 25.12.1-alt1
- new version

* Wed Nov 19 2025 Sergey V Turchin <zerg@altlinux.org> 25.08.3-alt1
- new version

* Mon Oct 13 2025 Sergey V Turchin <zerg@altlinux.org> 25.08.2-alt1
- new version

* Tue Sep 23 2025 Sergey V Turchin <zerg@altlinux.org> 25.08.1-alt1
- new version

* Fri Jul 25 2025 Sergey V Turchin <zerg@altlinux.org> 25.04.3-alt1
- new version

* Wed Jun 11 2025 Sergey V Turchin <zerg@altlinux.org> 25.04.2-alt1
- new version

* Wed May 14 2025 Sergey V Turchin <zerg@altlinux.org> 25.04.1-alt1
- new version

* Tue Mar 11 2025 Sergey V Turchin <zerg@altlinux.org> 24.12.3-alt1
- new version

* Thu Mar 06 2025 Sergey V Turchin <zerg@altlinux.org> 24.12.2-alt1
- new version

* Wed Jan 29 2025 Sergey V Turchin <zerg@altlinux.org> 24.12.1-alt1
- new version

* Mon Nov 18 2024 Sergey V Turchin <zerg@altlinux.org> 24.08.3-alt1
- new version

* Thu Oct 17 2024 Sergey V Turchin <zerg@altlinux.org> 24.08.2-alt1
- initial build

