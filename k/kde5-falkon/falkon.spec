# spec file for package qupzilla
# Original author: Mariusz Fik (Fisiu)
# Copyright (c) 2011 SUSE LINUX Products GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself.

%define sover 3
%define libfalkonprivate libfalkonprivate%sover
%add_python3_path %_qt5_plugindir/falkon
%add_python3_req_skip Falkon

%define rname falkon
%def_enable python_plugins

Name: kde5-%rname
Version: 23.08.3
Release: alt3
%K5init no_altplace

Summary: Very fast web-browser
License: GPL-3.0-or-later
Group: Networking/WWW
Url: https://www.falkon.org/

ExcludeArch: %not_qt5_qtwebengine_arches

Provides: webclient x-www-browser
Requires(post,preun): alternatives >= 0.2
Requires: qt5-imageformats qt5-svg qt5-translations

Provides: %rname = %version-%release
Provides: %rname-gnome3 = %EVR
Obsoletes: %rname-gnome3 < %EVR
Provides: %rname-kde5 = %EVR
Obsoletes: %rname-kde5 < %EVR
Provides: %rname-core = %EVR
Obsoletes: %rname-core < %EVR
Provides: %rname-kde = %version-%release
Provides: qupzilla-kde5 = %version-%release
Obsoletes: qupzilla-kde5 < %version-%release
Provides: qupzilla-gnome3 = %version-%release
Obsoletes: qupzilla-gnome3 < %version-%release
Provides: qupzilla = %version-%release
Obsoletes: qupzilla < %version-%release
Obsoletes: rekonq < 2.5

Source: %rname-%version.tar
# FC
Patch1: falkon-3.1.0-native-scrollbars.patch

# Automatically added by buildreq on Fri Dec 08 2023 (-bi)
# optimized out: alt-os-release alternatives clang17.0 clang17.0-support cmake cmake-modules debugedit elfutils fontconfig-devel gcc-c++ glib2-devel glibc-kernheaders-generic glibc-kernheaders-x86 gtk4-update-icon-cache kf5-kauth-devel kf5-kbookmarks-devel kf5-kcodecs-devel kf5-kcompletion-devel kf5-kconfig-devel kf5-kconfigwidgets-devel kf5-kcoreaddons-devel kf5-kcrash-devel kf5-kitemviews-devel kf5-kjobwidgets-devel kf5-kservice-devel kf5-kwidgetsaddons-devel kf5-kwindowsystem-devel kf5-kxmlgui-devel kf5-solid-devel libICE-devel libSM-devel libX11-devel libXScrnSaver-devel libXau-devel libXcomposite-devel libXcursor-devel libXdamage-devel libXdmcp-devel libXext-devel libXfixes-devel libXft-devel libXi-devel libXinerama-devel libXmu-devel libXpm-devel libXrandr-devel libXrender-devel libXt-devel libXtst-devel libXv-devel libXxf86misc-devel libXxf86vm-devel libclang-cpp17 libctf-nobfd0 libdouble-conversion3 libfreetype-devel libglvnd-devel libgnome-keyring libgpg-error libp11-kit libqt5-concurrent libqt5-core libqt5-dbus libqt5-gui libqt5-network libqt5-positioning libqt5-printsupport libqt5-qml libqt5-qmlmodels libqt5-quick libqt5-quickwidgets libqt5-sql libqt5-svg libqt5-waylandclient libqt5-webchannel libqt5-webengine libqt5-webenginecore libqt5-webenginewidgets libqt5-widgets libqt5-x11extras libqt5-xml libqt5-xmlpatterns libsasl2-3 libssl-devel libstdc++-devel libwayland-client libwayland-cursor libxcb-devel libxcbutil-keysyms libxcbutil-keysyms-devel libxkbcommon-devel libxkbfile-devel llvm-common llvm17.0-libs pkg-config python-modules python2-base python3 python3-base python3-dev python3-module-PySide2 python3-module-paste python3-module-setuptools python3-module-shiboken2 python3-module-shiboken2-devel qt5-base-common qt5-base-devel qt5-declarative-devel qt5-location-devel qt5-tools qt5-webchannel-devel rpm-build-file rpm-build-gir rpm-build-python3 rpm-macros-python sh5 shiboken2 tzdata xorg-proto-devel xorg-xf86miscproto-devel
#BuildRequires: appstream clang extra-cmake-modules kf5-karchive-devel kf5-ki18n-devel kf5-kio-devel kf5-kwallet-devel kf5-purpose-devel libXaw-devel libXres-devel libgnome-keyring-devel libxcb-render-util-devel libxcbutil-cursor-devel libxcbutil-devel libxcbutil-icccm-devel libxcbutil-image-devel libxkbcommon-x11-devel python-modules-compiler python3-module-PySide2-devel python3-module-zope qt5-imageformats qt5-svg-devel qt5-tools-devel qt5-translations qt5-wayland-devel qt5-webengine-devel qt5-x11extras-devel
BuildRequires(pre): rpm-build-kf5 rpm-macros-qt5-webengine
BuildRequires: clang
BuildRequires: rpm-build-python3
BuildRequires: extra-cmake-modules
BuildRequires: libstdc++-devel
BuildRequires: libssl-devel
BuildRequires: libxcbutil-devel libxcbutil-devel
BuildRequires: qt5-multimedia-devel qt5-script-devel qt5-tools-devel qt5-webengine-devel qt5-websockets-devel qt5-x11extras-devel
%if_enabled python_plugins
BuildRequires: python3-devel python3-module-shiboken2-devel python3-module-PySide2-devel
%endif
BuildRequires: kf5-kwallet-devel kf5-ki18n-devel kf5-kio-devel kf5-kcrash-devel kf5-kcoreaddons-devel kf5-purpose-devel
BuildRequires: kf5-karchive-devel
BuildRequires: libgnome-keyring-devel

%description
Falkon is a KDE web browser. It uses QtWebEngine rendering engine.

%package -n %rname-core
Group: Graphical desktop/KDE
Summary: Falkon KDE integration
Requires(post,preun): alternatives >= 0.2
Provides: webclient x-www-browser
Provides: %rname = %EVR
Obsoletes: %rname < %EVR
Provides: qupzilla = %version-%release
Obsoletes: qupzilla < %version-%release
%description -n %rname-core
Falkon Web Browser base.

%package -n %rname-kde5
Group: Graphical desktop/KDE
Summary: Falkon KDE integration
Requires: %rname-core
Provides: webclient
Provides: %name = %version-%release
Provides: %rname = %version-%release
Provides: %rname-kde = %version-%release
Provides: qupzilla-kde5 = %version-%release
Obsoletes: qupzilla-kde5 < %version-%release
Obsoletes: rekonq < 2.5
%description -n %rname-kde5
Falkon KDE integration.

%package -n %rname-gnome3
Group: Graphical desktop/GNOME
Summary: Falkon GNOME integration
Requires: %rname-core
Provides: webclient
Provides: %rname = %version-%release
Provides: %rname-gnome = %version-%release
Provides: qupzilla-gnome3 = %version-%release
Obsoletes: qupzilla-gnome3 < %version-%release
%description -n %rname-gnome3
Falkon GNOME integration.

%package -n %libfalkonprivate
Group: System/Libraries
Summary: %name library
#Requires: %name-common
Requires: kf5-filesystem
%description -n %libfalkonprivate
%name library

%prep
%setup -n %rname-%version
%patch1 -p1

%build
%K5build \
    -DBUILD_KEYRING:BOO=ON \
    #

%install
%K5install
ln -s falkon %buildroot/%_K5bin/qupzilla

#install alternatives
install -d %buildroot/%_sysconfdir/alternatives/packages.d
cat > %buildroot/%_sysconfdir/alternatives/packages.d/%name <<__EOF__
%_bindir/xbrowser       %_K5bin/falkon      111
%_bindir/x-www-browser       %_K5bin/falkon      111
__EOF__

%find_lang --all-name --with-qt %name

%files -f %name.lang
%config /%_sysconfdir/alternatives/packages.d/%name
%_K5bin/falkon
%_K5bin/qupzilla
%_K5plug/falkon/
%_K5xdgapp/org.kde.falkon.desktop
%_K5icon/hicolor/*/*/*.*
%_datadir/falkon/
%_datadir/bash-completion/completions/falkon
%_datadir/metainfo/*.xml

%files -n %libfalkonprivate
%_K5lib/libFalkonPrivate.so.%sover
%_K5lib/libFalkonPrivate.so.*

%changelog
* Mon Dec 11 2023 Sergey V Turchin <zerg@altlinux.org> 23.08.3-alt3
- fix obsoletes

* Fri Dec 08 2023 Sergey V Turchin <zerg@altlinux.org> 23.08.3-alt2
- merge subpackages
- enable python plugins
- using native scrollbars by default

* Fri Nov 10 2023 Sergey V Turchin <zerg@altlinux.org> 23.08.3-alt1
- new version

* Mon Oct 16 2023 Sergey V Turchin <zerg@altlinux.org> 23.08.2-alt1
- new version

* Fri Jul 14 2023 Sergey V Turchin <zerg@altlinux.org> 23.04.3-alt1
- new version

* Fri Jun 09 2023 Sergey V Turchin <zerg@altlinux.org> 23.04.2-alt1
- new version

* Wed Jun 07 2023 Sergey V Turchin <zerg@altlinux.org> 23.04.1-alt1
- new version

* Mon Mar 06 2023 Sergey V Turchin <zerg@altlinux.org> 22.12.3-alt1
- new version

* Tue Feb 07 2023 Sergey V Turchin <zerg@altlinux.org> 22.12.2-alt1
- new version

* Tue Jan 17 2023 Sergey V Turchin <zerg@altlinux.org> 22.12.1-alt1
- new version

* Mon Nov 07 2022 Sergey V Turchin <zerg@altlinux.org> 22.08.3-alt1
- new version

* Tue Oct 18 2022 Sergey V Turchin <zerg@altlinux.org> 22.08.2-alt1
- new version

* Wed Sep 21 2022 Sergey V Turchin <zerg@altlinux.org> 22.08.1-alt1
- new version

* Fri Feb 18 2022 Sergey V Turchin <zerg@altlinux.org> 3.2.0-alt2
- using not_qt5_qtwebengine_arches macro

* Fri Feb 04 2022 Sergey V Turchin <zerg@altlinux.org> 3.2.0-alt1
- new version

* Tue Feb 01 2022 Sergey V Turchin <zerg@altlinux.org> 3.1.0-alt4
- don't build on e2k and ppc64le

* Fri Aug 28 2020 Sergey V Turchin <zerg@altlinux.org> 3.1.0-alt3
- fix to build with qt-5.15

* Thu Sep 19 2019 Sergey V Turchin <zerg@altlinux.org> 3.1.0-alt2
- obsolete rekonq

* Thu Mar 28 2019 Sergey V Turchin <zerg@altlinux.org> 3.1.0-alt1
- new version
- obsolete qupzilla

* Fri Aug 31 2018 Sergey V Turchin <zerg@altlinux.org> 3.0.1-alt2
- rebuild with new openssl (ALT# 35313)

* Tue May 15 2018 Sergey V Turchin <zerg@altlinux.org> 3.0.1-alt1
- new version

* Mon Apr 09 2018 Sergey V Turchin <zerg@altlinux.org> 3.0.0-alt3
- fix URL

* Thu Mar 22 2018 Igor Vlasenko <viy@altlinux.ru> 3.0.0-alt2
- NMU: added URL (closes: #34686)

* Tue Mar 20 2018 Oleg Solovyov <mcpain@altlinux.org> 3.0.0-alt1
- initial build for ALT
