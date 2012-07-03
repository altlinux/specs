%set_verify_elf_method textrel=relaxed

Name: libglide3
Version: 20050815
Release: alt2.1.1
Summary: Glide3 runtime for the 3Dfx Voodoo family of cards
Group: System/Libraries
License: GPL

Url: http://glide.sourceforge.net

# Create the Glide3 tarball by using:
#   cvs -d :pserver:anonymous@cvs.glide.sourceforge.net:/cvsroot/glide \
#     co -r glide-devel-branch Glide3
#   pushd Glide3 ; find . -name CVS -type d |xargs rm -rf
#   find . -name .cvsignore | xargs rm ; popd
#   tar jcf Glide3-$(date +"%%Y%%m%%d").tar.bz2 Glide3/
Source0: %name-%version.tar.bz2
Source1: glidelink.c

Packager: Repocop Q. A. Robot <repocop@altlinux.org>

BuildRequires: libX11-devel libXext-devel xorg-x11-proto-devel
BuildRequires: libXxf86dga-devel libXxf86vm-devel
BuildRequires: nasm

%description
Glide3 provides the necessary low-level interface glue between the Mesa
3D graphics library, and 3Dfx Voodoo series of hardware. This package is
required by the Xorg tdfx driver in order to provide 3D acceleration
support for the 3Dfx Voodoo 3 & 5. This package also contains support for
the Voodoo 2 & 1 in order to use the 3Dfx Voodoo 2 or 1 you need the
Glide3-libGL package or a native Glide3 application.

%package devel
Summary: Development libraries and headers for Glide3
Group: System/Libraries
Requires: libglide3 = %version-%release

%description devel
Glide3-devel contains the developmental files that must be installed in order
to compile native Glide3 applications.

%prep
%setup -q -n Glide3

%build
%ifarch %ix86
%define glide_flags USE_X86=1 USE_3DNOW=1 USE_MMX=1 USE_SSE=1 USE_SSE2=1 TEXUS2=1 DGA=1
%else
%define glide_flags TEXUS2=1
%endif

make -f makefile.linux FX_GLIDE_HW=h5 DRI=1 XPATH=/usr/X11R6/%_lib \
  OPTFLAGS="$RPM_OPT_FLAGS -Wno-unused-parameter" %glide_flags
mv h5/lib/libglide3.so libglide3-v5.so
make -f makefile.linux FX_GLIDE_HW=h5 realclean

make -f makefile.linux FX_GLIDE_HW=h3 DRI=1 XPATH=/usr/X11R6/%_lib \
  OPTFLAGS="$RPM_OPT_FLAGS -Wno-unused-parameter" %glide_flags
mv h3/lib/libglide3.so libglide3-v3.so
make -f makefile.linux FX_GLIDE_HW=h3 realclean

make -f makefile.linux FX_GLIDE_HW=cvg \
  OPTFLAGS="$RPM_OPT_FLAGS -Wno-unused-parameter" %glide_flags
mv cvg/lib/libglide3x.so libglide3-v2.so
make -f makefile.linux FX_GLIDE_HW=cvg realclean

#Sorry, no 64 bit support for Voodoo1 (yet)
%ifarch %ix86
make -f makefile.linux FX_GLIDE_HW=sst1 \
  OPTFLAGS="$RPM_OPT_FLAGS -Wno-unused-parameter" %glide_flags
mv sst1/lib/libglide3x.so libglide3-v1.so
make -f makefile.linux FX_GLIDE_HW=sst1 realclean
%endif

%install
%define libver 3.10.0
mkdir -p %buildroot/%_libdir
mkdir -p %buildroot/%_includedir/glide3

install -m 755 *.so %buildroot/%_libdir
# Point to v2 by default
ln -snf libglide3-v2.so %buildroot%_libdir/libglide3.so.%libver
ln -snf libglide3.so.%libver %buildroot%_libdir/libglide3.so.3
ln -snf libglide3.so.%libver %buildroot%_libdir/libglide3.so

install -p -m 644 swlibs/fxmisc/3dfx.h %buildroot/%_includedir/glide3
install -p -m 644 h5/glide3/src/g3ext.h %buildroot/%_includedir/glide3
install -p -m 644 h5/glide3/src/glide.h %buildroot/%_includedir/glide3
install -p -m 644 h5/glide3/src/glidesys.h %buildroot/%_includedir/glide3
install -p -m 644 h5/glide3/src/glideutl.h %buildroot/%_includedir/glide3
install -p -m 644 swlibs/fxmisc/linutil.h %buildroot/%_includedir/glide3
install -p -m 644 h5/incsrc/sst1vid.h %buildroot/%_includedir/glide3
install -p -m 644 swlibs/texus2/lib/texus.h %buildroot/%_includedir/glide3

%files
%doc COPYING
%_libdir/libglide3.so.3
%_libdir/libglide3.so.%libver
%ifarch %ix86
%_libdir/libglide3-v1.so
%endif
%_libdir/libglide3-v2.so
%_libdir/libglide3-v3.so
%_libdir/libglide3-v5.so

%files devel
%dir %_includedir/glide3
%_includedir/glide3/*
%_libdir/libglide3.so

%changelog
* Wed Nov 04 2009 Igor Vlasenko <viy@altlinux.ru> 20050815-alt2.1.1
- NMU (by repocop): the following fixes applied:
  * post_ldconfig for libglide3
  * postun_ldconfig for libglide3

* Tue Dec 02 2008 Valery Inozemtsev <shrek@altlinux.ru> 20050815-alt2.1
- NMU:
  * updated build dependencies

* Mon Aug 20 2007 Pavlov Konstantin <thresh@altlinux.ru> 20050815-alt2
- Don't BR anyasm, nasm is enough.

* Sun Feb 18 2007 Pavlov Konstantin <thresh@altlinux.ru> 20050815-alt1
- Built for Sisyphus, spec file based on fc one.

