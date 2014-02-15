%set_verify_elf_method unresolved=strict

Name: gnustep-MPDCon
Version: 1.5.1
Release: alt3
Summary: A GNUstep MPD client
License: GPLv2
Group: Graphical desktop/GNUstep
Url: http://wiki.gnustep.org/index.php/MPDCon.app
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
Source1: %name.menu

BuildPreReq: clang-devel gnustep-make-devel libgnustep-objc2-devel /proc
BuildPreReq: gnustep-gui-devel libsqlite3-devel libmpdclient-devel
BuildPreReq: gnustep-sqlclient-devel libbsd-devel

Requires: mpd
Requires: gnustep-back

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
. %_datadir/GNUstep/Makefiles/GNUstep.sh

%make_build \
	messages=yes \
	debug=yes \
	strip=no \
	shared=yes \
	CONFIG_SYSTEM_LIBS='-lSQLClient -lmpdclient -lbsd'
 
%install
. %_datadir/GNUstep/Makefiles/GNUstep.sh

%makeinstall_std GNUSTEP_INSTALLATION_DOMAIN=SYSTEM

install -p -D -m644 %SOURCE1 %buildroot%_menudir/%name

%files
%doc ChangeLog
%_bindir/*
%_libdir/GNUstep
%_menudir/*

%changelog
* Sat Feb 15 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.5.1-alt3
- Built with clang

* Wed Jan 29 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.5.1-alt2
- Added Requires: gnustep-back

* Mon Jan 20 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.5.1-alt1
- Version 1.5.1

* Thu Oct 03 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4-alt3
- Rebuilt with new gnustep-sqlclient

* Fri Mar 01 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4-alt2
- Added menu file (thnx kostyalamer@)

* Wed Feb 27 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4-alt1
- Initial build for Sisyphus

