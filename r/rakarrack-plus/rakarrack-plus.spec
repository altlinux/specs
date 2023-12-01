Name:    rakarrack-plus
Version: 1.2.4
Release: alt1

Summary: Rakarrack plus LV2s
License: GPL-2.0
Group:   Sound
Url:     https://github.com/Stazed/rakarrack-plus

Packager: Artyom Bystrov <arbars@altlinux.org>

Source: %name-%version.tar

BuildRequires(Pre): rpm-macros-cmake
BuildRequires: cmake alsa-utils gcc-c++ jackit-devel libXext-devel libXft-devel
BuildRequires: libXpm-devel libalsa-devel libfltk-devel libjpeg-devel
BuildRequires: libpng-devel libsamplerate-devel libsndfile-devel

BuildRequires: libpixman-devel libcairo-devel libXinerama-devel
BuildRequires: libXfixes-devel libfftw3-devel libXcursor-devel
BuildRequires: desktop-file-utils liblo-devel lv2-devel

Conflicts: rakarrack

%description
This project is a merging of original rakarrack (http://rakarrack.sourceforge.net)
and the program's effects ported to LV2 from (https://github.com/ssj71/rkrlv2).
In addition there are many bug fixes and enhancements to rakarrack and the LV2s.
Rakarrack-plus-1.0.0 is the first version under the new name.

%package data
Summary: Data files and documentation for Rakarrack-plus
Group: Sound
BuildArch: noarch

%description data
This package contains data files and documentation for Rakarrack-plus.

%package lv2-plugins
Summary: Data files and documentation for Rakarrack-plus
Group: Sound

%description lv2-plugins
This package contains plugins and sample data for LV2 in Rakarrack-plus.

%prep
%setup
%ifarch %e2k
# error: unrecognized command line option
sed -i 's/-fvect-cost-model//' CMakeLists.txt
%endif

%build
%cmake \
    -DCMAKE_BUILD_TYPE=Release \
    -DCMAKE_INSTALL_PREFIX=/usr \
    -DEnableSysex=ON -DBuildCarlaPresets=ON \
    -Wno-dev
%cmake_build

%install
%cmake_install


%files
%_bindir/*

%files data
%_desktopdir/%name.desktop
%_man1dir/%name.1*
%_pixmapsdir/*
%_datadir/%name
%_datadir/doc/%name

%files lv2-plugins
%_prefix/lib/lv2/RakarrackPlus.lv2
%_datadir/RakarrackPlus.lv2

%changelog
* Fri Dec  1 2023 Artyom Bystrov <arbars@altlinux.org> 1.2.4-alt1
- Update to new version

* Mon Sep 25 2023 Ilya Kurdyukov <ilyakurdyukov@altlinux.org> 1.2.3-alt1.1
- Fixed build for Elbrus

* Wed Sep 06 2023 Artyom Bystrov <arbars@altlinux.org> 1.2.3-alt1
- Initial build for Sisyphus
