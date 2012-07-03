Name: prboom
Version: 2.5.0
Release: alt0.3

Summary: Doom - classic 3D shoot-em-up game
Group: Games/Arcade
URL: http://prboom.sourceforge.net/
License: GPL

Source0: %name-%version.tar.gz

Packager: Ilya Mashkin <oddity@altlinux.ru>

# Automatically added by buildreq on Mon Aug 14 2006
BuildRequires: esound libpng-devel libSDL-devel libSDL_mixer-devel libSDL_net-devel linux-libc-headers

%description
Doom is the classic 3D shoot-em-up game. It must have been one of the best
selling games ever; it totally outclassed any  3D world games that preceded
it, with amazing speed, flexibility, and outstanding gameplay. The specs to
the game were released, and thousands of extra levels were written by fans of
the game; even today new levels are written for Doom faster then any one person
could play them.

%prep
%setup -q

%build
%configure \
	--disable-cpu-opt
%make_build

%install
%make_install DESTDIR=%buildroot docdir=%_docdir/%name-%version/ install

rm -rf %buildroot%_docdir/%name-%version/COPYING

%files
%doc %dir %_docdir/%name-%version
%_docdir/%name-%version/*
%_gamesbindir/*
%_gamesdatadir/doom/prboom.wad
%_man5dir/*
%_man6dir/*

%changelog

* Sun May 01 2011 Ilya Mashkin <oddity@altlinux.ru> 2.5.0-alt0.3
- rebuild

* Tue Aug 17 2010 Ilya Mashkin <oddity@altlinux.ru> 2.5.0-alt0.2
- rebuild

* Tue Mar 10 2009 Ilya Mashkin <oddity@altlinux.ru> 2.5.0-alt0.1
- 2.5.0

* Wed Nov 29 2006 Igor Zubkov <icesik@altlinux.org> 2.4.7-alt1
- 2.4.5 -> 2.4.7

* Mon Aug 14 2006 Igor Zubkov <icesik@altlinux.ru> 2.4.5-alt1
- 2.4.4 -> 2.4.5
- buildreq

* Tue Aug 01 2006 Igor Zubkov <icesik@altlinux.ru> 2.4.4-alt1
- 2.4.4

* Tue Jul 25 2006 Igor Zubkov <icesik@altlinux.ru> 2.4.3-alt1
- 2.4.3
- remove COPYING (GPL v2) from package

* Mon Jul 17 2006 Igor Zubkov <icesik@altlinux.ru> 2.4.2-alt1
- 2.4.2 

* Mon Apr 10 2006 Igor Zubkov <icesik@altlinux.ru> 2.4.1-alt1
- 2.4.1
- buildreq

* Tue Apr 04 2006 Igor Zubkov <icesik@altlinux.ru> 2.4.0-alt1
- 2.4.0
- buildreq

* Mon Nov 07 2005 Igor Zubkov <icesik@altlinux.ru> 2.2.6-alt1
- Initial build for Sisyphus
