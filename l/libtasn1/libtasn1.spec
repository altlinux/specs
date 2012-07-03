Name: libtasn1
Version: 2.12
Release: alt1

Summary: The ASN.1 library used in GNUTLS
Group: System/Libraries
License: LGPLv2+
URL: http://www.gnu.org/software/gnutls/
# ftp://ftp.gnu.org/gnu/%name/%name-%version.tar.gz
Source: %name-%version.tar

# due to gtkdocize
BuildRequires: gtk-doc

%description
Libtasn1 is the ASN.1 library used in GNUTLS for ASN.1
(Abstract Syntax Notation One) structures management and DER
(Distinguished Encoding Rules) encoding functions.

This package contains libtasn1 runtime library.

%package devel
Summary: Files for development of libtasn1-based applications
Group: Development/C
License: LGPLv2+
Requires: %name = %version-%release

%description devel
Libtasn1 is the ASN.1 library used in GNUTLS for ASN.1
(Abstract Syntax Notation One) structures management and DER
(Distinguished Encoding Rules) encoding functions.

This package contains files for development of applications
which will use libtasn1.

%package utils
Summary: ASN.1 development utilities
Group: Development/Other
License: GPLv3+
Requires: %name = %version-%release

%description utils
Libtasn1 is the ASN.1 library used in GNUTLS for ASN.1
(Abstract Syntax Notation One) structures management and DER
(Distinguished Encoding Rules) encoding functions.

This package contains libtasn1 development utilities.

%package devel-doc
Summary: Development documentation for %name
Group: Development/C
License: LGPLv2+
Conflicts: %name-devel < %version
BuildArch: noarch

%description devel-doc
Libtasn1 is the ASN.1 library used in GNUTLS for ASN.1
(Abstract Syntax Notation One) structures management and DER
(Distinguished Encoding Rules) encoding functions.

This package contains libtasn1 development documentation.

%prep
%setup

%build
%autoreconf
%def_disable static
%configure --disable-static --disable-silent-rules
%make_build

%install
%makeinstall_std

%define docdir %_docdir/%name-%version
mkdir -p %buildroot%docdir/reference/html
install -pm644 doc/*.html doc/*.pdf %buildroot%docdir/
install -pm644 AUTHORS NEWS README THANKS %buildroot%docdir/
ln -s %_licensedir/LGPL-2.1 %buildroot%docdir/COPYING.LIB
install -pm644 doc/reference/*.pdf %buildroot%docdir/reference/
install -pm644 doc/reference/html/* %buildroot%docdir/reference/html/

%set_verify_elf_method strict
%define _unpackaged_files_terminate_build 1

%check
%make_build -k check

%files
%_libdir/*.so.*
%dir %docdir
%docdir/[ACNRT]*

%files utils
%_bindir/asn1*
%_man1dir/*

%files devel
%_libdir/*.so
%_includedir/*
%_pkgconfigdir/*

%files devel-doc
%_infodir/*
%_man3dir/*
%dir %docdir
%docdir/*.html
%docdir/*.pdf
%docdir/reference/

%changelog
* Fri Mar 23 2012 Dmitry V. Levin <ldv@altlinux.org> 2.12-alt1
- Updated to 2.12 (fixes CVE-2012-1569).

* Thu Dec 08 2011 Dmitry V. Levin <ldv@altlinux.org> 2.11-alt1
- Updated to 2.11.
- Rewritten specfile.

* Fri Mar 04 2011 Alexey Tourbin <at@altlinux.ru> 2.9-alt2
- rebuilt for pkgconfig
- made libtasn1-devel-doc noarch

* Sun Dec 19 2010 Afanasov Dmitry <ender@altlinux.org> 2.9-alt1
- 2.9

* Tue Oct 19 2010 Afanasov Dmitry <ender@altlinux.org> 2.8-alt1
- 2.8

* Fri Nov 06 2009 Afanasov Dmitry <ender@altlinux.org> 2.3-alt1
- 2.3

* Fri May 22 2009 Afanasov Dmitry <ender@altlinux.org> 2.2-alt1
- 2.2
- remove %%install_info's invocations

* Fri Apr 17 2009 Afanasov Dmitry <ender@altlinux.org> 2.1-alt1
- 2.1
- minor changes:
  + Fix compilation failure

* Tue Apr 14 2009 Afanasov Dmitry <ender@altlinux.org> 2.0-alt1
- 2.0
  + The libtasn1-config tool has been removed (see NEWS for details)

* Mon Jan 26 2009 Afanasov Dmitry <ender@altlinux.org> 1.8-alt1
- 1.8

* Tue Dec 02 2008 Afanasov Dmitry <ender@altlinux.org> 1.7-alt2
- change packager.
- merge shaba@ updates.
- remove libtasn1.m4. it was removed in v1.6 and using pkg-config was
  offered (see NEWS for details)

* Wed Nov 26 2008 Alexey Shabalin <shaba@altlinux.ru> 1.7-alt1
- 1.7
- remove ldconfig from %%post

* Mon Oct 27 2008 Pavlov Konstantin <thresh@altlinux.ru> 1.5-alt1
- 1.5 release.

* Fri Sep 21 2007 Pavlov Konstantin <thresh@altlinux.ru> 1.1-alt1
- 1.1 release.

* Tue May 29 2007 Pavlov Konstantin <thresh@altlinux.ru> 0.3.10-alt1
- 0.3.10 release.

* Tue Apr 10 2007 Pavlov Konstantin <thresh@altlinux.ru> 0.3.9-alt1
- 0.3.9 release.

* Sat Jan 27 2007 Pavlov Konstantin <thresh@altlinux.ru> 0.3.8-alt1
- 0.3.8 release.
- Minor spec cleanup.
- Fixed BuildRequires.
- Hacked the configure.in to use autoconf 2.59.
- Added onceonly.m4 file to source tree to be able to use macros
  appeared in autoconf 2.60.

* Sat Sep 02 2006 Mikhail Zabaluev <mhz@altlinux.ru> 0.3.6-alt1
- Updated to 0.3.6

* Tue May 30 2006 Mikhail Zabaluev <mhz@altlinux.ru> 0.3.4-alt1
- Updated to 0.3.4
- Added libtasn1-utils package
- Buildreq

* Sat Feb 11 2006 Mikhail Zabaluev <mhz@altlinux.ru> 0.2.18-alt1
- 0.2.18, fixes SA18794

* Tue Nov 29 2005 Mikhail Zabaluev <mhz@altlinux.ru> 0.2.17-alt1
- Updated to 0.2.17
- Moved documentation to the devel-doc subpackage

* Sun Aug 14 2005 Mikhail Zabaluev <mhz@altlinux.ru> 0.2.15-alt1
- Updated to 0.2.15

* Mon Jan 03 2005 Mikhail Zabaluev <mhz@altlinux.ru> 0.2.13-alt1
- Updated to 0.2.13
- Serialized make

* Tue May 25 2004 Mikhail Zabaluev <mhz@altlinux.ru> 0.2.10-alt1
- Updated to 0.2.10
- Added configure scripts to the file list

* Sat Mar 06 2004 Mikhail Zabaluev <mhz@altlinux.ru> 0.2.7-alt1
- New upstream release

* Fri Jan 02 2004 Mikhail Zabaluev <mhz@altlinux.ru> 0.2.6-alt1
- Initial release for Sisyphus
