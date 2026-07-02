%define rname plasma-browser-integration

Name: %rname
Version: 6.7.2
Release: alt1
%K6init

Group: Graphical desktop/KDE
Summary: KDE Plasma integration of web browsers
Url: http://www.kde.org
License: GPL-3.0-or-later

Provides: plasma5-browser-integration = %EVR
Obsoletes: plasma5-browser-integration < %EVR

Source: %rname-%version.tar
Patch2: alt-detect-more-browsers.patch

BuildRequires(pre): rpm-build-kf6
BuildRequires: libvulkan-devel
BuildRequires: extra-cmake-modules qt6-base-devel qt6-declarative-devel
BuildRequires: kf6-kcrash-devel kf6-kdbusaddons-devel kf6-kded kf6-kfilemetadata-devel
BuildRequires: kf6-ki18n-devel kf6-kio-devel kf6-knotifications-devel kf6-kpackage-devel kf6-krunner-devel
BuildRequires: kf6-purpose-devel kf6-kitemmodels-devel kf6-kstatusnotifieritem-devel
BuildRequires: plasma-workspace-devel plasma6-activities-devel

%description
This package aims to provide better integration of web browsers with the KDE Plasma desktop.

%prep
%setup -n %rname-%version
%patch2 -p1

# disable krunners by default
for f in host/*.desktop ; do
    sed -i 's|^X-KDE-PluginInfo-EnabledByDefault=.*$|X-KDE-PluginInfo-EnabledByDefault=false|' $f
done


%build
%K6build \
    -DMOZILLA_DIR:PATH=%_libdir/mozilla \
    #
#    -DINSTALL_CHROME_MANIFEST=ON \

%install
%K6install
%K6install_move data krunner
%find_lang %name --all-name

%files -f %name.lang
%doc LICENSES/*
%config %_sysconfdir/chromium/native-messaging-hosts/org.kde.plasma.browser_integration.json
%config %_sysconfdir/opt/chrome/native-messaging-hosts/org.kde.plasma.browser_integration.json
%config %_sysconfdir/opt/edge/native-messaging-hosts/org.kde.plasma.browser_integration.json
/usr/lib/librewolf/native-messaging-hosts/org.kde.plasma.browser_integration.json
/usr/lib/waterfox/native-messaging-hosts/org.kde.plasma.browser_integration.json
%_libdir/mozilla/native-messaging-hosts/org.kde.plasma.browser_integration.json
%_K6bin/plasma-browser-integration-host
%_K6plug/kf6/kded/browserintegration*.so
%_K6data/krunner/dbusplugins/plasma-runner-*.desktop
%_K6xdgapp/*browser_integration*.desktop
%changelog
* Wed Jul 01 2026 Sergey V Turchin <zerg@altlinux.org> 6.7.2-alt1
- new version

* Mon Jun 29 2026 Sergey V Turchin <zerg@altlinux.org> 6.7.1-alt1
- new version

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

