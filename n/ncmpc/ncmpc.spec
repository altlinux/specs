Name: ncmpc
Version: 0.19
Release: alt1

Summary: curses client for mpd
License: GPL
Group: Sound
Url: http://mpd.wikia.com/wiki/Client:Ncmpc

Source: http://downloads.sourceforge.net/musicpd/ncmpc-%version.tar.bz2
Source1: %name.desktop
Packager: Damir Shayhutdinov <damir@altlinux.ru>

BuildRequires: glib2-devel libncursesw-devel libtinfo-devel pkg-config
BuildRequires: libmpdclient-devel
BuildRequires: desktop-file-utils

%description
ncmpc is a curses client for the Music Player Daemon (MPD). ncmpc
connects to a MPD running on a machine on the local network, and
controls this with an interface inspired by cplay. If ncmpc is used
with lirc and irpty it can be used to manage playlists and control MPD
with a remote control.

%prep
%setup

%build
%autoreconf
%add_optflags -Wextra -Wno-unused
%configure --enable-wide
%make_build

%install
%makeinstall_std
%find_lang %name
cp -f doc/{config.sample,keys.sample,ncmpc.lirc} ./

install -m 644 -D %SOURCE1 %buildroot/%_desktopdir/%name.desktop
desktop-file-install --dir %buildroot%_desktopdir \
	--add-category=AudioVideo \
	--add-category=Player \
	%buildroot%_desktopdir/ncmpc.desktop


%files -f %name.lang
%doc AUTHORS NEWS README COPYING config.sample keys.sample ncmpc.lirc
%_bindir/*
%_man1dir/*
%_desktopdir/%name.desktop
%exclude %_datadir/doc/ncmpc

%changelog
* Sat Sep 17 2011 Slava Semushin <php-coder@altlinux.ru> 0.19-alt1
- NMU
- Updated to 0.19

* Thu May 19 2011 Damir Shayhutdinov <damir@altlinux.ru> 0.18-alt2
- Applied patch from repocop (adds proper categories to .desktop file)

* Sat Dec 04 2010 Slava Semushin <php-coder@altlinux.ru> 0.18-alt1
- NMU
- Updated to 0.18

* Sun Jul 25 2010 Slava Semushin <php-coder@altlinux.ru> 0.17-alt1
- NMU
- Updated to 0.17

* Sun Feb 28 2010 Slava Semushin <php-coder@altlinux.ru> 0.16.1-alt1
- NMU
- Updated to 0.16.1

* Sun Jan 17 2010 Slava Semushin <php-coder@altlinux.ru> 0.16-alt1
- NMU
- Updated to 0.16 (Closes: #20170)
- Updated home page

* Sun Nov 23 2008 Damir Shayhutdinov <damir@altlinux.ru> 0.11.1-alt6
- Removed obsolete update_menu macros

* Mon Jun 05 2006 Damir Shayhutdinov <damir@altlinux.ru> 0.11.1-alt5
- Built with libncursesw-devel

* Sun May 21 2006 Damir Shayhutdinov <damir@altlinux.ru> 0.11.1-alt4
- Built with libncursesw
- Fixed .desktop (#9153)

* Wed Jan 18 2006 Damir Shayhutdinov <damir@altlinux.ru> 0.11.1-alt3
- Added patch to allow build with ncursesw (disabled by default)
- Fixed more typos in translation
- Added menu

* Thu Nov 03 2005 Damir Shayhutdinov <damir@altlinux.ru> 0.11.1-alt2
- Corrected russian translation encoding
- Fixed typos in translation

* Sat Oct 29 2005 Damir Shayhutdinov <damir@altlinux.ru> 0.11.1-alt1
- Initial build for Sisyphus

