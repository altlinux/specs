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
%add_python3_path %_qt6_plugindir/falkon
%add_python3_req_skip Falkon

%define rname falkon
%def_enable python_plugins

Name: %rname
Version: 26.04.2
Release: alt1
%K6init no_altplace

Summary: Very fast web-browser
License: GPL-3.0-or-later
Group: Networking/WWW
Url: https://www.falkon.org/

ExcludeArch: %not_qt6_qtwebengine_arches

Provides: webclient x-www-browser
Requires(post,preun): alternatives >= 0.2
Requires: qt6-imageformats qt6-svg qt6-translations

%if "%name" == "%rname"
%else
Provides: %rname = %EVR
%endif
Provides:  kde5-falkon = %EVR
Obsoletes: kde5-falkon < %EVR

Source: %rname-%version.tar
# FC
Patch1: native-scrollbars.patch

BuildRequires(pre): rpm-build-kf6 rpm-macros-qt6-webengine
BuildRequires: clang
BuildRequires: rpm-build-python3
BuildRequires: extra-cmake-modules
BuildRequires: libstdc++-devel
BuildRequires: libssl-devel
BuildRequires: libxcbutil-devel libxcbutil-devel
BuildRequires: qt6-multimedia-devel qt6-declarative-devel qt6-tools-devel qt6-5compat-devel qt6-webengine-devel qt6-websockets-devel 
%if_enabled python_plugins
BuildRequires: python3-devel python3-module-shiboken6-devel python3-module-pyside6-devel
%endif
BuildRequires: kf6-kwallet-devel kf6-ki18n-devel kf6-kio-devel kf6-kcrash-devel kf6-kcoreaddons-devel kf6-purpose-devel
BuildRequires: kf6-karchive-devel
BuildRequires: libgnome-keyring-devel

%description
Falkon is a KDE web browser. It uses QtWebEngine rendering engine.

%package -n %libfalkonprivate
Group: System/Libraries
Summary: %name library
#Requires: %name-common
Requires: kde-common
%description -n %libfalkonprivate
%name library

%prep
%setup -n %rname-%version
%patch1 -p1

%build
%K6build \
    -DBUILD_KEYRING:BOO=ON \
    #

%install
%K6install
ln -s falkon %buildroot/%_K6bin/qupzilla

#install alternatives
install -d %buildroot/%_sysconfdir/alternatives/packages.d
cat > %buildroot/%_sysconfdir/alternatives/packages.d/%name <<__EOF__
%_bindir/xbrowser       %_K6bin/falkon      112
%_bindir/x-www-browser       %_K6bin/falkon      112
__EOF__

%find_lang --all-name --with-qt %name

%files -f %name.lang
%config /%_sysconfdir/alternatives/packages.d/%name
%_K6bin/falkon
%_K6bin/qupzilla
%_K6plug/falkon/
%_K6xdgapp/org.kde.falkon.desktop
%_K6icon/hicolor/*/*/*.*
%_datadir/falkon/
%_datadir/bash-completion/completions/falkon
%_datadir/metainfo/*.xml

%files -n %libfalkonprivate
%_K6lib/libFalkonPrivate.so.%sover
%_K6lib/libFalkonPrivate.so.*


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

