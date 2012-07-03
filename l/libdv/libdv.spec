%def_enable shared
%def_enable static
%def_without debug

%def_enable asm
%def_enable sdl
%def_enable xv
%def_enable gtk
%def_with x
# YV12|YUY2
%define pal-yuv YUY2
#----------------------------------------------------------------------

Name: libdv
Version: 1.0.0
Release: alt5.5
Summary: DV software video codec
License: %lgpl2plus
Group: System/Libraries
URL: http://%name.sourceforge.net
Source: %name-%version.tar
Patch: %name-%version-%release.patch
%define popt_ver 1.7-alt5
Requires: libpopt >= %popt_ver
Packager: Led <led@altlinux.ru>

BuildRequires(pre): rpm-build-licenses
BuildRequires: libpopt-devel >= %popt_ver
%{?_enable_sdl:BuildRequires: libSDL-devel >= 1.1.6}
%{?_enable_xv:BuildRequires: libXv-devel libXext-devel xorg-xextproto-devel}
%{?_enable_gtk:BuildRequires: gtk+-devel > 1.2}
%{?_with_x:BuildRequires: libXt-devel xorg-cf-files}

%description
The Quasar DV codec (%name) is a software codec for DV video.  DV is
the encoding format used by most digital camcorders, typically those
that support the IEEE 1394 (aka FireWire or i.Link) interface. %name
was developed according to the official standards for DV video, IEC
61834 and SMPTE 314M.

%name package contains shared libraries you can use to run %name
applications.


%package devel
Summary: Development files from %name
Group: Development/C
Requires: %name%{?_disable_shared:-devel-static} = %version-%release
Requires: libpopt-devel >= %popt_ver

%description devel
The Quasar DV codec (%name) is a software codec for DV video. DV is the
encoding format used by most digital camcorders, typically those that
support the IEEE 1394 (aka FireWire or i.Link) interface. %name was
developed according to the official standards for DV video, IEC 61834
and SMPTE 314M.

This is the libraries, include files and other resources you can use
to incorporate %name into applications.


%if_enabled static
%package devel-static
Summary: Static %name libraries
Group: Development/C
%{?_enable_shared:Requires: %name-devel = %version-%release}

%description devel-static
The Quasar DV codec (%name) is a software codec for DV video. DV is the
encoding format used by most digital camcorders, typically those that
support the IEEE 1394 (aka FireWire or i.Link) interface. %name was
developed according to the official standards for DV video, IEC 61834
and SMPTE 314M.

This package contains static libraries you can use to build %name
applications.
%endif


%package utils
Summary: Binaries from %name
Group: Video
Requires: %name = %version-%release
Requires: libpopt >= %popt_ver

%description utils
The Quasar DV codec (%name) is a software codec for DV video. DV is the
encoding format used by most digital camcorders, typically those that
support the IEEE 1394 (aka FireWire or i.Link) interface. %name was
developed according to the official standards for DV video, IEC 61834
and SMPTE 314M.


%prep
%setup
%patch -p1


%build
%define _optlevel 3
%add_optflags %optflags_shared
%ifnarch %ix86 x86_64
%add_optflags -DBRUTE_FORCE_DCT_88 -DBRUTE_FORCE_DCT_248
%endif
%configure \
    %{subst_enable static} \
    %{subst_enable shared} \
    %{subst_with debug} \
%ifarch %ix86 x86_64
    %{subst_enable asm} \
%else
    --disable-asm \
%endif
    %{subst_enable sdl} \
    %{subst_enable gtk} \
    %{subst_enable xv} \
    %{subst_with x} \
    %{?pal_yuv:--with-pal-yuv=%pal_yuv}
sed -ri 's/^(hardcode_libdir_flag_spec|runpath_var)=.*/\1=/' libtool
%make_build
bzip2 --best --keep --force ChangeLog


%install
%makeinstall_std

%ifarch %ix86
%{?_enable_asm:%set_verify_elf_method textrel=relaxed}
%endif


%if_enabled shared
%files
%doc AUTHORS
%_libdir/*.so.*
%endif


%files devel
%doc ChangeLog.* TODO
%if_enabled shared
%_libdir/*.so
%else
%doc AUTHORS
%endif
%_includedir/*
%_pkgconfigdir/*


%if_enabled static
%files devel-static
%_libdir/*.a
%endif


%files utils
%doc README.*
%_bindir/*
%_man1dir/*


%changelog
* Sun Feb 26 2012 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.0.0-alt5.5
- built on arm

* Thu Dec 15 2011 Dmitry V. Levin <ldv@altlinux.org> 1.0.0-alt5.4
- Fixed RPATH issue.

* Mon Mar 21 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.0-alt5.3
- Rebuilt for debuginfo

* Wed Nov 03 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.0-alt5.2
- Rebuilt for soname set-versions

* Mon Jul 26 2010 Dmitry V. Levin <ldv@altlinux.org> 1.0.0-alt5.1
- Built for sisyphus.

* Sun Jul 18 2010 Led <led@altlinux.ru> 1.0.0-alt5
- updated BuildRequires

* Tue Dec 02 2008 Led <led@altlinux.ru> 1.0.0-alt4
- fixed License
- cleaned up spec
- cleaned up sources for x86_64

* Tue Dec 02 2008 Yuri N. Sedunov <aris@altlinux.org> 1.0.0-alt3
- updated buildreqs
- removed obsolete %%post{,un}_ldconfig

* Wed Feb 14 2007 Led <led@altlinux.ru> 1.0.0-alt2
- fixed License (#6688)
- cleaned up BuildPreReq

* Thu Oct 05 2006 Led <led@altlinux.ru> 1.0.0-alt1
- 1.0.0
- cleaned up spec

* Fri Jan 13 2006 LAKostis <lakostis at altlinux.ru> 0.104-alt1.1
- NMU;
- remove unwanted builddeps;
- s,kernel-headers-up,linux-libc-headers;
- PIC fixes to x86_64 code (from Mandriva).

* Tue Dec 14 2004 Yuri N. Sedunov <aris@altlinux.ru> 0.104-alt1
- 0.104

* Mon Jun 07 2004 Yuri N. Sedunov <aris@altlinux.ru> 0.102-alt1
- 0.102
- do not build devel-static subpackage by default.

* Fri Nov 28 2003 Yuri N. Sedunov <aris@altlinux.ru> 0.99-alt2
- use libtool-1.4.
- do not package .la files.
- use %%set_verify_elf_method textrel=relaxed, I can't fix asm code.

* Mon Apr 07 2003 Yuri N. Sedunov <aris@altlinux.ru> 0.99-alt1
- 0.99

* Wed Oct 16 2002 Yuri N. Sedunov <aris@altlinux.ru> 0.98-alt2
- Rebuild with gcc-3.2. 

* Tue Aug 20 2002 Yuri N. Sedunov <aris@altlinux.ru> 0.98-alt1.1
- 0.98
- (inger) update buildres (XFree86-static-libs)

* Fri May 03 2002 Yuri N. Sedunov <aris@altlinux.ru> 0.9.5-alt1
- First build for Sisyphus.
