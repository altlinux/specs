%define rname plasma-browser-integration

Name: %rname
Version: 6.1.4
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
%_libdir/mozilla/native-messaging-hosts/org.kde.plasma.browser_integration.json
%_K6bin/plasma-browser-integration-host
%_K6plug/kf6/kded/browserintegrationreminder.so
%_K6data/krunner/dbusplugins/plasma-runner-*.desktop
%_K6xdgapp/*browser_integration*.desktop

%changelog
* Thu Aug 15 2024 Sergey V Turchin <zerg@altlinux.org> 6.1.4-alt1
- new version

* Thu Jul 11 2024 Sergey V Turchin <zerg@altlinux.org> 6.1.2-alt1
- new version

* Wed Jun 26 2024 Sergey V Turchin <zerg@altlinux.org> 6.1.1-alt1
- new version

* Tue Jun 25 2024 Sergey V Turchin <zerg@altlinux.org> 6.1.0-alt1
- initial build

