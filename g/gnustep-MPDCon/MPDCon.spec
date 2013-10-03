%set_verify_elf_method unresolved=strict

Name: gnustep-MPDCon
Version: 1.4
Release: alt3
Summary: A GNUstep MPD client
License: GPLv2
Group: Graphical desktop/GNUstep
Url: http://www.gnustep.org/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
Source1: %name.menu

BuildPreReq: gcc-objc gnustep-make-devel libgnustep-objc2-devel /proc
BuildPreReq: gnustep-gui-devel libsqlite3-devel libmpdclient-devel
BuildPreReq: gnustep-sqlclient-devel libbsd-devel

Requires: mpd

%description
A client for the Music Player Daemon (MPD).

Features:
* connects to an MPD server
* Playlist and Collections
* Lyrics Inspector connecting to lyrics.wikia.com
* Song Inspector
* Rating of songs in the Playlist
* Playlist Inspector

%prep
%setup

%build
%make_build \
	messages=yes \
	debug=yes \
	strip=no \
	shared=yes \
	AUXILIARY_CPPFLAGS='-O2' \
	CONFIG_SYSTEM_LIBS='-lSQLClient -lmpdclient -lbsd'
 
%install
%makeinstall_std GNUSTEP_INSTALLATION_DOMAIN=SYSTEM

install -p -D -m644 %SOURCE1 %buildroot%_menudir/%name

%files
%doc ChangeLog
%_bindir/*
%_libdir/GNUstep
%_menudir/*

%changelog
* Thu Oct 03 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4-alt3
- Rebuilt with new gnustep-sqlclient

* Fri Mar 01 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4-alt2
- Added menu file (thnx kostyalamer@)

* Wed Feb 27 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4-alt1
- Initial build for Sisyphus

