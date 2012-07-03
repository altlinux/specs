Name: gpgme
Version: 1.3.1
Release: alt2

%define min_gnupg_version 1.9.6

Summary: GnuPG Made Easy is a library designed to make access to GnuPG easier for applications
License: LGPLv2.1+
Group: System/Libraries
Url: http://www.gnupg.org/related_software/gpgme/index.html

# ftp://ftp.gnupg.org/gcrypt/gpgme/gpgme-%version.tar.bz2
Source: gpgme-%version.tar

Patch1: gpgme-1.3.0-alt-version-script.patch
Patch2: gpgme-1.3.0-alt-gpgme-config-assuan.patch
Patch3: gpgme-1.3.0-alt-tests.patch
Patch4: gpgme-1.3.1-rh-alt-linkage.patch

Requires: gnupg2-gpg >= %min_gnupg_version

%def_disable static
%{?_enable_static:BuildPreReq: glibc-devel-static}

BuildRequires: gcc-c++ gnupg2 libgpg-error-devel libpth-devel libstdc++-devel libassuan-devel >= 2.0

%package -n lib%name
Summary: GnuPG Made Easy!
Group: System/Libraries
Requires: gnupg2-gpg >= %min_gnupg_version
Provides: libgpgme1 = %version-%release
Obsoletes: libgpgme1 < %version-%release

%package -n lib%name-devel
Summary: Include files for development with GPGME
Group: Development/C
Requires: lib%name = %version-%release
Requires: libgpg-error-devel
Provides: libgpgme1-devel = %version-%release
Obsoletes: libgpgme1-devel < %version-%release

%package -n lib%name-devel-static
Summary: Static libraries for development with GPGME
Group: Development/C
Requires: lib%name-devel = %version-%release
Provides: libgpgme1-devel-static = %version-%release
Obsoletes: libgpgme1-devel-static < %version-%release

%description
GnuPG Made Easy (GPGME) is a C language library that allows to add
support for cryptography to a program.  It is designed to make access
to public key crypto engines like GnuPG or GpgSM easier for
applications.  GPGME provides a high-level crypto API for encryption,
decryption, signing, signature verification and key management.

%description -n lib%name
GnuPG Made Easy (GPGME) is a C language library that allows to add
support for cryptography to a program.  It is designed to make access
to public key crypto engines like GnuPG or GpgSM easier for
applications.  GPGME provides a high-level crypto API for encryption,
decryption, signing, signature verification and key management.

%description -n lib%name-devel
GnuPG Made Easy (GPGME) is a C language library that allows to add
support for cryptography to a program.  It is designed to make access
to public key crypto engines like GnuPG or GpgSM easier for
applications.  GPGME provides a high-level crypto API for encryption,
decryption, signing, signature verification and key management.

This package contains include files required for development of
GPGME-based applications.

%description -n lib%name-devel-static
GnuPG Made Easy (GPGME) is a C language library that allows to add
support for cryptography to a program.  It is designed to make access
to public key crypto engines like GnuPG or GpgSM easier for
applications.  GPGME provides a high-level crypto API for encryption,
decryption, signing, signature verification and key management.

This package contains static libraries required for development of
GPGME-based statically linked applications.

%prep
%setup
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1

rm doc/*.info* m4/{libtool,lt}*.m4

%build
%autoreconf
mkdir -p tmp_bin
ln -sf %_bindir/gpg2 tmp_bin/gpg
export PATH=$PWD/tmp_bin:$PATH

%{?!_enable_static:export lt_cv_prog_cc_static_works=no}
# --enable-maintainer-mode is required to generate the info file
# when building from CVS snapshot
%configure \
	%{?cvsdate: --enable-maintainer-mode } \
	%{subst_enable static} \
	--with-gpg=%_bindir/gpg2 \
	--with-gpgsm=%_bindir/gpgsm

%make_build MAKEINFOFLAGS=--no-split

%install
%makeinstall_std

%check
%make_build -k check

%files -n lib%name
%_libdir/*.so.*
%doc AUTHORS NEWS README THANKS

%files -n lib%name-devel
%_bindir/*
%_includedir/*.h
%_libdir/*.so
%_datadir/aclocal/*.m4
%_infodir/*.info*

%if_enabled static
%files -n lib%name-devel-static
%_libdir/*.a
%endif

%changelog
* Wed May 23 2012 Dmitry V. Levin <ldv@altlinux.org> 1.3.1-alt2
- Fixed build with ld --no-copy-dt-needed-entries.

* Mon Aug 29 2011 Sergey V Turchin <zerg@altlinux.org> 1.3.1-alt1
- new version

* Tue Mar 08 2011 Dmitry V. Levin <ldv@altlinux.org> 1.3.0-alt5
- Fixed tests to work with gnupg-2.0.17.

* Thu Nov 18 2010 Dmitry V. Levin <ldv@altlinux.org> 1.3.0-alt4
- Rebuilt for soname set-versions.

* Mon Feb 15 2010 Dmitry V. Levin <ldv@altlinux.org> 1.3.0-alt3
- Fixed gpgme-config so it won't force redundant linkage with -lassuan
  any longer; libgpgme is already linked with -lassuan, that's enough.
  This unwanted gpgme-config behaviour was introduced in 1.3.0 version.
- Dropped -texinfo.patch, install-info(1) starting with texinfo-4.12
  formats direntries automatically.
- Forced info docs regeneration with makeinfo --no-split.

* Sun Feb 07 2010 Dmitry V. Levin <ldv@altlinux.org> 1.3.0-alt2
- Rebuilt with libassuan2.so.0.
- Updated version script.
- Cleaned up specfile.

* Wed Feb 03 2010 Sergey V Turchin <zerg@altlinux.org> 1.3.0-alt1
- new version

* Tue Jun 30 2009 Sergey V Turchin <zerg@altlinux.org> 1.2.0-alt1
- new version (ALT#20640)

* Tue May 12 2009 Sergey V Turchin <zerg@altlinux.org> 1.1.8-alt0.M50.1
- built for M50

* Thu May 07 2009 Sergey V Turchin <zerg@altlinux.org> 1.1.8-alt1
- new version
- remove deprecated macroses from specfile
- fix requires to gnupg2-gpg

* Tue Oct 21 2008 Sergey V Turchin <zerg at altlinux dot org> 1.1.7-alt2
- fix requires

* Mon Oct 20 2008 Sergey V Turchin <zerg at altlinux dot org> 1.1.7-alt1
- new version

* Wed Jan 09 2008 Sergey V Turchin <zerg at altlinux dot org> 1.1.6-alt1
- new version

* Tue Jul 10 2007 Sergey V Turchin <zerg at altlinux dot org> 1.1.5-alt1
- new version

* Fri Mar 09 2007 Sergey V Turchin <zerg at altlinux dot org> 1.1.3-alt2
- add multiple-message.patch from upstream

* Tue Jan 30 2007 Sergey V Turchin <zerg at altlinux dot org> 1.1.3-alt1
- new version

* Fri Mar 03 2006 Sergey V Turchin <zerg at altlinux dot org> 1.1.2-alt1
- new version

* Wed Nov 30 2005 Sergey V Turchin <zerg at altlinux dot org> 1.1.0-alt1
- new version

* Tue Nov 29 2005 Sergey V Turchin <zerg at altlinux dot org> 1.0.3-alt2
- obsolete libgpgme1

* Tue Jun 21 2005 Sergey V Turchin <zerg at altlinux dot org> 1.0.3-alt1
- new version

* Wed Jun 01 2005 Sergey V Turchin <zerg at altlinux dot org> 1.0.2-alt1
- new version

* Mon Oct 25 2004 Sergey V Turchin <zerg at altlinux dot org> 1.0.1-alt1
- new version

* Mon Oct 11 2004 Sergey V Turchin <zerg at altlinux dot org> 1.0.0-alt1
- new version

* Thu Aug 26 2004 Sergey Vlasov <vsu@altlinux.ru> 0.3.16-alt2
- Added gpgme-0.3.16-fix-select-status.patch: fix hang in tests/gpg/t-edit (the
  event loop was remembering that the fd was ready even after
  rungpg.c:read_status() had flushed it).
- Updated BuildRequires.

* Fri Dec 12 2003 Sergey Vlasov <vsu@altlinux.ru> 0.3.16-alt1
- 0.3.16 release:
  * Compatibility fixes for GnuPG 1.9.x
- Do not package static libraries by default.
- Removed *.la files.
- Updated BuildRequires.

* Thu May 29 2003 Sergey Vlasov <vsu@altlinux.ru> 0.3.15-alt1
- 0.3.15 release.
- Build with libpth support (does not introduce new dependencies for the
  binary package - thread library is detected using weak symbols).
- Build with gpgsm support (but the dependency to newpg is not added -
  the application/library package which links to libgpgme and uses the
  gpgsm features must have this dependency).

* Fri Feb 07 2003 Sergey Vlasov <vsu@altlinux.ru> 0.3.14-alt2
- Updated URL (#1656) and source location.
- Removed patch to set minimum required GnuPG version to 1.0.7.
  Now GnuPG >= 1.2.0 is required.

* Fri Feb 07 2003 Sergey V Turchin <zerg@altlinux.ru> 0.3.14-alt1
- new version

* Sun Oct 27 2002 Sergey Vlasov <vsu@altlinux.ru> 0.3.12-alt1
- 0.3.12 release.
- Patch to set minimum required GnuPG version to 1.0.7
  (I don't see any changes which would require GnuPG 1.2.0).
- Added "make check" to make sure the library really works.

* Thu Aug 29 2002 Sergey Vlasov <vsu@altlinux.ru> 0.3.10-alt0.1
- Version from CVS 20020829 (bug with child process handling was fixed).
- Removed gnupg requires from *-devel.
- More specfile cleanup.
- Patch to backport gpgme.m4 to old autoconf (removed AC_HELP_STRING).

* Mon Sep 17 2001 Sergey Vlasov <vsu@altlinux.ru> 0.2.3-alt1
- 0.2.3

* Tue Apr 10 2001 Dmitry V. Levin <ldv@altlinux.ru> 0.2.1-alt1
- 0.2.1
- Moved static libraries to devel-static subpackage.
- Specfile cleanup.

* Mon Feb 19 2001 AEN <aen@logic.ru>
- first build for Sisyphus
