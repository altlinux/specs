%set_verify_elf_method unresolved=strict

Name: gnustep-Poe
Version: 0.5.1
Release: alt4.1
Summary: Poe, or "a Pugnacious Ogg Editor", is a vorbis comment editor
License: GPLv2
Group: Graphical desktop/GNUstep
Url: http://wiki.gnustep.org/index.php/Poe.app
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
Source1: %name.menu

BuildPreReq: clang-devel gnustep-make-devel libgnustep-objc2-devel /proc
BuildPreReq: gnustep-gui-devel
BuildPreReq: libgmp-devel libgnutls-devel libgcrypt-devel
BuildPreReq: libxslt-devel libffi-devel libicu-devel zlib-devel
BuildPreReq: libvorbis-devel libogg-devel

Requires: gnustep-back

%description
Poe tries to follow the vorbis comment header specification
(v-comment.html, Field Names, and Implications are the pertinent parts)
closely, while being convenient and flexible to use.

Towards that end, it doesn't have a static 'form' style interface.
Instead, it has an editable table of comments. The contents of the table
change dependent upon preference settings, and what comments are in the
ogg file you are editing.

Features:
* Allows multiple Artist, Performer, and Genre fields.
* Flexible choice of comment fields to edit.
* Allows editing of all the comment fields in a file, not just the ones
  Poe is aware of.

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
* Thu Jan 14 2016 Mikhail Efremov <sem@altlinux.org> 0.5.1-alt4.1
- NMU: Rebuild with libgnutls30.

* Sun Feb 16 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5.1-alt4
- Added menu file (thnx kostyalamer@)

* Sat Feb 15 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5.1-alt3
- Built with clang

* Thu Jan 30 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5.1-alt2
- Added Requires: gnustep-back

* Tue Jan 21 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5.1-alt1
- Initial build for Sisyphus

