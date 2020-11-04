#set_verify_elf_method unresolved=strict

Name: gnustep-Grr
Version: 1.0
Release: alt7
Summary: RSS Reader application
License: GPL
Group: Graphical desktop/GNUstep
Url: http://gap.nongnu.org/grr/index.html
Packager: Andrey Cherepanov <cas@altlinux.org>

Source: %name-%version.tar
Source1: %name.menu

BuildPreReq: gnustep-make-devel /proc
BuildPreReq: gnustep-RSSkit-devel gnustep-gui-devel
BuildPreReq: libgmp-devel libgnutls-devel libgcrypt-devel
BuildPreReq: libxslt-devel libffi-devel libicu-devel zlib-devel

Requires: gnustep-RSSkit
Requires: gnustep-back

%description
Grr is a reader for RSS news feeds. It (since version 0.9.0) is part of
the GNUstep Application project.

Features:
From the website:
* Parsing RSS Feeds
* Fetching feeds from the web
* Showing headlines
* Showing the article's descriptions
* Categories for feeds
* Articles can be rated
* Simple HTML rendering on GNUstep
* Serializing obtained feed-information to hard-disk
* Managing (Adding, removing) feeds
* Parsing ATOM feeds.
* Macintosh Cocoa port

%prep
%setup

%build
. %_datadir/GNUstep/Makefiles/GNUstep.sh

%make_build \
	messages=yes \
	debug=yes \
	strip=no \
	shared=yes
 
%install
. %_datadir/GNUstep/Makefiles/GNUstep.sh

%makeinstall_std GNUSTEP_INSTALLATION_DOMAIN=SYSTEM

install -p -D -m644 %SOURCE1 %buildroot%_menudir/%name

%files
%doc ChangeLog README TODO
%_bindir/*
%_libdir/GNUstep
%_menudir/*

%changelog
* Wed Nov 04 2020 Andrey Cherepanov <cas@altlinux.org> 1.0-alt7
- Remove redundant clang-devel for build

* Wed Oct 07 2020 Andrey Cherepanov <cas@altlinux.org> 1.0-alt6
- Build without libgnustep-objc2-devel.

* Thu Jan 14 2016 Mikhail Efremov <sem@altlinux.org> 1.0-alt5.1
- NMU: Rebuild with libgnutls30.

* Fri Feb 14 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0-alt5
- Built with clang

* Wed Jan 29 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0-alt4
- Added Requires: gnustep-back

* Mon Jan 20 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0-alt3
- Rebuilt with new gnustep-gui

* Sat Mar 02 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0-alt2
- Added menu file (thnx kostyalamer@)

* Wed Feb 27 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0-alt1
- Initial build for Sisyphus

