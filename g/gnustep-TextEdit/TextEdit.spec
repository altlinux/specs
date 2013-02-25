%set_verify_elf_method unresolved=strict

Name: gnustep-TextEdit
Version: 4.0
Release: alt1
Summary: Text editor for GNUstep
License: Free
Group: Graphical desktop/GNUstep
Url: http://www.gnustep.org/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: gcc-objc gnustep-make-devel libgnustep-objc2-devel /proc
BuildPreReq: gnustep-gui-devel

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

%files
%doc README.rtf
%_bindir/*
%_libdir/GNUstep

%changelog
* Mon Feb 25 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0-alt1
- Initial build for Sisyphus

