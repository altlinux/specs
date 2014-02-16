%set_verify_elf_method unresolved=strict

Name: gnustep-MusicKit
Version: 5.6.2
Release: alt4.git20110723
Summary: Software system for building music, sound, signal processing, and MIDI applications
License: GPLv2+
Group: Graphical desktop/GNUstep
Url: http://musickit.sourceforge.net/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://musickit.svn.sourceforge.net/svnroot/musickit/trunk/
Source: %name-%version.tar
Source1: %name.menu

BuildRequires: rpm-macros-make
BuildPreReq: clang-devel gnustep-make-devel gnustep-base-devel
BuildPreReq: libgnustep-objc2-devel gnustep-performance-devel /proc
BuildPreReq: gnustep-gui-devel libalsa-devel
BuildPreReq: doxygen graphviz ltxml openjade
BuildPreReq: libportaudio2-devel libogg-devel libvorbis-devel
BuildPreReq: libsndfile-devel libshout2-devel libmp3hip-devel
BuildPreReq: libportmidi libportmidi-devel liblame-devel
BuildPreReq: gcc-c++ texinfo texi2html
BuildPreReq: libgmp-devel libgnutls-devel libgcrypt-devel
BuildPreReq: libxslt-devel libffi-devel libicu-devel zlib-devel

Requires: gnustep-back

%description
The MusicKit is an object-oriented software system for building music,
sound, signal processing, and MIDI applications. It has been used in
such diverse commercial applications as music sequencers, computer
games, and document processors. Professors and students in academia have
used the MusicKit in a host of areas, including music performance,
scientific experiments, computer-aided instruction, and physical
modeling. The MusicKit was the first to unify the MIDI and Music V
paradigms, thus combining interaction with generality (Music V, written
by Max Mathews and others at Bell Labs four decades ago, was the first
widely available "computer music compiler").

%package -n lib%name
Summary: Libraries for %name
Group: System/Libraries
License: LGPLv2+ and LGPLv3+

%description -n lib%name
The MusicKit is an object-oriented software system for building music,
sound, signal processing, and MIDI applications. It has been used in
such diverse commercial applications as music sequencers, computer
games, and document processors. Professors and students in academia have
used the MusicKit in a host of areas, including music performance,
scientific experiments, computer-aided instruction, and physical
modeling. The MusicKit was the first to unify the MIDI and Music V
paradigms, thus combining interaction with generality (Music V, written
by Max Mathews and others at Bell Labs four decades ago, was the first
widely available "computer music compiler").

This package contains the libraries for %name.

%package -n lib%name-devel
Summary: Header files for the gnustep-gui package
Group: Development/Objective-C
Provides: %name-devel = %EVR
Requires: gnustep-base-devel /proc
Requires: lib%name = %version-%release
Requires: %name = %version-%release

%description -n lib%name-devel
The MusicKit is an object-oriented software system for building music,
sound, signal processing, and MIDI applications. It has been used in
such diverse commercial applications as music sequencers, computer
games, and document processors. Professors and students in academia have
used the MusicKit in a host of areas, including music performance,
scientific experiments, computer-aided instruction, and physical
modeling. The MusicKit was the first to unify the MIDI and Music V
paradigms, thus combining interaction with generality (Music V, written
by Max Mathews and others at Bell Labs four decades ago, was the first
widely available "computer music compiler").

This package contains the header files for gnustep-gui.

%package examples
Summary: Examples of %name
Group: Development/Objective-C
Requires: %name = %EVR

%description examples
The MusicKit is an object-oriented software system for building music,
sound, signal processing, and MIDI applications. It has been used in
such diverse commercial applications as music sequencers, computer
games, and document processors. Professors and students in academia have
used the MusicKit in a host of areas, including music performance,
scientific experiments, computer-aided instruction, and physical
modeling. The MusicKit was the first to unify the MIDI and Music V
paradigms, thus combining interaction with generality (Music V, written
by Max Mathews and others at Bell Labs four decades ago, was the first
widely available "computer music compiler").

This package contains examples of %name.

%package docs
Summary: Documentation for %name
Group: Documentation
BuildArch: noarch
License: GFDL

%description docs
The MusicKit is an object-oriented software system for building music,
sound, signal processing, and MIDI applications. It has been used in
such diverse commercial applications as music sequencers, computer
games, and document processors. Professors and students in academia have
used the MusicKit in a host of areas, including music performance,
scientific experiments, computer-aided instruction, and physical
modeling. The MusicKit was the first to unify the MIDI and Music V
paradigms, thus combining interaction with generality (Music V, written
by Max Mathews and others at Bell Labs four decades ago, was the first
widely available "computer music compiler").

This package contains the documentation for %name.

%prep
%setup -n MusicKit-%version

cp -fR MusicKit/Examples _ex

%install
. %_datadir/GNUstep/Makefiles/GNUstep.sh
TOPDIR=$PWD

autoIt() {
autoconf ||aclocal ||:
autoheader || autoconf ||:
}

pushd MusicKit
autoIt
%configure
popd

pushd MusicKit/Frameworks/PlatformDependent/MKPerformSndMIDI_portaudio
%make_build \
	messages=yes \
	debug=yes \
	strip=no \
	shared=yes \
	OBJCFLAGS="%optflags -DGNUSTEP" \
	USE_NONFRAGILE_ABI=no

%makeinstall_std GNUSTEP_INSTALLATION_DOMAIN=SYSTEM

popd

pushd MusicKit/Frameworks/SndKit
%make_build \
	messages=yes \
	debug=yes \
	strip=no \
	shared=yes \
	CONFIG_SYSTEM_LIBS='-lMKPerformSndMIDI' \
	AUXILIARY_CPPFLAGS='-DHAVE_CONFIG_H -I%buildroot%_includedir' \
	BUILDLIBROOT=%buildroot%_libdir

%makeinstall_std GNUSTEP_INSTALLATION_DOMAIN=SYSTEM \
	BUILDLIBROOT=%buildroot%_libdir

popd

pushd MusicKit/Frameworks/MKDSP_Native
%make_build \
	messages=yes \
	debug=yes \
	strip=no \
	shared=yes \
	AUXILIARY_CPPFLAGS='-I%buildroot%_includedir' \
	OBJCFLAGS="%optflags -DGNUSTEP" \
	USE_NONFRAGILE_ABI=no

%makeinstall_std GNUSTEP_INSTALLATION_DOMAIN=SYSTEM \
	BUILDLIBROOT=%buildroot%_libdir

popd

pushd MusicKit/Frameworks/MusicKit
%make \
	messages=yes \
	debug=yes \
	strip=no \
	shared=yes \
	AUXILIARY_CPPFLAGS='-I%buildroot%_includedir' \
	CONFIG_SYSTEM_LIBS='-lMKDSP -lSndKit -lMKPerformSndMIDI' \
	BUILDLIBROOT=%buildroot%_libdir \
	OBJCFLAGS="%optflags -DGNUSTEP" \
	USE_NONFRAGILE_ABI=no

%makeinstall_std GNUSTEP_INSTALLATION_DOMAIN=SYSTEM \
	BUILDLIBROOT=%buildroot%_libdir

popd

pushd MusicKit
%make_build \
	messages=yes \
	debug=yes \
	strip=no \
	shared=yes \
	AUXILIARY_CPPFLAGS='-I%buildroot%_includedir' \
	CONFIG_SYSTEM_LIBS='-lMKDSP -lSndKit -lMKPerformSndMIDI' \
	BUILDLIBROOT=%buildroot%_libdir \
	OBJCFLAGS="%optflags -DGNUSTEP" \
	USE_NONFRAGILE_ABI=no

%makeinstall_std GNUSTEP_INSTALLATION_DOMAIN=SYSTEM \
	BUILDLIBROOT=%buildroot%_libdir

popd

pushd MusicKit/Documentation
touch /tmp/MusicKit_ChangeLog.txt
%make_build \
	messages=yes

%makeinstall_std \
	GNUSTEP_INSTALLATION_DOMAIN=SYSTEM \
	DSTROOT=%buildroot
popd

pushd %buildroot%_libdir
for j in MKPerformSndMIDI SndKit MKDSP MusicKit; do
	for i in lib$j.so*; do
		rm -f $i
		mv GNUstep/Frameworks/$j.framework/Versions/Current/$i ./
		for k in lib$j.so.*.*; do
			ln -s %_libdir/$k GNUstep/Frameworks/$j.framework/Versions/Current/$i
			rm GNUstep/Frameworks/$j.framework/Versions/Current/$j
			ln -s %_libdir/$k GNUstep/Frameworks/$j.framework/Versions/Current/$j
		done
	done
done
popd

install -p -D -m644 %SOURCE1 %buildroot%_menudir/%name

%files
%_bindir/EnvelopeEd
%_bindir/Midi*
%_bindir/MultipleSoundPlayer
%_bindir/PianoRoll
%_bindir/ScorePlayer
%_bindir/Spectro
%_bindir/TwoWaves
%_libdir/GNUstep
%exclude %_libdir/GNUstep/Frameworks/*.framework/Versions/5/Headers
%exclude %_libdir/GNUstep/Frameworks/*.framework/Headers
%_menudir/*

%files -n lib%name
%_libdir/*.so.*

%files -n lib%name-devel
%_includedir/*
%_libdir/*.so
%_libdir/GNUstep/Frameworks/*.framework/Versions/5/Headers
%_libdir/GNUstep/Frameworks/*.framework/Headers

%files docs
%_docdir/GNUstep
%doc MusicKit/Applications/PhysicalModels/Documentation/*

%files examples
%_bindir/*
%exclude %_bindir/EnvelopeEd
%exclude %_bindir/Midi*
%exclude %_bindir/MultipleSoundPlayer
%exclude %_bindir/PianoRoll
%exclude %_bindir/ScorePlayer
%exclude %_bindir/Spectro
%exclude %_bindir/TwoWaves
%doc _ex/*

%changelog
* Sun Feb 16 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.6.2-alt4.git20110723
- Built with clang

* Sat Feb 15 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.6.2-alt3.git20110723
- Added menu file (thnx kostyalamer@)

* Wed Jan 29 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.6.2-alt2.git20110723
- Added Requires: gnustep-back

* Tue Jan 28 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.6.2-alt1.git20110723
- Initial build for Sisyphus

