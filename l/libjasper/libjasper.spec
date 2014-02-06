Name: libjasper
Version: 1.900.1
Release: alt3

Summary: Implementation of the codec specified in the JPEG-2000 Part-1 standard
Summary(ru_RU.UTF8): Реализация кодеков по спецификации стандарта JPEG-2000, часть I

License: Modified BSD
Group: System/Libraries
Url: http://www.ece.uvic.ca/~mdadams/jasper/

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://www.ece.uvic.ca/~mdadams/jasper/software/jasper-%version.tar

Patch1: jasper-1.701.0-GL.patch
# autoconf/automake bits of patch1
Patch2: jasper-1.701.0-GL-ac.patch
# CVE-2007-2721 (bug #240397)
# borrowed from http://bugs.debian.org/cgi-bin/bugreport.cgi?bug=413041;msg=88
Patch3: patch-libjasper-stepsizes-overflow.patch
# borrowed from http://bugs.debian.org/cgi-bin/bugreport.cgi?bug=469786 
Patch4: jpc_dec.c.patch
# OpenBSD hardening patches addressing couple of possible integer overflows
# during the memory allocations
# https://bugzilla.redhat.com/show_bug.cgi?id=CVE-2008-3520
Patch5: jasper-1.900.1-CVE-2008-3520.patch
# https://bugzilla.redhat.com/show_bug.cgi?id=CVE-2008-3522
Patch6: jasper-1.900.1-CVE-2008-3522.patch
# add pkg-config support
Patch7: jasper-pkgconfig.patch

Patch8: jasper-1.900.1-CVE-2011-4516-CVE-2011-4517-CERT-VU-887409.patch

# Issues found by static analysis of code
Patch10: jasper-1.900.1-Coverity-BAD_SIZEOF.patch
Patch11: jasper-1.900.1-Coverity-CHECKED_RETURN.patch
Patch12: jasper-1.900.1-Coverity-FORWARD_NULL.patch
Patch13: jasper-1.900.1-Coverity-NULL_RETURNS.patch
Patch14: jasper-1.900.1-Coverity-RESOURCE_LEAK.patch
Patch15: jasper-1.900.1-Coverity-UNREACHABLE.patch
Patch16: jasper-1.900.1-Coverity-UNUSED_VALUE.patch

# jas_icc.c:744:2: warning: assuming signed overflow does not occur
# when assuming that (X + c) < X is always false [-Wstrict-overflow]
#
# comment from Red Hat Security Response Team:
# gcc inlines jas_iccattrtab_resize into jas_iccattrtab_add. Additionally, it
# essentially removes the "assert(maxents >= tab->numattrs);" assertion in
# jas_iccattrtab_resize, because it assumes that "maxents >= tab->numattrs" will
# always be true due to jas_iccattrtab_resize(attrtab, attrtab->numattrs + 32),
# especially the + 32. This assumption can only be true if it completely ignores
# the problem of signed integer overflows. I don't think it's a smart idea to
# accept that.
# -fno-strict-overflow forces gcc into keeping the assertion there.
%add_optflags -fno-strict-overflow


# Automatically added by buildreq on Wed Nov 18 2009
BuildRequires: gcc-c++ imake libGL-devel libXext-devel libXi-devel libXmu-devel libGLUT-devel libjpeg-devel

%description
JasPer is a collection
of software (i.e., a library and application programs) for the coding
and manipulation of images.  This software can handle image data in a
variety of formats.  One such format supported by JasPer is the JPEG-2000
format defined in ISO/IEC 15444-1:2000.

%package devel
Summary: Include Files and Documentation
Group: Development/C
Requires: %name = %version

%description devel
Libraries/include files for development with %name.

%package -n jasper
Summary: JasPer utilities
Group: Graphics
Requires: %name = %version

%description -n jasper
JasPer is a collection
of software (i.e., a library and application programs) for the coding
and manipulation of images.  This software can handle image data in a
variety of formats.  One such format supported by JasPer is the JPEG-2000
code stream format defined in ISO/IEC 15444-1:2000.

%prep
%setup -n jasper-%version
%patch1 -p1 -b .GL
%patch2 -p1 -b .GL-ac
%patch3 -p1 -b .CVE-2007-2721
%patch4 -p1 -b .jpc_dec_assertion
%patch5 -p1 -b .CVE-2008-3520
%patch6 -p1 -b .CVE-2008-3522
%patch7 -p1 -b .pkgconfig
%patch8 -p1 -b .CVE-2011-4516-4517

%patch10 -p1 -b .BAD_SIZEOF
%patch11 -p1 -b .CHECKED_RETURN
%patch12 -p1 -b .FORWARD_NULL
%patch13 -p1 -b .NULL_RETURNS
%patch14 -p1 -b .RESOURCE_LEAK
%patch15 -p1 -b .UNREACHABLE
%patch16 -p1 -b .UNUSED_VALUE

%autoreconf

%configure --enable-shared --disable-static

%build
%make_build

%install
%makeinstall_std

%check
make check

%files
%doc README LICENSE ChangeLog NEWS
%_libdir/lib*.so.*

%files -n jasper
%_bindir/*
%_man1dir/*

%files devel
# no API docs yet :(
# %doc doc/html/*

%_includedir/jasper/
%_libdir/libjasper.so
%_pkgconfigdir/jasper.pc
#%prefix/lib/lib*.a

%changelog
* Thu Feb 06 2014 Vitaly Lipatov <lav@altlinux.ru> 1.900.1-alt3
- add patches against multiple security vulnerabilities (ALT bug #29241)
- add pkg-config file
- thanks, Fedora!

* Wed Mar 09 2011 Igor Vlasenko <viy@altlinux.ru> 1.900.1-alt2.qa2
- rebuild for debuginfo

* Thu Nov 25 2010 Igor Vlasenko <viy@altlinux.ru> 1.900.1-alt2.qa1
- rebuild using girar-nmu to require/provide setversion 
  by request of mithraen@

* Wed Nov 18 2009 Vitaly Lipatov <lav@altlinux.ru> 1.900.1-alt2
- cleanup spec, update buildreqs, pack man pages

* Sat May 12 2007 Vitaly Lipatov <lav@altlinux.ru> 1.900.1-alt1
- new version 1.900.1 (with rpmrb script)

* Mon Dec 25 2006 Vitaly Lipatov <lav@altlinux.ru> 1.900.0-alt0.1
- new version 1.900.0 (with rpmrb script)
- pack include/jasper (fix bug 10510)
- update buildreq

* Tue Apr 26 2005 Vitaly Lipatov <lav@altlinux.ru> 1.701.0-alt2
- fix postun script (fix bug #6639)
- fix summary

* Sun Dec 26 2004 Vitaly Lipatov <lav@altlinux.ru> 1.701.0-alt1
- first build for ALT Linux Sisyphus

* Fri Oct 25 2002 Alexander D. Karaivanov <adk@medical-insight.com>
- spec file created
