Name:		gish
Version:	1.53
Release:	alt2
License:	GPLv2
Summary:	2D platformer with 12-pound ball of tar named Gish as a hero
Group:		Games/Arcade
URL: http://crypticsea.blogspot.com/2010/05/gish-open-source.html
# http://github.com/blinry/gish
# http://github.com/blinry/gish.git
Source:		%name-%version.tar
Source1:	%name.sh.in

Requires: gxmessage
%define GSHARE %_gamesdatadir/%name
%define GHOME $HOME/.%name
%define MSG You must install your copy of GISH files into %GSHARE or %GHOME

# Automatically added by buildreq on Mon May 31 2010
BuildRequires: cmake libGL-devel libSDL-devel libopenal-devel libvorbis-devel

%description
Gish isn't your average hero, in fact he's not your average anything...
see Gish is a ball of tar. A Sunday stroll with his lady friend Brea
goes awry when a shadowy figure emerges from an open man hole and pulls
Brea into the ground below. Following Brea's calls for help Gish
suddenly finds himself in the subterranean sewers of Dross, a long
forgotten city filled with twisting corridors, evil traps and some of
the most demented creatures imaginable.

With his gelatinous structure as his only means of defense Gish must
follow the echoing cries of his damsel in distress deep into the earth
below. What freakish creatures dwell in this subterranean land? Who is
Brea's captor? And just how far down does the rabbit hole go?

Life isn't easy when you're a 12 pound ball of tar...

%MSG

%prep
%setup
sed -i 's/target_link_libraries(gish/target_link_libraries(gish -lm/' CMakeLists.txt

%build
sed 's|@GSHARE@|%GSHARE|g
s|@GHOME@|%GHOME|g
s|@MSG@|%MSG|g' < %SOURCE1 > %name.sh

cmake cmake -DCMAKE_INSTALL_PREFIX=/usr -DLIB_DESTINATION=%_lib -DCMAKE_CXX_FLAGS:STRING='-pipe -Wall -O2' -DCMAKE_C_FLAGS:STRING='-pipe -Wall -O2' -DCMAKE_C_FLAGS_RELEASE:STRING="-DNDEBUG" -DCMAKE_CXX_FLAGS_RELEASE:STRING="-DQT_NO_DEBUG" -DCMAKE_SKIP_RPATH:STRING="ON" .
%make_build

%install
install -D %name %buildroot%_gamesbindir/%name.bin
install -D %name.sh %buildroot%_gamesbindir/%name

%files
%_gamesbindir/*

%changelog
* Thu May 24 2012 Fr. Br. George <george@altlinux.ru> 1.53-alt2
- DSO list completion

* Tue Jun 01 2010 Fr. Br. George <george@altlinux.ru> 1.53-alt1
- Initial build from scratch

