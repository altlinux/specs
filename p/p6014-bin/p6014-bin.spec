%define _unpackaged_files_terminate_build 1
%def_without debug

%define rname p6014
%define what bin
Name: %rname-%what
Version: 0.2.1
Release: alt3

Group: Games/Adventure
Summary: Mod sequel to Star Control II: The Ur-Quan Masters
Url: http://code.google.com/p/project6014/
License: GPLv2+

Requires: %rname-content = 0.2.1
Requires: %rname-common = %version
#Obsoletes: %rname-game
#Depends: libgl1-mesa-glx | libgl1, libmikmod2 (>= 3.1.10), libsdl-image1.2 (>= 1.2.10), libsdl1.2debian (>= 1.2.10-1), libvorbisfile3 (>= 1.1.2), zlib1g (>= 1:1.1.4), p6014-content (>= 0.2.1)
#Recommends: p6014-hires (>= 0.2.1)

Source0: %rname-%version-src.tar.gz

Source10: %rname.png
Source11: config.state

BuildRequires: libGL-devel libmikmod-devel libopenal-devel libSDL-devel
BuildRequires: libSDL_image-devel libvorbis-devel zlib-devel

%description
Project 6014 - A fan-made sequel to The Ur-Quan Masters

It is the year 2165.
Four years ago you travelled the galaxy, assembling the scattered forces of the old Alliance of Free Stars, striving to free the human race from Ur-Quan enslavement.
You succeeded.
The Ur-Quan fled, leaving their Hierarchy forces in disarray. The Chmmr have emerged as the new leaders of known space and have asserted their authority.
Slave worlds have been freed. And a new era of peace has emerged.
For their service to the Ur-Quan defense, Hierarchy battle thralls have been punished.
The New Alliance of Free Stars is rebuilding decimated homeworlds, and continues to drive out the scattered Ur-Quan from known space.
After many years of travelling the galaxy fighting the Ur-Quan, a peaceful life on Unzervalt with Talana beckons. You have devoted your years to the study of Precursor technology, not willing to be involved in diplomacy, politics or military operations.
But your new life must wait.
Alliance command at Procyon has received a distress signal from a Shofixti scout deep in unknown space. The urgent, garbled message refers to an enormous machine that destroyed several scout vessels upon contact. Then... only static.
The Chmmr have asked YOU to lead an expedition to travel to the distress site far from Earth to track down the Shofixti and neutralize this artifact.
As you punch through the fabric of truespace, you wonder: Are you ready for this?

This package contains binary executable program for this game.


%prep
%setup -c -n %rname-%version

%build
export CFLAGS="%optflags" LDFLAGS="%optflags -lm"

cd sc2
rm -f config.state
%if_with debug
echo "CHOICE_debug_VALUE='debug'" >> config.state
%else
echo "CHOICE_debug_VALUE='nodebug'" >> config.state
%endif
cat %{SOURCE11} >> config.state
echo "INPUT_install_libdir_VALUE='$prefix/%_lib'" >> config.state
./build.sh uqm << __EOF__


__EOF__

%install
mkdir -p %buildroot/{%_gamesbindir,%_desktopdir,%_libdir/games}
mkdir -p %buildroot/%_gamesdatadir/%rname/content/packages/addons
%if_with debug
install -m 755 sc2/%{rname}-debug %buildroot/%_libdir/games/%{rname}
%else
install -m 755 sc2/%{rname} %buildroot/%_libdir/games/%{rname}
%endif
install -m 644 sc2/content/version %buildroot/%_gamesdatadir/%rname/content/version

cat > %buildroot%_gamesbindir/%{rname} <<'__EOF__'
#!/bin/sh
# Wrapper script for starting Project 6014
exec "%_libdir/games/%{rname}" "--contentdir=/usr/share/games/p6014/content" "$@"
__EOF__
chmod 755 %buildroot%_gamesbindir/%{rname}

cat > %buildroot%_desktopdir/%rname.desktop <<__EOF__
[Desktop Entry]
Version=1.0
Type=Application
Name=Project 6014
Exec=%_gamesbindir/%rname
Icon=%rname
Categories=Game;AdventureGame;
Comment=A fan-made sequel to The Ur-Quan Masters
__EOF__

# when option will appear, uncomment, add option for x4mode
# and move to corresponding hires packs
#cat > %buildroot%_desktopdir/%rname-hires.desktop <<__EOF__
#[Desktop Entry]
#Version=1.0
#Type=Application
#Name=Project 6014 - High Resolution
#Exec=%_gamesbindir/%rname -q high -f -o
#Icon=%rname
#Categories=Game;AdventureGame;
#Comment=A fan-made sequel to The Ur-Quan Masters (high resolution mode)
#__EOF__

mkdir -p %buildroot/%_liconsdir/
install -m 644 %SOURCE10 %buildroot/%_liconsdir/%rname.png

%files
%doc sc2/{AUTHORS,COPYING,ChangeLog,README,WhatsNew,uqm.lsm}
%doc sc2/doc/users/manual* sc2/doc/devel
%_gamesbindir/%rname
%_gamesdatadir/%rname
%_libdir/games/%{rname}
%_desktopdir/*.desktop
%_liconsdir/%rname.png

%changelog
* Tue Apr 01 2014 Igor Vlasenko <viy@altlinux.ru> 0.2.1-alt3
- added -lm -- fixed linkage

* Wed May 01 2013 Igor Vlasenko <viy@altlinux.ru> 0.2.1-alt2
- dropped hires desktop - misleading as switch to hires x4 is manual

* Mon Apr 29 2013 Igor Vlasenko <viy@altlinux.ru> 0.2.1-alt1
- initial spec
