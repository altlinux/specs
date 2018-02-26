Name: beecrypt
Version: 4.2.1
Release: alt7

Summary: The BeeCrypt Cryptography Library
License: LGPLv2+
Group: System/Libraries
Url: http://sourceforge.net/projects/beecrypt

Source: beecrypt-%version.tar
Patch1: beecrypt-4.1.2-rh-biarch.patch
Patch2: beecrypt-4.2.1-rh-no-c++.patch
Patch3: beecrypt-4.2.1-alt-arm.patch
Patch4: beecrypt-4.2.1-alt-assert.patch

%define soname 7

%package -n lib%name%soname
Summary: The BeeCrypt Cryptography Library
Group: System/Libraries
Provides: %name = %version-%release
Provides: lib%name = %version-%release
Obsoletes: %name

%package -n lib%name-devel
Summary: Development environment for the BeeCrypt Cryptography Library
Group: Development/C
Provides: %name-devel = %version-%release
Obsoletes: %name-devel
Requires: lib%name%soname = %version-%release

%package -n lib%name-devel-static
Summary: Static version of the BeeCrypt Cryptography Library
Group: Development/C
Provides: %name-devel-static = %version-%release
Obsoletes: %name-devel-static
Requires: lib%name-devel = %version-%release

%description
BeeCrypt is an open source cryptography library that contains
highly optimized C and assembler implementations of many
well-known algorithms including Blowfish, MD5, SHA-1,
Diffie-Hellman, and ElGamal.

%description -n lib%name%soname
BeeCrypt is an open source cryptography library that contains
highly optimized C and assembler implementations of many
well-known algorithms including Blowfish, MD5, SHA-1,
Diffie-Hellman, and ElGamal.

%description -n lib%name-devel
BeeCrypt is an open source cryptography library that contains
highly optimized C and assembler implementations of many
well-known algorithms including Blowfish, MD5, SHA-1,
Diffie-Hellman, and ElGamal.

This package contains development files required for building
BeeCrypt-based software.

%description -n lib%name-devel-static
BeeCrypt is an open source cryptography library that contains
highly optimized C and assembler implementations of many
well-known algorithms including Blowfish, MD5, SHA-1,
Diffie-Hellman, and ElGamal.

This package contains static library required for building
BeeCrypt-based statically linked software.

%prep
%setup -q
%patch1 -p1
%patch2 -p1
%patch3 -p2
%patch4 -p2
bzip2 -9k BENCHMARKS

%build
%autoreconf

%configure \
	--enable-static \
	%{subst_enable debug} \
	--with-cplusplus=no \
	--with-java=no \
	--with-python=no \
	#
%make_build

%install
%makeinstall_std

iconv -f ISO-8859-1 -t UTF-8 CONTRIBUTORS -o CONTRIBUTORS.utf8
mv -f CONTRIBUTORS.utf8 CONTRIBUTORS

%check
%make_build -k check

%files -n lib%name%soname
%_libdir/*.so.*
%doc AUTHORS BENCHMARKS.bz2 BUGS CONTRIBUTORS NEWS README

%files -n lib%name-devel
%_libdir/*.so
%_includedir/*

%files -n lib%name-devel-static
%_libdir/*.a

%changelog
* Thu Apr 07 2011 Dmitry V. Levin <ldv@altlinux.org> 4.2.1-alt7
- Rebuilt for debuginfo.

* Wed Jan 12 2011 Kirill A. Shutemov <kas@altlinux.org> 4.2.1-alt6
- Do not redefine assert, always include <assert.h>. Closes: #24905.

* Wed Oct 20 2010 Dmitry V. Levin <ldv@altlinux.org> 4.2.1-alt5
- Rebuilt for soname set-versions.
=======

* Tue Aug 17 2010 Kirill A. Shutemov <kas@altlinux.org> 4.2.1-alt4
- Fix build on ARM.

* Fri Aug 13 2010 Kirill A. Shutemov <kas@altlinux.org> 4.2.1-alt3
- Add provide libbeecrypt = %%version-%%release for libbeecrypt%%soname
  subpackage

* Fri Aug 13 2010 Dmitry V. Levin <ldv@altlinux.org> 4.2.1-alt2
- Run test suite during build.

* Sat Aug 07 2010 Kirill A. Shutemov <kas@altlinux.org> 4.2.1-alt1
- 4.2.1
  + sync with Fedora 4.2.1-2

* Wed May 06 2009 Dmitry V. Levin <ldv@altlinux.org> 2.2.0-alt8
- Fixed build with fresh autotools.

* Sun Dec 14 2008 Dmitry V. Levin <ldv@altlinux.org> 2.2.0-alt7
- Removed obsolete %%post_ldconfig/%%postun_ldconfig calls.

* Thu Apr 12 2007 Dmitry V. Levin <ldv@altlinux.org> 2.2.0-alt6
- Fixed compilation warnings.

* Sat Mar 18 2006 Dmitry V. Levin <ldv@altlinux.org> 2.2.0-alt5
- Build with -Wa,--noexecstack.

* Wed Apr 28 2004 Dmitry V. Levin <ldv@altlinux.org> 2.2.0-alt4
- Rebuilt with glibc-2.3.x.

* Tue Nov 25 2003 Dmitry V. Levin <ldv@altlinux.org> 2.2.0-alt3
- Do not package .la files.
- Fixed arm platform support (#2803).

* Tue Sep 03 2002 Dmitry V. Levin <ldv@altlinux.org> 2.2.0-alt2
- Updated %post/%postun scripts.
- Updated devel-static requirements.

* Mon Mar 25 2002 Dmitry V. Levin <ldv@alt-linux.org> 2.2.0-alt1
- Updated to pseudo-official beecrypt-2.2.0 from jbj,
  to sync with rpm-4.0.4
- Corrected compilation options.

* Thu Dec 06 2001 Dmitry V. Levin <ldv@alt-linux.org> 2.1.0-alt1
- Initial revision (PLD-based).
