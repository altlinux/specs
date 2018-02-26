%set_verify_elf_method relaxed

Name: speed-dreams
Version: 1.4.0
Release: alt4

Summary: Speed Dreams is a fork of the famous open racing car simulator TORCS, aiming to implement exciting new features
Summary(ru_RU.UTF-8): Speed Dreams - это ответвление от знаменитого проекта TORCS, ставящее своей основной целью реализацию самых последних возможностей

License: GPLv2
Group: Games/Sports
Url: http://speed-dreams.sourceforge.net/

Packager: Anton Chernyshov <ach@altlinux.org>
Source0: %name-%version.tar
Source1: %name.desktop

# Thanks Gentoo for patch
Patch0:  %name-%version-gentoo.patch
Patch1:  %name-%version-makefile-alt.patch

Requires: %name-data = %version-%release 

BuildRequires: gcc-c++ imake libopenal-devel libalut-devel libfreeglut-devel libpng-devel libjpeg-devel libICE-devel libGL-devel libSM-devel libX11-devel libXext-devel libXi-devel libXrandr-devel libXrender-devel libXt-devel libXmu-devel plib-devel zlib-devel libXxf86vm-devel

# Automatically added by buildreq on Wed Oct 20 2010 (-bi)
BuildRequires: gdb

%description
Speed Dreams is a fork of the famous open racing car simulator TORCS, aiming
to implement exciting new features, cars, tracks and AI opponents to make
a more enjoyable game for the player, as well as constantly improving visual
and physics realism. 

In other words, Speed Dreams is the place:
* where developers can try their ideas and have every chance to get them
released to the end-users (democracy is the main principle ruling the dev
team)
* where end-users can enjoy the completion of these ideas and give their
opinion about it, and/or make new suggestions.

%description -l ru_RU.UTF-8
Speed Dreams - это ответвление хорошо известной игры-симулятора TORCS, которое
ставит своей целью реализацию новых возможностей, автомобилей, трасс и
искусственного интеллекта соперников, улучшение визуального и физического
реализма  Это позволит пользователям получить большее удовольствие от игрового
процесса.

Другими словами проект Speed Dreams вам подойдет, если:
* вы конечный пользователь и желаете внести какие-то идеи по развитию проекта,
чтобы затем получить удовольствие от их реализаци
* вы разработчик, имеющий множество идей и хотите как можно быстрее донести
их до конечных пользователей (демократия - основной принцип, которым
руководствуется команда разработчиков).

%package data
Buildarch: noarch
Summary: Data files needed for %name
Summary(ru_RU.UTF-8): Файлы, необходимые для работы игры %name
Group: Games/Sports

%description data
Data files for %name

%description data -l ru_RU.UTF-8
Файлы ресурсов, необходимые для игры %name - трассы, автомобили, компьютерные
соперники и т.п.

%prep
%setup
%patch0 -p0
%patch1 -p0

%build
%__autoconf
%__autoheader
%configure --x-libraries=%_libdir

# single thread build
%make

%install
%makeinstall_std

# Install data files
%make_install DESTDIR=%buildroot datainstall
%find_lang %name

# Install game .desktop and .icon files
%__install -D -m 0644 %{SOURCE1} %buildroot/%_desktopdir/%name.desktop
%__install -D -m 0644 icon.png %buildroot/%_iconsdir/%name.png

%files -f %name.lang
%_bindir/*
%_libdir/%name/*
%_desktopdir/%name.desktop
%_iconsdir/%name.png

%files data
%_gamesdatadir/%name/*
%doc CHANGES INSTALL README COPYING TODO icon* doc/*
%exclude %_gamesdatadir/%name/CHANGES
%exclude %_gamesdatadir/%name/COPYING
%exclude %_gamesdatadir/%name/README
%exclude %_gamesdatadir/%name/TODO
%exclude %_gamesdatadir/%name/icon.*

%changelog
* Thu Apr 21 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.4.0-alt4
- fix build

* Tue Oct 26 2010 Anton Chernyshov <ach@altlinux.org> 1.4.0-alt3
- fix build dependencies
- fix .desktop file
- add and fix some macroses

* Wed Oct 13 2010 Anton Chernyshov <ach@altlinux.org> 1.4.0-alt2
- split package on two parts (main and resources)
- create .desktop file

* Tue Oct 12 2010 Anton Chernyshov <ach@altlinux.org> 1.4.0-alt1
- create spec file and first successful build
