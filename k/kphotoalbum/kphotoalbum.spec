%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1

%def_with check

Name: kphotoalbum
Version: 6.2.0
Release: alt2

Summary: Photo Album for easy organization of your images
License: GPL-2.0-or-later
Group: Graphical desktop/KDE
Url: https://invent.kde.org/graphics/kphotoalbum

Source: %name-%version.tar

Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-build-kf6
BuildRequires(pre): rpm-macros-cmake

BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: extra-cmake-modules

BuildRequires: pkgconfig(Qt6)
BuildRequires: pkgconfig(Qt6Qml)
BuildRequires: pkgconfig(libjpeg)
BuildRequires: pkgconfig(Qt6Core5Compat)
BuildRequires: pkgconfig(Qt6WebEngineWidgets)
BuildRequires: pkgconfig(cups)
BuildRequires: pkgconfig(exiv2)
BuildRequires: pkgconfig(libvlc)

BuildRequires: qt6-phonon-devel
BuildRequires: kf6-karchive-devel
BuildRequires: kf6-kcompletion-devel
BuildRequires: kf6-kconfig-devel
BuildRequires: kf6-kcoreaddons-devel
BuildRequires: kf6-ki18n-devel
BuildRequires: kf6-kiconthemes-devel
BuildRequires: kf6-kjobwidgets-devel
BuildRequires: kf6-kio-devel
BuildRequires: kf6-ktextwidgets-devel
BuildRequires: kf6-kdoctools-devel
BuildRequires: kf6-purpose-devel
BuildRequires: kde6-libkdcraw-devel
BuildRequires: marble-devel
BuildRequires: qt6-multimedia-devel

%if_with check
BuildRequires: ctest
BuildRequires: icon-theme-breeze
BuildRequires: libqt6-sql
BuildRequires: xauth
BuildRequires: xvfb-run
%endif

Requires: libqt6-sql
Requires: marble-addon-maps
Requires: ffmpeg
Requires: kf6-kio

Requires: plasma6-breeze
Requires: icon-theme-breeze

Requires: %{name}-data = %{version}-%{release}
Requires: lib%{name}libs = %{version}-%{release}

ExcludeArch: %ix86 riscv64

%description
KPhotoAlbum lets you index, search, group and view images by keywords,
date, locations and persons. It provides a quick and elegant way to
lookup groups of images when you have thousands of pictures on your hard
disk.

The information associated with each photo is stored in an XML file.
Together with its keywords, KPhotoAlbum stores each picture's MD5 sum,
so it will recognize them even if you move them to another directory.
KPhotoAlbum can also create HTML galleries with the images you select.

KPhotoAlbum can also make use of the KIPI image handling plugins to
extend its capabilities. The kipi-plugins package contains many useful
extensions. Among others, it contains extensions for photo manipulation,
importing, exporting and batch processing.

%package data
Summary: Data files for %name
Group: Graphical desktop/KDE
BuildArch: noarch

%description data
KPhotoAlbum lets you index, search, group and view images by keywords,
date, locations and persons. It provides a quick and elegant way to
lookup groups of images when you have thousands of pictures on your hard
disk.

The information associated with each photo is stored in an XML file.
Together with its keywords, KPhotoAlbum stores each picture's MD5 sum,
so it will recognize them even if you move them to another directory.
KPhotoAlbum can also create HTML galleries with the images you select.

KPhotoAlbum can also make use of the KIPI image handling plugins to
extend its capabilities. The kipi-plugins package contains many useful
extensions. Among others, it contains extensions for photo manipulation,
importing, exporting and batch processing.

This package provides the architecture independent data files for %name.

%package -n lib%{name}libs
Group: System/Libraries
Summary: libraries for %name

%description -n lib%{name}libs
This package contains libraries for %name.

%prep
%setup
%patch -p1

%build
%cmake \
%if_with check
       -DBUILD_TESTING=ON
%else
       -DBUILD_TESTING=OFF
%endif
%cmake_build

%install
%cmake_install

%find_lang %name --with-kde --all-name --with-man

%check
xvfb-run -a --server-args="-screen 0 1024x768x24+32" %ctest -j1 -VV

%files
%doc README.md
%_sysconfdir/xdg/kphotoalbumrc
%_K6bin/kpa-backup.sh
%_K6bin/kpa-thumbnailtool
%_K6bin/kphotoalbum
%_K6bin/open-raw.pl
%_K6xdgapp/org.kde.kphotoalbum-import.desktop
%_K6xdgapp/org.kde.kphotoalbum.desktop
%_K6xdgapp/org.kde.kphotoalbum.open-raw.desktop
%_K6icon/hicolor/*/*/*

%files -n lib%{name}libs
%_K6lib/libkpabase.so
%_K6lib/libkpaexif.so
%_K6lib/libkpathumbnails.so

%files data -f %name.lang
%dir %_K6data/kphotoalbum
%_K6data/kphotoalbum/*
%_K6data/metainfo/org.kde.kphotoalbum.appdata.xml

%changelog
* Thu Jun 11 2026 Nikolay Strelkov <snk@altlinux.org> 6.2.0-alt2
- Moved libraries to libkphotoalbumlibs package.

* Sun Mar 15 2026 Nikolay Strelkov <snk@altlinux.org> 6.2.0-alt1
- New version 6.2.0.

* Thu Feb 05 2026 Nikolay Strelkov <snk@altlinux.org> 6.1.0-alt1
- Initial build of kf6-based KPhotoAlbum for Sisyphus
