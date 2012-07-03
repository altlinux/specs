Name: prboom-plus
Version: 2.5.1.3
Release: alt1

Summary: Doom - classic 3D shoot-em-up game
Group: Games/Arcade
URL: http://prboom-plus.sourceforge.net/
License: GPL

Source0: %name-%version.tar.gz

Patch0: prboom-plus-2.5.0.3-alt-build.patch

Packager: Igor Zubkov <icesik@altlinux.org>

# Automatically added by buildreq on Thu Apr 12 2012
# optimized out: dumb libGL-devel libGLU-devel libSDL-devel libogg-devel libpng-devel libvorbis-devel zlib-devel
BuildRequires: dumb-devel libSDL_image-devel libSDL_mixer-devel libSDL_net-devel libfluidsynth-devel libmad-devel libpcre-devel

%description
Doom is the classic 3D shoot-em-up game. It must have been one of the best
selling games ever; it totally outclassed any  3D world games that preceded
it, with amazing speed, flexibility, and outstanding gameplay. The specs to
the game were released, and thousands of extra levels were written by fans of
the game; even today new levels are written for Doom faster then any one person
could play them.

%prep
%setup -q
%patch0 -p1

%build
%configure \
	--disable-cpu-opt
%make_build

%install
%make_install DESTDIR=%buildroot docdir=%_docdir/%name-%version/ install

rm -rf %buildroot%_docdir/%name-%version/COPYING

%files
%dir %_docdir/prboom-plus-%version
%_docdir/%name-%version/*
%_gamesbindir/*
%_gamesdatadir/doom/prboom-plus.wad
%_man5dir/*
%_man6dir/*

%changelog
* Thu Apr 12 2012 Igor Zubkov <icesik@altlinux.org> 2.5.1.3-alt1
- 2.5.0.6 -> 2.5.1.3

* Tue Dec 29 2009 Igor Zubkov <icesik@altlinux.org> 2.5.0.6-alt1
- 2.5.0.5 -> 2.5.0.6

* Wed Dec 16 2009 Igor Zubkov <icesik@altlinux.org> 2.5.0.5-alt1
- 2.5.0.4 -> 2.5.0.5

* Fri Oct 16 2009 Igor Zubkov <icesik@altlinux.org> 2.5.0.4-alt1
- 2.5.0.3 -> 2.5.0.4

* Tue Aug 04 2009 Igor Zubkov <icesik@altlinux.org> 2.5.0.3-alt2
- own doc dir

* Fri Jul 31 2009 Igor Zubkov <icesik@altlinux.org> 2.5.0.3-alt1
- 2.5.0.1 -> 2.5.0.3

* Wed Mar 25 2009 Igor Zubkov <icesik@altlinux.org> 2.5.0.1-alt1
- 2.4.8.2 -> 2.5.0.1

* Sun May 18 2008 Igor Zubkov <icesik@altlinux.org> 2.4.8.2-alt1
- 2.4.6.1 -> 2.4.8.2
- buildreq

* Mon Oct 02 2006 Igor Zubkov <icesik@altlinux.org> 2.4.6.1-alt1
- 2.4.3.1 -> 2.4.6.1
- buildreq

* Mon Aug 14 2006 Igor Zubkov <icesik@altlinux.ru> 2.4.3.1-alt1
- Initial build for Sisyphus

* Mon Aug 14 2006 Igor Zubkov <icesik@altlinux.ru> 2.4.5-alt1
- 2.4.4 -> 2.4.5

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
