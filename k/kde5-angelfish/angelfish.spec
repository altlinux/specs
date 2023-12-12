%define rname angelfish

%define sover 3
%define libfalkonprivate libfalkonprivate%sover

Name: kde5-%rname
Version: 23.08.4
Release: alt1
%K5init

Summary: Webbrowser designed for mobile devices
License: GPLv3+
Group: Networking/WWW
Url: https://anongit.kde.org/plasma-angelfish.git

ExcludeArch: %not_qt5_qtwebengine_arches

Requires(post,preun): alternatives >= 0.2
Requires: qt5-feedback
Provides: webclient x-www-browser
Provides: kde5-plasma-angelfish = %EVR
Obsoletes: kde5-plasma-angelfish < %EVR

Source: %rname-%version.tar
Source1: po-ru-add.po
Patch1: alt-def-size.patch
Patch2: alt-i18n.patch

# Automatically added by buildreq on Tue Feb 25 2020 (-bi)
# optimized out: alternatives cmake cmake-modules elfutils fontconfig gcc-c++ glibc-kernheaders-generic glibc-kernheaders-x86 libgdk-pixbuf libglvnd-devel libgpg-error libopencore-amrnb0 libopencore-amrwb0 libp11-kit libqt5-core libqt5-gui libqt5-network libqt5-positioning libqt5-qml libqt5-quick libqt5-quickcontrols2 libqt5-svg libqt5-test libqt5-webchannel libqt5-webengine libqt5-webenginecore libqt5-widgets libsasl2-3 libstdc++-devel libx265-176 python-modules python2-base python3 python3-base qt5-base-devel qt5-declarative-devel qt5-location-devel qt5-webchannel-devel rpm-build-python3 sh4
#BuildRequires: appstream extra-cmake-modules git-core kf5-kcoreaddons-devel kf5-ki18n-devel kf5-kirigami-devel kf5-purpose-devel libssl-devel python3-dev qt5-quickcontrols2-devel qt5-svg-devel qt5-wayland-devel qt5-webengine-devel
BuildRequires(pre): rpm-build-kf5 rpm-macros-qt5-webengine
BuildRequires: qt5-quickcontrols2-devel qt5-svg-devel qt5-wayland-devel qt5-webengine-devel
BuildRequires: qt5-feedback-devel qcoro5-devel
BuildRequires: futuresql-qt5-devel
BuildRequires: extra-cmake-modules kf5-kcoreaddons-devel kf5-ki18n-devel kf5-kirigami-devel kf5-purpose-devel
BuildRequires: kf5-kwindowsystem-devel kf5-kconfig-devel kf5-kdbusaddons-devel kf5-knotifications-devel
BuildRequires: kf5-kirigami-addons-devel kf5-qqc2-desktop-style-devel
BuildRequires: desktop-file-utils

%description
This is the webbrowser designed to
- be used on small mobile devices,
- integrate well in Plasma workspaces


%prep
%setup -n %rname-%version
%patch1 -p1
%patch2 -p1

msgcat --use-first po/ru/angelfish.po %SOURCE1 > po/ru/angelfish.po.tmp
cat po/ru/angelfish.po.tmp >po/ru/angelfish.po
rm -f po/ru/angelfish.po.tmp

%build
%K5build \
    -DBUILD_TESTING:BOOL=OFF \
    #

%install
%K5install

#install alternatives
install -d %buildroot/%_sysconfdir/alternatives/packages.d
cat > %buildroot/%_sysconfdir/alternatives/packages.d/%name <<__EOF__
%_bindir/xbrowser       %_K5bin/angelfish      55
%_bindir/x-www-browser       %_K5bin/angelfish      55
__EOF__

# add mime types categories
#desktop-file-install --mode=0755 --dir %buildroot/%_K5xdgapp \
#    --add-mime-type=x-scheme-handler/http \
#    --add-mime-type=x-scheme-handler/https \
#    %buildroot/%_K5xdgapp/org.kde.angelfish.desktop

%find_lang --all-name --with-qt %name

%files -f %name.lang
%config /%_sysconfdir/alternatives/packages.d/%name
%_K5bin/angelfish*
%_K5xdgapp/*angelfish*.desktop
%_K5icon/*/*/apps/*angelfish*.*
%_K5cfg/*angelfish*
%_K5notif/*angelfish*
%_datadir/metainfo/*.xml

%changelog
* Tue Dec 12 2023 Sergey V Turchin <zerg@altlinux.org> 23.08.4-alt1
- new version

* Fri Nov 10 2023 Sergey V Turchin <zerg@altlinux.org> 23.08.3-alt1
- new version

* Mon Oct 16 2023 Sergey V Turchin <zerg@altlinux.org> 23.08.2-alt1
- new version

* Wed Sep 06 2023 Sergey V Turchin <zerg@altlinux.org> 23.04.3-alt2
- fix "Search for" context menu i18n

* Fri Jul 14 2023 Sergey V Turchin <zerg@altlinux.org> 23.04.3-alt1
- new version

* Wed Jun 14 2023 Sergey V Turchin <zerg@altlinux.org> 23.04.2-alt1
- new version

* Wed Apr 26 2023 Sergey V Turchin <zerg@altlinux.org> 23.04.0-alt1
- new version

* Fri Feb 03 2023 Sergey V Turchin <zerg@altlinux.org> 23.01.0-alt1
- new version

* Mon Dec 05 2022 Sergey V Turchin <zerg@altlinux.org> 22.11-alt1
- new version

* Wed Oct 05 2022 Sergey V Turchin <zerg@altlinux.org> 22.09-alt1
- new version

* Tue Jul 05 2022 Sergey V Turchin <zerg@altlinux.org> 22.06-alt1
- new version

* Wed May 04 2022 Sergey V Turchin <zerg@altlinux.org> 22.04-alt1
- new version

* Fri Feb 18 2022 Sergey V Turchin <zerg@altlinux.org> 22.02-alt2
- using not_qt5_qtwebengine_arches macro

* Mon Feb 14 2022 Sergey V Turchin <zerg@altlinux.org> 22.02-alt1
- new version

* Tue Feb 01 2022 Sergey V Turchin <zerg@altlinux.org> 21.12-alt2
- build with parity of qtwebengine arches

* Fri Dec 10 2021 Sergey V Turchin <zerg@altlinux.org> 21.12-alt1
- new version

* Wed Sep 08 2021 Sergey V Turchin <zerg@altlinux.org> 21.08-alt1
- new version

* Fri Aug 27 2021 Sergey V Turchin <zerg@altlinux.org> 21.07-alt2
- build with qtfeedback

* Wed Aug 18 2021 Sergey V Turchin <zerg@altlinux.org> 21.07-alt1
- new version

* Fri Jun 11 2021 Sergey V Turchin <zerg@altlinux.org> 21.06-alt1
- new version

* Mon Mar 16 2020 Sergey V Turchin <zerg@altlinux.org> 1.5.1-alt2
- fix permission question (Closes: 38167)

* Fri Mar 06 2020 Sergey V Turchin <zerg@altlinux.org> 1.5.1-alt1
- new version

* Thu Feb 27 2020 Sergey V Turchin <zerg@altlinux.org> 1.4.0-alt4
- fix package description

* Tue Feb 25 2020 Sergey V Turchin <zerg@altlinux.org> 1.4.0-alt3
- fix provides and requires

* Tue Feb 25 2020 Sergey V Turchin <zerg@altlinux.org> 1.4.0-alt2
- add x-scheme-handler/http to desktop-file

* Tue Feb 25 2020 Sergey V Turchin <zerg@altlinux.org> 1.4.0-alt1
- initial build
