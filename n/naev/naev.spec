%define rev 05df6692
Name: naev
Version: 0.5.3
Release: alt1.%rev
Summary: NAEV is a 2D space trading and combat game, in a similar vein to Escape Velocity
Group: Games/Other
License: GPLv3
Packager: Andrew Clark <andyc@altlinux.org>
Url: http://naev.org
Source: http://naev.googlecode.com/files/%name-%version.tar.bz2
#Source1: %name.desktop
Source2: %name.png
Source3: %name.sh
Patch0: %name-desktop.patch

# Automatically added by buildreq on Mon Jun 13 2011
# optimized out: libGL-devel libGLU-devel libSDL-devel libogg-devel pkg-config zlib-devel
BuildRequires: libSDL_image-devel libSDL_mixer-devel libfreetype-devel libopenal-devel libpng-devel libvorbis-devel libxml2-devel

Requires: %name-data = %version

%description
NAEV is a space trading and combat game, inspired by Escape Velocity.
Played from a top-down perspective with isometric sprites, the player
is free to explore the galaxy as they see fit, trading or pirating
their way to a vast fortune. NAEV is set in a futuristic science
fiction environment, in which the player finds himself in the wake of
a massive galactic cataclysm which erupted from the Sol system and
destroyed everything within tens of lightyears, resulting in a
massive, volatile nebula.

%package data
Group: Games/Other
Summary: naev data files
BuildArch: noarch

%description data
naev data files.

%prep
%setup
%patch0 -p1

%build
%autoreconf
%configure --enable-debug=no --docdir=%_docdir/%name-%version --with-ndata-path=%_gamesdatadir/ndata/
%make_build

%install
mkdir -p %buildroot{%_bindir,%_man6dir,%_desktopdir,%_liconsdir}
%makeinstall_std
install -pD -m 755 %buildroot%_datadir/%name/%name-confupdate.sh %buildroot%_bindir/%name-confupdate
rm -rf %buildroot%_datadir/%name/
install -pD -m 644 %SOURCE2 %buildroot%_liconsdir/%name.png
install -pD -m 755 %SOURCE3 %buildroot%_bindir/%name.sh

%files
%doc AUTHORS LICENSE README TODO
%_bindir/*
%_man6dir/*
%_pixmapsdir/*.png
%_desktopdir/%name.desktop
%_liconsdir/*.png
%files data
%_gamesdatadir/ndata/

%changelog
* Mon Apr 30 2012 Andrew Clark <andyc@altlinux.org> 0.5.3-alt1.05df6692
- version update to 0.5.3-alt1.05df6692

* Fri Mar 23 2012 Andrew Clark <andyc@altlinux.org> 0.5.1-alt1.ab21e6f4
- version update to 0.5.1-alt1.ab21e6f4

* Sun Jan 1 2012 Andrew Clark <andyc@altlinux.org> 0.5.0-alt1.c4bb297
- version update to 0.5.0-alt1.c4bb297

* Tue Sep 27 2011 Andrew Clark <andyc@altlinux.org> 0.5.0-alt1.8a56300
- version update to 0.5.0-alt1.8a56300

* Sun Sep 25 2011 Andrew Clark <andyc@altlinux.org> 0.5.0-alt1.711a428
- version update to 0.5.0-alt1.711a428

* Mon Jun 13 2011 Andrew Clark <andyc@altlinux.org> 0.5.0-alt1.375f72e
- initial build for ALT.

