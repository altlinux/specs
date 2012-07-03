Name: pipenightdreams
Version: 0.10.0
Release: alt3.qa1

Summary: Connect the waterpipes to create a proper pipeline
Group: Games/Puzzles
License: GPLv2+
URL: http://www.libsdl.org/projects/pipenightdreams/

Source0: http://www.libsdl.org/projects/pipenightdreams/packages/pipenightdreams-0.10.0.tar.gz
Source1: %name.desktop
Source2: pipenightdreams-48x48.png
Source3: pipenightdreams-32x32.png
Source4: pipenightdreams-16x16.png

Patch0: pipenightdreams-0.10.0-gcc41.patch
Patch1: pipenightdreams-0.10.0-datadir.patch
Patch2: pipenightdreams-0.10.0-sanitize.patch
Patch3: pipenightdreams-0.10.0-quit.patch

Packager: Igor Zubkov <icesik@altlinux.org>

# Automatically added by buildreq on Sat Nov 15 2008
BuildRequires: flex gcc-c++ libSDL-devel libSDL_image-devel
BuildRequires: desktop-file-utils

%description
PipeNightDreams is a puzzle-game where you must race against the clock to
connect the waterpipes to create a proper pipeline before the water starts
flowing. It has 25 levels with increasing difficulty, and you can create
your own by just editing text files. It has a lot of cool graphics, score,
lives, required pipes per level and an easy and fast interface.

%prep
%setup -q
%patch0 -p1 -z .gcc41
%patch1 -p1 -z .datadir
%patch2 -p1 -z .sanitize
%patch3 -p1 -z .quit

%build
%configure
%make_build CXXFLAGS="%optflags -I/usr/include/SDL"

%install
%make_install DESTDIR=%buildroot install

# fix up the broken datadir install (its this or patch a zillion makefiles)
mv %buildroot%_datadir/games/%name %buildroot%_datadir
rmdir %buildroot%_datadir/games

mkdir -p %buildroot%_desktopdir/
install -p -m 644 %SOURCE1 %buildroot%_desktopdir/

mkdir -p %buildroot%_niconsdir/
mkdir -p %buildroot%_liconsdir/
mkdir -p %buildroot%_miconsdir/

install -p -m 644 %SOURCE2 %buildroot%_liconsdir/%name.png
install -p -m 644 %SOURCE3 %buildroot%_niconsdir/%name.png
install -p -m 644 %SOURCE4 %buildroot%_miconsdir/%name.png
desktop-file-install --dir %buildroot%_desktopdir \
	--add-category=LogicGame \
	%buildroot%_desktopdir/pipenightdreams.desktop

%files
%doc README TODO ChangeLog
%_bindir/%name
%_datadir/%name
%_man6dir/pipenightdreams.*
%_desktopdir/*.desktop
%_niconsdir/%name.png
%_liconsdir/%name.png
%_miconsdir/%name.png

%changelog
* Tue May 17 2011 Repocop Q. A. Robot <repocop@altlinux.org> 0.10.0-alt3.qa1
- NMU (by repocop): the following fixes applied:
  * freedesktop-desktop-file-proposed-patch for pipenightdreams

* Sat Nov 15 2008 Igor Zubkov <icesik@altlinux.org> 0.10.0-alt3
- apply patch from repocop

* Fri Jul 11 2008 Igor Zubkov <icesik@altlinux.org> 0.10.0-alt2
- fix desktop file and icons

* Sun Dec 16 2007 Igor Zubkov <icesik@altlinux.org> 0.10.0-alt1
- build for Sisyphus

* Tue Aug 29 2006 Hans de Goede <j.w.r.degoede@hhs.nl> 0.10.0-5
- FE6 Rebuild

* Sat Jun 10 2006 Hans de Goede <j.w.r.degoede@hhs.nl> 0.10.0-4
- Add BuildRequires: flex to fix building with new stripped mock config.

* Sun May  7 2006 Hans de Goede <j.w.r.degoede@hhs.nl> 0.10.0-3
- Add Patch3 which fixes quiting during the "try again dialog" (bz 188345)

* Fri Apr  7 2006 Hans de Goede <j.w.r.degoede@hhs.nl> 0.10.0-2
- Remove use of a trademarked term from %%description, manpage and docs

* Wed Apr  5 2006 Hans de Goede <j.w.r.degoede@hhs.nl> 0.10.0-1
- initial Fedora Extras package
