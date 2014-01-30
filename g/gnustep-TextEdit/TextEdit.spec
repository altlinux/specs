%set_verify_elf_method unresolved=strict

Name: gnustep-TextEdit
Version: 4.0
Release: alt4
Summary: Text editor for GNUstep
License: Free
Group: Graphical desktop/GNUstep
Url: http://wiki.gnustep.org/index.php/TextEdit.app
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
Source1: %name.menu

BuildPreReq: gcc-objc gnustep-make-devel libgnustep-objc2-devel /proc
BuildPreReq: gnustep-gui-devel
BuildPreReq: libgmp-devel libgnutls-devel libgcrypt-devel
BuildPreReq: libxslt-devel libffi-devel libicu-devel zlib-devel

Requires: gnustep-back

%description
TextEdit is a relatively basic text editor. It handles plain text or
RTF, has a nice "Wrap to Page" mode, has search/replace functionality,
and can display any file as text.

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
	GNUSTEP_SYSTEM_ROOT=%buildroot

install -p -D -m644 %SOURCE1 %buildroot%_menudir/%name

%files
%doc README.rtf
%_bindir/*
%_libdir/GNUstep
%_menudir/*

%changelog
* Thu Jan 30 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0-alt4
- Added Requires: gnustep-back

* Mon Jan 20 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0-alt3
- Rebuilt with new gnustep-gui

* Thu Feb 28 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0-alt2
- Added menu file (thnx kostyalamer@)

* Mon Feb 25 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0-alt1
- Initial build for Sisyphus

