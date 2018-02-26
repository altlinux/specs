Name: passwdqc
Version: 1.2.2
Release: alt1

Summary: A passphrase strength checking and policy enforcement toolset
License: LGPLv2+
Group: System/Base
Url: http://www.openwall.com/passwdqc/
Packager: Dmitry V. Levin <ldv@altlinux.org>

# http://www.openwall.com/passwdqc/%name-%version.tar.gz
Source: %name-%version-%release.tar

# due to PAM policy.
BuildRequires(pre): libpam-devel
# due to change in format of PAM modules requirements.
BuildRequires: rpm-build >= 0:4.0.4-alt55

%set_pam_name pam_%name

%package control
Summary: Control rules for the passwdqc passphrase quality checker
License: GPLv2+
Group: System/Base
BuildArch: noarch

%package -n lib%name
Summary: Passphrase quality checker shared library
License: LGPLv2+
Group: System/Libraries
PreReq: %name-control = %version-%release, control

%package -n lib%name-devel
Summary: Library and header file for building passwdqc-aware applications
License: LGPLv2+
Group: Development/C
Requires: lib%name = %version-%release

%package utils
Summary: Password quality checker utilities
License: GPLv2+
Group: System/Base
Requires: lib%name = %version-%release

%package -n %pam_name
Summary: Pluggable passphrase quality checker
License: LGPLv2+
Group: System/Base
Provides: pam_%name = %version-%release
Obsoletes: pam_%name
Requires: lib%name = %version-%release

%description
passwdqc is a passphrase strength checking and policy enforcement
toolset, including a PAM module (pam_passwdqc), command-line programs
(pwqcheck and pwqgen), and a library (libpasswdqc).

pam_passwdqc is normally invoked on passphrase changes by programs
such as passwd(1).  It is capable of checking password or passphrase
strength, enforcing a policy, and offering randomly-generated
passphrases, with all of these features being optional and easily
(re-)configurable.

pwqcheck and pwqgen are standalone passphrase strength checking and
random passphrase generator programs, respectively, which are usable
from scripts.

libpasswdqc is the underlying library, which may also be used from
third-party programs.

%description control
This package contains control rules for passphrase strength
checking library.  See control(8) for details.

%description -n lib%name
The libpasswdqc is a passphrase strength checking library.
In addition to checking regular passphrases, it offers support
for passphrases and can provide randomly generated passphrases.
All features are optional and can be (re-)configured without
rebuilding.

This package contains shared passwdqc library.

%description -n lib%name-devel
The libpasswdqc is a passphrase strength checking library.
In addition to checking regular passphrases, it offers support
for passphrases and can provide randomly generated passphrases.
All features are optional and can be (re-)configured without
rebuilding.

This package contains development library and header file
needed for building passwdqc-aware applications.

%description utils
This package contains standalone utilities which are usable from scripts:
pwqcheck (a standalone passphrase strength checking program),
and pwqgen (a standalone random passphrase generator program).

%description -n %pam_name
pam_passwdqc is a passphrase strength checking module for
PAM-aware passphrase changing programs, such as passwd(1).
In addition to checking regular passphrases, it offers support
for passphrases and can provide randomly generated passphrases.
All features are optional and can be (re-)configured without
rebuilding.

%prep
%setup -q -n %name-%version-%release

%build
%add_optflags -W -Werror
%make_build \
	CFLAGS_lib='%optflags %optflags_shared -DLINUX_PAM' \
	CFLAGS_bin='%optflags'

%install
%make_install install DESTDIR=%buildroot \
	SHARED_LIBDIR=/%_lib DEVEL_LIBDIR=%_libdir SECUREDIR=/%_lib/security
install -pD -m755 passwdqc.control \
        %buildroot%_controldir/passwdqc-enforce

%pre -n lib%name
%pre_control passwdqc-enforce

%post -n lib%name
%post_control -s users passwdqc-enforce

%files control
%config %_controldir/*

%files -n lib%name
%config(noreplace) /etc/passwdqc.conf
/%_lib/lib*.so*
%_man5dir/*
%doc LICENSE README PLATFORMS

%files -n lib%name-devel
%_libdir/lib*.so
%_includedir/*.h

%files -n %pam_name
/%_lib/security/*
%_man8dir/*

%files utils
%_bindir/*
%_man1dir/*

%changelog
* Fri Jul 16 2010 Dmitry V. Levin <ldv@altlinux.org> 1.2.2-alt1
- Merged with 1.2.2-owl1.

* Tue Mar 30 2010 Dmitry V. Levin <ldv@altlinux.org> 1.2.1-alt1
- Merged with 1.2.1-owl1.

* Tue Mar 16 2010 Dmitry V. Levin <ldv@altlinux.org> 1.2.0-alt1
- Merged with 1.2.0-owl1.

* Fri Nov 20 2009 Dmitry V. Levin <ldv@altlinux.org> 1.1.4-alt1
- Merged with 1.1.4-owl1.

* Thu Oct 22 2009 Dmitry V. Levin <ldv@altlinux.org> 1.1.3-alt1
- Merged with 1.1.3-owl1:
  + Added pw_dir checks to passwdqc_check(), similar to already existing
    pw_gecos checks.
  + Dropped undocumented support for multiple options per config file line.
  + Various portability fixes.
- Packaged -control subpackage as noarch.

* Wed Oct 21 2009 Dmitry V. Levin <ldv@altlinux.org> 1.1.2-alt1
- Merged with 1.1.2-owl1:
  + Ensure that pwqgen's exit status is zero only if generated
    passphrase has been printed successfully.
  + Changed pwqcheck to print "OK" line on success, and to print
    "Weak passphrase" diagnostics to stdout instead of stderr.

* Sun Oct 11 2009 Dmitry V. Levin <ldv@altlinux.org> 1.1.0-alt1
- Merged with 1.1.0-owl1:
  Added passwdqc.conf(5), pwqgen(1) and pwqcheck(1) manual pages.

* Sun Dec 14 2008 Dmitry V. Levin <ldv@altlinux.org> 1.1.0-alt0.7
- Removed obsolete %%post_ldconfig/%%postun_ldconfig calls.

* Thu Oct 30 2008 Dmitry V. Levin <ldv@altlinux.org> 1.1.0-alt0.6
- Fixed build with fresh gcc.

* Wed Feb 20 2008 Dmitry V. Levin <ldv@altlinux.org> 1.1.0-alt0.5
- Merged with 1.0.5-owl1:
  * Tue Feb 12 2008 Solar Designer <solar-at-owl.openwall.com> 1.0.5-owl1
  - Replaced the separator characters with some of those defined by RFC 3986
    as being safe within "userinfo" part of URLs without encoding.
  - Reduced the default value for the N2 parameter to min=... (the minimum
    length for passphrases) from 12 to 11.
  - Corrected the potentially misleading description of N2 (Debian bug #310595).
  - Applied minor grammar and style corrections to the documentation, a
    pam_passwdqc message, and source code comments.
- libpasswdqc: Detect and refuse nested file opening.
- pwqcheck: Documented stdin format.

* Tue Feb 05 2008 Dmitry V. Levin <ldv@altlinux.org> 1.1.0-alt0.4
- Added control(8) for /etc/passwdqc.conf (#12194).

* Fri Aug 10 2007 Dmitry V. Levin <ldv@altlinux.org> 1.1.0-alt0.3
- Reworked error reporting.

* Fri Jun 22 2007 Dmitry V. Levin <ldv@altlinux.org> 1.1.0-alt0.2
- Implemented config= parameter.
- Packaged /etc/passwdqc.conf file with default config.

* Tue Jun 19 2007 Dmitry V. Levin <ldv@altlinux.org> 1.1.0-alt0.1
- Created libpasswdqc shared library.
- Created pwqgen and pwqcheck utilities.

* Tue Apr 10 2007 Dmitry V. Levin <ldv@altlinux.org> 1.0.4-alt2
- Gearified.

* Sun Jun 04 2006 Dmitry V. Levin <ldv@altlinux.org> 1.0.4-alt1
- Updated to 1.0.4.

* Thu Jan 12 2006 Dmitry V. Levin <ldv@altlinux.org> 1.0.3-alt2
- Rebuilt for new style PAM dependencies generated by rpm-build-4.0.4-alt55.

* Wed Aug 24 2005 Dmitry V. Levin <ldv@altlinux.org> 1.0.3-alt1
- Updated to 1.0.3 (with all changes made in previous release applied).

* Tue Aug 09 2005 Dmitry V. Levin <ldv@altlinux.org> 1.0.2-alt1
- Updated to 1.0.2.
- Restricted list of global symbols exported by the pam module.
- Fixed potential memory leak in say().

* Tue Apr 19 2005 Dmitry V. Levin <ldv@altlinux.org> 1.0.1-alt1
- Updated to 1.0.1.

* Thu Feb 10 2005 Dmitry V. Levin <ldv@altlinux.org> 0.7.6-alt3
- Fixed multilib.

* Wed Feb 09 2005 Dmitry V. Levin <ldv@altlinux.org> 0.7.6-alt2
- Deal with compilation warnings generated on x86_64 platform.

* Sun Jan 30 2005 Dmitry V. Levin <ldv@altlinux.org> 0.7.6-alt1
- Updated to 0.7.6.

* Fri Jan 02 2004 Dmitry V. Levin <ldv@altlinux.org> 0.7.5-alt2
- Deal with compilation warnings generated by new gcc compiler.

* Sun Nov 09 2003 Dmitry V. Levin <ldv@altlinux.org> 0.7.5-alt1
- Updated to 0.7.5.

* Tue Oct 07 2003 Dmitry V. Levin <ldv@altlinux.org> 0.7.4-alt1
- Updated to 0.7.4.

* Thu Jun 05 2003 Dmitry V. Levin <ldv@altlinux.org> 0.7.3-alt2
- Fixed build with OpenPAM.
- Added Linux-PAM/OpenPAM multi-build support.

* Wed Mar 05 2003 Dmitry V. Levin <ldv@altlinux.org> 0.7.3-alt1
- Updated to 0.7.3, alt-makefile patch merged upstream:
  * Thu Oct 31 2002 Solar Designer <solar@owl.openwall.com>
  - When compiling with gcc, also link with gcc.
  - Use $(MAKE) to invoke sub-makes.
  * Fri Oct 04 2002 Solar Designer <solar@owl.openwall.com>
  - Solaris 9 notes in PLATFORMS.

* Tue Sep 24 2002 Dmitry V. Levin <ldv@altlinux.org> 0.7.1-alt1
- Updated to 0.7.1:
  * Wed Sep 18 2002 Solar Designer <solar@owl.openwall.com>
  - Build with Sun's C compiler cleanly, from Kevin Steves.
  - Use install -c as that actually makes a difference on at least HP-UX
  (otherwise install would possibly move files and not change the owner).
  * Fri Sep 13 2002 Solar Designer <solar@owl.openwall.com>
  - Have the same pam_passwdqc binary work for both trusted and non-trusted
  HP-UX, from Kevin Steves.
  * Fri Sep 06 2002 Solar Designer <solar@owl.openwall.com>
  - Use bigcrypt() on HP-UX whenever necessary, from Kevin Steves of Atomic
  Gears LLC.
  - Moved the old password checking into a separate function.

* Mon Aug 05 2002 Dmitry V. Levin <ldv@altlinux.org> 0.6-alt1
- 0.6:
  * Sat Jul 27 2002 Solar Designer <solar@owl.openwall.com>
  - Documented that the man page is under the 3-clause BSD-style license.
  * Tue Jul 23 2002 Solar Designer <solar@owl.openwall.com>
  - Applied minor corrections to the man page and at the same time eliminated
  unneeded/unimportant differences between it and the README.
  * Sun Jul 21 2002 Solar Designer <solar@owl.openwall.com>
  - 0.5.1: imported the pam_passwdqc(8) manual page back from FreeBSD.
  * Tue Apr 16 2002 Solar Designer <solar@owl.openwall.com>
  - 0.5: preliminary OpenPAM (FreeBSD-current) support in the code and related
  code cleanups (thanks to Dag-Erling Smorgrav).

* Thu Dec 20 2001 Dmitry V. Levin <ldv@alt-linux.org> 0.4-alt3
- Rebuilt (to fix documentation permissions).

* Tue Nov 13 2001 Dmitry V. Levin <ldv@alt-linux.org> 0.4-alt2
- Corrected Url (thanx to Solar for the hint).

* Sun Nov 04 2001 Dmitry V. Levin <ldv@alt-linux.org> 0.4-alt1
- 0.4

* Fri Feb 02 2001 Dmitry V. Levin <ldv@fandra.org> 0.3-ipl1
- RE adaptions.

* Mon Oct 30 2000 Solar Designer <solar@owl.openwall.com>
- 0.3: portability fixes (this might build on non-Linux-PAM now).

* Fri Sep 22 2000 Solar Designer <solar@owl.openwall.com>
- 0.2: added "use_authtok", added README.

* Fri Aug 18 2000 Solar Designer <solar@owl.openwall.com>
- 0.1, "retry_wanted" bugfix.

* Sun Jul 02 2000 Solar Designer <solar@owl.openwall.com>
- Initial version (non-public).
