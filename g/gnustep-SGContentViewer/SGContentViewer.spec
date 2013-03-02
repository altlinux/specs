%set_verify_elf_method unresolved=strict

Name: gnustep-SGContentViewer
Version: 2006
Release: alt1
Summary: A contents Inspector that can play music files
License: LGPLv2.1
Group: Graphical desktop/GNUstep
Url: http://www.gnustep.org/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: gcc-objc gnustep-make-devel libgnustep-objc2-devel /proc
BuildPreReq: gnustep-ShengGuang-devel gnustep-libId3-devel

Requires: gnustep-ShengGuang

%description
A contents Inspector that can play Ogg Vorbis, mp3, speex, flac,
shorten, voc, midi, and mod files.

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
	GNUSTEP_MAKEFILES=%_datadir/GNUstep/Makefiles \
	GNUSTEP_SYSTEM_ROOT=%buildroot

%files
%doc ChangeLog README TODO
%_libdir/GNUstep

%changelog
* Sat Mar 02 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2006-alt1
- Initial build for Sisyphus

