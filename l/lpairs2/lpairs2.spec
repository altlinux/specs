
Summary: Classical memory game with cards
Name: lpairs2
Version: 2.3.1
Release: alt1
Url: http://lgames.sourceforge.io/LPairs
Source0: https://sourceforge.net/projects/lgames/files/%name/%name-%version.tar.gz
License: GPLv3+
Group: Games/Other
Packager: Ilya Mashkin <oddity@altlinux.ru>
BuildRequires:  libSDL2-devel libSDL2_ttf-devel libSDL2_mixer-devel libSDL2_image-devel
BuildRequires:  gettext gettext-tools gcc gcc-c++
BuildRequires:  desktop-file-utils
Obsoletes: lpairs < 2
Provides: lpairs

%description
LPairs2 is a memory game with 2x36 high resolution animal cards where you turn
over any two cards and if they match they get removed. If they don't match they
are turned back over. The game is over when all cards have been matched. You
can play with different set sizes in fullscreen (6x4 to 12x6) or windowed mode
(6x4 to 10x7). And for anyone who's bored by just matching pairs: You can try
to match triplets and quadruplets as well. There is also a 2-player mode with a
CPU opponent.

%prep
%setup

%build
%configure	--bindir=%_gamesbindir \
		--with-libiconv-prefix=%prefix \
		--with-libintl-prefix=%prefix \
		--localstatedir=%_localstatedir/games
%make_build

%install
install -d %buildroot%_localstatedir/games
%makeinstall_std

desktop-file-install --dir %{buildroot}%{_datadir}/applications \
        lpairs2.desktop

%files
%doc README TODO
%attr(2711, root, games) %_gamesbindir/*
%_datadir/%name
%_datadir/applications/%name.desktop
%_iconsdir/%name.png

%changelog
* Thu Jun 27 2024 Ilya Mashkin <oddity@altlinux.ru> 2.3.1-alt1
- 2.3.1

* Wed Aug 02 2023 Ilya Mashkin <oddity@altlinux.ru> 2.3-alt1
- 2.3

* Wed Jul 19 2023 Ilya Mashkin <oddity@altlinux.ru> 2.2.1-alt1
- 2.2.1

* Fri Oct 14 2022 Ilya Mashkin <oddity@altlinux.ru> 2.2-alt1
- 2.2


