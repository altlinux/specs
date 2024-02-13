Name: stratagus
Version: 3.3.2
Release: alt1
Summary: A free real time strategy game engine
License: GPLv2+
Group: Games/Strategy
URL: http://stratagus.sourceforge.net
Vcs: https://github.com/Wargus/stratagus
Source0: %name-%version.tar
Source1: stratagus-16.png
Source2: stratagus-32.png
Source3: stratagus-48.png
Source9: vendor.tar

BuildRequires(pre): cmake rpm-macros-cmake gcc-c++
# Automatically added by buildreq on Fri Feb 02 2024 (-bi)
# optimized out: cmake-modules debugedit elfutils glibc-kernheaders-generic glibc-kernheaders-x86 libSDL2-devel libX11-devel libctf-nobfd0 libgpg-error libjpeg-devel liblua5.1-compat-devel liblua5.1-devel libogg-devel libp11-kit libsasl2-3 libstdc++-devel libtolua++-lua5.1 python3 python3-base python3-dev rpm-build-file rpm-build-python3 sh5 xorg-proto-devel xz zlib-devel
BuildRequires: bzlib-devel cmake doctest-devel doxygen gcc-c++ libSDL2_image-devel libSDL2_mixer-devel libmng-devel libpng-devel libtheora-devel libtolua++-lua5.1-devel libvorbis-devel python3-module-setuptools

%if_with doc
BuildRequires: doxygen graphviz
%endif

%description
Stratagus is a free cross-platform real-time strategy gaming engine.
It includes support for playing over the internet/LAN, or playing a computer
opponent. The engine is configurable and can be used to create games with a
wide-range of features specific to your needs. See the data sets page for a
list of current games using the stratagus engine.

%package devel
Summary:        Development files for %name
Group:          Development/Other
BuildArch:      noarch
Requires:       %name = %version-%release

%description devel
This package contains development files for %name.

%if_with doc
%package doc
Summary:        Documentation  for %name
Group:          Documentation 
BuildArch:      noarch
Requires:       %name = %version-%release

%description doc
This package contains documentation for %name.
%endif

%prep
%setup -n %name-%version
tar xf %SOURCE9 -C third-party
subst 's|third-party/doctest/doctest|/usr/include/doctest|' CMakeLists.txt

%build
%cmake \
       -DENABLE_DEV=ON \
       -DENABLE_UPX=ON \
       -DENABLE_TOUCHSCREEN=ON \
       -DLUA_LIBRARIES=lua5.1 \
#       -DTOLUA++_APP=tolua++ \
#       -DTOLUA++_LIBRARY=tolua++ \
#       -DENABLE_DOC=ON \

%cmake_build

%install
%cmake_install

mkdir -p %buildroot%_gamesdatadir/%name

mkdir -p %buildroot%_man6dir/
mv doc/*.6 %buildroot%_man6dir

install -pD -m644 %SOURCE1 %buildroot%_miconsdir/%name.png
install -pD -m644 %SOURCE2 %buildroot%_niconsdir/%name.png
install -pD -m644 %SOURCE3 %buildroot%_liconsdir/%name.png

%find_lang %name

%files -f %name.lang
%_gamesbindir/%name
%_bindir/png2%name
%_man6dir/%name.6*
%dir %_gamesdatadir/%name
%_miconsdir/%name.png
%_niconsdir/%name.png
%_liconsdir/%name.png

%files devel
%_includedir/*

%if_with doc
%files doc
%_docdir/%name
%endif

%changelog
* Fri Feb 02 2024 Ildar Mulyukov <ildar@altlinux.ru> 3.3.2-alt1
- new version

* Mon May 15 2017 Anton Farygin <rider@altlinux.ru> 2.4.1-alt2
- NMU: rebuild with new libmng

* Fri Nov 11 2016 Anton Midyukov <antohami@altlinux.org> 2.4.1-alt1
- New version 2.4.1

* Sat Jul 02 2016 Anton Midyukov <antohami@altlinux.org> 2.4.0-alt1
- New version 2.4.0.

* Fri Aug 25 2006 Alexey Tourbin <at@altlinux.ru> 2.1rel-alt2
- sync debian stratagus_2.1-9.1.diff.gz

* Mon Jun 12 2006 Alexey Tourbin <at@altlinux.ru> 2.1rel-alt1
- updated to 2.1 release
- hacked for lua-5.1
- Battle of Survival data files to be packaged separately (noarch)

* Wed Jun 30 2004 Kachalov Anton <mouse@altlinux.ru> 2.1pre2-alt1
- new version 2.1pre2

* Wed Mar 10 2004 Kachalov Anton <mouse@altlinux.ru> 2.0-alt1
- first build for Sisyphus
