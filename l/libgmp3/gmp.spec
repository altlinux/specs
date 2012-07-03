Name: libgmp3
Version: 4.3.2
Release: alt4

Summary: GNU MP arbitrary precision arithmetic library
License: LGPLv3+
Group: System/Libraries
Url: http://gmplib.org/

# ftp://ftp.gnu.org/gnu/gmp/gmp-%version.tar.bz2
Source: gmp-%version.tar
Patch: gmp-%version-%release.patch

Provides: gmp = %version-%release, libgmp = %version-%release
Obsoletes: gmp, libgmp

# Automatically added by buildreq on Mon Jun 16 2003
BuildRequires: flex libreadline-devel

%ifarch %ix86
%def_enable fat
%else
%def_disable fat
%endif

%description
GNU MP is a library for arbitrary precision arithmetic, operating on
signed integers, rational numbers, and floating point numbers.  It has
a rich set of functions, and the functions have a regular interface.

%prep
%setup -n gmp-%version
%patch -p1

%build
%autoreconf
%configure --disable-mpbsd --disable-cxx %{subst_enable fat}
LANG=C awk 'NR>=3&&$1=="#define"&&$2~/^[a-z_0-9]+$/&&$3~/^__/{print gensub("^__MPN\\(([^)]+)\\)","__gmpn_\\1",1,$3)}' \
	gmp.h >libgmp.sym
sed -n 's/^[^ ]\+ \([^ ]\+\) __GMP_PROTO .*/\1/p' randmt.h >>libgmp.sym
# extra symbols required by libgmpxx and test suite
cat >>libgmp.sym <<'EOF'
__gmp_allocate_func
__gmp_asprintf_final
__gmp_asprintf_memory
__gmp_asprintf_reps
__gmp_assert_fail
__gmp_binvert_limb_table
__gmp_default_allocate
__gmp_default_free
__gmp_default_reallocate
__gmp_doprnt_integer
__gmp_doprnt_mpf2
__gmp_fib_table
__gmp_free_func
__gmp_randinit_mt_noseed
__gmp_rands
__gmp_rands_initialized
__gmp_reallocate_func
__gmp_tmp_reentrant_alloc
__gmp_tmp_reentrant_free
__gmpn_bases
__gmpn_clz_tab
__gmpn_copyd
__gmpn_copyi
__gmpn_cpuvec
__gmpn_cpuvec_init
__gmpn_divexact_1
__gmpn_get_d
__gmpn_hgcd
__gmpn_hgcd_itch
__gmpn_hgcd_matrix_init
__gmpn_invert_limb
__gmpn_jacobi_base
__gmpn_kara_mul_n
__gmpn_matrix22_mul
__gmpn_matrix22_mul_itch
__gmpn_mod_34lsub1
__gmpn_mul_basecase
__gmpn_preinv_divrem_1
__gmpn_sqr_basecase
__gmpn_toom3_mul_n
__gmpz_divexact_gcd
EOF
sort -u -o libgmp.sym libgmp.sym
%make_build

%install
%makeinstall_std
install -pm644 gmp-mparam.h randmt.h %buildroot%_includedir/

%check
%make_build -k check

%files
%doc AUTHORS README NEWS
%_libdir/libgmp.so.3*

%changelog
* Wed Jun 06 2012 Dmitry V. Levin <ldv@altlinux.org> 4.3.2-alt4
- Packaged libgmp3 compatibility library.

* Fri Feb 18 2011 Dmitry V. Levin <ldv@altlinux.org> 4.3.2-alt3
- Rebuilt for debuginfo.

* Tue Oct 12 2010 Dmitry V. Levin <ldv@altlinux.org> 4.3.2-alt2
- Fixed build on arm (by silicium@).
- Rebuilt for soname set-versions.

* Thu Jun 17 2010 Dmitry V. Levin <ldv@altlinux.org> 4.3.2-alt1
- Updated to 4.3.2.

* Thu Sep 10 2009 Dmitry V. Levin <ldv@altlinux.org> 4.2.4-alt3
- Moved "make check" to %%check section.

* Tue Sep 01 2009 Dmitry V. Levin <ldv@altlinux.org> 4.2.4-alt2
- Packaged randmt.h and exported all ELF symbols declared
  in this header file (closes: #21325).
- Removed obsolete %%install_info/%%uninstall_info calls.

* Tue Mar 10 2009 Dmitry V. Levin <ldv@altlinux.org> 4.2.4-alt1
- Updated to 4.2.4.
- Imported patches from http://gmplib.org/patches/.

* Mon Dec 15 2008 Dmitry V. Levin <ldv@altlinux.org> 4.2.2-alt2
- Removed obsolete %%post_ldconfig/%%postun_ldconfig calls.

* Fri Mar 14 2008 Dmitry V. Levin <ldv@altlinux.org> 4.2.2-alt1
- Updated to 4.2.2.
- Updated URL, license tag, dropped manually added prereqs.
- gmp.h: Fixed to support gcc >= 4.3.0.
- Build with --enable-fat on %%ix86.
- Restricted list of global symbols exported by the libgmp library to
  only those which are either declared in gmp.h or required by test suit.

* Sat Apr 14 2007 Dmitry V. Levin <ldv@altlinux.org> 4.1.4-alt5
- Uncompressed tarball.

* Sun Apr 23 2006 Dmitry V. Levin <ldv@altlinux.org> 4.1.4-alt4
- Build without --enable-mpfr, because
  MPFR is separate project and packaged separately.

* Fri Apr 14 2006 Dmitry V. Levin <ldv@altlinux.org> 4.1.4-alt3
- Applied fixes from Debian and FC gmp packages.
- Build with --enable-mpfr, because
  GMP with MPFR support is required to build fortran (#8861).

* Tue May 24 2005 Dmitry V. Levin <ldv@altlinux.org> 4.1.4-alt2
- Applied fixes from Debian gmp package.
- Added multilib support (mouse, closes #6030).
- Fixed License tag (at, closes #6705).

* Fri Apr 29 2005 Anton D. Kachalov <mouse@altlinux.org> 4.1.4-alt1.1
- multilib support

* Tue Jan 18 2005 Stanislav Ievlev <inger@altlinux.org> 4.1.4-alt1
- 4.1.4

* Fri Feb 27 2004 Stanislav Ievlev <inger@altlinux.org> 4.1.2-alt3
- force building with automake 1.7

* Tue Dec 02 2003 Stanislav Ievlev <inger@altlinux.org> 4.1.2-alt2.2
- rebuild without .la files

* Mon Jun 16 2003 Stanislav Ievlev <inger@altlinux.ru> 4.1.2-alt2.1
- fixed buildreq
- added special hack to build under bte

* Fri Feb 28 2003 Stanislav Ievlev <inger@altlinux.ru> 4.1.2-alt2
- fixed ldconfig usage according packaging policy

* Tue Feb 25 2003 Stanislav Ievlev <inger@altlinux.ru> 4.1.2-alt1
- review patches:
  lc-assert-always - removed
  noinline - removed
  vafixes  - removed
  x86_64   - updated
  gmpxx.h.getnum - removed (included)
  mpf_inp_str.c - removed (included)
  powm_ui.c.41 - removed (included)
- added subpackage with C++ API (like liddb4_cxx)

* Fri Sep 20 2002 Stanislav Ievlev <inger@altlinux.ru> 4.1-alt1
- 4.1
- little spec improvements
- added devel-static subpackage
- added gmpxx.h header to %_includedir
- merge with latest RH and MDK patches

* Fri Mar 02 2001 Dmitry V. Levin <ldv@fandra.org> 3.1.1-ipl2mdk
- Libification.
- Added ia64 patch.
- Build Berkley MP compatibility library.

* Fri Dec 01 2000 Dmitry V. Levin <ldv@fandra.org> 3.1.1-ipl1mdk
- 3.1.1
- Fixed configure script.
- Fixed texinfo documentation.

* Fri Apr 28 2000 Dmitry V. Levin <ldv@fandra.org>
- 3.0.1

* Thu Apr 20 2000 Dmitry V. Levin <ldv@fandra.org>
- 3.0

* Fri Oct 22 1999 Dmitry V. Levin <ldv@fandra.org>
- Fandra adaptions

* Wed Oct 20 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- Release version.

* Tue Jul 22 1999 Thierry Vignaud <tvignaud@mandrakesoft.com>
- add french description

* Sat Apr 10 1999 Bernhard Rosenkraenzer <bero@linux-mandrake.com>
- Mandrake adaptions
- bzip2 man/info pages
- add de locale
- .spec optimizations

* Thu Feb 11 1999 Michael Johnson <johnsonm@redhat.com>
- include the private header file gmp-mparam.h because several
  apps seem to assume that they are building against the gmp
  source tree and require it.  Sigh.

* Tue Jan 12 1999 Michael K. Johnson <johnsonm@redhat.com>
- libtoolize to work on arm

* Thu Sep 10 1998 Cristian Gafton <gafton@redhat.com>
- yet another touch of the spec file

* Wed Sep  2 1998 Michael Fulbright <msf@redhat.com>
- looked over before inclusion in RH 5.2

* Sat May 24 1998 Dick Porter <dick@cymru.net>
- Patch Makefile.in, not Makefile
- Don't specify i586, let configure decide the arch

* Sat Jan 24 1998 Marc Ewing <marc@redhat.com>
- started with package from Toshio Kuratomi <toshiok@cats.ucsc.edu>
- cleaned up file list
- fixed up install-info support
