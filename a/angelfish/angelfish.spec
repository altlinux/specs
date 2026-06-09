%define rname angelfish

Name: %rname
Version: 26.04.2
Release: alt1
%K6init

Group: Networking/WWW
Summary: Webbrowser designed for mobile devices
Url: https://apps.kde.org/angelfish
License: GPL-2.0-or-later

ExcludeArch: %not_qt6_qtwebengine_arches

Requires(post,preun): alternatives >= 0.2
#Requires: qt6-feedback
Provides: webclient x-www-browser
Provides: kde5-plasma-angelfish = %EVR
Obsoletes: kde5-plasma-angelfish < %EVR
Provides: kde5-angelfish = %EVR
Obsoletes: kde5-angelfish < %EVR

Source: %rname-%version.tar
Source1: po-ru-add.po
Patch1: alt-def-size.patch

BuildRequires(pre): rpm-build-kf6 rpm-macros-qt6-webengine
BuildRequires: qt6-declarative-devel qt6-svg-devel qt6-wayland-devel qt6-webengine-devel
BuildRequires: qcoro6-devel
#BuildRequires: qt6-feedback-devel
BuildRequires: futuresql-qt6-devel
BuildRequires: extra-cmake-modules kf6-kcoreaddons-devel kf6-ki18n-devel kf6-kirigami-devel kf6-purpose-devel
BuildRequires: kf6-kwindowsystem-devel kf6-kconfig-devel kf6-kdbusaddons-devel kf6-knotifications-devel
BuildRequires: kf6-qqc2-desktop-style-devel kf6-kcrash-devel
BuildRequires: kf6-kirigami-addons-devel
BuildRequires: desktop-file-utils

%description
This is the webbrowser designed to
- be used on small mobile devices,
- integrate well in Plasma workspaces


%prep
%setup -n %rname-%version
%patch1 -p1

msgcat --use-first po/ru/angelfish.po %SOURCE1 > po/ru/angelfish.po.tmp
cat po/ru/angelfish.po.tmp >po/ru/angelfish.po
rm -f po/ru/angelfish.po.tmp

%build
%K6build \
    -DBUILD_TESTING:BOOL=OFF \
    #

%install
%K6install

#install alternatives
install -d %buildroot/%_sysconfdir/alternatives/packages.d
cat > %buildroot/%_sysconfdir/alternatives/packages.d/%name <<__EOF__
%_bindir/xbrowser       %_K6bin/angelfish      56
%_bindir/x-www-browser       %_K6bin/angelfish      56
__EOF__

# add mime types categories
#desktop-file-install --mode=0755 --dir %buildroot/%_K6xdgapp \
#    --add-mime-type=x-scheme-handler/http \
#    --add-mime-type=x-scheme-handler/https \
#    %buildroot/%_K6xdgapp/org.kde.angelfish.desktop

%find_lang --all-name --with-qt %name

%files -f %name.lang
%config /%_sysconfdir/alternatives/packages.d/%name
%_K6bin/angelfish*
%_K6xdgapp/*angelfish*.desktop
%_K6icon/*/*/apps/*angelfish*.*
%_K6cfg/*angelfish*
%_K6notif/*angelfish*
%_datadir/metainfo/*.xml


%changelog
* Mon Jun 08 2026 Sergey V Turchin <zerg@altlinux.org> 26.04.2-alt1
- new version

* Sun May 10 2026 Sergey V Turchin <zerg@altlinux.org> 26.04.1-alt1
- new version

* Tue Mar 10 2026 Sergey V Turchin <zerg@altlinux.org> 25.12.3-alt1
- new version

* Sat Feb 07 2026 Sergey V Turchin <zerg@altlinux.org> 25.12.2-alt1
- new version

* Tue Jan 20 2026 Sergey V Turchin <zerg@altlinux.org> 25.12.1-alt1
- new version

* Wed Nov 19 2025 Sergey V Turchin <zerg@altlinux.org> 25.08.3-alt1
- new version

* Wed Sep 24 2025 Sergey V Turchin <zerg@altlinux.org> 25.08.1-alt1
- new version

* Mon Jun 23 2025 Sergey V Turchin <zerg@altlinux.org> 25.04.2-alt1
- new version

* Thu May 22 2025 Sergey V Turchin <zerg@altlinux.org> 25.04.1-alt1
- new version

* Wed Mar 19 2025 Sergey V Turchin <zerg@altlinux.org> 24.12.3-alt1
- new version

* Wed Feb 19 2025 Sergey V Turchin <zerg@altlinux.org> 24.12.2-alt1
- new version

* Mon Feb 03 2025 Sergey V Turchin <zerg@altlinux.org> 24.12.1-alt1
- new version

* Thu Oct 24 2024 Sergey V Turchin <zerg@altlinux.org> 24.08.2-alt1
- initial build

