%set_verify_elf_method unresolved=strict

Name: gnustep-NoteBook
Version: 0.3
Release: alt4
Summary: Application to store and organize your notes 
License: GPL
Group: Graphical desktop/GNUstep
Url: http://wiki.gnustep.org/index.php/NoteBook.app
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
Source1: %name.menu

BuildPreReq: gcc-objc gnustep-make-devel libgnustep-objc2-devel /proc
BuildPreReq: gnustep-gui-devel
BuildPreReq: libgmp-devel libgnutls-devel libgcrypt-devel
BuildPreReq: libxslt-devel libffi-devel libicu-devel zlib-devel

%description
NoteBook is an application to store and organize your notes.

Features:
* Uses a document interface to open multiple Notebooks.
* Each notebook has it's own tree interface navigable via a NSBrowser
  control. Both branch pages and leaf pages can contain note
  information.
* Stores note pages in Rich Text Format allowing you to format the note
  with different fonts, styles, weights, etc...

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

install -Dp -m644 %SOURCE1 %buildroot%_menudir/%name

%files
%_bindir/*
%_libdir/GNUstep
%_menudir/*

%changelog
* Mon Jan 20 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3-alt4
- Rebuilt with new gnustep-gui

* Sat Mar 02 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3-alt3
- Fixed menu file by kostyalamer@

* Wed Feb 27 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3-alt2
- Added menu file (thnx kostyalamer@)

* Tue Feb 26 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3-alt1
- Initial build for Sisyphus

