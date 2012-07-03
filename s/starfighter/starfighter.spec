Name: starfighter
Version: 1.2
Release: alt1

Summary: Project: Starfighter - old school 2D shoot'em up
Group: Games/Arcade
License: GPL
Url: http://sourceforge.net/projects/pr-starfighter/

Source: %name-%version.tar.gz
Source1: %name.desktop

Patch0: %name-1.1-alt-makefile.patch

# Automatically added by buildreq on Wed Mar 22 2006
BuildRequires: gcc-c++ libSDL-devel libSDL_image-devel libSDL_mixer-devel

%description
Project: Starfighter is an old school 2D shoot 'em up. In the game you
take on the role of a rebel pilot called Chris, who is attempting to
overthrow a military corporation called Weapco. Weapco has seized
control of the known universe and currently rules it with an iron fist.
Chris can no longer stand back and watch as millions of people suffer
and die. He steals an experimental craft known as "Firefly" and begins
his mission to fight his way to Sol, freeing key systems along the way.
The game opens with Chris attempting to escape a Weapco patrol that has
intercepted him.

%prep
%setup
#patch0 -p1

%build
%make_build \
	BINDIR="%_gamesbindir/" \
	DATADIR="%_gamesdatadir/%name/" \
	DOCDIR="%_defaultdocdir/%name" \
	OPT_CFLAGS="$RPM_OPT_FLAGS"

%install
mkdir -p %buildroot%_gamesbindir/
mkdir -p %buildroot%_gamesdatadir/%name/
mkdir -p %buildroot%_defaultdocdir/%name/

%makeinstall \
	BINDIR="%_gamesbindir/" \
	DATADIR="%_gamesdatadir/%name/" \
	DOCDIR="%_defaultdocdir/%name" \
	DESTDIR="%buildroot"

install -D %SOURCE1 %buildroot%_desktopdir/%name.desktop
install -D gfx/rocketAmmo.png %buildroot%_niconsdir/%name.png

%files
%doc %_defaultdocdir/%name/*
%_gamesbindir/*
%_gamesdatadir/%name/
%_desktopdir/%name.desktop
%_niconsdir/%name.png

%changelog
* Mon Jun 18 2012 Fr. Br. George <george@altlinux.ru> 1.2-alt1
- Autobuild version bump to 1.2
- Fix build

* Wed May 12 2010 Fr. Br. George <george@altlinux.ru> 1.1.1-alt3
- Resurrected from orphaned
- Replace menu file by desktop file

* Wed Mar 22 2006 Igor Zubkov <icesik@altlinux.ru> 1.1.1-alt2
- fix build with new ld / -Wl,--as-needed

* Fri Aug 05 2005 Igor Zubkov <icesik@altlinux.ru> 1.1.1-alt1
- Initial build for Sisyphus
