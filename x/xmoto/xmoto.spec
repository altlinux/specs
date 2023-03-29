%define git %nil

Name: xmoto
Version: 0.6.2
Release: alt1

Summary: A challenging 2D motocross platform game.
License: GPLv2
Group: Games/Arcade

Url: https://xmoto.tuxfamily.org
# https://github.com/%name/%name/archive/%version/%version.tar.gz
Source: %name-%version-src.tar
Packager: Denis Pynkin <dans@altlinux.ru>

Patch0: %name-0.6.2-alt-system-ode.patch
Patch1: %name-0.6.1-alt-asian-font-path.patch

BuildRequires: gcc-c++ libSDL2-devel libSDL2_mixer-devel libjpeg-devel
BuildRequires: lua-devel libode-devel libpng-devel libstdc++-devel
BuildRequires: zlib-devel bzlib-devel libcurl-devel
BuildRequires: libSDL2_gfx-devel libsqlite3-devel libSDL2_ttf-devel
BuildRequires: libSDL2_net-devel
BuildRequires: libxdg-basedir-devel
BuildRequires(pre): rpm-build-fonts cmake ninja-build
BuildRequires: libxml2-devel libGLU-devel liblzma-devel
# chinese locale requires fonts-ttf-chinese-big5, JFI
Requires: fonts-ttf-dejavu, %name-data = %EVR

%description
XMoto is a challenging 2D motocross platform game, where physics play an
all important role in the gameplay. You need to control your bike to its
limit, if you want to have a chance finishing the more difficult of the
challenges.

%package data
Group: Games/Arcade
Summary: %name gamepack data
BuildArch: noarch

%description data
%summary

%prep
%setup
%autopatch -p3

%builD
%ifarch %e2k
# -std=c++03 by default as of lcc 1.23.12
%add_optflags -std=c++11
%endif
%cmake \
  -GNinja

ninja \
  -vvv \
  -j %__nprocs \
  -C %_cmake__builddir

%install
DESTDIR=%buildroot ninja -C %_cmake__builddir install

rm -rf %buildroot%_datadir/%name/Textures/Fonts/*.ttf
ln -sr %buildroot%_ttffontsdir/dejavu/DejaVuSans{,Mono}.ttf \
	%buildroot%_datadir/%name/Textures/Fonts/

%find_lang --output=%name.files %name

%files -f %name.files
%doc ChangeLog COPYING README.md
%_bindir/*
%_pixmapsdir/%name.png
%_datadir/applications/%name.desktop
%_man6dir/*

%files data
%_datadir/%name

%changelog
* Wed Mar 29 2023 L.A. Kostis <lakostis@altlinux.ru> 0.6.2-alt1
- 0.6.2.

* Mon Sep 19 2022 L.A. Kostis <lakostis@altlinux.ru> 0.6.1-alt4.g470ddaf
- .spec:
  + fix URL (use https)
  + add suggestion which asian font to use
- src: fix asian font path.

* Mon Sep 19 2022 L.A. Kostis <lakostis@altlinux.ru> 0.6.1-alt3.g470ddaf
- Added LZMA support.
- Use system libode.

* Mon Sep 19 2022 L.A. Kostis <lakostis@altlinux.ru> 0.6.1-alt2.g470ddaf
- Fix circular deps for -data.

* Mon Sep 19 2022 L.A. Kostis <lakostis@altlinux.ru> 0.6.1-alt1.g470ddaf
- GIT 470ddaf (to really enable SDL2).
- relocate to bin dir.
- make gamepack noarch.

* Mon Sep 19 2022 L.A. Kostis <lakostis@altlinux.ru> 0.6.1-alt1
- 0.6.1.
- use cmake instead of autotools.

* Wed Jun 19 2019 Michael Shigorin <mike@altlinux.org> 0.5.11-alt3.r3421
- E2K: explicit -std=c++11
- Spec cleanup

* Thu Apr 26 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 0.5.11-alt2.r3421
- Fixed build with new toolchain.

* Tue Feb 07 2017 Igor Vlasenko <viy@altlinux.ru> 0.5.11-alt1.r3421.1
- rebuild with new lua 5.3

* Wed Jul 20 2016 Denis Pynkin <dans@altlinux.org> 0.5.11-alt1.r3421
- New version from SVN trunk (closes: #32260)
- Removed unneeded patches

* Mon Apr 11 2016 Gleb F-Malinovskiy (qa) <qa_glebfm@altlinux.org> 0.5.9-alt1.3.qa1
- Rebuilt for gcc5 C++11 ABI.

* Mon Jul 07 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5.9-alt1.3
- Rebuilt with new ODE

* Wed Oct 03 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5.9-alt1.2
- Rebuilt with libpng15

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

