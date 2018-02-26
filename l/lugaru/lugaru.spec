Name:		lugaru
# ( cd lugaru; hg log | head -1 | cut -d: -f2 )
Version:	0.0.r262
Release:	alt2
Group:		Games/Adventure
Summary:	A well-trained ninja rabbit fight through a detailed 3D world
License:	GPL
# hg clone http://hg.icculus.org/icculus/lugaru
Source:		%name-%version.tar
Source1:	Makefile

# Automatically added by buildreq on Sat May 15 2010
BuildRequires: gcc-c++ libGL-devel libSDL-devel libjpeg-devel libopenal-devel libpng-devel libvorbis-devel cmake

%description
Lugaru (pronounced Loo-GAH-roo) is the predecessor to Overgrowth. It is
a DRM-free, third-person action game available for Mac, Windows, and
Linux. The main character, Turner, is an anthropomorphic rebel bunny
rabbit with impressive combat skills. In his quest to find those
responsible for slaughtering his village, he uncovers a far-reaching
conspiracy involving the corrupt leaders of the rabbit republic and the
starving wolves from a nearby den. Turner takes it upon himself to fight
against their plot and save his fellow rabbits from slavery.

%package data
License: nonfree
Group: Games/Adventure
Summary: %name game data and artwork
BuildArch: noarch
Requires: %name = %version

%description data
Game data for %name, %summary

%prep
%setup
find . -name .DS_Store -exec rm {} \;

sed -i '/chdirToAppPath(argv\[0\]);/s@.*@ chdir("%_gamesdatadir/%name");@' Source/OpenGL_Windows.cpp
sed -i '/ConvertFileName(mapname), "wb"/s@ConvertFileName(mapname), "wb"@ConvertFileName(mapname, "w"), "wb"@' Source/GameInitDispose.cpp

mkdir build

%build
cd build
cmake .. -DCMAKE_SKIP_RPATH:BOOL=yes -DCMAKE_BUILD_TYPE=MinSizeRel -DCMAKE_C_FLAGS:STRING='-pipe -Wall -O2' -DCMAKE_CXX_FLAGS:STRING='-pipe -Wall -O2' -DCMAKE_INSTALL_PREFIX=%_prefix -DLIB_DESTINATION=%_lib -DLUGARU_INSTALL_PREFIX=%_gamesdatadir/%name\
    %if "lib64" == "lib64" 
    -DLIB_SUFFIX="64"
    %else 
    -DLIB_SUFFIX=""
    %endif 

%make_build

%install
cd build
%makeinstall DESTDIR=%buildroot
install -m755 -D %buildroot%_gamesdatadir/%name/%name %buildroot%_gamesbindir/%name
rm %buildroot%_gamesdatadir/%name/%name

%files
%_gamesbindir/*

%files data
%doc CONTENT-LICENSE.txt
%_gamesdatadir/%name

%changelog
* Sun May 16 2010 Fr. Br. George <george@altlinux.ru> 0.0.r262-alt2
- Fix 'user do not saved' bug

* Sun May 16 2010 Fr. Br. George <george@altlinux.ru> 0.0.r262-alt1
- Initial build from scratch

