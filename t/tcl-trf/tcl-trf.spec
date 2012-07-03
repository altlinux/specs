# -*- rpm-spec -*-
# $Id: tcl-trf,v 1.14 2006/07/21 22:24:51 me Exp $

%define snapshot 20060124
%define teaname trf
%define uver %nil

Name: tcl-%teaname
Version: 2.1
Release: alt7

Summary: A tcl extension called Tcl Data transformations
License: BSD
Group: Development/Tcl
Url: http://tcltrf.sourceforge.net/

%ifdef snapshot
Source: %name-%snapshot.tar.bz2
%else
Source: http://download.sourceforge.net/%teaname/%teaname%version%uver.tar.bz2
%endif

Patch0: %teaname-2.1p2-alt-sharedcompr.patch
Patch1: %teaname-2.1p2-alt-sharedcrypt.patch

Requires: tcl >= 8.4.0-alt1
BuildRequires: bzlib-devel zlib-devel libssl-devel tcl-devel >= 8.4.0-alt1 tcl-memchan rpm-build-tcl >= 0.2-alt1

%package devel
Summary: Header files and C programming manual for Trf
Group: Development/C
Requires: %name = %version-%release

%description
%name is a collection of data transformation:
- generation of message digests (hash values, checksums)
  MD2, MD5, SHA/SHS, SHA-1, HAVAL, RIPEMD-128, -160,
  CRC (polynomial used by PGP),  ADLER (based upon zlib)
- conversion from and to various data encodings:
  dual, octal, hexadecimal representation, uuencoding,
  base64-encoding, ASCII85-encoding
- a reed-solomon error correcting coder
- (de)compression based on zlib and bzlib

%description devel
%name is a collection of data transformation:
- generation of message digests (hash values, checksums)
  MD2, MD5, SHA/SHS, SHA-1, HAVAL, RIPEMD-128, -160,
  CRC (polynomial used by PGP),  ADLER (based upon zlib)
- conversion from and to various data encodings:
  dual, octal, hexadecimal representation, uuencoding,
  base64-encoding, ASCII85-encoding
- a reed-solomon error correcting coder
- (de)compression based on zlib and bzlib

This package includes header files for Trf.

%prep
%setup -q %{?snapshot:-c}%{!?snapshot:-n %teaname%version%uver}
%patch0 -p1
%patch1 -p1
%teapatch

%build
%__aclocal -I .
%__autoconf
%configure \
    --enable-shared-zlib \
    --enable-shared-bzlib
%make_build

%install
%makeinstall

%files
%doc ChangeLog README doc/license.terms
%_tcllibdir/libTrf%version.so
%_tcldatadir/Trf%version

%files devel
%_includedir/*
%_tcllibdir/libTrfstub2.1.a

%changelog
* Sat Jul 22 2006 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.1-alt7
- updated from CVS @20060124
- fixed build on x86_64

* Tue Jan 10 2006 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.1-alt6
- updated from CVS @ 20051006

* Wed Nov  3 2004 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.1-alt5
- rebuilt against new shiny reqprov finder

* Sat May 15 2004 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.1-alt4
- updated from CVS @ 200402018
- dynamically linked with zlib, bzlib, libcrypt instead of dlopen()

* Sat Mar  8 2003 Sergey Bolshakov <s.bolshakov@sam-solutions.net> 2.1-alt3
- bzlib bindings fixed

* Wed Sep 25 2002 Sergey Bolshakov <s.bolshakov@belcaf.com> 2.1-alt2
- rebuilt in new env

* Tue Aug  6 2002 Sergey Bolshakov <s.bolshakov@belcaf.com> 2.1-alt1
- first build for %distribution


