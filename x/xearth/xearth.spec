Name: xearth
Version: 1.1
Release: alt1.qa2
Epoch: 1

Summary: An X display of the Earth from space
License: MIT
Group: Toys

Url: http://hewgill.com/xearth/original/
Source0: ftp://cag.lcs.mit.edu/pub/tuna/xearth-1.1.tar.bz2
Source1: xearth_locations.txt
Source3: xearth16.xpm
Source4: xearth32.xpm
Source5: xearth48.xpm
Packager: Michael Shigorin <mike@altlinux.org>

# Automatically added by buildreq on Sat Mar 04 2006
BuildRequires: imake libICE-devel libSM-devel libX11-devel libXext-devel libXt-devel xorg-cf-files xorg-x11-proto-devel

Summary(fr): affiche en 3D la terre vue du soleil en fonds d'écran

%description
Xearth is an X Window System based graphic that shows a globe of the
Earth, including markers for major cities and MandrakeSoft.  The
Earth is correctly shaded for the current position of the sun, and the
displayed image is updated every five minutes.

%description -l fr
Xearth est un programme pour le système X Window qui affiche le globe terrestre
en 3D, tel qui l'est vu du soleil (avec ombrage).  Les continents sont
parsemées par des points indiquant les grandes villes ainsi que le siège de
MandrakeSoft.
L'écran est mis à jour toutes les 5mn.

%prep
%setup

%build
xmkmf
%make CDEBUGFLAGS="%optflags"

%install
make DESTDIR=%buildroot install install.man
mkdir -p %buildroot%_datadir/xearth
cp %SOURCE1 %buildroot%_datadir/xearth/xearth_locations.txt

#install icons
mkdir -p %buildroot%_miconsdir
mkdir -p %buildroot%_niconsdir
mkdir -p %buildroot%_liconsdir

cp %SOURCE3 %buildroot%_miconsdir/xearth.xpm
cp %SOURCE4 %buildroot%_niconsdir/xearth.xpm
cp %SOURCE5 %buildroot%_liconsdir/xearth.xpm

install -m755 -d %buildroot%_desktopdir/
cat > %buildroot%_desktopdir/%{name}.desktop <<EOF
[Desktop Entry]
Version=1.0
Type=Application
Name=Xearth
Comment=Display the Earth on your desktop
Exec=%name -bigstars 20 -label -labelpos -5-150 -markerfile /usr/share/xearth/xearth_locations.txt
Icon=%name
Terminal=false
Categories=Game;Amusement;
EOF

%files
%_x11bindir/*
%_x11mandir/man1/*
%_datadir/%name/
%_desktopdir/%name.desktop
%_miconsdir/*.xpm
%_niconsdir/*.xpm
%_liconsdir/*.xpm

%changelog
* Mon Apr 18 2011 Igor Vlasenko <viy@altlinux.ru> 1:1.1-alt1.qa2
- NMU: converted menu to desktop file

* Thu Dec 04 2008 Michael Shigorin <mike@altlinux.org> 1:1.1-alt1.1
- applied repocop patch

* Tue May 13 2008 Michael Shigorin <mike@altlinux.org> 1:1.1-alt1
- picked up such an orphan

* Sat Mar 04 2006 Sergei Epiphanov <serpiph@altlinux.ru> 1.1-ipl11mdk
- cleanup spec

* Tue Oct 15 2002 Stanislav Ievlev <inger@altlinux.ru> 1.1-ipl10mdk
- rebuild with gcc3

* Tue Jul 24 2001 Stanislav Ievlev <inger@altlinux.ru> 1.1-ipl9mdk
- Returned Paris to it's place on Earth.

* Wed Jan 17 2001 AEN <aen@logic.ru>
- RE adaptation
* Tue Aug 08 2000 Frederic Lepied <flepied@mandrakesoft.com> 1.1-7mdk
- automatically added BuildRequires

* Wed Jul 26 2000 Thierry Vignaud <tvignaud@mandrakesoft.com> 1.1-6mdk
- fix buildroot

* Mon Jul 24 2000 Thierry Vignaud <tvignaud@mandrakesoft.com> 1.1-5mdk
- use new macros

* Fri Apr 28 2000 DindinX <odin@mandrakesoft.com> 1.1-4mdk
- Added 32x32 and 48x48 icons

* Fri Apr 28 2000 DindinX <odin@mandrakesoft.com> 1.1-3mdk
- remove menu icon path

* Wed Apr 26 2000 DindinX <odin@mandrakesoft.com> 1.1-2mdk
- added an icon for the menu

* Wed Apr  5 2000 DindinX <odin@mandrakesoft.com> 1.1-1mdk
- New version
- Added menu
- Use a more complete markerfile

* Sat Mar 25 2000 Dindinx <odin@mandrakesoft.com> 1.0-6mdk
- Use spec-helper
- Fix group

* Tue Nov 02 1999 Pablo Saratxaga <pablo@mandrakesoft.com>
- rebuild for new environment

* Wed Jul 28 1999 Thierry Vignaud <tvignaud@mandrakesoft.com>
- remove unuseful patch
- add MandrakeSoft home on map
- add french translation
- fix english description

* Thu May 06 1999 Bernhard Rosenkraenzer <bero@mandrakesoft.com>
- Mandrake adaptions
- handle RPM_OPT_FLAGS
