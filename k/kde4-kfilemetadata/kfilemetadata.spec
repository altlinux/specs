
%define rname kfilemetadata
Name: kde4-kfilemetadata
Version: 4.13.1
Release: alt1

Group: System/Libraries
Summary: A library for extracting file metadata
Url: https://projects.kde.org/projects/kde/kdelibs/%rname
License: LGPLv2 / LGPLv3

Source: %rname-%version.tar

# Automatically added by buildreq on Fri Apr 18 2014 (-bi)
# optimized out: automoc cmake cmake-modules elfutils fontconfig fontconfig-devel glibc-devel-static kde4libs libICE-devel libSM-devel libX11-devel libXScrnSaver-devel libXau-devel libXcomposite-devel libXcursor-devel libXdamage-devel libXdmcp-devel libXext-devel libXfixes-devel libXft-devel libXi-devel libXinerama-devel libXpm-devel libXrandr-devel libXrender-devel libXt-devel libXtst-devel libXv-devel libXxf86vm-devel libavcodec-devel libavutil-devel libcloog-isl4 libdbus-devel libfreetype-devel libopencore-amrnb0 libopencore-amrwb0 libpng-devel libpoppler4-qt4 libqt4-core libqt4-dbus libqt4-devel libqt4-gui libqt4-network libqt4-svg libqt4-test libqt4-xml libsoprano-devel libssl-devel libstdc++-devel libxkbfile-devel phonon-devel pkg-config python-base ruby ruby-stdlibs xorg-kbproto-devel xorg-xproto-devel zlib-devel
#BuildRequires: ebook-tools-devel gcc-c++ glib2-devel kde4libs-devel libavdevice-devel libavformat-devel libexiv2-devel libicu50 libpoppler-qt4-devel libpostproc-devel libswscale-devel libtag-devel python-module-protobuf qt4-designer rpm-build-ruby zlib-devel-static
BuildRequires: ebook-tools-devel gcc-c++ kde4libs-devel libavdevice-devel libavformat-devel
BuildRequires: libexiv2-devel libpoppler-qt4-devel libpostproc-devel libswscale-devel
BuildRequires: libtag-devel
BuildRequires: kde-common-devel
#BuildRequires: qmobipocket-devel

%description
%summary.

%package devel
Group: Development/KDE and QT
Summary: Developer files for %name
Requires: kde4libs-devel
%description devel
%summary.

%package -n libkfilemetadata4
Group: System/Libraries
Summary: %name library
%description -n libkfilemetadata4
%name library

%prep
%setup -qn %rname-%version

%build
%K4build

%install
%K4install


%files -n libkfilemetadata4
%_K4libdir/libkfilemetadata.so.*
%_K4lib/kfilemetadata_*extractor.so
%_K4srv/kfilemetadata_*extractor.desktop
%_K4srvtyp/kfilemetadataextractor.desktop

%files devel
%_K4includedir/kfilemetadata/
%_K4link/lib*.so
%_K4libdir/cmake/KFileMetaData/

%changelog
* Tue May 13 2014 Sergey V Turchin <zerg@altlinux.org> 4.13.1-alt1
- new version

* Fri Apr 18 2014 Sergey V Turchin <zerg@altlinux.org> 4.13.0-alt1
- initial build
