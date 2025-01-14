Name: eureka
Version: 2.0.2
Release: alt1
Summary: A cross-platform map editor for the classic DOOM games
Summary(ru_RU.UTF-8): Кросплатформенный редактор карт классического Doom
Group: Editors
License: GPLv2
Url: http://eureka-editor.sourceforge.net/
Packager: Artyom Bystrov <arbars@altlinux.org>

Source: %name-%version.tar
Patch0: eureka-1.27-Makefile.patch
Patch1: 0001-fix-loading-wad-files-on-aarch64.patch
Patch2: 0001-no-cc0-code.patch
Patch3: 0000-quoted-cflags.patch

BuildRequires(Pre): rpm-macros-cmake cmake
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
BuildRequires: bzlib-devel
BuildRequires: libXpm-devel
BuildRequires: ImageMagick-tools

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
#%%patch0 -p1 

%patch2 -p1
%patch3 -p1

# Remove CC0-licensed code
rm -rf src/tl/

%ifarch aarch64
%patch1 -p1
%endif

%build
%cmake -DENABLE_UNIT_TESTS=OFF
%cmake_build 


%install
%cmake_install

install -m 755 -d %{buildroot}%{_datadir}/icons/hicolor/128x128/apps
magick convert misc/eureka.ico %{buildroot}%{_datadir}/icons/hicolor/128x128/apps/eureka.png
 
install -m 755 -d %{buildroot}/%{_mandir}/man6/
install -m 644 -p misc/eureka.6 %{buildroot}%{_mandir}/man6/%{name}.6
 
install -m 755 -d %{buildroot}%{_datadir}/applications
install -m 644 -p misc/eureka.desktop %{buildroot}%{_datadir}/applications/%{name}.desktop
 

%files
%doc README.txt TODO.txt GPL.txt docs/*
%_bindir/%name
%_datadir/%name/
%_iconsdir/hicolor/128x128/apps/eureka.png
%_datadir/applications/%name.desktop
%_man6dir/%name.6.xz

%changelog
* Tue Jan 14 2025 Artyom Bystrov <arbars@altlinux.org> 2.0.2-alt1
- Update to new version

* Thu Feb 15 2024 Artyom Bystrov <arbars@altlinux.org> 1.27b-alt1
- Update to new version

* Wed Oct 18 2023 Artyom Bystrov <arbars@altlinux.org> 1.27-alt2
- Fix load WAD files on aarch64

* Tue Feb 18 2020 Artyom Bystrov <arbars@altlinux.org> 1.27-alt1
- Update to 1.27

* Thu Apr 18 2019 Artyom Bystrov <arbars@altlinux.org> 1.24-alt1
- initial build for ALT Sisyphus
- getting the Makefile and patch from Mageia's package
- updating the sources
