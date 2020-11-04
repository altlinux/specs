%set_verify_elf_method unresolved=strict

Name: gnustep-Popup
Version: 0.5
Release: alt6
Summary: Spaced repetition learning system for pairs of words
License: GPLv2
Group: Graphical desktop/GNUstep
Url: http://wiki.gnustep.org/index.php/Popup.app
Packager: Andrey Cherepanov <cas@altlinux.org>

Source: %name-%version.tar
Source1: %name.menu

BuildPreReq: gnustep-make-devel /proc
BuildPreReq: gnustep-gui-devel
BuildPreReq: libgmp-devel libgnutls-devel libgcrypt-devel
BuildPreReq: libxslt-devel libffi-devel libicu-devel zlib-devel

Requires: gnustep-back

%description
Popup is an interactive learning aid for pairs of words. It behaves much
like a stack of flashcards, but handles one-to-many and many-to-one word
relationships better, and includes an integrated scheduler for efficient
use of your 'cards'.

Features:

* An editor with support for copying and pasting groups of words, as
  well as drag and drop.
* Three quiz styles: multiple choice, spelling, and flashcard.
* Supports quizes and practice
* Graduated time interval scheduler.
* Localized for Thai and German.

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
%_bindir/*
%_libdir/GNUstep
%_menudir/*

%changelog
* Wed Nov 04 2020 Andrey Cherepanov <cas@altlinux.org> 0.5-alt6
- Remove redundant clang-devel for build

* Wed Oct 07 2020 Andrey Cherepanov <cas@altlinux.org> 0.5-alt5
- Build without libgnustep-objc2-devel.

* Thu Jan 14 2016 Mikhail Efremov <sem@altlinux.org> 0.5-alt4.pre1.1
- NMU: Rebuild with libgnutls30.

* Sun Feb 16 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5-alt4.pre1
- Added menu file (thnx kostyalamer@)

* Sat Feb 15 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5-alt3.pre1
- Built with clang

* Thu Jan 30 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5-alt2.pre1
- Added Requires: gnustep-back

* Wed Jan 22 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5-alt1.pre1
- Initial build for Sisyphus

