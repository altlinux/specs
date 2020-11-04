%set_verify_elf_method unresolved=strict

Name: gnustep-SGContentViewer
Version: 2006
Release: alt6
Summary: A contents Inspector that can play music files
License: LGPLv2.1
Group: Graphical desktop/GNUstep
Url: http://wiki.gnustep.org/index.php/GWorkspace.app
Packager: Andrey Cherepanov <cas@altlinux.org>

Source: %name-%version.tar

BuildPreReq: gnustep-make-devel /proc
BuildPreReq: gnustep-ShengGuang-devel gnustep-libId3-devel
BuildPreReq: libgmp-devel libgnutls-devel libgcrypt-devel
BuildPreReq: libxslt-devel libffi-devel libicu-devel zlib-devel

Requires: gnustep-ShengGuang
Requires: gnustep-back

%description
A contents Inspector that can play Ogg Vorbis, mp3, speex, flac,
shorten, voc, midi, and mod files.

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

%makeinstall_std GNUSTEP_INSTALLATION_DOMAIN=SYSTEM \
	GNUSTEP_SYSTEM_ROOT=%buildroot

%files
%doc ChangeLog README TODO
%_libdir/GNUstep

%changelog
* Wed Nov 04 2020 Andrey Cherepanov <cas@altlinux.org> 2006-alt6
- Remove redundant clang-devel for build

* Wed Oct 07 2020 Andrey Cherepanov <cas@altlinux.org> 2006-alt5
- Build without libgnustep-objc2-devel.

* Thu Jan 14 2016 Mikhail Efremov <sem@altlinux.org> 2006-alt4.1
- NMU: Rebuild with libgnutls30.

* Sat Feb 15 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2006-alt4
- Built with clang

* Thu Jan 30 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2006-alt3
- Added Requires: gnustep-back

* Tue Jan 21 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2006-alt2
- Rebuilt with new gnustep-gui

* Sat Mar 02 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2006-alt1
- Initial build for Sisyphus

