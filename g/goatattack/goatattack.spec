# BEGIN SourceDeps(oneline):
BuildRequires: gcc-c++
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           goatattack
Version:        0.5.0
Release:        alt1
Summary:        Fast-paced multiplayer pixel art shooter game
Group:          Games/Arcade
License:        GPLv3+ and CC BY-SA 4.0
URL:            http://www.goatattack.net
Source0:        https://github.com/goatattack/goatattack/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(sdl2)
BuildRequires:  pkgconfig(SDL2_mixer)
BuildRequires:  pkgconfig(zlib)
Requires:       %{name}-data >= %{version}
Source44: import.info

%description
Goat Attack is a multiplayer 2D platformer pixel art shooter game for Linux,
OS X and Windows. You can play it in a local network or over the Internet.
This project is splitted three subprojects. the game itself, its map editor
and a master server. six gameplay modes are supported. deathmatch, team
deathmatch, capture the flag, speed race, catch the coin and goat of the hill.

%package data
Group: Games/Arcade
Summary:        Arch-independent data files for the game Goat Attack
BuildArch:      noarch

%description data
This package contains arch-independent data files (graphics, sounds, music,
levels) for the multiplayer game Goat Attack.

%prep
%setup -q


rm -rf src/shared/zlib

%build
%add_optflags -std=c++14
export CPPFLAGS+="-I/usr/include/freetype2"
autoreconf -vfi

rm -rf %{_builddir}/build-dedicated
mkdir %{_builddir}/build-dedicated
cp -a . %{_builddir}/build-dedicated

%configure \
  --bindir=%{_gamesbindir} \
  --datadir=%{_gamesdatadir} \
  --enable-map-editor

%make_build

pushd %{_builddir}/build-dedicated
%configure \
  --bindir=%{_gamesbindir} \
  --datadir=%{_gamesdatadir} \
  --enable-dedicated-server
%make_build
popd

%install
%makeinstall_std

install -m755 %{_builddir}/build-dedicated/src/Server/%{name}-server \
  %{buildroot}%{_gamesbindir}/%{name}-server
install -m755 %{_builddir}/build-dedicated/src/Server/man/%{name}-server.6 \
  %{buildroot}%{_mandir}/man6/%{name}-server.6

%files
%doc AUTHORS ChangeLog README.md server_*.conf
%{_datadir}/appdata/%{name}*.appdata.xml
%{_datadir}/applications/%{name}*.desktop
%{_gamesbindir}/%{name}
%{_gamesbindir}/%{name}-mapeditor
%{_gamesbindir}/%{name}-server
%{_iconsdir}/hicolor/scalable/apps/%{name}*.svg
%{_mandir}/man6/%{name}*.6*

%files data
%{_gamesdatadir}/%{name}/


%changelog
* Wed Jul 10 2024 Ilya Mashkin <oddity@altlinux.ru> 0.5.0-alt1
- 0.5.0

* Mon Apr 25 2022 Ilya Mashkin <oddity@altlinux.ru> 0.4.5-alt2
- Rebuild for Sisyphus

* Sat Feb 15 2020 Igor Vlasenko <viy@altlinux.ru> 0.4.5-alt1_3
- update by mgaimport

* Thu Oct 04 2018 Igor Vlasenko <viy@altlinux.ru> 0.4.5-alt1_2
- update by mgaimport

* Sun Mar 18 2018 Igor Vlasenko <viy@altlinux.ru> 0.4.5-alt1_1
- new version

