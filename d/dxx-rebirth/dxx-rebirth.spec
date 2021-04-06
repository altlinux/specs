Summary: The port of Descent/Descent 2 for Linux
Name: dxx-rebirth
Version: 20210326
Release: alt1
License: GPLv3
Group: Games/Arcade
Url: https://www.dxx-rebirth.com
Patch: dxx-d1x-rebirth-utilities.patch
Source: %{name}_%version-src.tar.xz
Requires: d1x-rebirth d2x-rebirth

# Automatically added by buildreq on Tue Apr 06 2021
# optimized out: fontconfig glibc-kernheaders-generic glibc-kernheaders-x86 libImageMagick6-common libSDL2-devel libglvnd-devel libstdc++-devel pkg-config python2-base python3 python3-base python3-module-pkg_resources sh4 xz zlib-devel
BuildRequires: ImageMagick-tools dos2unix flex gcc-c++ git-core libGLU-devel libSDL2_image-devel libSDL2_mixer-devel libphysfs-devel libpng-devel scons

%description
This is the port of Descent and Descent 2, the famous 3D games for PC.

D2X is based on source code that was released the 14 December 1999 by
Parallax Software Corporation.

%package -n d1x-rebirth
Group: Games/Arcade
License: GPLv3
Summary: The port of Descent for Linux
Obsoletes: d1x-rebirth-sdl <= 0.58.1 d1x-rebirth-gl <= 0.58.1

%description -n d1x-rebirth
%summary
To use this package you'll need some datafiles installed in %_datadir/descent.

You may use SHAREWARE version of descent with d2x
You can get desc14sw.tar.gz from here:
http://icculus.org/d2x/
and untar it like this:
tar xvf desc14sw.tar.gz --one-top-level=$HOME/.d1x-rebirth --strip=1

%package -n d2x-rebirth
Group: Games/Arcade
License: GPLv3
Summary: The port of Descent 2 for Linux
Obsoletes: d2x-rebirth-sdl <= 0.58.1 d2x-rebirth-gl <= 0.58.1

%description -n d2x-rebirth
%summary
To use this package you'll need some datafiles installed in %_datadir/descent2.

You may use SHAREWARE version of descent with d2x
You can get d2shar10.tar.gz from here:
http://icculus.org/d2x/
and untar it like this:
tar xvf d2shar10.tar.gz --one-top-level=$HOME/.d2x-rebirth --strip=1

%prep
%setup -n %{name}_%version-src
%patch -p1

dos2unix     */*.ini */*.txt
sed -i '/MAX_MULTI_MESSAGE_LEN+4/s/MAX_MULTI_MESSAGE_LEN+4/MAX_MULTI_MESSAGE_LEN+22/' common/main/multi.h
sed -i '/MAX_MULTI_MESSAGE_LEN+4/s/MAX_MULTI_MESSAGE_LEN+4/MAX_MULTI_MESSAGE_LEN+22/' similar/main/multi.cpp

%build
for i in 16 32 48 64 128; do
  for x in 1 2; do
	convert d${x}x-rebirth/d${x}x-rebirth.xpm d${x}x-$i.png
  done
done

scons -C d1x-rebirth/utilities

for F in d2x-rebirth/utilities/*.c; do
	make ${F%%.c}
done

%define SCOPTS prefix=/usr \\\
	d1x_sharepath=%_datadir/descent \\\
	d2x_sharepath=%_datadir/descent2 \\\
    d1x_program_name=`pwd`/d1x-rebirth/d1x-rebirth \\\
    d2x_program_name=`pwd`/d2x-rebirth/d2x-rebirth \\\
	sdlmixer=1 \\\
	sdl2=1 \\\
    editor=1 \\\
	verbosebuild=1

scons 	-j`nproc` %SCOPTS

	#sdl_opengl=0 sdlmixer=1 \
	#dxx=sdl, dxx=ogl,e, \
	#d1x_ogl_program_name=d2x-rebirth-gl \
	#d1x_sdl_program_name=d2x-rebirth-sdl \
	#d2x_ogl_program_name=d2x-rebirth-gl \
	#d2x_sdl_program_name=d2x-rebirth-sdl \

%install
for i in 16 32 48 64 128; do
  for x in 1 2; do
	install -D d${x}x-$i.png %buildroot%_iconsdir/hicolor/${i}x${i}/apps/d${x}x-rebirth.png
  done
done

for F in d2x-rebirth/utilities/*.c; do
	P=${F##*/}
	install -D ${F%%.c} %buildroot%_bindir/${P%%.c}
	install -D ${F%%.c}.1 %buildroot%_man6dir/${P%%.c}.6
done

scons	%SCOPTS DESTDIR=%buildroot install

mkdir -p %buildroot%_datadir/descent/missions
mkdir -p %buildroot%_datadir/descent2/missions
install d1x-rebirth/utilities/macd1extract %buildroot%_bindir/
mkdir -p %buildroot%_desktopdir
install */*.desktop %buildroot%_desktopdir/

%files -n d1x-rebirth
%doc d1x*/*.txt d1x*/*.plist d1x*/*.ini
%_datadir/descent
%_iconsdir/hicolor/*/*/d1x*.png
%_bindir/d1x*
%_bindir/macd1extract
%_desktopdir/d1x*

%files -n d2x-rebirth
%doc d1x*/*.txt d1x*/*.plist d1x*/*.ini
%_datadir/descent2
%_man6dir/*
%_iconsdir/hicolor/*/*/d2x*.png
%_bindir/*
%exclude %_bindir/d1x*
%exclude %_bindir/macd1extract
%_desktopdir/d2x*

%changelog
* Tue Apr 06 2021 George V. Kouryachy (Fr. Br. George) <george@altlinux.org> 20210326-alt1
- Final (?) update

* Sat Mar 28 2020 Fr. Br. George <george@altlinux.ru> 20200301-alt1
- Initial build from source

