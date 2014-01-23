%set_verify_elf_method unresolved=strict

Name: gnustep-GRubik
Version: 0.1
Release: alt1
Summary: GRubik is a virtual 3D Rubik's cube for you to solve
License: GPLv2
Group: Graphical desktop/GNUstep
Url: http://wiki.gnustep.org/index.php/GRubik.app
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: gcc-objc gnustep-make-devel libgnustep-objc2-devel /proc
BuildPreReq: gnustep-gui-devel
BuildPreReq: libgmp-devel libgnutls-devel libgcrypt-devel
BuildPreReq: libxslt-devel libffi-devel libicu-devel zlib-devel

%description
GRubik is a virtual 3D Rubik's cube for you to solve.

Features:

* simple but functional and fast 3D
* a smart scramble that ensures you get a solvable cube
* interesting code that you might enjoy reading and which uses a variety
  of programming techniques.

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
	GNUSTEP_MAKEFILES=%_datadir/GNUstep/Makefiles \
	GNUSTEP_SYSTEM_ROOT=%buildroot%_libdir/GNUstep

install -d %buildroot%_bindir
ln -s %_libdir/GNUstep/Applications/GRubik.app/GRubik \
	%buildroot%_bindir/

%files
%_bindir/*
%_libdir/GNUstep

%changelog
* Thu Jan 23 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1-alt1
- Initial build for Sisyphus

