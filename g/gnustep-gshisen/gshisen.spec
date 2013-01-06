%set_verify_elf_method unresolved=strict

Name: gnustep-gshisen
Version: 1.3.0
Release: alt1
Summary: GShisen is a game for GNUstep
License: GPL
Group: Graphical desktop/GNUstep
Url: http://www.nongnu.org/gap/gshisen/index.html
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: gcc-objc gnustep-make-devel libgnustep-objc2-devel /proc
BuildPreReq: gnustep-base-devel gnustep-gui-devel

%description
GShisen is the first GNUstep game!

The object of the game is to remove all tiles from the field. Only two
matching tiles can be removed at a time. Two tiles can only be removed
if they can be connected with at most three connected lines. Lines can
be horizontal or vertical but not diagonal.

Remember that lines may cross the empty border. If you are stuck, you
can use the Hint feature to find two tiles which may be removed.

%prep
%setup

%build
%make_build \
	messages=yes \
	debug=yes \
	strip=no \
	shared=yes \
	GNUSTEP_MAKEFILES=%_datadir/GNUstep/Makefiles
 
%install
%makeinstall_std GNUSTEP_INSTALLATION_DOMAIN=SYSTEM \
	GNUSTEP_MAKEFILES=%_datadir/GNUstep/Makefiles

%files
%doc ChangeLog
%_bindir/*
%_libdir/GNUstep

%changelog
* Sun Jan 06 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.0-alt1
- Initial build for Sisyphus

