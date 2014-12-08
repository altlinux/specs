%define prerel beta

Name: lincity-ng
Version: 2.9
Release: alt0.2

Summary: LinCity-NG is a city simulation game. It is a polished and improved version of the classic LinCity game
Summary(ru_RU.UTF-8): LinCity-NG - это игра-симулятор города. Она представляет собой улучшенную версию классической игры LinCity.

License: GPLv2
Group: Games/Strategy
Url: http://code.google.com/p/%name

# use makerelease.sh in git tree to build tarball
Source: %name-%version.%prerel.tar.bz2

Requires: %name-data = %version-%release

BuildPreReq: gcc-c++
BuildPreReq: jam
BuildPreReq: libxml2-devel
BuildPreReq: libGL-devel
BuildPreReq: libGLU-devel
BuildPreReq: libSDL-devel
BuildPreReq: libSDL_mixer-devel
BuildPreReq: libSDL_image-devel
BuildPreReq: libSDL_ttf-devel
BuildPreReq: libSDL_gfx-devel
BuildPreReq: libphysfs-devel
BuildPreReq: vorbis-tools
BuildPreReq: zlib-devel

%description
LinCity-NG is a city simulation game. It is a polished and improved
version of the classic LinCity game. In the game, you are required
to build and maintain a city. You can win the game either by building
a sustainable economy or by evacuating all citizens with spaceships.

%description -l ru_RU.UTF-8
LinCity-NG - игра-симулятор города. Это улучшенная и доработанная
версия, ставшей классикой LinCity. В этой игре вам надо будет
построить и развивать город. Выиграть в игре можно двумя способами.
Первый - это построить устройчивую экономику. Второй способ -
построить космический корабль и отправить на нем всех жителей в
космос.
На официальной вики игры, находящейся по адресу: %url
можно получить более подробную информацию об игровом процессе,
разработчиках игры, посмотреть скриншоты.

%package data
Summary: Data files needed to run lincity-ng
# data bits are dual licensed GPLv2+ or CC-BY-SA
License: GPLv2+ or CC-BY-SA
Group: Games/Strategy
Requires: %name = %version-%release
Requires: fonts-ttf-dejavu
BuildArch: noarch

%description data
This package contains the data files (graphics, models, audio) necessary to
play Lincity-NG.

%define _pkgdocdir %_docdir/%name-%version

%prep
%setup -n %name-%version.%prerel

sed -i "s/CFLAGS += -O3 -g -Wall/CFLAGS += $RPM_OPT_FLAGS/" Jamrules
sed -i "s/CXXFLAGS += -O3 -g -Wall/CXXFLAGS += $RPM_OPT_FLAGS/" Jamrules
sed -i 's|lincity-ng.png|lincity-ng|g' lincity-ng.desktop

%build
%configure
jam

%install
DESTDIR=%buildroot jam -sappdocdir=%_pkgdocdir install

# Make a symlink to system font, rather than include a copy of DejaVu Sans
ln -fs %_datadir/fonts/ttf/dejavu/DejaVuSans.ttf %buildroot%_datadir/%name/fonts/sans.ttf

# compress wav files to ogg
for i in %buildroot/%_datadir/%name/sounds/*.wav; do
  oggenc --quiet $i && rm $i
done
# and fix sounds.xml
subst 's/\.wav/.ogg/' %buildroot/%_datadir/%name/sounds/sounds.xml

%find_lang %name

%files -f %name.lang
%_bindir/*

%files data
%_desktopdir/*
%_pixmapsdir/*
%_datadir/%name/*
%doc %_pkgdocdir/

%changelog
* Mon Dec 08 2014 Yuri N. Sedunov <aris@altlinux.org> 2.9-alt0.2
- fixed sounds.xml

* Thu Dec 04 2014 Yuri N. Sedunov <aris@altlinux.org> 2.9-alt0.1
- 2.9 beta snapshot (4900c2e5519a)
- moved arch independent files to separate -data subpackage
- do not bundle DejaVu Sans font in -data subpackage and
  use symlink to system fonts-ttf-dejavu
- do not use rare %%_gamesdatadir as %_datadir any more

* Fri Apr 19 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 2.0-alt1.1.qa2
- NMU: rebuilt for updated dependencies.

* Tue May 24 2011 Repocop Q. A. Robot <repocop@altlinux.org> 2.0-alt1.1.qa1
- NMU (by repocop). See http://www.altlinux.org/Tools/Repocop
- applied repocop fixes:
  * docdir-is-not-owned for lincity-ng
  * postclean-03-private-rpm-macros for the spec file

* Mon Nov 8 2010 Anton Chernyshov <ach@altlinux.org> 2.0-alt1.1
- add new build dependency - libGLU-devel

* Sun Nov 7 2010 Anton Chernyshov <ach@altlinux.org> 2.0-alt1
- create (more or less) generic spec file and initial build...
