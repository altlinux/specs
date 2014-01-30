%set_verify_elf_method unresolved=strict

Name: gnustep-Popup
Version: 0.5
Release: alt2.pre1
Summary: Spaced repetition learning system for pairs of words
License: GPLv2
Group: Graphical desktop/GNUstep
Url: http://wiki.gnustep.org/index.php/Popup.app
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: gcc-objc gnustep-make-devel libgnustep-objc2-devel /proc
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
%make_build \
	messages=yes \
	debug=yes \
	strip=no \
	shared=yes \
	AUXILIARY_CPPFLAGS='-O2 -DGNUSTEP' \
	GNUSTEP_MAKEFILES=%_datadir/GNUstep/Makefiles
 
%install
%makeinstall_std GNUSTEP_INSTALLATION_DOMAIN=SYSTEM \
	GNUSTEP_MAKEFILES=%_datadir/GNUstep/Makefiles

%files
%_bindir/*
%_libdir/GNUstep

%changelog
* Thu Jan 30 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5-alt2.pre1
- Added Requires: gnustep-back

* Wed Jan 22 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5-alt1.pre1
- Initial build for Sisyphus

