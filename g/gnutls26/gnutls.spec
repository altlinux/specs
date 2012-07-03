Name: gnutls26
Version: 2.12.18
Release: alt1

Summary: A TLS protocol implementation
# The libgnutls library is LGPLv2+, utilities and remaining libraries are GPLv3+
License: LGPLv2+ and GPLv3+
Group: System/Libraries
Url: http://www.gnu.org/software/gnutls/
# ftp://ftp.gnutls.org/pub/gnutls/gnutls-%version.tar.bz2
Source: gnutls-%version.tar
Patch: gnutls-2.12.14-rh-tests.patch

%define libcxx libgnutlsxx27
%define libssl libgnutls27-openssl
%def_disable guile
%def_with lzo

# Automatically added by buildreq on Thu Dec 08 2011
BuildRequires: gcc-c++ gtk-doc libgcrypt-devel libp11-kit-devel libreadline-devel libtasn1-devel zlib-devel
%if_with guile
BuildRequires: guile-devel
%endif
%if_with lzo
BuildRequires: liblzo2-devel 
%endif

%description
GnuTLS is a project that aims to develop a library which provides a
secure  layer, over a reliable transport layer.  Currently the GnuTLS
library implements the proposed standards by the IETF's TLS working
group.

%package -n lib%name
Summary: Transport Layer Security library
License: LGPLv2+
Group: System/Libraries
Provides: libgnutls = %version
Obsoletes: libgnutls < %version
Obsoletes: libgnutls-new < %version

%description -n lib%name
GnuTLS is a project that aims to develop a library which provides a
secure  layer, over a reliable transport layer.  Currently the GnuTLS
library implements the proposed standards by the IETF's TLS working
group.

This package contains the GnuTLS runtime library.

%package -n libgnutls-devel
Summary: Development files for lib%name
Group: Development/C
Requires: lib%name = %version-%release
Provides: libgnutls-devel = %version
Obsoletes: libgnutls-new-devel < %version

%description -n libgnutls-devel
GnuTLS is a project that aims to develop a library which provides a
secure  layer, over a reliable transport layer.  Currently the GnuTLS
library implements the proposed standards by the IETF's TLS working
group.

This package contains headers and other development files required to
build GnuTLS-based software.

%package -n %libcxx
Summary: Transport Layer Security C++ library
Group: System/Libraries
License: GPLv3+
Requires: lib%name = %version-%release
Provides: libgnutlsxx = %version
Obsoletes: libgnutlsxx < %version
Obsoletes: libgnutls-newxx < %version

%description -n %libcxx
GnuTLS is a project that aims to develop a library which provides a
secure  layer, over a reliable transport layer.  Currently the GnuTLS
library implements the proposed standards by the IETF's TLS working
group.

This package contains the GnuTLS C++ runtime library.

%package -n libgnutlsxx-devel
Summary: Development files for libgnutlsxx
Group: Development/C++
Requires: %libcxx = %version-%release
Requires: libgnutls-devel = %version-%release
Obsoletes: libgnutls-newxx-devel < %version

%description -n libgnutlsxx-devel
GnuTLS is a project that aims to develop a library which provides a
secure  layer, over a reliable transport layer.  Currently the GnuTLS
library implements the proposed standards by the IETF's TLS working
group.

This package contains headers and other development files required to
build GnuTLS-based software using C++.

%package -n lib%name-extra
Summary: Transport Layer Security library, extra functions
Group: System/Libraries
Requires: lib%name = %version-%release
Provides: libgnutls-extra = %version
Obsoletes: libgnutls-extra < %version
Obsoletes: libgnutls-new-extra < %version

%description -n lib%name-extra
GnuTLS is a project that aims to develop a library which provides a
secure  layer, over a reliable transport layer.  Currently the GnuTLS
library implements the proposed standards by the IETF's TLS working
group.

This package contains the GnuTLS runtime library with extra functions.

%package -n libgnutls-extra-devel
Summary: Development files for lib%name-extra
Group: Development/C
Requires: lib%name-extra = %version-%release
Requires: libgnutls-devel = %version-%release
Obsoletes: libgnutls-new-extra-devel < %version

%description -n libgnutls-extra-devel
GnuTLS is a project that aims to develop a library which provides a
secure  layer, over a reliable transport layer.  Currently the GnuTLS
library implements the proposed standards by the IETF's TLS working
group.

This package contains headers and other development files required to
build applications using the GnuTLS extra library.

%package -n %libssl
Summary: OpenSSL compatibility layer for the GnuTLS library
Group: System/Libraries
Requires: lib%name = %version-%release
Provides: libgnutls-openssl = %version
Obsoletes: libgnutls-openssl < %version
Obsoletes: libgnutls-new-openssl < %version

%description -n %libssl
GnuTLS is a project that aims to develop a library which provides a
secure  layer, over a reliable transport layer.  Currently the GnuTLS
library implements the proposed standards by the IETF's TLS working
group.

This package contains the GnuTLS runtime OpenSSL compatibility library.

%package -n libgnutls-openssl-devel
Summary: Development files for %libssl
Group: Development/C
Requires: %libssl = %version-%release
Requires: libgnutls-devel = %version-%release
Obsoletes: libgnutls-new-openssl-devel < %version

%description -n libgnutls-openssl-devel
GnuTLS is a project that aims to develop a library which provides a
secure  layer, over a reliable transport layer.  Currently the GnuTLS
library implements the proposed standards by the IETF's TLS working
group.

This package contains headers and other development files required to
build applications using the GnuTLS compatibility OpenSSL library.

%package utils
Summary: TLS protocol utilities
Group: Security/Networking
Requires: lib%name-extra = %version-%release
Provides: gnutls-utils = %version
Obsoletes: gnutls-utils < %version

%description utils
GnuTLS is a project that aims to develop a library which provides a
secure  layer, over a reliable transport layer.  Currently the GnuTLS
library implements the proposed standards by the IETF's TLS working
group.

This package contains command line TLS client and server, and
certificate manipulation tools.

%package -n libgnutls-guile
Summary: GnuTLS Guile bindings
Group: Development/Other
Requires: lib%name = %version-%release
Obsoletes: libgnutls-new-guile < %version

%description -n libgnutls-guile
GnuTLS is a project that aims to develop a library which provides a
secure  layer, over a reliable transport layer.  Currently the GnuTLS
library implements the proposed standards by the IETF's TLS working
group.

This package contains Guile bindings for the library.

%package devel-doc
Summary: Development documentation for GnuTLS
Group: Development/C
Conflicts: libgnutls-devel < %version
Provides: gnutls-devel-doc = %version
Obsoletes: gnutls-devel-doc < %version
Obsoletes: gnutls-new-devel-doc < %version
BuildArch: noarch

%description devel-doc
GnuTLS is a project that aims to develop a library which provides a
secure  layer, over a reliable transport layer.  Currently the GnuTLS
library implements the proposed standards by the IETF's TLS working
group.

This package contains the GnuTLS API Reference Manual.

%prep
%setup -n gnutls-%version
%patch -p1

%build
%autoreconf
%def_disable static
%configure \
	--disable-rpath \
	--disable-static \
	--disable-silent-rules \
	--with-libgcrypt \
	%{subst_enable guile} \
	%{subst_with lzo}
%make_build

%install
%makeinstall_std
find %buildroot%_infodir/ -name '*.png' -delete -print
%define docdir %_docdir/gnutls-%version
mkdir -p %buildroot%docdir/{examples,reference}
install -p -m644 AUTHORS NEWS README THANKS %buildroot%docdir/
install -p -m644 doc/*.{cfg,css,html,png} %buildroot%docdir/
install -pm644 doc/examples/*.[hc]* %buildroot%docdir/examples/
install -pm644 doc/reference/html/* %buildroot%docdir/reference/
ln -s %_licensedir/GPL-2 %buildroot%docdir/COPYING
ln -s %_licensedir/LGPL-2.1 %buildroot%docdir/COPYING.LIB

%find_lang libgnutls
%set_verify_elf_method strict
%define _unpackaged_files_terminate_build 1

%check
%make_build -k check

%files -n lib%name -f libgnutls.lang
%dir %docdir
%docdir/[ACNRT]*
%_libdir/libgnutls.so.*

%files -n %libcxx
%_libdir/libgnutlsxx.so.*

%files -n lib%name-extra
%_libdir/libgnutls-extra.so.*

%files -n %libssl
%_libdir/libgnutls-openssl.so.*

%files -n libgnutls-devel
%_includedir/gnutls/
%exclude %_includedir/gnutls/gnutlsxx.h
%exclude %_includedir/gnutls/extra.h
%exclude %_includedir/gnutls/openssl.h
%_libdir/libgnutls.so
%_pkgconfigdir/gnutls.pc

%files -n libgnutlsxx-devel
%dir %_includedir/gnutls/
%_includedir/gnutls/gnutlsxx.h
%_libdir/libgnutlsxx.so

%files -n libgnutls-extra-devel
%dir %_includedir/gnutls/
%_includedir/gnutls/extra.h
%_libdir/libgnutls-extra.so
%_pkgconfigdir/gnutls-extra.pc

%files -n libgnutls-openssl-devel
%dir %_includedir/gnutls/
%_includedir/gnutls/openssl.h
%_libdir/libgnutls-openssl.so

%files devel-doc
%dir %docdir
%docdir/*.css
%docdir/*.html
%docdir/*.png
%docdir/examples/
%docdir/reference/
%_man3dir/*
%_infodir/*

%files utils
%_bindir/*
%_man1dir/*
%dir %docdir
%docdir/*.cfg

%if_with guile
# %%_datadir/guile belongs to guile package
# %%_datadir/guile/site may contain not only gnutls guile files.
# therefore %%_datadir/guile and %%_datadir/guile/site are not packaged. 
# is there some package using 'site' directory?
%files -n libgnutls-guile
%_libdir/libguile*
%_datadir/guile/site/gnutls
%_datadir/guile/site/gnutls.scm
%endif

%changelog
* Fri Mar 23 2012 Dmitry V. Levin <ldv@altlinux.org> 2.12.18-alt1
- Updated to 2.12.18.

* Thu Dec 08 2011 Dmitry V. Levin <ldv@altlinux.org> 2.12.14-alt1
- Updated to 2.12.14.
- Rewritten specfile.

* Fri Aug 05 2011 Dmitry V. Levin <ldv@altlinux.org> 2.10.5-alt1
- Updated to gnutls_2_10_5-4-g4eeba9b.
- Backported upstream fix for incorrect calls to libgcrypt.

* Fri Mar 04 2011 Alexey Tourbin <at@altlinux.ru> 2.10.4-alt3
- rebuilt for debuginfo
- updated dependencies
- made gnutls26-devel-doc noarch

* Tue Dec 21 2010 Afanasov Dmitry <ender@altlinux.org> 2.10.4-alt2
- build with internal libopencdk.

* Sun Dec 19 2010 Afanasov Dmitry <ender@altlinux.org> 2.10.4-alt1
- 2.10.4 release.

* Tue Oct 19 2010 Afanasov Dmitry <ender@altlinux.org> 2.10.2-alt1
- 2.10.2 release.

* Tue Jun 29 2010 Afanasov Dmitry <ender@altlinux.org> 2.10.0-alt1
- 2.10.0

* Tue Mar 23 2010 Afanasov Dmitry <ender@altlinux.org> 2.8.6-alt1
- 2.8.6 release.

* Tue Nov 17 2009 Afanasov Dmitry <ender@altlinux.org> 2.8.5-alt1
- 2.8.3 release.
- remove deb-fixtimebomb patch (fixed by upstream)

* Fri Nov 06 2009 Afanasov Dmitry <ender@altlinux.org> 2.8.3-alt2
- add deb-fixtimebomb patch that fixes check with expired certificate

* Fri Aug 28 2009 Afanasov Dmitry <ender@altlinux.org> 2.8.3-alt1
- 2.8.3 release.
  + Fix MinGW cross-compiling build error.
  + Fix problem with NUL bytes in X.509 CN and SAN fields.
  + Fix off-by-one size computation error in unknown DN printing.
  + Fix rare failure in gnutls_x509_crt_import.

* Thu Jun 11 2009 Afanasov Dmitry <ender@altlinux.org> 2.8.1-alt1
- 2.8.1 release.
  + Fix crash in gnutls_global_init after earlier init/deinit cycle.
  + Fix PKCS#12 decryption from password.

* Sun May 31 2009 Afanasov Dmitry <ender@altlinux.org> 2.8.0-alt1
- 2.8.0 release.
  + API/ABI changes in GnuTLS 2.8 compared to GnuTLS 2.6.x: The library
    should be completely backwards compatible on both the source and
    binary level.
  + Old libgnutls.m4 and libgnutls-config scripts removed. Please use
    pkg-config instead.
  + use 'libgnutls' as gettext domain
- patch: remove soversion from gettext domain, use offered domain
  (libgnutls) instead.
- don't install pictures in info dorectory
- remove obsolete install_info's invocations

* Mon May 25 2009 Afanasov Dmitry <ender@altlinux.org> 2.6.6-alt2
- %%set_verify_info_method relaxed until info-install filetringger will accept
  pictures used by gnutls in info files.

* Thu Apr 30 2009 Afanasov Dmitry <ender@altlinux.org> 2.6.6-alt1
- 2.6.6 release. 
  + fix Corrected double free on signature verification failure (CVE-2009-1415)
  + fix DSA key generation (CVE-2009-1416)
  + fix gnutls-cli expiration/activation time check (CVE-2009-1417)
- release fixes #19873 also.

* Tue Apr 14 2009 Afanasov Dmitry <ender@altlinux.org> 2.6.5-alt1.1
- build against libtasn1-2.0-alt1.

* Mon Apr 13 2009 Afanasov Dmitry <ender@altlinux.org> 2.6.5-alt1
- 2.6.5 release.
  + GnuTLS no longer uses the libtasn1-config (see NEWS)
- enable lzo by default

* Mon Feb 09 2009 Afanasov Dmitry <ender@altlinux.org> 2.6.4-alt1
- 2.6.4 release. 

* Tue Jan 27 2009 Afanasov Dmitry <ender@altlinux.org> 2.6.3-alt2
- change libgcrypt dependancy (Closes: #18654)

* Sun Dec 21 2008 Afanasov Dmitry <ender@altlinux.org> 2.6.3-alt1
- 2.6.3 release (see NEW for details)
  + Fix chain verification for chains that ends with RSA-MD2 CAs (CVE-2008-4989)
  + Fix memory leak in PSK authentication.
  + gnutls-cli minor updates
- return macroses that updates info's (fix repocop warnings)

* Tue Dec 02 2008 Afanasov Dmitry <ender@altlinux.org> 2.6.2-alt2
- fix unmet with devel packages.

* Wed Nov 26 2008 Afanasov Dmitry <ender@altlinux.org> 2.6.2-alt1
- 2.6.2 release.
- append soname to gettext files (fix conflict with gnutls that 
  has another soname).

* Sat Nov 08 2008 Afanasov Dmitry <ender@altlinux.org> 2.6.0-alt1
- 2.6.0 release.
- update buildreq.
- add support for lzo, guile controlled by --with/--without options.
  disable by default.
- remove obsolete %%post/%%pre actions.

* Fri Jul 11 2008 Pavlov Konstantin <thresh@altlinux.ru> 2.4.1-alt1
- 2.4.1 release.

* Thu Mar 13 2008 Pavlov Konstantin <thresh@altlinux.ru> 2.2.2-alt1
- 2.2.2 release.

* Mon Dec 03 2007 Pavlov Konstantin <thresh@altlinux.ru> 2.0.4-alt1
- 2.0.4 release.

* Fri Sep 21 2007 Pavlov Konstantin <thresh@altlinux.ru> 2.0.1-alt1
- 2.0.1 release.

* Fri Sep 14 2007 Pavlov Konstantin <thresh@altlinux.ru> 2.0.0-alt1
- 2.0.0 release.
- Do not try to use valgrind on non-x86/x86_64 architectures (thx kas@).

* Tue Jun 05 2007 Pavlov Konstantin <thresh@altlinux.ru> 1.6.3-alt1
- 1.6.3 release.

* Thu Apr 19 2007 Pavlov Konstantin <thresh@altlinux.ru> 1.6.2-alt1
- 1.6.2 release.

* Wed Feb 21 2007 Pavlov Konstantin <thresh@altlinux.ru> 1.6.1-alt5
- Reverted -alt4 fixes, introduced a real fix for tasn1.

* Wed Feb 14 2007 Pavlov Konstantin <thresh@altlinux.ru> 1.6.1-alt4
- Fixed #10822: removed .private.

* Sun Jan 21 2007 Pavlov Konstantin <thresh@altlinux.ru> 1.6.1-alt3
- Modified symbol versioning:
  Added GNUTLS_1_6_1 with two new symbols.

* Sun Jan 21 2007 Pavlov Konstantin <thresh@altlinux.ru> 1.6.1-alt2
- Added libgnutlsxx and libgnutlsxx-devel subpackages.
- Spec cleanup.

* Mon Jan 08 2007 Pavlov Konstantin <thresh@altlinux.ru> 1.6.1-alt1
- Release 1.6.1.

* Sun Sep 24 2006 Mikhail Zabaluev <mhz@altlinux.ru> 1.4.4-alt1
- Release 1.4.4

* Sun Sep 10 2006 Mikhail Zabaluev <mhz@altlinux.ru> 1.4.3-alt1
- Release 1.4.3

* Sat Sep 02 2006 Mikhail Zabaluev <mhz@altlinux.ru> 1.4.2-alt1
- Updated to 1.4.2

* Tue May 30 2006 Mikhail Zabaluev <mhz@altlinux.ru> 1.4.0-alt1
- Updated to 1.4.0
- Updated Patch0

* Fri Mar 24 2006 Mikhail Zabaluev <mhz@altlinux.ru> 1.2.10-alt2
- Patch0: fixes build problems with ld --as-needed flag

* Sat Feb 11 2006 Mikhail Zabaluev <mhz@altlinux.ru> 1.2.10-alt1
- 1.2.10, fixes SA18794
- Correct packaging of examples
- Info install scripts moved to gnutls-devel-doc

* Thu Feb 02 2006 ALT QA Team Robot <qa-robot@altlinux.org> 1.2.9-alt1.1
- Rebuilt for new pkg-config dependencies.

* Sat Dec 03 2005 Mikhail Zabaluev <mhz@altlinux.ru> 1.2.9-alt1
- Updated to 1.2.9
- Moved documentation off to gnutls-devel-doc

* Tue Aug 16 2005 ALT QA Team Robot <qa-robot@altlinux.org> 1.2.6-alt1.1
- rebuild with libopencdk.

* Sun Aug 14 2005 Mikhail Zabaluev <mhz@altlinux.ru> 1.2.6-alt1
- Updated to upstream release 1.2.6

* Fri May 27 2005 Mikhail Zabaluev <mhz@altlinux.ru> 1.2.3-alt1
- Updated to upstream release 1.2.3

* Mon Jan 03 2005 Mikhail Zabaluev <mhz@altlinux.ru> 1.0.23-alt1
- Updated to upstream release 1.0.23

* Sat Oct 16 2004 Mikhail Zabaluev <mhz@altlinux.ru> 1.0.21-alt1
- Updated to upstream release 1.0.21

* Tue May 25 2004 Mikhail Zabaluev <mhz@altlinux.ru> 1.0.13-alt1
- Updated to upstream release 1.0.13
- Added /usr/bin/srptool to the utils file list

* Thu Apr 08 2004 Mikhail Zabaluev <mhz@altlinux.ru> 1.0.10-alt1
- Updated to upstream release 1.0.10

* Sat Mar 27 2004 Mikhail Zabaluev <mhz@altlinux.ru> 1.0.8-alt2
- Rebuilt against libgcrypt 1.1.93

* Sat Mar 06 2004 Mikhail Zabaluev <mhz@altlinux.ru> 1.0.8-alt1
- Updated to 1.0.8 upstream release
- Build fixes for new autotools

* Sat Jan 10 2004 Mikhail Zabaluev <mhz@altlinux.ru> 1.0.4-alt1
- Updated to 1.0.4 upstream release
- Renamed the source package to gnutls
- Added openssl subpackage family to pack libgnutls-openssl

* Sat Jan 10 2004 Mikhail Zabaluev <mhz@altlinux.ru> 0.8.9-alt3
- Made external libtasn1 linkage optional, disabled per default

* Fri Jan 02 2004 Mikhail Zabaluev <mhz@altlinux.ru> 0.8.9-alt2
- Spec cleanup
- Build against libtasn1
- Removed libtool files from the filelist

* Sun Jul 20 2003 Mikhail Zabaluev <mhz@altlinux.ru> 0.8.9-alt1
- Ported the package to ALT Linux
