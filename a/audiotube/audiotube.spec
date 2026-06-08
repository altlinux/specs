%define rname audiotube

%define sover 6
%define libaudiotubecore libaudiotubecore%sover

Name: %rname
Version: 26.04.2
Release: alt1
%K6init

Group: Sound
Summary: YouTube Music client
Url: http://www.kde.org
License: GPL-2.0-or-later

Requires: qt6-multimedia qt6-imageformats
# TESTED_YTMUSICAPI_VERSION
Requires: python3(ytmusicapi) python3(yt_dlp)
Requires: kf6-kirigami-addons
Provides: kde5-audiotube = %EVR
Obsoletes: kde5-audiotube < %EVR

Source: %rname-%version.tar
Patch1: alt-buildreq.patch

BuildRequires(pre): rpm-build-kf6
BuildRequires: pybind11-devel python3-devel python3(ytmusicapi) python3(yt_dlp)
BuildRequires: qt6-declarative-devel qt6-multimedia-devel qt6-svg-devel
BuildRequires: futuresql-qt6-devel qcoro6-devel
BuildRequires: kf6-kirigami-addons-devel
BuildRequires: extra-cmake-modules
BuildRequires: kf6-kcoreaddons-devel kf6-kcrash-devel kf6-ki18n-devel kf6-kirigami-addons-devel
BuildRequires: kf6-kirigami-devel kf6-kwindowsystem-devel kf6-kiconthemes-devel kf6-kconfig-devel

%description
Convergent YouTube Music client.

%prep
%setup -n %rname-%version
%patch1 -p1

%build
ADD_I="`pkg-config --cflags python3`"
%add_optflags %optflags_shared $ADD_I
%K6build \
    -DCMAKE_EXE_LINKER_FLAGS:STRING='-lpython3' \
    -DCMAKE_SHARED_LINKER_FLAGS:STRING='-lpython3' \
    -DQT_MAJOR_VERSION=6 \
    #

%install
%K6install

mkdir -p %buildroot/%_K6data/audiotube/
## gen dep for ytmusicapi
#TESTED_YTMUSICAPI=`grep TESTED_YTMUSICAPI_VERSION src/ytmusic.h | sed -e 's|^\(.*\)".*|\1|' -e 's|^.*"||'`
#[ -n "$TESTED_YTMUSICAPI" ] || exit 1
#ln -sf /usr/share/doc/python3-module-ytmusicapi-"$TESTED_YTMUSICAPI"/README.rst %buildroot/%_K6data/audiotube/README-ytmusicapi.rst

%find_lang %name --with-kde --all-name

%files -f %name.lang
%doc LICENSES/*
%_K6bin/*
%_K6xdgapp/*audiotube.desktop
%_K6icon/*/*/apps/*%{rname}*
%_K6data/audiotube/
%_datadir/metainfo/*.xml


%changelog
* Fri Jun 05 2026 Sergey V Turchin <zerg@altlinux.org> 26.04.2-alt1
- new version

* Fri May 29 2026 Sergey V Turchin <zerg@altlinux.org> 26.04.1-alt2
- fix to build

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

* Tue Mar 11 2025 Sergey V Turchin <zerg@altlinux.org> 24.12.3-alt1
- new version

* Tue Feb 18 2025 Sergey V Turchin <zerg@altlinux.org> 24.12.2-alt1
- new version

* Mon Jan 20 2025 Sergey V Turchin <zerg@altlinux.org> 24.12.1-alt1
- new version

* Thu Nov 14 2024 Sergey V Turchin <zerg@altlinux.org> 24.08.3-alt2
- generate deps for ytmusicapi

* Wed Nov 13 2024 Sergey V Turchin <zerg@altlinux.org> 24.08.3-alt1
- new version

* Fri Oct 25 2024 Sergey V Turchin <zerg@altlinux.org> 24.08.2-alt1
- new version

* Wed Sep 25 2024 Sergey V Turchin <zerg@altlinux.org> 24.08.1-alt1
- initial build

