Summary: Fight evil balls by dividing each to a pair of smaller one
Name: ceferino
Version: 0.97.8
Release: alt2.qa1
URL: http://www.losersjuegos.com.ar
Source: %name-%version.tar.gz
Source1: %name.desktop
Patch: %name-gcc44.patch
License: GPL
Group: Games/Arcade
Packager: Fr. Br. George <george@altlinux.ru>
# Automatically added by buildreq on Sat Mar 25 2006
BuildRequires: gcc-c++ libSDL-devel libSDL_image-devel libSDL_mixer-devel
Requires: /usr/bin/sound_wrapper

%description
Fight evil balls by dividing each to a pair of smaller one until they disappear


%prep
%setup -q
%patch -p1

%build
%configure --bindir=%_gamesbindir --datadir=%_gamesdatadir
%make_build

%install
mkdir -p %buildroot{%_gamesbindir,%_gamesdatadir}
make install DESTDIR=%buildroot

# desktop-file
install -p -m644 -D %SOURCE1  %buildroot%_desktopdir/%name.desktop
install -D data/ima/icono.png %buildroot%_liconsdir/%name.png

%files
%_gamesbindir/*
%_gamesdatadir/*
%_desktopdir/%name.desktop
%_liconsdir/%name.png
%doc README ChangeLog TODO AUTHORS

%changelog
* Tue Apr 12 2011 Igor Vlasenko <viy@altlinux.ru> 0.97.8-alt2.qa1
- NMU: .desktop files should use /usr/bin/sound_wrapper

* Wed May 27 2009 Fr. Br. George <george@altlinux.ru> 0.97.8-alt2
- GCC4.4 build fixup

* Wed Oct 10 2007 Fr. Br. George <george@altlinux.ru> 0.97.8-alt1
- Initial ALT build

