Name:		crates
Version:	0.7.1
Release:	alt3
Summary:	Extensible 3D crate moving puzzle game
Group:		Games/Puzzles
License:	GPL
Source:		%name-%version.tar.gz
Source1:	oexedirname.c
Patch:		%name-localconfig.patch
URL:		http://www.octaspire.com/crates/

# Automatically added by buildreq on Sun Aug 29 2010
BuildRequires: ctest libGL-devel libSDL_mixer-devel libXScrnSaver-devel libXau-devel libXcomposite-devel libXcursor-devel libXdmcp-devel libXext-devel libXft-devel libXinerama-devel libXpm-devel libXrandr-devel libXt-devel libXtst-devel libXv-devel liblua5-devel libpng-devel libxkbfile-devel

%description
Crates is a three dimensional puzzle game. It consists of missions
that consist of levels. To pass a level, you must move player to the
exit by interacting with the different kinds of crates in the level.
Before that you must also collect all the keys and toggle all the
toggles that the level might contain. Every level has a password that
makes it possible to continue playing from that level whenever you
want, but if you want to get your name in the hall of fame, you must
play the whole mission at one go. On that case, the faster you are, the
better is your position in the hall of fame.

%prep
%setup
sed 's+@EXEDIRNAME@+%_gamesdatadir/%name/.+g' < %SOURCE1 > src/posix/linux/oexedirname.c
%patch
sed -i 's/target_link_libraries(crates/target_link_libraries(crates -lm/' CMakeLists.txt

%build
mkdir build
cd build
cmake .. -DCMAKE_SKIP_RPATH:BOOL=yes -DCMAKE_BUILD_TYPE=MinSizeRel -DCMAKE_C_FLAGS:STRING='%optflags' -DCMAKE_INSTALL_PREFIX=%prefix 
%make_build

%install
install -D %name %buildroot%_gamesbindir/%name
mkdir -p %buildroot%_gamesdatadir/%name
cp -r resources %buildroot%_gamesdatadir/%name
install -D man/man6/%name.6 %buildroot%_man6dir/%name.6

%files
%doc README HISTORY
%_gamesbindir/%name
%dir %_gamesdatadir/%name
%_gamesdatadir/%name/*
%_man6dir/*

%changelog
* Thu May 24 2012 Fr. Br. George <george@altlinux.ru> 0.7.1-alt3
- DSO list completion

* Wed Sep 01 2010 Fr. Br. George <george@altlinux.ru> 0.7.1-alt2
- Homepage URL added

* Sun Aug 29 2010 Fr. Br. George <george@altlinux.ru> 0.7.1-alt1
- Initial build from scratch

