%define rname audiocd-kio

%define sover 5
%define libaudiocdplugins libaudiocdplugins%sover

Name: %rname
Version: 24.08.1
Release: alt1
%K6init

Group: Sound
Summary: Audio CD ioslave
Url: http://www.kde.org
License: GPL-2.0-or-later

Requires: lame

Source: %rname-%version.tar
Patch1: alt-docpath.patch

BuildRequires(pre): rpm-build-kf6
BuildRequires: extra-cmake-modules qt6-declarative-devel qt6-phonon-devel
BuildRequires: lame libalsa-devel libcdparanoia-devel libflac-devel libvorbis-devel
BuildRequires: kf6-kdoctools-devel kf6-kio-devel kf6-ki18n-devel kf6-kcmutils-devel
BuildRequires: kde6-libkcddb-devel kde6-libkcompactdisc-devel

%description
Allows treating audio CDs like a 'real' filesystem, where tracks
are represented as files and, when copied from the folder,
are digitally extracted from the CD. This ensures a perfect
copy of the audio data.

%package -n kio-audiocd
Group: Sound
Summary: Audio CD ioslave
Requires: %name-common
Requires: lame
Provides: kde5-kio-audiocd = %EVR
Obsoletes: kde5-kio-audiocd < %EVR
%description -n kio-audiocd
Allows treating audio CDs like a 'real' filesystem, where tracks
are represented as files and, when copied from the folder,
are digitally extracted from the CD. This ensures a perfect
copy of the audio data.

%package common
Summary: %name common package
Group: System/Configuration/Other
BuildArch: noarch
Requires: kde-common
Provides: kde5-audiocd-kio-common = %EVR
Obsoletes: kde5-audiocd-kio-common < %EVR
%description common
%name common package

%package devel
Group: Development/KDE and QT
Summary: Development files for %name
%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%package -n %libaudiocdplugins
Group: System/Libraries
Summary: %name library
Requires: %name-common >= %EVR
%description -n %libaudiocdplugins
%name library


%prep
%setup -n %rname-%version
%patch1 -p1

%build
%K6build \
    -DKDE_INSTALL_INCLUDEDIR=%_K6inc \
    #

%install
%K6install
%K6install_move data konqsidebartng solid
%find_lang %name --with-kde --all-name

%files common -f %name.lang
%doc COPYING*
%_datadir/qlogging-categories6/*.*categories

%files -n kio-audiocd
%_K6plug/*audiocd*.so
%_K6plug/kf6/kio/*audiocd*.so
%_K6plug/plasma/kcms/systemsettings_qwidgets/*audiocd*.so
%_K6xdgapp/*audiocd*.desktop
%_K6cfg/*audiocd*
%_K6data/konqsidebartng/virtual_folders/services/*audiocd*
%_K6data/solid/actions/*audiocd*
%_datadir/metainfo/*.xml

%files devel
%_K6inc/*audiocd*
%_K6link/lib*.so
#%_K6lib/cmake/audiocd-kio

%files -n %libaudiocdplugins
%_K6lib/libaudiocdplugins.so.%sover
%_K6lib/libaudiocdplugins.so.*


%changelog
* Wed Sep 25 2024 Sergey V Turchin <zerg@altlinux.org> 24.08.1-alt1
- initial build

