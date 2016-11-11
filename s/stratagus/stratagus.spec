Name: stratagus
Version: 2.4.1
Release: alt1

Summary: A free real time strategy game engine
License: GPLv2+
Group: Games/Strategy

URL: https://github.com/Wargus/stratagus
#URL: http://stratagus.sourceforge.net
Source0: %name-%version.tar

Source1: stratagus-16.png
Source2: stratagus-32.png
Source3: stratagus-48.png

#Patch1: stratagus-2.1-alt-gc.patch
#Patch2: stratagus-2.1-alt-FunctionName.patch

BuildRequires(pre): cmake rpm-macros-cmake gcc-c++
BuildRequires: doxygen bzlib-devel libGL-devel libGLES-devel libGLU-devel libSDL-devel libX11-devel libmikmod-devel libmng-devel libpng-devel libsqlite3-devel libtheora-devel pkgconfig(ogg) pkgconfig(oggz) pkgconfig(vorbis) pkgconfig(vorbisenc) pkgconfig(vorbisfile) tolua++-devel zlib-devel

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

%package doc
Summary:        Documentation  for %name
Group:          Documentation 
BuildArch:      noarch
Requires:       %name = %version-%release

%description doc
This package contains documentation for %name.

%prep
%setup -n %name-%version

%build
%cmake -DENABLE_DEV=ON \
       -DENABLE_UPX=ON \
       -DENABLE_DOC=ON \
       -DENABLE_TOUCHSCREEN=ON
       
%make_build -C BUILD

%install
%makeinstall_std -C BUILD

mkdir -p %buildroot%_gamesdatadir/%name

mkdir -p %buildroot%_man6dir/
mv doc/*.6 %buildroot%_man6dir

install -pD -m644 %SOURCE1 %buildroot%_miconsdir/%name.png
install -pD -m644 %SOURCE2 %buildroot%_niconsdir/%name.png
install -pD -m644 %SOURCE3 %buildroot%_liconsdir/%name.png

%find_lang %name

%files -f %name.lang
%_gamesbindir/%name
%_sbindir/metaserver
%_bindir/png2%name
%_man6dir/%name.6*
%dir %_gamesdatadir/%name
%_miconsdir/%name.png
%_niconsdir/%name.png
%_liconsdir/%name.png

%files devel
%_includedir/*

%files doc
%_docdir/%name

%changelog
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
