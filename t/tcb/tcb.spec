Name: tcb
Version: 1.1
Release: alt1

Summary: Libraries and tools implementing the %name password shadowing scheme
License: GPL or BSD
Group: System/Base
Url: http://www.openwall.com/tcb/

Source: ftp://ftp.openwall.com/pub/projects/tcb/%name-%version.tar
Source1: tcb_chkpwd.control

Patch1: tcb-0.9.9-alt-makefile-pam.patch
Patch2: tcb-0.9.9-alt-tcb_convert-try_auth.patch

# due to PAM policy.
BuildRequires(pre): libpam-devel
# due to change in format of PAM modules requirements.
BuildRequires: rpm-build >= 0:4.0.4-alt55
# due to crypt_gensalt.
#BuildPreReq: libcrypt.so.1(GLIBC_2.2.2)

%description
This package consists of three components: pam_tcb, libnss_tcb, and
libtcb.  pam-tcb is a PAM module which supersedes pam_unix.  It also
implements the tcb password shadowing scheme (see tcb(5) for details).
The tcb scheme allows many core system utilities (passwd(1) being the
primary example) to operate with little privilege.  libnss_tcb is the
accompanying NSS module.  libtcb contains code shared by the PAM and
NSS modules and is also used by programs from the shadow-utils package.

%package -n lib%name
Summary: %name shared library
License: GPL or BSD
Group: System/Libraries

%package -n lib%name-devel
Summary: Libraries and header files for building %name-aware applications
License: GPL or BSD
Group: Development/C
PreReq: lib%name = %version-%release

%package -n lib%name-devel-static
Summary: Static libraries for building statically linked %name-aware applications
License: GPL or BSD
Group: Development/C
Requires: lib%name-devel = %version-%release

%package -n nss_%name
Summary: %name NSS module
License: GPL or BSD
Group: System/Libraries
PreReq: lib%name = %version-%release

%set_pam_name pam_%name
%package -n %pam_name
Summary: %name PAM module
License: GPL or BSD
Group: System/Base
PreReq: nss_%name = %version-%release, libpam%_pam_name_suffix, control
Requires: glibc-crypt_blowfish >= 1.2
Provides: pam_%name = %version-%release
Obsoletes: pam_%name

%package utils
Summary: %name utilities
License: GPL
Group: System/Base
Provides: /etc/tcb
PreReq: %pam_name = %version-%release, shadow-convert

%description -n lib%name
This package contains code shared by the PAM and NSS modules and is also used
by programs from the shadow-utils package.

%description -n lib%name-devel
This package contains library and header files needed for
building %name-aware applications.

%description -n lib%name-devel-static
This package contains static library needed for
building statically linked %name-aware applications.

%description -n nss_%name
This package contains nss_%name - %name NSS module.

%description -n %pam_name
This package contains %pam_name - %name PAM module which supersedes pam_unix.

%description utils
This package contains utilities to convert to and from the tcb
password shadowing scheme.

%prep
%setup
%patch1 -p1
%patch2 -p1

# /usr/libexec is hardcoded in the sources.
if [ "%_libexecdir" != '/usr/libexec' ]; then
	find -type f -print0 |
		xargs -r0 grep -FZl /usr/libexec -- |
		xargs -r0 %__subst -p 's,/usr/libexec,%_libexecdir,g' --
fi

%build
CFLAGS='%optflags -W -DENABLE_SETFSUGID -DENABLE_NLS -DNLS_PACKAGE=\"Linux-PAM\"' make

%install
%make_install install-non-root install-pam_unix install-pam_pwdb \
	DESTDIR=%buildroot \
	MANDIR=%_mandir \
	LIBDIR=%_libdir \
	SLIBDIR=/%_lib \
	#
install -pD -m755 %_sourcedir/tcb_chkpwd.control \
	%buildroot%_controldir/tcb_chkpwd
%__subst -p 's,@libexecdir@,%_libexecdir,g' \
	%buildroot%_controldir/tcb_chkpwd
mkdir -p %buildroot/etc/tcb

%pre -n %pam_name
groupadd=/usr/sbin/groupadd
$groupadd -r -f chkpwd >/dev/null 2>&1 ||:
$groupadd -r -f shadow >/dev/null 2>&1 ||:
%pre_control tcb_chkpwd

%post -n %pam_name
%post_control -s tcb tcb_chkpwd

%triggerpostun -n %pam_name -- pam_tcb < 0:0.9.8.3-alt1
/usr/sbin/control tcb_chkpwd tcb

%pre utils
groupadd=/usr/sbin/groupadd
$groupadd -r -f auth >/dev/null 2>&1 ||:

%post utils
if [ $1 = 1 -a ! -e /etc/tcb ]; then
	/sbin/tcb_convert
fi

%files -n lib%name
/%_lib/lib%name.so.*
%doc ChangeLog LICENSE

%files -n lib%name-devel
%_libdir/lib*.so
%_includedir/*

%files -n lib%name-devel-static
%_libdir/*.a

%files -n nss_%name
/%_lib/libnss_*

%files -n %pam_name
/%_lib/security/pam_*.so*
%attr(710,root,chkpwd) %dir %_libexecdir/chkpwd
%attr(700,root,root) %verify(not mode group) %_libexecdir/chkpwd/tcb_chkpwd
%config %_controldir/tcb_chkpwd
%_man8dir/pam_*

%files utils
%attr(710,root,shadow) %ghost /etc/tcb
/sbin/%{name}_*convert
%_man5dir/%name.*
%_man8dir/tcb_*

%changelog
* Fri Aug 12 2011 Dmitry V. Levin <ldv@altlinux.org> 1.1-alt1
- Updated to 1.1:
  * Sun Jul 17 2011 Solar Designer <solar@owl> 1.1-owl1
  - Changed the default hash encoding prefix from "$2a$" to "$2y$"
    (requires crypt_blowfish 1.2 or newer).

* Tue May 24 2011 Dmitry V. Levin <ldv@altlinux.org> 1.0.6-alt4
- pam0_tcb: Added and enabled NLS support.

* Wed Mar 09 2011 Dmitry V. Levin <ldv@altlinux.org> 1.0.6-alt3
- pam0_tcb: Added description to tcb_chkpwd control (closes: #17283).
- Rebuilt for debuginfo.

* Fri Nov 05 2010 Dmitry V. Levin <ldv@altlinux.org> 1.0.6-alt2
- Rebuilt for soname set-versions.

* Tue Jun 08 2010 Dmitry V. Levin <ldv@altlinux.org> 1.0.6-alt1
- Dropped faulty check for sparse files in tcb_is_suspect().

* Sun Feb 28 2010 Dmitry V. Levin <ldv@altlinux.org> 1.0.5-alt1
- Decreased the size of tcb_privs structure allocated in .data segment
  from 256K to a two dozen bytes by moving a groups array to .bss segment.

* Thu Feb 11 2010 Dmitry V. Levin <ldv@altlinux.org> 1.0.4-alt1
- Fixed potential grpbuf buffer overflow in tcb_drop_priv_r().
  There doesn't appear to be any untrusted user input involved,
  so this bug doesn't have to be treated as a security issue.
- Patched Makefiles to use LDFLAGS more consistently.  Reported
  by Pawel Hajdan.

* Fri Apr 03 2009 Dmitry V. Levin <ldv@altlinux.org> 1.0.3-alt1
- In the PAM module, replaced all calls to exit(3) in child processes
  with calls to _exit(2).  Reported by Pascal Terjan.
- In the PAM module, added fflush(3) and fsync(2) calls right before
  closing file opened for writing.  Reported by Ermanno Scaglione.

* Sun Dec 14 2008 Dmitry V. Levin <ldv@altlinux.org> 1.0.2-alt3
- Removed obsolete %%post_ldconfig/%%postun_ldconfig calls.

* Tue Jul 08 2008 Dmitry V. Levin <ldv@altlinux.org> 1.0.2-alt2
- Adjusted %%post scripts for current rpmbuild.

* Thu Nov 02 2006 Dmitry V. Levin <ldv@altlinux.org> 1.0.2-alt1
- In the PAM module and tcb_chkpwd helper, fixed memory leaks
  reported by Alexander Kanevskiy.

* Sat May 06 2006 Dmitry V. Levin <ldv@altlinux.org> 1.0.1-alt1
- In the PAM module, hardened pam_sm_open_session() to fail for unknown users.

* Thu Jan 12 2006 Dmitry V. Levin <ldv@altlinux.org> 1.0-alt2
- Rebuilt for new style PAM dependencies generated by rpm-build-4.0.4-alt55.

* Sat Dec 31 2005 Dmitry V. Levin <ldv@altlinux.org> 1.0-alt1
- Updated to 1.0 (with all changes made in previous release applied).

* Mon Sep 26 2005 Dmitry V. Levin <ldv@altlinux.org> 0.9.9-alt3
- In the PAM module, changed conversation code to use pam_prompt.

* Mon Sep 12 2005 Dmitry V. Levin <ldv@altlinux.org> 0.9.9-alt2
- In the PAM module,
  + Fixed potential NULL dereferences in unix_verify_password_plain()
    and pam_sm_chauthtok().
  + Disabled overriding default prompt in pam_get_user() calls.
  + Changed logging to use pam_syslog.

* Wed Aug 24 2005 Dmitry V. Levin <ldv@altlinux.org> 0.9.9-alt1
- Updated to 0.9.9 (with all changes made in previous release applied).

* Wed Aug 10 2005 Dmitry V. Levin <ldv@altlinux.org> 0.9.8.9-alt2
- Restricted list of global symbols exported by the library,
  NSS and PAM modules.
- In the PAM module, implemented "openlog" option and disabled
  openlog/closelog calls for each logging function invocation,
  according to new convention introduced in pam-0.80-alt1.

* Tue May 03 2005 Dmitry V. Levin <ldv@altlinux.org> 0.9.8.9-alt1
- Updated to 0.9.8.9 (with alt-warnings applied).
- tcb-utils: packaged /etc/tcb as %%ghost.
- pam_tcb: removed obsolete pam_unix* provides.

* Wed Apr 20 2005 Dmitry V. Levin <ldv@altlinux.org> 0.9.8.8-alt4
- Redone alt-warnings and alt-openpam patches.
- In pam_tcb:
  + keep tcb_chkpwd at mode "restricted" in the package, but default
    it to "tcb" in %%post when the package is first installed.
    This avoids a race and fail-open behavior.
  + Instructed RPM to not verify permissions and group ownership
    of tcb_chkpwd file which is controlled via control(8) facility.

* Fri Feb 11 2005 Dmitry V. Levin <ldv@altlinux.org> 0.9.8.8-alt3
- Fixed multilib [take 2] (closes #4896).

* Thu Feb 10 2005 Dmitry V. Levin <ldv@altlinux.org> 0.9.8.8-alt2
- Fixed multilib (closes #4896).

* Fri Jun 25 2004 Dmitry V. Levin <ldv@altlinux.org> 0.9.8.8-alt1
- tcb_unconvert: Zero errno before each readdir(3) call.

* Fri Jan 02 2004 Dmitry V. Levin <ldv@altlinux.org> 0.9.8.7-alt2
- Deal with compilation warnings generated by new gcc compiler.

* Thu Nov 06 2003 Dmitry V. Levin <ldv@altlinux.org> 0.9.8.7-alt1
- Updated to 0.9.8.7:
  * Sun Nov 02 2003 Solar Designer <solar@owl> 0.9.8.7-owl1
  - Build the PAM module with -fPIC.
  - Renamed FAKEROOT to DESTDIR.
- Rediffed patches.

* Thu Oct 30 2003 Dmitry V. Levin <ldv@altlinux.org> 0.9.8.6-alt1
- Updated to 0.9.8.6:
  * Wed Oct 29 2003 Solar Designer <solar@owl> 0.9.8.6-owl1
  - Don't depend on *BSD-style asprintf(3) semantics
    as glibc upstream has rejected that patch.

* Thu Jun 05 2003 Dmitry V. Levin <ldv@altlinux.org> 0.9.8.5-alt2
- Fixed build with OpenPAM.
- Added Linux-PAM/OpenPAM multi-build support.

* Sat Apr 19 2003 Dmitry V. Levin <ldv@altlinux.org> 0.9.8.5-alt1
- Updated to 0.9.8.5:
  * Fri Apr 18 2003 Solar Designer <solar@owl> 0.9.8.5-owl1
  - Use bold face for component names in .SH NAME, but avoid *roff commands
    to not confuse makewhatis and apropos(1).

* Wed Apr 16 2003 Dmitry V. Levin <ldv@altlinux.org> 0.9.8.4-alt1
- In pam_tcb, implemented proper fake salt creation to avoid a timing attack.

* Tue Apr 15 2003 Dmitry V. Levin <ldv@altlinux.org> 0.9.8.3-alt2
- Implemented proper dummy salt creation to avoid a timing attack.

* Sun Jan 12 2003 Dmitry V. Levin <ldv@altlinux.org> 0.9.8.3-alt1
- Updated to 0.9.8.3:
  * Thu Oct 31 2002 Solar Designer <solar@owl>
  - Optimized unix_verify_password() a bit, from Dmitry V. Levin of ALT Linux.
  * Wed Oct 30 2002 Solar Designer <solar@owl>
  - In tcb_convert.8, noted that /etc/shadow backups need to be removed as
    well, with /etc/shadow- as the particular example.
- Added control support for tcb_chkpwd, with three alternatives:
  "tcb" (default), "traditional" (for shadow/nis) and "restricted" (root only).

* Mon Oct 28 2002 Dmitry V. Levin <ldv@altlinux.org> 0.9.8.1-alt1
- Updated to 0.9.8.1:
  * Thu Oct 24 2002 Solar Designer <solar@owl>
  - Cleaned up the recent changes.
  * Mon Aug 19 2002 Rafal Wojtczuk <nergal@owl>
  - Merged enhancements which remove 32K users limit.
  - Added ENABLE_SETFSUGID.
  - Pass the username to the helper binary such that it can handle
    non-unique UIDs.
- tcb_chkpwd: optimized unix_verify_password() a bit.

* Mon Sep 02 2002 Dmitry V. Levin <ldv@altlinux.org> 0.9.7.4-alt2
- Use subst instead of perl for build.
- Updated devel-static requirements.

* Wed Aug 14 2002 Dmitry V. Levin <ldv@altlinux.org> 0.9.7.4-alt1
- 0.9.7.4:
  + Moved the pam_tcb and pam_unix manual pages to section 8.
  + No longer let root enforced password changes (sp_lstchg == 0) take
    precedence over expired accounts (sp_expire).
- Moved static library to devel-static subpackage.
- Fixed libtcb.so symlink (appeared to be broken in previous release).

* Tue May 21 2002 Dmitry V. Levin <ldv@altlinux.org> 0.9.7.1-alt1
- 0.9.7.1: relocated helper:
  /sbin/chkpwd.d/tcb_chkpwd --> %_libexecdir/chkpwd/tcb_chkpwd.

* Thu Feb 07 2002 Dmitry V. Levin <ldv@altlinux.org> 0.9.7-alt4
- Refined fsuid patch.

* Wed Feb 06 2002 Dmitry V. Levin <ldv@altlinux.org> 0.9.7-alt3
- libtcb/tcb_{drop,gain}_priv_r: use fsuid instead of euid.

* Thu Dec 20 2001 Dmitry V. Levin <ldv@altlinux.org> 0.9.7-alt2
- tcb_convert: try auth group by default.

* Thu Dec 13 2001 Dmitry V. Levin <ldv@altlinux.org> 0.9.7-alt1
- ALT adaptions, libification.

* Sun Dec 09 2001 Solar Designer <solar@owl.openwall.com>
- Various minor fixes from Dmitry V. Levin of ALT Linux.
- A GNU-style ChangeLog will now be maintained.

* Sun Nov 18 2001 Solar Designer <solar@owl.openwall.com>
- Patches from Nergal to make delays on failure work with the "fork"
option and to not produce a warning when su'ing to pseudo-users from
root.

* Fri Nov 16 2001 Solar Designer <solar@owl.openwall.com>
- Don't include the /sbin/chkpwd.d directory in this package as it's
provided by our pam package.
- Use a trigger on shadow-utils for possibly creating and making use of
group shadow.  This makes no difference on Owl as either the group is
provided by owl-etc (on new installs) or groupadd is already available
when this package is installed, but may be useful on hybrid systems.

* Thu Nov 15 2001 Solar Designer <solar@owl.openwall.com>
- Provide compatibility symlinks and a man page for pam_unix.
- tcb_convert(8) man page fixes from Nergal.
- Moved all of pam_tcb's prompts and messages to support.h and made them
more consistent with those used by pam_passwdqc.
- Improved logging.

* Thu Nov 01 2001 Solar Designer <solar@owl.openwall.com>
- Changed everything all over the place during October. ;-)

* Tue Sep 11 2001 Rafal Wojtczuk <nergal@owl.openwall.com>
- Makefiles and code layout rewrite.
- Added reentrant tcb_*_privs_r() functions, needed for nss.

* Sun Aug 19 2001 Rafal Wojtczuk <nergal@owl.openwall.com>
- version 0.5
- man pages
- nis fixes
- removed ugly _unix_getpwnam(), clean replacement

* Sat Aug 04 2001 Rafal Wojtczuk <nergal@owl.openwall.com>
- 0.4 packaged for Owl.
