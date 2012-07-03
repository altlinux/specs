#%define doc_dir %_defaultdocdir/%name-%version

Name: twolame
Version: 0.3.12
Release: alt2

Summary: TwoLAME, an optimized MPEG Audio Layer 2 encoder
License: LGPL
Group: Sound
Url: http://%name.sourceforge.net/
Packager: Pavlov Konstantin <thresh@altlinux.ru>

Source: http://prdownloads.sourceforge.net/twolame/%name-%version.tar.gz

Requires: lib%name = %version-%release

BuildRequires: gcc-c++ libsndfile-devel

%description
TwoLAME is an optimized MPEG Audio Layer 2 (MP2) encoder.
It is based heavily on:

- tooLAME by Michael Cheng
- the ISO dist10 code
- improvement to algorithms as part of the LAME project (lame.sf.net)
- other contributors (see AUTHORS)

TwoLAME should be able to be used as a drop-in replacement for
LAME (a MPEG Layer 3 encoder). The frontend takes very similar
command line options to LAME, and the backend library has a very
similar API to LAME.

%package -n lib%name
Summary: TwoLAME shared library
Group: System/Libraries

%description -n lib%name
This package contains shared library required by %name-based software.

%package -n lib%name-devel
Summary: TwoLAME development file
Group: Development/C
Requires: lib%name = %version-%release

%description -n lib%name-devel
This package contains header files required to develop
%name-based software.

%package -n lib%name-devel-static
Summary: TwoLAME static libraries
Group: Development/C
Requires: lib%name-devel = %version-%release

%description -n lib%name-devel-static
This package contains static library required to develop
%name-based software.

%def_disable static

%prep
%setup -q

%build
%__autoreconf
%configure \
	%{subst_enable static}

%make_build

%install
%make_install DESTDIR="%buildroot" install

install -pD -m644 AUTHORS README ChangeLog TODO %buildroot%_docdir/%name-%version/

ln -sf /usr/share/license/LGPL-2.1 %buildroot%_docdir/%name-%version/COPYING

%files
%_bindir/%name
%_man1dir/*
%exclude %_docdir/%name-%version/html
%_docdir/%name-%version

%files -n lib%name
%_libdir/lib%name.so.*

%files -n lib%name-devel
%_includedir/%name.h
%_libdir/lib%name.so
%_pkgconfigdir/%name.pc
%_docdir/%name-%version/html

%if_enabled static
%files -n lib%name-devel-static
%_libdir/lib%name.a
%endif

%changelog
* Mon Nov 01 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.12-alt2
- Rebuilt for soname set-versions

* Mon Nov 02 2009 Igor Vlasenko <viy@altlinux.ru> 0.3.12-alt1.1
- NMU (by repocop): the following fixes applied:
  * post_ldconfig for libtwolame
  * postun_ldconfig for libtwolame

* Thu Aug 14 2008 Pavlov Konstantin <thresh@altlinux.ru> 0.3.12-alt1
- 0.3.12 release.

* Mon Apr 23 2007 Pavlov Konstantin <thresh@altlinux.ru> 0.3.10-alt1
- 0.3.10 release.
- Untarred source tree and merged patch to it.

* Sat Jan 06 2007 Pavlov Konstantin <thresh@altlinux.ru> 0.3.9-alt1
- 0.3.9 release.

* Mon Aug 07 2006 Pavlov Konstantin <thresh@altlinux.ru> 0.3.8-alt1
- Initial build for ALTLinux.

