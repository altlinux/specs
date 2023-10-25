%def_disable static
%def_disable htmldoc

Name: stk
Version: 4.6.1
Release: alt2
License: MIT
Group: Sound
Summary: C++ classes for audio digital signal processing
Url: http://www-ccrma.stanford.edu/software/stk/
Source: stk-%version.tar
Patch0: stk-4.6.1-header.patch
Patch1: stk-4.6.1-cflags-lib.patch
Patch2: stk-4.6.1-alt-add-pkgconfig-jack.patch

Requires: lib%name = %EVR

# Automatically added by buildreq on Thu Nov 22 2007
BuildRequires: gcc-c++ jackit-devel libalsa-devel util-linux-ng
BuildRequires: desktop-file-utils symlinks
%if_enabled htmldoc
BuildRequires: doxygen
%endif

%description
The Synthesis ToolKit in C++ (STK) is a set of open source audio signal
processing and algorithmic synthesis classes written in C++. STK was
designed to facilitate rapid development of music synthesis and audio
processing software, with an emphasis on cross-platform functionality,
realtime control, ease of use, and educational example code. The Synthesis
ToolKit is extremely portable (it's mostly platform-independent C and C++
code), and it's completely user-extensible (all source included, no unusual
libraries, and no hidden drivers). We like to think that this increases the
chances that our programs will still work in another 5-10 years. In fact,
the ToolKit has been working continuously for nearly 8 years now. STK
currently runs with "realtime" support (audio and MIDI) on SGI (Irix),
Linux, Macintosh OS X, and Windows computer platforms. Generic,
non-realtime support has been tested under NeXTStep, Sun, and other
platforms and should work with any standard C++ compiler.

%package -n lib%name
Summary: C++ classes for audio digital signal processing
Group: System/Libraries
Provides: %{name} = %EVR

%description -n lib%name
The Synthesis ToolKit in C++ (STK) is a set of open source audio signal
processing and algorithmic synthesis classes written in C++. STK was
designed to facilitate rapid development of music synthesis and audio
processing software, with an emphasis on cross-platform functionality,
realtime control, ease of use, and educational example code. The Synthesis
ToolKit is extremely portable (it's mostly platform-independent C and C++
code), and it's completely user-extensible (all source included, no unusual
libraries, and no hidden drivers). We like to think that this increases the
chances that our programs will still work in another 5-10 years. In fact,
the ToolKit has been working continuously for nearly 8 years now. STK
currently runs with "realtime" support (audio and MIDI) on SGI (Irix),
Linux, Macintosh OS X, and Windows computer platforms. Generic,
non-realtime support has been tested under NeXTStep, Sun, and other
platforms and should work with any standard C++ compiler.

%package -n lib%name-devel
Summary: Header files for LibSTK library
Group: Development/C++
Requires: lib%name = %version-%release
%description -n lib%name-devel
Header files for LibSTK library.

%package -n lib%name-devel-static
Summary: Static LibSTK library
Group: Development/C++
Obsoletes: lib%name-static

%description -n lib%name-devel-static
Static LibSTK library.

%package demo
Group: Sound
Summary:        Demo applications for %{name}
Requires:       libtk tk
Requires:       lib%{name} = %EVR
Provides: %{name} = %EVR
Conflicts: stk < 4.6.0
Obsoletes: stk < 4.6.0

%description demo
The %{name}-demo package contains the demo applications for the
C++ Sound Synthesis ToolKit.

%package doc
Summary: Documentation for the sound synthesis toolkit (STK)
Group: Documentation
BuildArch: noarch
%description doc
This package contains the documentation for the sound synthesis
toolkit. The documentation is developer oriented and covers all
you need to know if you want to develop an STK application.

%prep
%setup
%patch0 -p1
%patch1 -p1
%patch2 -p1

sed -i 's:../../rawwaves/:/usr/share/stk/rawwaves/:g' projects/demo/demo.cpp

%build
#export LIBS=(pkg-config --libs jack)
%autoreconf
%configure \
	--with-alsa \
	--with-jack \
	--enable-shared \
	%{subst_enable static} \
	RAWWAVE_PATH=%_datadir/stk/rawwaves/

%make_build
%make_build -C projects/demo libMd2Skini

%install
mkdir -p \
  %buildroot%_includedir/stk \
  %buildroot%_libdir \
  %buildroot%_bindir \
  %buildroot%_datadir/stk/rawwaves \
  %buildroot%_datadir/stk/demo \
  %buildroot%_datadir/stk/examples \
  %buildroot%_datadir/stk/effects \
  %buildroot%_datadir/stk/ragamatic \
  %buildroot%_datadir/stk/eguitar

cp -p include/* %buildroot%_includedir/stk
cp -pd src/libstk*.* %buildroot%_libdir
cp -p rawwaves/*.raw %buildroot%_datadir/stk/rawwaves

cp -pr projects/demo/tcl %buildroot%_datadir/stk/demo
cp -pr projects/demo/scores %buildroot%_datadir/stk/demo
cp -p projects/demo/stk-demo %buildroot%_bindir/stk-demo
cp -p projects/demo/Md2Skini %buildroot%_bindir/Md2Skini
for f in Banded Drums Modal Physical Shakers StkDemo Voice ; do
  chmod +x projects/demo/$f
  sed -e 's,\./demo,%_bindir/stk-demo,' -e '1i#! /bin/sh' \
    -i projects/demo/$f
  cp -p projects/demo/$f %buildroot%_datadir/stk/demo
done

cp -pr projects/examples/midifiles %buildroot%_datadir/stk/examples
cp -pr projects/examples/rawwaves %buildroot%_datadir/stk/examples
cp -pr projects/examples/scores %buildroot%_datadir/stk/examples
for f in sine sineosc foursine audioprobe midiprobe duplex play \
    record inetIn inetOut rtsine crtsine bethree controlbee \
    threebees playsmf grains ; do
  cp -p projects/examples/$f %buildroot%_bindir/stk-$f
  # absolute links, will be shortened later
  ln -s %buildroot%_bindir/stk-$f %buildroot%_datadir/stk/examples/$f
done

cp -pr projects/effects/tcl %buildroot%_datadir/stk/effects
cp -p projects/effects/effects %buildroot%_bindir/stk-effects
sed -e 's,\./effects,%_bindir/stk-effects,' -e '1i#! /bin/sh' \
  -i projects/effects/StkEffects
cp -p projects/effects/StkEffects %buildroot%_datadir/stk/effects

cp -pr projects/ragamatic/tcl %buildroot%_datadir/stk/ragamatic
cp -pr projects/ragamatic/rawwaves %buildroot%_datadir/stk/ragamatic
cp -p projects/ragamatic/ragamat %buildroot%_bindir/stk-ragamat
sed -e 's,\./ragamat,%_bindir/stk-ragamat,' -e '1i#! /bin/sh' \
  -i projects/ragamatic/Raga
cp -p projects/ragamatic/Raga %buildroot%_datadir/stk/ragamatic

cp -pr projects/eguitar/tcl %buildroot%_datadir/stk/eguitar
cp -pr projects/eguitar/scores %buildroot%_datadir/stk/eguitar
cp -p projects/eguitar/eguitar %buildroot%_bindir/stk-eguitar
sed -e 's,\./eguitar,%_bindir/stk-eguitar,' -e '1i#! /bin/sh' \
  -i projects/eguitar/ElectricGuitar
cp -p projects/eguitar/ElectricGuitar %buildroot%_datadir/stk/eguitar

# fix symlinks
symlinks -crv %buildroot

# fix encoding
iconv -f iso-8859-1 -t utf-8 doc/doxygen/index.txt \
  -o doc/doxygen/index.txt.tmp
mv doc/doxygen/index.txt.tmp doc/doxygen/index.txt

%files -n %name-demo
%_bindir/*
%_datadir/stk/*
%exclude %_datadir/stk/rawwaves

%files -n lib%name
%dir %_datadir/stk
%doc README*
%_libdir/libstk-*.so
%_datadir/stk/rawwaves

%files -n lib%name-devel
%_libdir/libstk.so
%_includedir/stk

%if_enabled static
%files -n lib%name-devel-static
%_libdir/*.a
%endif

%if_enabled htmldoc
%files doc
%doc doc/html
%doc doc/*.txt
%endif

%changelog
* Wed Oct 25 2023 Igor Vlasenko <viy@altlinux.org> 4.6.1-alt2
- fixed build (closes: #48158)

* Tue Oct 12 2021 Igor Vlasenko <viy@altlinux.org> 4.6.1-alt1
- new version

* Tue Jun  7 2016 Ivan Zakharyaschev <imz@altlinux.org> 4.5.0-alt1.1
- rebuild for new C++ ABI

* Fri Oct 03 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.5.0-alt1
- Version 4.5.0

* Sat Sep 14 2013 Slava Dubrovskiy <dubrsl@altlinux.org> 4.4.4-alt1
- New version (ALT#28756)

* Tue Apr 23 2013 Repocop Q. A. Robot <repocop@altlinux.org> 4.4.1-alt1.1.qa2
- NMU (by repocop). See http://www.altlinux.org/Tools/Repocop
- applied repocop fixes:
  * arch-dep-package-consists-of-usr-share for stk-doc

* Tue May 24 2011 Repocop Q. A. Robot <repocop@altlinux.org> 4.4.1-alt1.1.qa1
- NMU (by repocop). See http://www.altlinux.org/Tools/Repocop
- applied repocop fixes:
  * freedesktop-desktop-file-proposed-patch for stk
  * postclean-03-private-rpm-macros for the spec file

* Tue Nov 09 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.4.1-alt1.1
- Rebuilt for soname set-versions

* Mon Sep 28 2009 Slava Dubrovskiy <dubrsl@altlinux.org> 4.4.1-alt1
- New version
- Switch to git
- Update all patches

* Mon May 11 2009 Slava Dubrovskiy <dubrsl@altlinux.org> 4.3.1-alt3
- Add Patch14 for fix build with gcc4.4

* Mon Dec 15 2008 Slava Dubrovskiy <dubrsl@altlinux.org> 4.3.1-alt2
- Add patches from FC11
- Fixed repocop warnings in %name.desktop
- Remmove depricated update-menus and ldconfig call in post

* Fri Sep 12 2008 Slava Dubrovskiy <dubrsl@altlinux.org> 4.3.1-alt1
- New version

* Sat Mar 29 2008 Slava Dubrovskiy <dubrsl@altlinux.org> 4.3.0-alt3
- Rename lib%name-static -> lib%name-devel-static

* Fri Dec 07 2007 Slava Dubrovskiy <dubrsl@altlinux.org> 4.3.0-alt2
- Fix build in x86_64

* Wed Nov 21 2007 Slava Dubrovskiy <dubrsl@altlinux.org> 4.3.0-alt1
- Initial build
