%define prerel %nil

Name: lincity-ng
Version: 2.11.0
Release: alt1

Summary: LinCity-NG is a city simulation game
Summary(ru_RU.UTF-8): LinCity-NG - это игра-симулятор города. Она представляет собой улучшенную версию классической игры LinCity.
License: GPL-2.0-or-later
Group: Games/Strategy
Url: https://github.com/lincity-ng/lincity-ng

Vcs: https://github.com/lincity-ng/lincity-ng.git
Source: https://github.com/lincity-ng/lincity-ng/archive/refs/tags/%name-%version%prerel.tar.gz

Requires: %name-data = %EVR

BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake gcc-c++
BuildRequires: pkgconfig(sdl2)
BuildRequires: pkgconfig(SDL2_gfx)
BuildRequires: pkgconfig(SDL2_image)
BuildRequires: pkgconfig(SDL2_mixer)
BuildRequires: pkgconfig(SDL2_ttf)
BuildRequires: pkgconfig(zlib)
BuildRequires: pkgconfig(libxml-2.0)
BuildRequires: pkgconfig(physfs)
BuildRequires: pkgconfig(liblzma)
BuildRequires: pkgconfig(libxslt) xsltproc
# for compress .wav files
BuildRequires: vorbis-tools

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
Requires: fonts-ttf-dejavu
BuildArch: noarch

%description data
This package contains the data files (graphics, models, audio) necessary to
play Lincity-NG.

%define _pkgdocdir %_docdir/%name

%prep
%setup -n %name-%name-%version%prerel

%build
%cmake -DCMAKE_INSTALL_MANDIR=%_man6dir
%cmake_build

%install
%cmake_install

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
%_desktopdir/*

%files data
%_datadir/%name/*
%_iconsdir/hicolor/*x*/apps/%name.png
%_man6dir/%name.6*
%doc %_pkgdocdir/

%changelog
* Thu Jun 27 2024 Yuri N. Sedunov <aris@altlinux.org> 2.11.0-alt1
- 2.11.0

* Tue Apr 23 2024 Yuri N. Sedunov <aris@altlinux.org> 2.10.2-alt1
- 2.10.2

* Fri Mar 22 2024 Yuri N. Sedunov <aris@altlinux.org> 2.10.1-alt1
- 2.10.1 (ported to CMake build system)

* Mon Feb 26 2024 Yuri N. Sedunov <aris@altlinux.org> 2.9.0-alt1
- 2.9.0 release (ported to SDL2)

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
