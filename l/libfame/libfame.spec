Name: libfame
Version: 0.9.1
Release: alt5

Summary: library for fast MPEG video encoding
License: LGPL
Group: System/Libraries
Url: http://fame.sourceforge.net

Packager: Valery Inozemtsev <shrek@altlinux.ru>

Source: %name-%version.tar.gz

Patch0: libfame-0.9.1-alt-configure.patch
Patch1: libfame-0.9.1-mmx_sse.patch
Patch2: libfame-0.9.1-x86_64.patch
Patch3: libfame-ac_fixes.patch
Patch4: libfame-0.9.1-alt-soname.patch

%description
libFAME is a library for fast (real-time) MPEG video encoding, written
in C and assembly. libFAME currently allows encoding of fast MPEG-1 video,
as well as MPEG-4 (OpenDivX compatible) rectangular and arbitrary shaped video.

%package devel
Summary: Development files for libFAME
Group: Development/C
Requires: %name = %version-%release

%description devel
This package contains development files for libfame.

%ifarch %ix86
%def_enable sse
%def_enable mmx
%endif

%set_verify_elf_method textrel=relaxed

%prep
%setup -q

%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1

rm -f acinclude.m4

%build
%autoreconf
%configure \
	%{subst_enable sse} \
	%{subst_enable mmx} \
	--disable-static

%make_build

%install
%make DESTDIR=%buildroot install

%files
%doc AUTHORS BUGS CHANGES README TODO
%_libdir/*.so.*

%files devel
%_includedir/*
%_bindir/*
%_libdir/*.so
%_datadir/aclocal/*
%_man3dir/*

%if_enabled static
%files devel-static
%_libdir/*.a
%endif

%changelog
* Sat Nov 22 2008 Valery Inozemtsev <shrek@altlinux.ru> 0.9.1-alt5
- removed obsolete %%post_ldconfig/%%postun_ldconfig calls

* Mon Oct 27 2008 Valery Inozemtsev <shrek@altlinux.ru> 0.9.1-alt4
- libfame-config: fixed --libs (close #15158)

* Tue Mar 11 2008 Valery Inozemtsev <shrek@altlinux.ru> 0.9.1-alt3
- enabled SSE for %%ix86

* Wed Feb 07 2007 Valery Inozemtsev <shrek@altlinux.ru> 0.9.1-alt2
- fixed linking on x86_64

* Wed Feb 07 2007 Valery Inozemtsev <shrek@altlinux.ru> 0.9.1-alt1
- update to 0.9.1
- added %name-0.9.1-mmx_sse.patch for enabling build with MMX and SSE optimization
- added %name-0.9.1-x86_64.patch

* Mon May 29 2006 Valery Inozemtsev <shrek@altlinux.ru> 0.9.0-alt4
- disabled MMX

* Wed Dec 17 2003 Yuri N. Sedunov <aris@altlinux.ru> 0.9.0-alt3
- do not package .la files.
- do not build devel-static subpackage by default.
- use %%set_verify_elf_method textrel=relaxed, I can't fix asm code.

* Sun Oct 13 2002 Yuri N. Sedunov <aris@altlinux.ru> 0.9.0-alt2
- Rebuild with gcc-3.2

* Fri May 31 2002 Yuri N. Sedunov <aris@altlinux.ru> 0.9.0-alt1
- 0.9.0

* Thu May 16 2002 Yuri N. Sedunov <aris@altlinux.ru> 0.8.10-alt1
- First build for Sisyphus.

