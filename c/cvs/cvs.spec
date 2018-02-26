Name: cvs
Version: 1.11.23
Release: alt5

Summary: A version control system
License: GPLv2+
Group: Development/Other
Url: http://www.nongnu.org/cvs/

# ftp://ftp.gnu.org/non-gnu/cvs/source/stable/%version/cvs-%version.tar.bz2
Source: cvs-%version.tar

Source1: cvsrc
Source2: cvs.sh
Source4: cvs.xinetd
Source5: cvs-pserver
Source6: cvs-pserver.conf
Source7: cvs-pserver.8
Source8: cvsinitroot
Source9: cvs-README.ALT

Patch1: cvs-1.11.23-up-CVE-2010-3846.patch
Patch11: cvs-1.11.23-alt-remove-unused.patch
Patch12: cvs-1.11.23-owl-fixes.patch
Patch13: cvs-1.11.23-alt-texinfo.patch
Patch14: cvs-1.11.23-alt-version.patch
Patch15: cvs-1.11.23-alt-errno.patch
Patch16: cvs-1.11.23-alt-vitmp.patch
Patch17: cvs-1.11.23-owl-no-world-writables.patch
Patch18: cvs-1.11.23-alt-mdk-owl-canonicalize.patch
Patch19: cvs-1.11.23-alt-cvsbug-ypcat.patch
Patch20: cvs-1.11.23-owl-alt-tmp.patch
Patch21: cvs-1.11.23-deb-alt-doc.patch
Patch22: cvs-1.11.23-bsd-deb-local_branch_num.patch
Patch23: cvs-1.11.23-deb-normalize_cvsroot.patch
Patch24: cvs-1.11.23-deb-expand_keywords-alphanumeric.patch
Patch25: cvs-1.11.23-deb-server-wrapper.patch
Patch26: cvs-1.11.23-deb-fast-edit.patch
Patch27: cvs-1.11.23-alt-password_entry_operation.patch
Patch28: cvs-1.11.23-deb-alt-homedir.patch
Patch29: cvs-1.11.23-deb-alt-newlines.patch
Patch30: cvs-1.11.23-alt-cvsrc.patch
Patch31: cvs-1.11.23-alt-tagloginfo.patch
Patch32: cvs-1.11.23-alt-xasprintf.patch
Patch33: cvs-1.11.23-alt-env.patch
Patch34: cvs-1.11.23-alt-server-log.patch
Patch35: cvs-1.11.23-deb-alt-LocalKeyword-KeywordExpand.patch
Patch36: cvs-1.11.23-alt-noreadlock.patch
Patch37: cvs-1.11.23-alt-ssh.patch
Patch38: cvs-1.11.23-alt-config.patch
Patch39: cvs-1.11.23-alt-format.patch
Patch40: cvs-1.11.23-alt-testsuite-fixes.patch
Patch41: cvs-1.11.23-alt-testsuite-sleep.patch

Requires: mktemp >= 1:1.3.1, vitmp

# The cvsadmin group check must be disabled to run CVS test suit.
%{?!_without_check:%{?!_disable_check:BuildRequires: groupdel-cvsadmin}}
%{?!_without_check:%{?!_disable_check:BuildConflicts: cvs < 0:1.11.2-alt1}}

# Automatically added by buildreq on Thu Jan 16 2003
BuildRequires: zlib-devel

%description
CVS means Concurrent Version System; it is a version control
system which can record the history of your files (usually,
but not always, source code).  CVS only stores the differences
between versions, instead of every version of every file
you've ever created.  CVS also keeps a log of who, when and
why changes occurred, among other aspects.

CVS is very helpful for managing releases and controlling
the concurrent editing of source files among multiple
authors.  Instead of providing version control for a
collection of files in a single directory, CVS provides
version control for a hierarchical collection of
directories consisting of revision controlled files.

These directories and files can then be combined together
to form a software release.

%package pserver
Summary: CVS pserver script, documentation and default configuration
Group: System/Servers
Requires: %name = %version-%release
BuildArch: noarch

%description pserver
cvs-pserver is a wrapper around CVS which loads some default variables.
It is normally run by xinetd.

%package doc
Summary: Various documentation about the CVS
Group: Development/Other
Conflicts: %name < %version-%release, %name > %version-%release
BuildArch: noarch

%description doc
Various documentation about the Concurrent Version System.

%package contrib
Summary: Contributed soft for the CVS
Group: Development/Other
Requires: %name = %version-%release
BuildArch: noarch

%description contrib
Contributed soft for the Concurrent Version System.

%prep
%setup

# Remove useless/harmful stuff to ensure it will not be suddently used.
rm -rf emx os2 windows-NT vms zlib
find -type f \( -name getopt\* -o -name regex.\* -o -name getdate.c \) \
	-delete -print

# Fix dos-style lines.
r=$(printf '\r')
find contrib -type f -print0 |
	xargs -r0 grep -Zl "$r\$" -- |
	xargs -r0 sed -i "s/$r\$//g" --
unset r

%patch1
%patch11 -p1
%patch12 -p1
%patch13 -p1
%patch14 -p1
%patch15 -p1
%patch16 -p1
%patch17 -p1
%patch18 -p1
%patch19 -p1
%patch20 -p1
%patch21 -p1
%patch22 -p1
%patch23 -p1
%patch24 -p1
%patch25 -p1
%patch26 -p1
%patch27 -p1
%patch28 -p1
%patch29 -p1
%patch30 -p1
%patch31 -p1
%patch32 -p1
%patch33 -p1
%patch34 -p1
%patch35 -p1
%patch36 -p1
%patch37 -p1
%patch38 -p1
%patch39 -p1
%patch40 -p1
%patch41 -p1

find -type f \( -size 0 -o -name \*~ -o -name \*.orig -o -name .cvsignore \) -delete
sed -i 's|${TMPDIR}/cvs-serv|${TMPDIR:-/tmp}/cvs-serv|g' src/sanity.sh

# Fix texinfo warnings.
sed -i 's/@strong{Note:/@strong{Please notice:/' doc/cvs.texinfo

%build
%add_optflags -D_GNU_SOURCE

export ac_cv_func_mkstemp=yes \
	ac_cv_lib_nsl_main=no \
	ac_cv_path_CSH=/bin/csh \
	ac_cv_path_PERL=%__perl \
	ac_cv_path_PS2PDF=/usr/bin/ps2pdf \
	ac_cv_path_ROFF=/usr/bin/groff \
	ac_cv_path_SENDMAIL=/usr/sbin/sendmail \
	ac_cv_path_TEXI2DVI=/usr/bin/texi2dvi \
	ac_cv_prog_with_default_rsh=ssh \
	ac_cv_prog_with_default_ssh=ssh \
	#

%autoreconf
%configure \
	--with-rsh=ssh \
	--with-ssh=ssh \
	--with-tmpdir=/tmp \
	--with-editor=/bin/vitmp \
	--without-gssapi \
	#
%make_build
bzip2 -9 ChangeLog FAQ NEWS TODO

%check
export TMPDIR=/tmp
%make_build check

%install
%makeinstall_std install-info

install -pD -m755 %_sourcedir/cvs-pserver %buildroot%_sbindir/cvs-pserver
install -pD -m600 %_sourcedir/cvs-pserver.conf %buildroot%_sysconfdir/cvs/pserver.conf
install -pD -m644 %_sourcedir/cvs-pserver.8 %buildroot%_man8dir/cvs-pserver.8

install -pD -m644 %_sourcedir/cvsrc %buildroot%_sysconfdir/cvs/cvsrc
install -pD -m755 %_sourcedir/cvs.sh %buildroot%_sysconfdir/profile.d/cvs.sh
install -pD -m640 %_sourcedir/cvs.xinetd %buildroot%_sysconfdir/xinetd.d/cvs
install -pD -m755 %_sourcedir/cvsinitroot %buildroot%_sbindir/cvsinitroot

install -dm3770 %buildroot/var/lock/cvs

%define docdir %_docdir/%name-%version
rm -rf %buildroot%docdir
install -pD -m644 %_sourcedir/cvs-README.ALT \
	%buildroot%docdir/README.ALT
install -pm644 \
	AUTHORS *BUGS DEVEL-CVS HACKING PROJECTS README *.bz2 doc/*.pdf \
	%buildroot%docdir/

%pre
/usr/sbin/groupadd -rf cvs
/usr/sbin/groupadd -rf cvsadmin

%files
%attr(3770,root,cvs) %dir /var/lock/cvs
%attr(755,root,root) %dir %_sysconfdir/cvs
%config(noreplace) %_sysconfdir/cvs/cvsrc
%config(noreplace) %_sysconfdir/profile.d/*sh
%_bindir/cvs*
%_sbindir/cvsinitroot
%_man1dir/*
%_man5dir/*
%_man8dir/cvsbug.*
%_infodir/*.info*
%dir %docdir
%docdir/[A-Z]*

%files pserver
%attr(755,root,root) %dir %_sysconfdir/cvs
%config(noreplace) %_sysconfdir/cvs/pserver.conf
%config(noreplace) %_sysconfdir/xinetd.d/*
%_sbindir/cvs-pserver
%_man8dir/cvs-pserver.*

%files doc
%dir %docdir
%docdir/*.pdf

%files contrib
%_bindir/rcs*
%_datadir/cvs

%changelog
* Mon Dec 05 2011 Dmitry V. Levin <ldv@altlinux.org> 1.11.23-alt5
- Worked around timestamp issues in test suite.

* Fri Dec 03 2010 Dmitry V. Levin <ldv@altlinux.org> 1.11.23-alt4
- Applied upstream fix to an array index error, leading to a heap-based
  buffer overflow, found in the way CVS applied certain delta fragment
  changes from input files in the RCS (Revision Control System) file
  format.  If an attacker in control of a CVS repository stored a
  specially-crafted RCS file in that repository, this could result in
  arbitrary code execution with the privileges of the CVS server process
  on the system hosting the CVS repository when a remote user eventually
  checks out a revision of the affected file.
  Special thanks to Owl for the description.
  (CVE-2010-3846; closes: #24468).

* Wed Sep 09 2009 Dmitry V. Levin <ldv@altlinux.org> 1.11.23-alt3
- Moved "make check" to %%check section.

* Sun Jun 07 2009 Dmitry V. Levin <ldv@altlinux.org> 1.11.23-alt2
- Removed obsolete %%install_info/%%uninstall_info calls.
- Fixed some compilation warnings.
- Updated testsuite fixes.
- Enabled test suite by default.
- Packaged doc, pserver and contrib subpackages as noarch.

* Sat May 10 2008 Dmitry V. Levin <ldv@altlinux.org> 1.11.23-alt1
- Updated to 1.11.23.

* Tue Oct 09 2007 Dmitry V. Levin <ldv@altlinux.org> 1.11.22-alt3
- Synced with 1.11.22-owl1.

* Wed Aug 01 2007 Dmitry V. Levin <ldv@altlinux.org> 1.11.22-alt2
- Fixed "cvs login" crash introduced in cvs-1.11.22 (#12439).

* Sun Apr 15 2007 Dmitry V. Levin <ldv@altlinux.org> 1.11.22-alt1
- Updated to 1.11.22.

* Fri Sep 30 2005 Dmitry V. Levin <ldv@altlinux.org> 1.11.21-alt1
- Updated to 1.11.21.

* Thu Sep 29 2005 Dmitry V. Levin <ldv@altlinux.org> 1.11.20-alt2
- Patched gcc -Wall warnings (Owl).
- Patched texinfo warnings.
- Reviewed and rediffed patches.
- Updated LocalKeyword and KeywordExpand support to match
  cvs-1.12.x behaviour.

* Wed May 11 2005 Dmitry V. Levin <ldv@altlinux.org> 1.11.20-alt1
- Updated to 1.11.20.
- Updated patches.

* Wed Apr 06 2005 Dmitry V. Levin <ldv@altlinux.org> 1.11.19-alt1
- Updated to 1.11.19.
- Updated patches.
- Applied upstream security fixes for CAN-2005-0753 issue.

* Thu Jun 17 2004 Dmitry V. Levin <ldv@altlinux.org> 1.11.17-alt1
- Updated to 1.11.17.
- Updated patches.

* Tue Jun 08 2004 Dmitry V. Levin <ldv@altlinux.org> 1.11.15-alt4
- Applied upstream security fixes to CAN-2004-0414, CAN-2004-0416,
  CAN-2004-0417, CAN-2004-0418, and to some minor bugs which didn't
  appear to deserve CVE names.  Thanks to Stefan Esser, Sebastian
  Krahmer, and Derek Robert Price for finding and fixing these.

* Tue May 25 2004 Dmitry V. Levin <ldv@altlinux.org> 1.11.15-alt3
- Applied upstream fix for pserver heap overflow (CAN-2004-0414).

* Mon May 10 2004 Dmitry V. Levin <ldv@altlinux.org> 1.11.15-alt2
- Applied upstream fix for pserver heap overflow (CAN-2004-0396).

* Thu Apr 15 2004 Dmitry V. Levin <ldv@altlinux.org> 1.11.15-alt1
- Updated to 1.11.15.
- Updated patches.

* Wed Apr 07 2004 Dmitry V. Levin <ldv@altlinux.org> 1.11.14-alt2
- Applied upstream pserver client fixes (CAN-2004-0180).

* Sat Mar 20 2004 Dmitry V. Levin <ldv@altlinux.org> 1.11.14-alt1
- Updated to 1.11.14.
- Updated patches.

* Wed Jan 21 2004 Dmitry V. Levin <ldv@altlinux.org> 1.11.11-alt2
- Set cvs_rsh transport to ssh by default again
  (was broken since 1.11.10-alt1).

* Sat Jan 10 2004 Dmitry V. Levin <ldv@altlinux.org> 1.11.11-alt1
- Updated to 1.11.11.

* Sat Dec 20 2003 Dmitry V. Levin <ldv@altlinux.org> 1.11.10-alt1
- Updated to 1.11.10.
- Reviewed and updated patches.
- Removed devnull patch introduced in 1.11.2-alt1;
  empty readonly regular file "/dev/null" inside chroot jail is enough.
- Implemented CVSNOREADLOCK environment variable support.
- In CVSROOT/config, LockDir=/var/lock/cvs is no longer enabled
  by default, for compatibility with other cvs vendors.
  That is, LockDir should be explicitly uncommented after
  run of "cvs init" to get previous behaviour.

* Fri Dec 12 2003 Dmitry V. Levin <ldv@altlinux.org> 1.11.2-alt4
- Backported change from cvs-1.11.10 to reject absolute module paths.
- Reworked the temporary file handling patch (#3183).
- In canonicalize patch, handle the special case when the last path
  component doesn't yet exist and thus can't be canonicalized (Owl).
- Fixed typo in cvs-pserver (#2506).

* Thu Jan 16 2003 Dmitry V. Levin <ldv@altlinux.org> 1.11.2-alt3
- Applied fixes from Stefan Esser.

* Sun Nov 17 2002 Dmitry V. Levin <ldv@altlinux.org> 1.11.2-alt2
- cvs.xinetd: set nice and rlimit_as resource limits for pserver.
- cvs_pserver: clear TMPDIR variable (as well as HOME). 
- Merged in Debian patches:
  + added "-alt" to version number;
  + a fix from upstream which unbroke the watch commands was commited;
  + fixed up some typos in the man page;
  + made it possible to diff files named --foo and similar;
  + added note to cvs.texinfo explaining what the parameters to cvs import is;
  + fixed keyword handling to accept alphanumerics, not just alphabetics;
  + added fix to avoid spawn an editor on a remote system;
  + disabled init over pserver.

* Wed May 29 2002 Dmitry V. Levin <ldv@altlinux.org> 1.11.2-alt1
- 1.11.2, redone patches.
- Patched to support new automake/autoconf.
- Updated tmp races cleanup patch (now covers all shell scripts).
- Added xasprintf function for internal needs.
- Patched cvs server to work without /dev/null.
- Set default editor to vitmp.
- Updated RH patches: 1.11.1p1-authserver, 1.11.1p1-krb4.
- Merged in Debian patches:
  + newlines_in_commit_template;
  + fast_edit;
  + BSD_LOCAL_BRANCH_NUM;
  + create_cvspass;
  + normalize_correct_roots;
  + server_wrapper;
  + local_tag_expansions;
  + history_val-tag_world_writeable;
  + homedir;
  + parseopts;
  + cvs-pserver(8) manpage.
- Dropped mmap patch (unmaintained).
- /etc/cvs/cvsrc: empty by default.
- Renamed cvspserver to cvs-pserver.
- Changed cvs-pserver config from /etc/cvs/cvs.conf to /etc/cvs/pserver.conf.
- Moved cvs-pserver to pserver subpackage.
- Relocated cvsinitroot from %_bindir/ to %_sbindir/.
- Updated dependencies.
- Relocated docs.

* Sat Mar 10 2001 Dmitry V. Levin <ldv@fandra.org> 1.11-ipl4mdk
- Set cvs_rsh transport to ssh by default.
- Safe open files.

* Wed Dec 06 2000 Dmitry V. Levin <ldv@fandra.org> 1.11-ipl3mdk
- Fixed:
  + bug in lock_name();
  + script cvspserver (option -f was resurrected).

* Tue Nov 21 2000 Dmitry V. Levin <ldv@fandra.org> 1.11-ipl2mdk
- Implemented tagloginfo support.
- Fixed texinfo documentation.

* Wed Oct 18 2000 Dmitry V. Levin <ldv@fandra.org> 1.11-ipl1mdk
- 1.11
- Merged MDK and RH patches.

* Tue Apr 11 2000 Dmitry V. Levin <ldv@fandra.org>
- 1.10.8

* Wed Nov 10 1999 Dmitry V. Levin <ldv@fandra.org>
- env patch

* Wed Sep 21 1999 Dmitry V. Levin <ldv@fandra.org>
- Fandra adaptions

* Wed May 19 1999 Bernhard Rosenkränzer <bero@mandrakesoft.com>
- Fix several .spec bugs
- Update to 1.10.6

* Tue May 18 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- Bzipped info files.

* Tue May 11 1999 Bernhard Rosenkraenzer <bero@mandrakesoft.com>
- Mandrake adaptations

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com>
- auto rebuild in the new build environment (release 2)

* Mon Feb 22 1999 Jeff Johnson <jbj@redhat.com>
- updated text in spec file.

* Mon Feb 22 1999 Jeff Johnson <jbj@redhat.com>
- update to 1.10.5.

* Tue Feb  2 1999 Jeff Johnson <jbj@redhat.com>
- update to 1.10.4.

* Tue Oct 20 1998 Jeff Johnson <jbj@redhat.com>
- update to 1.10.3.

* Mon Sep 28 1998 Jeff Johnson <jbj@redhat.com>
- update to 1.10.2.

* Wed Sep 23 1998 Jeff Johnson <jbj@redhat.com>
- remove trailing characters from rcs2log mktemp args

* Thu Sep 10 1998 Jeff Johnson <jbj@redhat.com>
- update to 1.10.1

* Mon Aug 31 1998 Jeff Johnson <jbj@redhat.com>
- fix race conditions in cvsbug/rcs2log

* Sun Aug 16 1998 Jeff Johnson <jbj@redhat.com>
- update to 1.10.

* Wed Aug 12 1998 Jeff Johnson <jbj@redhat.com>
- update to 1.9.30.

* Mon Jun 08 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr

* Mon Jun  8 1998 Jeff Johnson <jbj@redhat.com>
- build root
- update to 1.9.28

* Mon Apr 27 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Wed Oct 29 1997 Otto Hammersmith <otto@redhat.com>
- added install-info stuff
- added changelog section
