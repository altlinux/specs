Name: xmoto
Version: 0.5.9
Release: alt1.1

Summary: A challenging 2D motocross platform game.
License: GPL
Group: Games/Arcade
Packager: Denis Pynkin <dans@altlinux.ru>

Url: http://xmoto.tuxfamily.org
Source: %name-%version-src.tar.gz

BuildRequires: gcc-c++ libSDL-devel libSDL_mixer-devel libjpeg-devel
BuildRequires: liblua5-devel libode-devel libpng-devel libstdc++-devel
BuildRequires: zlib-devel bzlib-devel libcurl-devel
BuildRequires: libSDL_gfx-devel libsqlite3-devel libSDL_ttf-devel
BuildRequires: libSDL_net-devel
BuildRequires: libxdg-basedir-devel
BuildRequires: rpm-build-fonts
BuildRequires: libxml2-devel

Requires: fonts-ttf-dejavu

%description
XMoto is a challenging 2D motocross platform game, where physics play an all important role in the gameplay. You need to control your bike to its limit, if you want to have a chance finishing the more difficult of the challenges.

%prep
%setup -q

%build

sed -i "s@/mang@/man6@g" Makefile.in

export LDFLAGS="-L%_x11libdir"
%configure --bindir=%_gamesbindir \
		--with-enable-zoom=1 \
		--with-enable-www=1 \
		--with-renderer-openGl=1

%define __nprocs 1
%make_build

%install
%make_install DESTDIR="%buildroot" install

mkdir -p %buildroot%_datadir/applications
cp extra/xmoto.desktop %buildroot%_datadir/applications
install -D -m 644 extra/xmoto.xpm %buildroot%_liconsdir/%name.xpm

rm -rf %buildroot%_datadir/%name/Textures/Fonts/*.ttf

ln -s %_ttffontsdir/dejavu/DejaVuSans.ttf %buildroot%_datadir/%name/Textures/Fonts/
ln -s %_ttffontsdir/dejavu/DejaVuSansMono.ttf %buildroot%_datadir/%name/Textures/Fonts/

%find_lang --output=%name.files %name

%files -f %name.files
%doc AUTHORS INSTALL README
%_gamesbindir/*
%_liconsdir/%name.xpm
%_datadir/applications/*
%_datadir/%name
%_man6dir/*

# FIXME: remove in next version
%triggerpostun -- %name < 0.5.7
[ -L %_datadir/%name/Textures/Fonts/DejaVuSans.ttf ] || ln -s %_ttffontsdir/dejavu/DejaVuSans.ttf %_datadir/%name/Textures/Fonts/
[ -L %_datadir/%name/Textures/Fonts/DejaVuSansMono.ttf ] || ln -s %_ttffontsdir/dejavu/DejaVuSansMono.ttf %_datadir/%name/Textures/Fonts/

%changelog
* Thu Mar 01 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5.9-alt1.1
- Rebuilt with updated ODE

* Mon Feb 27 2012 Denis Pynkin <dans@altlinux.org> 0.5.9-alt1
- New version (switched to libxml2)

* Sat Apr 30 2011 Denis Pynkin <dans@altlinux.ru> 0.5.7-alt1
- New version

* Tue Apr 05 2011 Denis Pynkin <dans@altlinux.ru> 0.5.6-alt3
- upgrade fixed (ALT #25376)
- upgrade from 0.5.6-alt2 is broken

* Sun Apr 03 2011 Denis Pynkin <dans@altlinux.ru> 0.5.6-alt2
- removed fonts duplicated in fonts-ttf-dejavu (ALT #25354)

* Fri Apr 01 2011 Denis Pynkin <dans@altlinux.ru> 0.5.6-alt1
- 0.5.6 release
- removed libmesa-devel from requirements

* Sun Dec 05 2010 Denis Pynkin <dans@altlinux.ru> 0.5.4-alt1
- 0.5.4 release

* Sun Jul 18 2010 Denis Pynkin <dans@altlinux.ru> 0.5.3-alt1
- 0.5.3 release

* Thu Jan 07 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5.2-alt1.qa1.1
- Rebuilt with libode 0.11.1

* Tue Nov 17 2009 Repocop Q. A. Robot <repocop@altlinux.org> 0.5.2-alt1.qa1
- NMU (by repocop): the following fixes applied:
  * pixmap-in-deprecated-location for xmoto
  * postclean-05-filetriggers for spec file

* Mon Sep 21 2009 Denis Pynkin <dans@altlinux.ru> 0.5.2-alt1
- 0.5.2 release

* Mon May 25 2009 Denis Pynkin <dans@altlinux.ru> 0.5.1-alt2
- added patch for gcc 4.4

* Wed Apr 15 2009 Denis Pynkin <dans@altlinux.ru> 0.5.1-alt1
- 0.5.1 release - bug fixes and performance improvements

* Mon Dec 01 2008 Denis Pynkin <dans@altlinux.ru> 0.5.0-alt1
- 0.5.0 release
- Added libSDL_net in requirements

* Wed May 07 2008 Denis Pynkin <dans@altlinux.ru> 0.4.2-alt1
- 0.4.2 release

* Tue Nov 06 2007 Pavlov Konstantin <thresh@altlinux.ru> 0.3.4-alt1
- 0.3.4 release.

* Wed Sep 05 2007 Pavlov Konstantin <thresh@altlinux.ru> 0.3.3-alt1
- 0.3.3 release.

* Wed Aug 22 2007 Pavlov Konstantin <thresh@altlinux.ru> 0.3.2-alt1
- 0.3.2 release.

* Tue Jul 17 2007 Pavlov Konstantin <thresh@altlinux.ru> 0.3.1-alt1
- 0.3.1 release.

* Wed Jun 27 2007 Pavlov Konstantin <thresh@altlinux.ru> 0.3.0-alt1
- 0.3.0 release.
- Some spec cleanup.
- Some buildrequires changes.

* Mon Mar 26 2007 Pavlov Konstantin <thresh@altlinux.ru> 0.2.7-alt1
- 0.2.7 release.

* Thu Mar 08 2007 Pavlov Konstantin <thresh@altlinux.ru> 0.2.6-alt1
- 0.2.6 release.

* Fri Jan 05 2007 Pavlov Konstantin <thresh@altlinux.ru> 0.2.4-alt1
- 0.2.4 release.

* Thu Oct 05 2006 Pavlov Konstantin <thresh@altlinux.ru> 0.2.2-alt1
- 0.2.2 release.
- added .desktop file.
- enabling zoom.

* Tue Sep 19 2006 Pavlov Konstantin <thresh@altlinux.ru> 0.2.1-alt1
- 0.2.1 release.

* Sat Jul 29 2006 Pavlov Konstantin <thresh@altlinux.ru> 0.2.0-alt1
- 0.2.0 release.
- Added bzlib-devel to build requires.

* Sun Jun 25 2006 Pavlov Konstantin <thresh@altlinux.ru> 0.1.16-alt1
- 0.1.16 release.
- Adding libcurl-devel to BR to fetch highscores from internet,
  rebuild with fetchscores to activate this.

* Tue May 16 2006 Pavlov Konstantin <thresh@altlinux.ru> 0.1.12-alt1
- 0.1.12 release.

* Tue Mar 21 2006 Pavlov Konstantin <thresh@altlinux.ru> 0.1.11-alt2
- Fixed build with --as-needed.

* Thu Feb 16 2006 Pavlov Konstantin <thresh@altlinux.ru> 0.1.11-alt1
- 0.1.11.

* Mon Dec 05 2005 Pavlov Konstantin <thresh@altlinux.ru> 0.1.10-alt1
- 0.1.10 release.

* Sat Dec 03 2005 Pavlov Konstantin <thresh@altlinux.ru> 0.1.9-alt1
- 0.1.9 release.

* Thu Nov 10 2005 Pavlov Konstantin <thresh@altlinux.ru> 0.1.8-alt1
- 0.1.8 release.

* Sun Oct 30 2005 Pavlov Konstantin <thresh@altlinux.ru> 0.1.7-alt1
- 0.1.7 release.
- Fixed LDFLAGS, now it should build on x86_64.

* Wed Oct 12 2005 Pavlov Konstantin <thresh@altlinux.ru> 0.1.6-alt1
- 0.1.6 release.

* Wed Oct 05 2005 Pavlov Konstantin <thresh@altlinux.ru> 0.1.5-alt1
- 0.1.5 release.

* Mon Sep 19 2005 Pavlov Konstantin <thresh@altlinux.ru> 0.1.3-alt1
- Initial build for Sisyphus.

