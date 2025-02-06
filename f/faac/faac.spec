%define ABIVERSION 0

Name:          faac
Version:       1.30
Release:       alt1
Summary:       FAAC is a Freeware Advanced Audio Coder
License:       LGPL
Group:         Sound
Url:           https://sourceforge.net/projects/faac/
Vcs:           https://github.com/knik0/faac.git

Source:        %name-%version.tar
BuildRequires: gcc-c++
BuildRequires: libmp4v2-devel
BuildRequires: pkgconfig(sndfile)

%description
FAAC is an Advanced Audio Coder (MPEG2-AAC, MPEG4-AAC). The goal of FAAC is to
explore the possibilities of AAC and exceed the quality of the currently best
MP3 encoders.

%package       -n lib%name
Summary:       Freeware Advanced Audio Coder (FAAC) libraries
Group:         Development/Other

Obsoletes:     lib%{name}%ABIVERSION < %EVR
Provides:      lib%{name}%ABIVERSION = %EVR

%description   -n lib%name
This package contains Freeware Advanced Audio Coder (FAAC) shared
libraries.

FAAC is an Advanced Audio Coder (MPEG2-AAC, MPEG4-AAC). The goal of FAAC is to
explore the possibilities of AAC and exceed the quality of the currently best
MP3 encoders.

%package       -n lib%name-devel
Summary:       Development files for the FAAC AAC coder library
Group:         Development/C

Requires:      gcc-c++
Requires:      libmp4v2-devel
Requires:      pkgconfig(sndfile)

%description   -n lib%name-devel
This package provides header files development libraries and
documentation for lib%name.

FAAC is an Advanced Audio Coder (MPEG2-AAC, MPEG4-AAC). The goal of FAAC is to
explore the possibilities of AAC and exceed the quality of the currently best
MP3 encoders.

%prep
%setup

%build
%autoreconf
%configure \
	--with-mp4v2 \
	--disable-static

%make_build

%install
%makeinstall

%files
%doc docs/%name.html
%_bindir/*
%_man1dir/*

%files         -n lib%name
%doc ChangeLog NEWS README TODO
%_libdir/*.so.*

%files         -n lib%name-devel
%doc docs/lib%name.html
%_includedir/*
%_libdir/*.so

%changelog
* Thu Feb 06 2025 Pavel Skrylev <majioa@altlinux.org> 1.30-alt1
- * changed gear style
- ^ 1.28 -> 1.30

* Sun Aug 13 2017 Anton Midyukov <antohami@altlinux.org> 1.28-alt2
- Return building for ALT Sisyphus
- Build with libmp4v2-devel.

* Tue Jun 02 2009 Valery Inozemtsev <shrek@altlinux.ru> 1.28-alt1.2
- removed "--enable-drm" from configure (libdrm != Digital Radio Mondiale)

* Thu Mar 19 2009 Alexey Morsov <swi@altlinux.ru> 1.28-alt1.1
- add Obsoletes

* Wed Mar 18 2009 Alexey Morsov <swi@altlinux.ru> 1.28-alt1
- new version
- clean spec
- remove post/postun (repocop)
- add abiversion to lib package

* Mon Oct 15 2007 Alexey Morsov <swi@altlinux.ru> 1.26-alt1
- version 1.26 

* Thu Apr 05 2007 Alexey Morsov <swi@altlinux.ru> 1.25-alt3
- add patch for broken pipe
- patch configure.in a bit
- add patch for WAVEFORMATEXTENSIBLE structure
- fix spec for gear hasher build

* Thu Jan 11 2007 Alexey Morsov <swi@altlinux.ru> 1.25-alt2
- change maintainer

* Sat Aug 26 2006 Mikhail Zabaluev <mhz@altlinux.ru> 1.25-alt1
- Release 1.25
- Patch1: Remove -lstdc++ from libmpeg4ip-related linker flags
  add -lmp4v2 to frontend linker flags (bug 9821)
- Patch0 is obsolete

* Fri Jul 28 2006 Mikhail Zabaluev <mhz@altlinux.ru> 1.24-alt3
- Build with libmpeg4ip-devel for MP4 support (bug 9821)

* Fri Apr 21 2006 Mikhail Zabaluev <mhz@altlinux.ru> 1.24-alt2
- Patch0: Add -lm to libfaac link flags to resolve all symbols
- Cleaned up the build script

* Tue Jan 18 2005 Yuri N. Sedunov <aris@altlinux.ru> 1.24-alt1.1
- rebuild aganst new faad.

* Mon May 31 2004 Yuri N. Sedunov <aris@altlinux.ru> 1.24-alt1
- 1.24

* Sun Jan 25 2004 Yuri N. Sedunov <aris@altlinux.ru> 1.23.1-alt0.5
- First build for Sisyphus.
