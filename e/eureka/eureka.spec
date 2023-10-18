Name: eureka
Version: 1.27
Release: alt2
Summary: A cross-platform map editor for the classic DOOM games
Summary(ru_RU.UTF-8): Кросплатформенный редактор карт классического Doom
Group: Editors
License: GPLv2
Url: http://eureka-editor.sourceforge.net/
Packager: Artyom Bystrov <arbars@altlinux.org>

Source: %name-%version.tar
Patch0: eureka-1.27-Makefile.patch
Patch1: 0001-fix-loading-wad-files-on-aarch64.patch

BuildRequires: gcc-c++
BuildRequires: binutils
BuildRequires: make
BuildRequires: zlib-devel
BuildRequires: libXext-devel
BuildRequires: libXcursor-devel
BuildRequires: libXft-devel
BuildRequires: libXfixes-devel
BuildRequires: libXinerama-devel
BuildRequires: libfltk-devel
BuildRequires: libjpeg-devel
BuildRequires: libnss-role
BuildRequires: libpng-devel
BuildRequires: libX11-devel
BuildRequires: libGL-devel
BuildRequires: xdg-utils

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

%ifarch aarch64
%patch1 -p1
%endif

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
* Wed Oct 18 2023 Artyom Bystrov <arbars@altlinux.org> 1.27-alt2
- Fix load WAD files on aarch64

* Tue Feb 18 2020 Artyom Bystrov <arbars@altlinux.org> 1.27-alt1
- Update to 1.27

* Thu Apr 18 2019 Artyom Bystrov <arbars@altlinux.org> 1.24-alt1
- initial build for ALT Sisyphus
- getting the Makefile and patch from Mageia's package
- updating the sources
