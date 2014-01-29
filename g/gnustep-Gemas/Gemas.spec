%set_verify_elf_method unresolved=strict

Name: gnustep-Gemas
Version: 0.3
Release: alt5
Summary: A simple code editor for GNUstepers 
License: GPLv3
Group: Graphical desktop/GNUstep
Url: http://www.gnustep.org/softwareindex/showdetail.php?app=123
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
Source1: %name.menu

BuildPreReq: gcc-objc gnustep-make-devel libgnustep-objc2-devel /proc
BuildPreReq: gnustep-HighlighterKit-devel gnustep-gui-devel
BuildPreReq: libgmp-devel libgnutls-devel libgcrypt-devel
BuildPreReq: libxslt-devel libffi-devel libicu-devel zlib-devel

Requires: gnustep-HighlighterKit
Requires: gnustep-back

%description
Gemas is a simple code editor for GNUstepers. Features:

* Highlight syntax for languages C, C++, Obj-C, Obj-C++, GSmarkup.
* Highlight syntax to edit Strings, Plist, GNUmakefile, ChangeLog files
  and Plain text.
* Auto indentation.
* Double click above a parentheses to select all code inside these.
* Emacs compatibility (this means that you can see correctly the
  indentation of a file you wrote on Emacs).
* Go to Line Panel.
* Preferences Panel to change colors, editor size, font, Highlighter
  theme, ...
* Menu options App and Tool to create a simple App or Tool

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

install -p -D -m644 %SOURCE1 %buildroot%_menudir/%name

%files
%doc Changelog README
%_bindir/*
%_libdir/GNUstep
%_menudir/*

%changelog
* Wed Jan 29 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3-alt5
- Added Requires: gnustep-back

* Mon Jan 20 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3-alt4
- Rebuilt with new gnustep-gui

* Thu Feb 28 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3-alt3
- Added menu file (thnx kostyalamer@)

* Tue Feb 26 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3-alt2
- Added requirement on gnustep-HighlighterKit (thnx aen@)

* Mon Feb 25 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3-alt1
- Initial build for Sisyphus

