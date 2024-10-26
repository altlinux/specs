%define rname kwave

%define sover 24
%define libkwavegui libkwavegui%sover
%define libkwave libkwave%sover

Name: %rname
Version: 24.08.2
Release: alt1
%K5init

Group: Sound
Summary: Simple Sound Editor
Url: http://www.kde.org
License: GPL-2.0-or-later

Provides:  kde5-kwave = %EVR
Obsoletes: kde5-kwave < %EVR

Requires: lame

Source: %rname-%version.tar
Patch2: alt-opus-pkgconvig-wrong-version.patch

BuildRequires(pre): rpm-build-kf5
BuildRequires: extra-cmake-modules qt5-declarative-devel qt5-multimedia-devel
BuildRequires: dconf doxygen librsvg-utils
BuildRequires: desktop-file-utils
BuildRequires: libGConf libalsa-devel libaudiofile-devel libfftw3-devel libflac++-devel libopus-devel libpulseaudio-devel libsamplerate-devel libvorbis-devel
BuildRequires: id3lib-devel libmad-devel
BuildRequires: kf5-kcrash-devel kf5-kdbusaddons-devel kf5-kdelibs4support kf5-kdoctools-devel kf5-kiconthemes-devel kf5-kio-devel kf5-ktextwidgets-devel
BuildRequires: kf5-karchive-devel

%description
Kwave is a simple sound editor.

%package common
Summary: %name common package
Group: System/Configuration/Other
BuildArch: noarch
Requires: kf5-filesystem
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
Summary: KF5 library
Requires: %name-common >= %EVR
Obsoletes: libkwave23 < %EVR
%description -n %libkwave
%name library


%prep
%setup -n %rname-%version
%patch2 -p1

%build
%K5build \
    #

%install
%K5install
%K5install_move data kwave
desktop-file-install --mode=0755 --dir %buildroot/%_K5xdgapp \
    --set-key="X-DocPath" \
    --set-value="kwave/index.html" \
    %buildroot/%_K5xdgapp/org.kde.kwave.desktop

%find_lang %name --with-kde --all-name

%files common -f %name.lang
%doc *LICENSE*

%files
%_K5bin/kwave
%_K5plug/kwave/
%_K5data/kwave/
%_K5icon/*/*/*/*kwave*.*
%_K5xdgapp/*kwave*.desktop
%_datadir/metainfo/*.xml

#%files devel
#%_K5inc/kwave_version.h
#%_K5inc/kwave/
#%_K5link/lib*.so
#%_K5lib/cmake/kwave
#%_K5archdata/mkspecs/modules/qt_kwave.pri

%files -n %libkwave
%_K5lib/libkwave.so.%sover
%_K5lib/libkwave.so.*
%files -n %libkwavegui
%_K5lib/libkwavegui.so.%sover
%_K5lib/libkwavegui.so.*

%changelog
* Thu Oct 24 2024 Sergey V Turchin <zerg@altlinux.org> 24.08.2-alt1
- initial build
