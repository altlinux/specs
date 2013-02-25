%set_verify_elf_method unresolved=strict

Name: gnustep-Gemas
Version: 0.3
Release: alt1
Summary: A simple code editor for GNUstepers 
License: GPLv3
Group: Graphical desktop/GNUstep
Url: http://www.gnustep.org/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: gcc-objc gnustep-make-devel libgnustep-objc2-devel /proc
BuildPreReq: gnustep-HighlighterKit-devel gnustep-gui-devel

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
	AUXILIARY_CPPFLAGS='-O2' \
	GNUSTEP_MAKEFILES=%_datadir/GNUstep/Makefiles
 
%install
%makeinstall_std GNUSTEP_INSTALLATION_DOMAIN=SYSTEM \
	GNUSTEP_MAKEFILES=%_datadir/GNUstep/Makefiles

%files
%doc Changelog README
%_bindir/*
%_libdir/GNUstep

%changelog
* Mon Feb 25 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3-alt1
- Initial build for Sisyphus

