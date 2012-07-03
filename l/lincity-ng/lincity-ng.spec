Name: lincity-ng
Version: 2.0
Release: alt1.1.qa1

Summary: LinCity-NG is a city simulation game. It is a polished and improved version of the classic LinCity game.
Summary(ru_RU.UTF-8): LinCity-NG - это игра-симулятор города. Она представляет собой улучшенную версию классической игры LinCity.

License: GPLv2
Group: Games/Strategy
Url: http://lincity-ng.berlios.de

Packager: Anton Chernyshov <ach@altlinux.org>
Source0: %name-%version.tar.bz2

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
На официальной вики игры, находящейся по адресу: http://lincity-ng.berlios.de 
можно получить более подробную информацию об игровом процессе, 
разработчиках игры, посмотреть скриншоты.

%prep
%setup

%build
%configure --datadir=%_gamesdatadir 
   
jam

%install

# game wants to install to /usr, but we don't want it
# thanks SUSE for idea how to do it
sed -i -e s+^prefix.*+prefix\ ?=\ \"%buildroot/usr\"\ \;+g \
	-e s+^bindir.*+bindir\ ?=\ \"%buildroot/%_bindir\"\ \;+g \
        -e s+^exec_prefix.*+exec_prefix\ ?=\ \"%buildroot/usr\"\ \;+g \
        -e s+^datadir.*+datadir\ ?=\ \"%buildroot/%_gamesdatadir\"\ \;+g \
        -e s+^oldincludedir.*+oldincludedir\ ?=\ \"%buildroot/usr/include\"\ \;+g \
    Jamconfig
jam install

# compress wav files to ogg
for i in %buildroot/%_gamesdatadir/%name/sounds/*.wav; do
  oggenc --quiet $i && rm $i
done

# move some game files to appropriate location
mkdir -p %buildroot/{%_defaultdocdir,%_desktopdir,%_pixmapsdir}
mv %buildroot/%_gamesdatadir/doc 		%buildroot/%_datadir/
mv %buildroot/%_gamesdatadir/applications 	%buildroot/%_datadir/
mv %buildroot/%_gamesdatadir/pixmaps		%buildroot/%_datadir/

%find_lang %name

%files -f %name.lang
%_bindir/*
%_desktopdir/*
%doc %_defaultdocdir/%name-%version/*
%_pixmapsdir/*
%_gamesdatadir/%name/*
# The package does not own its own docdir subdirectory.
# The line below is added by repocop to fix this bug in a straightforward way. 
# Another way is to rewrite the spec to use relative doc paths.
%dir %_docdir/lincity-ng-%version 

%changelog
* Tue May 24 2011 Repocop Q. A. Robot <repocop@altlinux.org> 2.0-alt1.1.qa1
- NMU (by repocop). See http://www.altlinux.org/Tools/Repocop
- applied repocop fixes:
  * docdir-is-not-owned for lincity-ng
  * postclean-03-private-rpm-macros for the spec file

* Mon Nov 8 2010 Anton Chernyshov <ach@altlinux.org> 2.0-alt1.1
- add new build dependency - libGLU-devel

* Sun Nov 7 2010 Anton Chernyshov <ach@altlinux.org> 2.0-alt1
- create (more or less) generic spec file and initial build...
