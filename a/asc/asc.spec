Name: asc
Version: 2.6.1.0
Release: alt1
Group: Games/Strategy
License: GPLv2+

# repacked 'https://heanet.dl.sourceforge.net/project/asc-hq/ASC Source/2.6.0/asc-%%version.tar.bz2'
Source: asc-%{version}.tar

Source1: frontiers.ogg
Source2: machine_wars.ogg
Source3: time_to_strike.ogg
URL: http://www.asc-hq.org/
Summary: ASC - a battle isle clone

# Automatically added by buildreq on Fri Jan 20 2017 (-ba)
# optimized out: boost-devel-headers elfutils libSDL-devel libgpg-error libstdc++-devel perl pkg-config python-base xz zlib-devel
BuildRequires: boost-devel bzlib-devel gcc-c++ libSDL_image-devel libSDL_mixer-devel libSDL_sound-devel libexpat-devel libfreetype-devel liblua5-devel libphysfs-devel libpng-devel libsigc++2-devel libwxGTK-devel libxvid-devel zip

BuildPreReq: libcurl-devel libogg-devel libxvid-devel

%description
ASC aims at providing a free clone of Bluebyte's Battle Isle(tm) series.

%prep
%setup 
cp %SOURCE1 %SOURCE2 %SOURCE3 data/music/

%build
%autoreconf
%add_optflags -fpermissive
%configure
%make_build

%install
%makeinstall

%files
%_gamesdatadir/asc
%_bindir/asc*
%_man6dir/*
%doc AUTHORS COPYING ChangeLog README TODO doc

%changelog
* Fri Jan 20 2017 Gleb F-Malinovskiy <glebfm@altlinux.org> 2.6.1.0-alt1
- Updated to 2.6.1.0.

* Thu Apr 07 2016 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 2.4.0.0-alt1.8.qa2
- NMU: rebuilt with boost 1.57.0 -> 1.58.0.

* Sat Jan 03 2015 Ivan A. Melnikov <iv@altlinux.org> 2.4.0.0-alt1.8.1
- rebuild with boost 1.57.0

* Mon Feb 11 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.4.0.0-alt1.8
- Rebuilt with Boost 1.53.0

* Wed Nov 28 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.4.0.0-alt1.7
- Fixed build with gcc 4.7

* Tue Sep 25 2012 Repocop Q. A. Robot <repocop@altlinux.org> 2.4.0.0-alt1.6.1
- rebuild with new wxGTK

* Thu Sep 06 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.4.0.0-alt1.6
- Rebuilt with Boost 1.51.0

* Wed Apr 04 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.4.0.0-alt1.5
- Rebuilt with Boost 1.49.0

* Sat Dec 03 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.4.0.0-alt1.4
- Rebuilt with Boost 1.48.0

* Fri Jul 29 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.4.0.0-alt1.3
- Rebuilt with Boost 1.47.0

* Thu Mar 24 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.4.0.0-alt1.2
- Rebuilt with Boost 1.46.1 and for debuginfo
- Added libxvid-devel into BuildPreReq

* Tue Dec 07 2010 Igor Vlasenko <viy@altlinux.ru> 2.4.0.0-alt1.1
- rebuild with new openssl and/or boost by request of git.alt administrator

* Sat Dec 26 2009 Ilya Mashkin <oddity@altlinux.ru> 2.4.0.0-alt1
- Version 2.4.0.0

* Sat Apr 04 2009 Ilya Mashkin <oddity@altlinux.ru> 2.2.0.0-alt1
- Version 2.2.0.0

* Thu Dec 11 2008 Eugene Ostapets <eostapets@altlinux.ru> 2.1.0.0-alt1
- new version

* Wed Jan 16 2008 Eugene Ostapets <eostapets@altlinux.ru> 2.0.1.0-alt1
- First build for Sisyphus

