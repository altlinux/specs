%define rname kwave

%define sover 26
%define libkwavegui libkwavegui%sover
%define libkwave libkwave%sover

Name: %rname
Version: 26.04.2
Release: alt1
%K6init

Group: Sound
Summary: Simple Sound Editor
Url: http://www.kde.org
License: GPL-2.0-or-later

Provides:  kde5-kwave = %EVR
Obsoletes: kde5-kwave < %EVR

Requires: lame

Source: %rname-%version.tar
Patch2: alt-opus-pkgconvig-wrong-version.patch

BuildRequires(pre): rpm-build-kf6
BuildRequires: extra-cmake-modules qt6-declarative-devel qt6-multimedia-devel
BuildRequires: libvulkan-devel
BuildRequires: dconf doxygen librsvg-utils
BuildRequires: desktop-file-utils
BuildRequires: libGConf libalsa-devel libaudiofile-devel libfftw3-devel libflac++-devel libopus-devel libpulseaudio-devel libsamplerate-devel libvorbis-devel
BuildRequires: id3lib-devel libmad-devel
BuildRequires: kf6-kcrash-devel kf6-kdbusaddons-devel kf6-kdoctools-devel kf6-kiconthemes-devel kf6-kio-devel kf6-ktextwidgets-devel
BuildRequires: kf6-karchive-devel

%description
Kwave is a simple sound editor.

%package common
Summary: %name common package
Group: System/Configuration/Other
BuildArch: noarch
Requires: kf6-filesystem
Provides:  kde5-kwave-common = %EVR
Obsoletes: kde5-kwave-common < %EVR
%description common
%name common package

%package devel
Group: Development/KDE and QT
Summary: Development files for %name
%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%package -n %libkwavegui
Group: System/Libraries
Summary: %name library
Requires: %name-common >= %EVR
Obsoletes: libkwavegui23 < %EVR
%description -n %libkwavegui
%name library

%package -n %libkwave
Group: System/Libraries
Summary: %name library
Requires: %name-common >= %EVR
Obsoletes: libkwave23 < %EVR
%description -n %libkwave
%name library


%prep
%setup -n %rname-%version
%patch2 -p1

%build
%K6build \
    #

%install
%K6install
%K6install_move data kwave
desktop-file-install --mode=0755 --dir %buildroot/%_K6xdgapp \
    --set-key="X-DocPath" \
    --set-value="kwave/index.html" \
    %buildroot/%_K6xdgapp/org.kde.kwave.desktop

%find_lang %name --with-kde --all-name

%files common -f %name.lang
%doc *LICENSE*

%files
%_K6bin/kwave
%_K6plug/kwave/
%_K6data/kwave/
%_K6icon/*/*/*/*kwave*.*
%_K6xdgapp/*kwave*.desktop
%_datadir/metainfo/*.xml

#%files devel
#%_K6inc/kwave_version.h
#%_K6inc/kwave/
#%_K6link/lib*.so
#%_K6lib/cmake/kwave
#%_K6archdata/mkspecs/modules/qt_kwave.pri

%files -n %libkwave
%_K6lib/libkwave.so.%sover
%_K6lib/libkwave.so.*
%files -n %libkwavegui
%_K6lib/libkwavegui.so.%sover
%_K6lib/libkwavegui.so.*

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

* Fri Dec 06 2024 Sergey V Turchin <zerg@altlinux.org> 24.11.90-alt1
- beta on KF6

* Thu Oct 24 2024 Sergey V Turchin <zerg@altlinux.org> 24.08.2-alt1
- initial build
