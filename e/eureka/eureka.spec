Name: eureka
Version: 1.24
Release: alt1
Summary: A cross-platform map editor for the classic DOOM games
Summary(ru_RU.UTF-8): Кросплатформенный редактор карт классического Doom
Group: Editors
License: GPLv2
Url: http://eureka-editor.sourceforge.net/
Packager: Artyom Bystrov <arbars@altlinux.org>

Source: %name-%version.tar.gz
Patch0: eureka-1.24-Makefile.patch
# Automatically added by buildreq on Thu Apr 18 2019
# optimized out: fontconfig fontconfig-devel libGL-devel libX11-devel libcloog-isl4 libstdc++-devel python-base python-modules python3 python3-base xorg-xproto-devel
BuildRequires: gcc-c++
BuildRequires: binutils
BuildRequires: make
BuildRequires: zlib-devel
BuildRequires: libXext-devel
BuildRequires: libXft-devel
BuildRequires: libXinerama-devel
BuildRequires: libfltk-devel
BuildRequires: libjpeg-devel
BuildRequires: libnss-role
BuildRequires: libpng-devel

%description
Eureka is a cross-platform map editor for the classic DOOM games.

It started when the ported the Yadex editor to a proper GUI toolkit, namely
FLTK, and implemented a system for multi-level Undo / Redo. These and other
features have required rewriting large potions of the existing code, and adding
lots of new code too. Eureka is now an independent program with its own
work-flow and its own quirks.

%description -l ru_RU.UTF-8
Eureka - кросплатформенный редактор карт классического Doom.
Проект начинался как порт другого редактора - Yadex, - на графический тулкит FLTK,
с внедрением системы работы с изменениями (Undo / Redo). Эта и многие другие улучшения
потребовали переписывания львиной части уже имеющегося кода и добавления немалого количества
нового. Теперь Eureka - независимый проект со своим подходом к работе и своими особенностями.

%prep
%setup -n %name-%version
%patch0 -p1 

%build
make OPTIMISE="%optflags"


%install
mkdir -p %buildroot%prefix
%makeinstall_std PREFIX=%_prefix

%files
%doc AUTHORS.txt CHANGES.txt README.txt TODO.txt GPL.txt docs/*
%_bindir/%name
%_datadir/%name/
%_datadir/applications/%name.desktop
%_datadir/pixmaps/%name.xpm
%_man6dir/%name.6.xz

%changelog
* Thu Apr 18 2019 Artyom Bystrov <arbars@altlinux.org> 1.24-alt1
- initial build for ALT Sisyphus
- getting the Makefile and patch from Mageia's package
- updating the sources
