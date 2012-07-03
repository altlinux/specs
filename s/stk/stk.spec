Name: stk
Version: 4.4.1
Release: alt1.1.qa1
License: GPL
Group: Sound
Summary: C++ classes for audio digital signal processing
Packager: Slava Dubrovskiy <dubrsl@altlinux.ru>
Url: http://www-ccrma.stanford.edu/software/stk/
Source: stk-%version.tar
Patch: %name-%version-%release.patch

Requires: lib%name = %version-%release

# Automatically added by buildreq on Thu Nov 22 2007
BuildRequires: gcc-c++ jackit-devel libalsa-devel util-linux-ng
BuildRequires: desktop-file-utils

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

%package doc
Summary: Documentation for the sound synthesis toolkit (STK)
Group: Documentation
%description doc
This package contains the documentation for the sound synthesis
toolkit. The documentation is developer oriented and covers all
you need to know if you want to develop an STK application.

%prep
%setup -q
%patch -p1

sed -i "s|/usr/lib|%_libdir|g" src/Makefile.in

%build
%configure --with-alsa \
	--with-oss \
	--with-jack \
	RAWWAVE_PATH=%_datadir/stk/rawwaves/
				       

%make

%install

%make -C src DESTDIR=%buildroot install

# there is no install target, so just install by hand
mkdir -p %buildroot%_bindir
mkdir -p %buildroot%_man1dir
mkdir -p %buildroot%_includedir/stk
mkdir -p %buildroot%_datadir/stk/
mkdir -p %buildroot%_datadir/stk/rawwaves

install -m 755 projects/demo/demo %buildroot%_bindir/stk-demo
install -m 755  STKDemo %buildroot%_bindir/STKDemo
install -m 644 rawwaves/*.raw %buildroot%_datadir/stk/rawwaves
cp -fR projects/demo/tcl %buildroot%_datadir/stk/
cp -fR stk-demo.1 %buildroot%_man1dir/

# menu
mkdir -p %buildroot%_desktopdir
cat << EOF > %buildroot%_desktopdir/%name.desktop
[Desktop Entry]
Name=STK (Demo)
GenericName=Synthesis ToolKit
Comment=Synthesis ToolKit
TryExec=STKDemo
Exec=STKDemo
Terminal=false
StartupNotify=true
Type=Application
Categories=AudioVideo,Sequencer;
EOF
desktop-file-install --dir %buildroot%_desktopdir \
	--remove-category=AudioVideo,Sequencer \
	--add-category=AudioVideo \
	--add-category=Sequencer \
	--add-category=Audio \
	%buildroot%_desktopdir/stk.desktop


%files
%_bindir/*
%_datadir/stk/*
%_man1dir/*
%_desktopdir/*

%exclude %_datadir/stk/rawwaves

%files -n lib%name
%dir %_datadir/stk
%doc README 
%_libdir/*.so.*
%_datadir/stk/rawwaves

%files -n lib%name-devel
%_libdir/*.so
%_includedir/stk

%files -n lib%name-devel-static
%_libdir/*.a

%files doc
%doc doc/html doc/*.txt

%changelog
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
