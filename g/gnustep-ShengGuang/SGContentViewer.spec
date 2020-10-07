%set_verify_elf_method unresolved=strict

Name: gnustep-ShengGuang
Version: 2006
Release: alt7
Summary: Library used by MusicBox for audio control
License: LGPLv2.1
Group: Graphical desktop/GNUstep
Url: http://www.gnustep.org/
Packager: Andrey Cherepanov <cas@altlinux.org>

Source: %name-%version.tar
Patch1: link-libs.patch

BuildPreReq: clang-devel gnustep-make-devel /proc
BuildPreReq: gnustep-gui-devel
BuildPreReq: libogg-devel libvorbis-devel libsmpeg-devel libflac-devel
BuildPreReq: libspeex-devel libSDL-devel libSDL_sound-devel

Requires: lib%name = %EVR
Requires: gnustep-back

%description
ShengGuang is a library used by MusicBox for audio control.
"Sheng Guang" means sound and light (video) in Chinese.
It contains classes supporting audio file and CD playback, OGG tag.
It uses bundles so that user can choose the external libraries to depend
on, as what backend of GNUstep do.
The default (and only) bundle use SDL and SDL_sound.

%package -n lib%name
Summary: Shared libraries of ShengGuang
Group: System/Libraries

%description -n lib%name
ShengGuang is a library used by MusicBox for audio control.
"Sheng Guang" means sound and light (video) in Chinese.
It contains classes supporting audio file and CD playback, OGG tag.
It uses bundles so that user can choose the external libraries to depend
on, as what backend of GNUstep do.
The default (and only) bundle use SDL and SDL_sound.

This package contains shared libraries of ShengGuang.

%package -n lib%name-devel
Summary: Development files of ShengGuang
Group: Development/Objective-C
Requires: lib%name = %EVR
Requires: %name = %EVR
Provides: %name-devel = %EVR

%description -n lib%name-devel
ShengGuang is a library used by MusicBox for audio control.
"Sheng Guang" means sound and light (video) in Chinese.
It contains classes supporting audio file and CD playback, OGG tag.
It uses bundles so that user can choose the external libraries to depend
on, as what backend of GNUstep do.
The default (and only) bundle use SDL and SDL_sound.

This package contains development files of ShengGuang.

%prep
%setup -n ShengGuang
%patch1 -p3

%build
. %_datadir/GNUstep/Makefiles/GNUstep.sh

%make_build \
	messages=yes \
	debug=yes \
	strip=no \
	shared=yes \
	AUXILIARY_CPPFLAGS="-I$PWD/.." \
	CONFIG_SYSTEM_LIBS='-lgnustep-gui -lgnustep-base' \
	OBJCFLAGS="%optflags -DGNUSTEP" \
	USE_NONFRAGILE_ABI=no
 
%install
. %_datadir/GNUstep/Makefiles/GNUstep.sh

%makeinstall_std GNUSTEP_INSTALLATION_DOMAIN=SYSTEM \
	LIB_SUFFIX=%_libsuff \
	GNUSTEP_MAKE_STRICT_V2_MODE=no \
	GNUSTEP_INSTALLATION_DIR=%buildroot%_libdir/GNUstep

pushd %buildroot%_libdir/GNUstep/Libraries
lib=$(ls *.so.*.*.*)
for i in *.so*; do
	mv $i %buildroot%_libdir/
	ln -s %_libdir/$lib ./$i
done
popd

install -d %buildroot%_includedir
ln -s %_libdir/GNUstep/Headers/ShengGuang \
	%buildroot%_includedir/

%files
%doc README
%_libdir/GNUstep
%exclude %_libdir/GNUstep/Headers

%files -n lib%name
%_libdir/*.so.*

%files -n lib%name-devel
%_includedir/*
%_libdir/*.so
%_libdir/GNUstep/Headers

%changelog
* Wed Oct 07 2020 Andrey Cherepanov <cas@altlinux.org> 2006-alt7
- Build without libgnustep-objc2-devel.

* Tue Jul 02 2019 Igor Vlasenko <viy@altlinux.ru> 2006-alt6
- NMU: fixed LIB_SUFFIX= on non-x86_64

* Sat Feb 15 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2006-alt5
- Built with clang

* Thu Jan 30 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2006-alt4
- Added Requires: gnustep-back

* Tue Jan 28 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2006-alt3
- Fixed build

* Mon Jan 20 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2006-alt2
- Rebuilt with new gnustep-gui

* Sat Mar 02 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2006-alt1
- Initial build for Sisyphus

