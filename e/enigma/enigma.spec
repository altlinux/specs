Group: Games/Arcade
# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/desktop-file-install /usr/bin/pdflatex ImageMagick-tools texinfo
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           enigma
Version:        1.21
Release:        alt1_11.20160222git0027b3b8e694
Summary:        Game where you control a marble with the mouse

License:        GPLv2+
URL:            http://www.nongnu.org/enigma/
# Using a git snapshot for the C++11 fixes.
# git clone https://github.com/Enigma-Game/Enigma.git
# cd Enigma
# git checkout 0027b3b8e694c8db75b5f8f825dada449ac2a6d1
# git archive --prefix=enigma-git0027b3b8e694/ 0027b3b8e694c8db75b5f8f825dada449ac2a6d1 | xz -9 > enigma-git0027b3b8e694.tar.xz
Source0:        enigma-git0027b3b8e694.tar.xz
#Source0:        http://downloads.sourceforge.net/enigma-game/enigma-%{version}.tar.gz
Patch1:         0001-Clean-up-.desktop-file-categories.patch
Patch2:         0002-build-use-system-zipios.patch
Patch3:         0003-prevent-ImageMagick-inserting-timestamps-to-PNGs.patch
Patch4:         0004-src-lev-Proxy.cc-fix-check-for-basic_ifstream-s-read.patch

Requires:       %{name}-data = %{version}-%{release}
Requires:       fonts-ttf-dejavu

BuildRequires:  gcc-c++
BuildRequires:  libSDL-devel
BuildRequires:  libSDL_image-devel
BuildRequires:  libSDL_mixer-devel
BuildRequires:  libSDL_ttf-devel
BuildRequires:  gettext gettext-tools
BuildRequires:  libpng-devel
BuildRequires:  libappstream-glib
BuildRequires:  desktop-file-utils
BuildRequires:  zlib-devel
BuildRequires:  libxerces-c-devel
BuildRequires:  libcurl-devel
BuildRequires:  ImageMagick
BuildRequires:  git
BuildRequires:  autoconf automake
BuildRequires:  libzipios++-devel
BuildRequires:  pkgconfig(libenet)
BuildRequires:  texi2html
Source44: import.info

%description
Enigma is a tribute to and a re-implementation of one of the most
original and intriguing computer games of the 1990's: Oxyd.  Your
objective is easily explained: find and uncover all pairs of identical
Oxyd stones in each landscape.  Sounds simple?  It would be, if it
weren't for hidden traps, vast mazes, insurmountable obstacles and
innumerable puzzles blocking your direct way to the Oxyd stones...

%package data
Group: Games/Arcade
Summary:        Data for Enigma game
License:        GPLv2+
BuildArch:      noarch

%description data
Data files (levels, graphics, sound, music) and documentation for Enigma.

%prep
%setup -q -n enigma-git0027b3b8e694
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
rm -r lib-src/zipios++ lib-src/enet/*

%build
aclocal -I m4 && autoheader && automake --add-missing --foreign --copy && autoconf
%configure --enable-optimize --with-system-enet
%make_build

%install
%makeinstall_std

# Use system fonts instead of bundling our own
rm -f $RPM_BUILD_ROOT%{_datadir}/%{name}/fonts/DejaVuSansCondensed.ttf
rm -f $RPM_BUILD_ROOT%{_datadir}/%{name}/fonts/vera_sans.ttf
ln -s %{_datadir}/fonts/ttf/dejavu/DejaVuSansCondensed.ttf $RPM_BUILD_ROOT%{_datadir}/%{name}/fonts/DejaVuSansCondensed.ttf
ln -s %{_datadir}/fonts/ttf/dejavu/DejaVuSans.ttf $RPM_BUILD_ROOT%{_datadir}/%{name}/fonts/vera_sans.ttf


desktop-file-install \
  --remove-key Version \
  --dir ${RPM_BUILD_ROOT}%{_datadir}/applications            \
  $RPM_BUILD_ROOT%{_datadir}/applications/enigma.desktop

appstream-util validate-relax --nonet $RPM_BUILD_ROOT%{_datadir}/appdata/enigma.appdata.xml

%find_lang %{name}

%files
%{_bindir}/enigma
%{_mandir}/man?/enigma.*
%{_datadir}/icons/hicolor/48x48/apps/enigma.png
%{_datadir}/pixmaps/enigma.png
%{_datadir}/applications/enigma.desktop
%{_datadir}/appdata/enigma.appdata.xml

%files data -f %{name}.lang
%{_docdir}/%{name}
%{_datadir}/enigma

%changelog
* Sat Nov 18 2017 Igor Vlasenko <viy@altlinux.ru> 1.21-alt1_11.20160222git0027b3b8e694
- new version

* Tue Jul 04 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 1.01-alt5.3
- Fixed build with gcc-6

* Thu Oct 04 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.01-alt5.2
- Rebuilt with libpng15

* Wed Jul 18 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.01-alt5.1
- Fixed build

* Tue Aug 17 2010 Ilya Mashkin <oddity@altlinux.ru> 1.01-alt5
- update requires

* Tue Jul 14 2009 Ilya Mashkin <oddity@altlinux.ru> 1.01-alt4
- fix build with gcc4.4

* Fri Nov 13 2008 Ilya Mashkin <oddity@altlinux.ru> 1.01-alt3
- fix build with gcc4.3

* Mon Oct 06 2008 Ilya Mashkin <oddity@altlinux.ru> 1.01-alt2.1
- rebuild

* Sat Feb  2 2008 Alexander Borovsky <partizan@altlinux.ru> 1.01-alt2
- Menu entry fixed

* Sun Nov 25 2007 Alexander Borovsky <partizan@altlinux.ru> 1.01-alt1
- New version
- Fixed build

* Thu Jan 04 2007 Alexander Borovsky <partizan@altlinux.ru> 1.0-alt1
- New version

* Fri Sep 15 2006 Alexander Borovsky <partizan@altlinux.ru> 0.92-alt2
- Fixed build with GCC4

* Sat Jun 18 2005 Alexander Borovsky <partizan@altlinux.ru> 0.92-alt1
- New version

* Tue Jan 18 2005 ALT QA Team Robot <qa-robot@altlinux.org> 0.90-alt1.1
- Rebuilt with libstdc++.so.6.

* Tue Nov 16 2004 Alexander Borovsky <partizan@altlinux.ru> 0.90-alt1
- New version (0.90-beta)

* Tue Jul 13 2004 Alexander Borovsky <partizan@altlinux.ru> 0.81-alt2
- Fixed menu file (#4772)

* Thu Jun 17 2004 Alexander Borovsky <partizan@altlinux.ru> 0.81-alt1
- First build for Sisyphus
