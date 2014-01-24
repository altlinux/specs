#set_verify_elf_method unresolved=strict

Name: gnustep-MP3ToWav
Version: 0.4.1
Release: alt1
Summary: MP3ToWav plugin for Burn.app
License: Free
Group: Graphical desktop/GNUstep
Url: http://gsburn.sourceforge.net/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: gcc-objc gnustep-make-devel libgnustep-objc2-devel /proc
BuildPreReq: gnustep-gui-devel
BuildPreReq: libgmp-devel libgnutls-devel libgcrypt-devel
BuildPreReq: libxslt-devel libffi-devel libicu-devel zlib-devel
BuildPreReq: libao-devel libmad-devel gnustep-Burn-devel

%description
MP3ToWav plugin for Burn.app.

%prep
%setup

%build
%make_build \
	messages=yes \
	debug=yes \
	strip=no \
	shared=yes \
	AUXILIARY_CPPFLAGS='-O2 -DGNUSTEP -I%_includedir/Burn' \
	GNUSTEP_MAKEFILES=%_datadir/GNUstep/Makefiles
 
%install
%makeinstall_std GNUSTEP_INSTALLATION_DOMAIN=SYSTEM \
	GNUSTEP_MAKEFILES=%_datadir/GNUstep/Makefiles \
	GNUSTEP_INSTALLATION_DIR=%buildroot%_libdir/GNUstep

%files
%doc README
%_libdir/GNUstep

%changelog
* Fri Jan 24 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.1-alt1
- Initial build for Sisyphus

