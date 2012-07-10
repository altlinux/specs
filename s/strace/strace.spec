Name: strace
Version: 4.7
Release: alt3

Summary: Tracks and displays system calls associated with a running process
License: BSD-style
Group: Development/Debuggers
Url: http://sourceforge.net/projects/strace/

# http://git.altlinux.org/gears/s/strace.git
Source: %name-%version-%release.tar

# due to use of deprecated -k option
Conflicts: rpm-utils <= 0:0.9.11-alt1

BuildRequires: libacl-devel libaio-devel

%package utils
Summary: Processes strace output and displays a graph of invoked subprocesses
Group: Development/Debuggers
BuildArch: noarch
Requires: %name = %version-%release

%description
The strace program intercepts and records the system calls called and
the signals received by a running process.  strace can print a record of
each system call, its arguments and its return value.  strace is useful
for diagnosing problems and debugging, as well as for instructional
purposes.

%description utils
The strace-graph Perl script processes strace -f output and displays
a graph of invoked subprocesses.  It is useful for finding out what
complex commands do.

%prep
%setup -n %name-%version-%release

%build
%autoreconf
%configure --enable-gcc-Werror #--enable-maintainer-mode
# Assume that adjust_kernel_headers --first has been run.
%make_build IOCTLDIR=/usr/include/linux/../../include

%install
%makeinstall_std

%check
make check

%files
%_bindir/strace
%_bindir/strace-log-merge
%_mandir/man?/*
%doc COPYRIGHT CREDITS NEWS README README-linux-ptrace

%files utils
%_bindir/strace-graph

%changelog
* Tue Jul 10 2012 Dmitry V. Levin <ldv@altlinux.org> 4.7-alt3
- Updated to v4.7-15-g26bc060.

* Tue May 15 2012 Dmitry V. Levin <ldv@altlinux.org> 4.7-alt2
- Updated to v4.7-7-gd376c92.

* Wed May 02 2012 Dmitry V. Levin <ldv@altlinux.org> 4.7-alt1
- Updated to v4.7.

* Tue May 01 2012 Dmitry V. Levin <ldv@altlinux.org> 4.6-alt14
- Updated to v4.6-398-ga5fd66b.

* Thu Apr 19 2012 Dmitry V. Levin <ldv@altlinux.org> 4.6-alt13
- Updated to v4.6-382-gebee04c.

* Sun Apr 08 2012 Dmitry V. Levin <ldv@altlinux.org> 4.6-alt12
- Updated to v4.6-373-g0cbed35.

* Mon Mar 26 2012 Dmitry V. Levin <ldv@altlinux.org> 4.6-alt11
- Updated to v4.6-369-g4372cc9.

* Mon Mar 26 2012 Dmitry V. Levin <ldv@altlinux.org> 4.6-alt10
- Updated to v4.6-364-g378f9c5.

* Fri Mar 16 2012 Dmitry V. Levin <ldv@altlinux.org> 4.6-alt9
- Updated to v4.6-318-g4a0ffea.

* Mon Mar 12 2012 Dmitry V. Levin <ldv@altlinux.org> 4.6-alt8
- Updated to v4.6-285-g328bf25.

* Wed Feb 08 2012 Dmitry V. Levin <ldv@altlinux.org> 4.6-alt7
- Updated to v4.6-228-gbdec9cb.

* Wed Jan 18 2012 Dmitry V. Levin <ldv@altlinux.org> 4.6-alt6
- Updated to v4.6-193-g7d55801.

* Sun Jan 08 2012 Dmitry V. Levin <ldv@altlinux.org> 4.6-alt5
- Updated to v4.6-182-gf1e6903.

* Tue Oct 11 2011 Dmitry V. Levin <ldv@altlinux.org> 4.6-alt4
- Updated to v4.6-148-gd99e48c.

* Sat Jun 25 2011 Dmitry V. Levin <ldv@altlinux.org> 4.6-alt3
- Updated to v4.6-60-g9015cd9.

* Fri Apr 08 2011 Dmitry V. Levin <ldv@altlinux.org> 4.6-alt2
- Updated to v4.6-2-g8a08277 (adds new strace options: -y and -P).

* Tue Mar 15 2011 Dmitry V. Levin <ldv@altlinux.org> 4.6-alt1
- Updated to v4.6.

* Mon Mar 14 2011 Dmitry V. Levin <ldv@altlinux.org> 4.6-alt0.1
- Updated to v4.5.20-109-g50e69cb.

* Sun Mar 06 2011 Dmitry V. Levin <ldv@altlinux.org> 4.5.20-alt10
- Updated to v4.5.20-102-g6c0e2fc.

* Fri Feb 25 2011 Dmitry V. Levin <ldv@altlinux.org> 4.5.20-alt9
- Updated to v4.5.20-89-ga6ca968.

* Thu Feb 17 2011 Dmitry V. Levin <ldv@altlinux.org> 4.5.20-alt8
- Updated to v4.5.20-64-g65c1a81.
- Built with libaio-devel for better decoding of io_* syscalls.

* Mon Jan 31 2011 Dmitry V. Levin <ldv@altlinux.org> 4.5.20-alt7
- Updated to v4.5.20-61-g50a218d.

* Tue Dec 07 2010 Dmitry V. Levin <ldv@altlinux.org> 4.5.20-alt6
- Updated to v4.5.20-42-g8044bc1 (closes: #24705).

* Fri Dec 03 2010 Dmitry V. Levin <ldv@altlinux.org> 4.5.20-alt5
- Updated to v4.5.20-41-gbdafa1a.

* Fri Sep 17 2010 Dmitry V. Levin <ldv@altlinux.org> 4.5.20-alt4
- Updated to v4.5.20-33-gdcd3a6f.

* Sun Aug 29 2010 Dmitry V. Levin <ldv@altlinux.org> 4.5.20-alt3
- Packaged strace-utils subpackage as noarch.

* Sun Aug 29 2010 Dmitry V. Levin <ldv@altlinux.org> 4.5.20-alt2
- Updated to v4.5.20-17-g21b8db4.

* Wed Apr 14 2010 Dmitry V. Levin <ldv@altlinux.org> 4.5.20-alt1
- Updated to v4.5.20 release.

* Wed Apr 07 2010 Dmitry V. Levin <ldv@altlinux.org> 4.5.19-alt3
- Updated to v4.5.19-37-gae4db5e.

* Fri Nov 06 2009 Dmitry V. Levin <ldv@altlinux.org> 4.5.19-alt2
- Updated to v4.5.19-8-g9906e6d.

* Wed Oct 21 2009 Dmitry V. Levin <ldv@altlinux.org> 4.5.19-alt1
- Updated to v4.5.19 release.

* Sat Oct 10 2009 Dmitry V. Levin <ldv@altlinux.org> 4.5.19-alt0.2
- Updated to v4.5.18-137-g76ac37d from
  git://strace.git.sourceforge.net/gitroot/strace/strace

* Sat Sep 19 2009 Dmitry V. Levin <ldv@altlinux.org> 4.5.19-alt0.1
- Updated to v4.5.18-111-gfbfed22 from
  git://strace.git.sourceforge.net/gitroot/strace/strace

* Thu Sep 03 2009 Dmitry V. Levin <ldv@altlinux.org> 4.5.18-alt8
- Updated to v4.5.18-102-g99c8569 from
  git://strace.git.sourceforge.net/gitroot/strace/strace

* Tue Jul 07 2009 Dmitry V. Levin <ldv@altlinux.org> 4.5.18-alt7
- Updated to v4.5.18-96-geb9e2e8 from
  git://strace.git.sourceforge.net/gitroot/strace

* Mon Jun 01 2009 Dmitry V. Levin <ldv@altlinux.org> 4.5.18-alt6
- Updated to cvs snapshot 20090601.

* Fri Jan 02 2009 Dmitry V. Levin <ldv@altlinux.org> 4.5.18-alt5
- Updated to cvs snapshot 20090101.

* Mon Nov 10 2008 Dmitry V. Levin <ldv@altlinux.org> 4.5.18-alt4
- sock_ioctl: Parse more SIOCS* ioctls.
- Fixed several corner cases in printpathn() and printstr().
- Updated capability flags and prctl values from linux-2.6.27.

* Thu Oct 23 2008 Dmitry V. Levin <ldv@altlinux.org> 4.5.18-alt3
- Implemented parsers for socket type flags introduced in linux 2.6.27.
- Implemented parsers for new syscalls introduced in linux 2.6.27.

* Mon Sep 29 2008 Dmitry V. Levin <ldv@altlinux.org> 4.5.18-alt2
- strace: exit/kill with traced child's exitcode/signal.
  This change makes -k option obsolete.

* Sat Aug 30 2008 Dmitry V. Levin <ldv@altlinux.org> 4.5.18-alt1
- Updated to cvs snapshot 20080828.

* Thu Jul 24 2008 Dmitry V. Levin <ldv@altlinux.org> 4.5.17-alt2
- Fix -F option backwards compatibility.

* Wed Jul 23 2008 Dmitry V. Levin <ldv@altlinux.org> 4.5.17-alt1
- Updated to cvs snapshot 20080722.

* Sat Apr 19 2008 Dmitry V. Levin <ldv@altlinux.org> 4.5.16-alt5
- Updated to cvs snapshot 20080326 with tcb changes reverted.
- Implemented timeout decoders for interrupted syscalls.
- Fixed and enabled prctl decoder.
- Updated errnoent.h
- Applied several fixes submitted to strace-devel.

* Sun Oct 14 2007 Dmitry V. Levin <ldv@altlinux.org> 4.5.16-alt4
- Updated to cvs snapshot 20071014.

* Mon Sep 24 2007 Dmitry V. Levin <ldv@altlinux.org> 4.5.16-alt3
- net.c (printsock): Output AF_UNIX socket address using
  printstr() to avoid unprintable characters in output.
- stream.c (decode_poll): Rearrange parser to decode input and
  output parameters separately.
- Reworked struct timespec decoders for better multiarch support.
- desc.c (sys_pselect6): Decode signal mask when entering syscall.

* Sat Sep 22 2007 Dmitry V. Levin <ldv@altlinux.org> 4.5.16-alt2
- Updated to cvs snapshot 20070712.
- Reverted attach/detach changes from Jan Kratochvil for a while
  because they introduced too many regressions.

* Mon Aug 06 2007 Dmitry V. Levin <ldv@altlinux.org> 4.5.16-alt1
- Updated to 4.5.16 release.

* Mon Jul 16 2007 Dmitry V. Levin <ldv@altlinux.org> 4.5.15-alt4
- Updated to cvs snapshot 20070711.

* Fri Mar 30 2007 Dmitry V. Levin <ldv@altlinux.org> 4.5.15-alt3
- Added linux SG_IO ioctl parser, based on patch from Vladimir Nadvornik.
- Add MAP_32BIT support, based on patch from Kirill A. Shutemov.

* Tue Jan 16 2007 Dmitry V. Levin <ldv@altlinux.org> 4.5.15-alt2
- Updated to cvs snapshot 20070113:
  Enhanced mount parser (ldv).

* Sat Jan 13 2007 Dmitry V. Levin <ldv@altlinux.org> 4.5.15-alt1
- Updated to cvs snapshot 20070113:
  Fixed adjtimex modes parser (ldv);
  Enhanced umount parser (ldv);
  Fixed open(2) flags parser (ldv, RH#222385);
  Bumped version to 4.5.15 (roland).
- Enhanced sock_ioctl parser (ldv).

* Thu Dec 21 2006 Dmitry V. Levin <ldv@altlinux.org> 4.5.14-alt8
- Further biarch fixes for counts and internal syscalls.

* Sat Dec 16 2006 Dmitry V. Levin <ldv@altlinux.org> 4.5.14-alt7
- Updated to cvs snapshot 20061213:
  Fixed -ff -o behaviour (ldv, RH#218435);
  Enhanced fix for piping trace output (ldv, RH#204950);
  Fixed biarch for readv/writev (jj, RH#218433);
  Fixed biarch for time related functions (ldv, RH#171626, RH#173050);
  Enhanced adjtimex parser (ldv).
- Enhanced mount and umount parsers (ldv).
- Fixed biarch for -c (ldv, RH#192193)
- Fixed biarch for internal syscalls (ldv, RH#179740).

* Mon Dec 04 2006 Dmitry V. Levin <ldv@altlinux.org> 4.5.14-alt6
- Updated to cvs snapshot 20061204:
  Fix build against 2.6.18+ headers (jj).

* Tue Oct 17 2006 Dmitry V. Levin <ldv@altlinux.org> 4.5.14-alt5
- Updated to cvs snapshot 20061016:
  Merge fixes made in 4.5.14-alt{2..4};
  Merge my enhanced quotactl parser.

* Fri Oct 06 2006 Dmitry V. Levin <ldv@altlinux.org> 4.5.14-alt4
- Fixed build with new glibc headers.

* Fri Sep 01 2006 Dmitry V. Levin <ldv@altlinux.org> 4.5.14-alt3
- Updated to cvs snapshot 20060822.
- Fixed memory corruption bug in print_xattr_val() (ldv, RH#200621).
- Fixed handling of untraced processes in trace() (ldv, RH#204950).
- Added hooks for new syscalls in 2.6.1[67] kernels,
  added decoders for *at, inotify*, pselect6, ppoll and unshare
  syscalls (RH#178633).

* Wed Mar 29 2006 Dmitry V. Levin <ldv@altlinux.org> 4.5.14-alt2
- Fixed race condition in tcb allocation code.

* Tue Jan 17 2006 Dmitry V. Levin <ldv@altlinux.org> 4.5.14-alt1
- Updated to 4.5.14.

* Fri Jan 13 2006 Dmitry V. Levin <ldv@altlinux.org> 4.5.13-alt5
- Updated to cvs snapshot 20060112.
- Merged upstream patches:
  alt-mount (RH#165377)
  owl-man (RH#165375)
  drepper-x86_64-ipc (RH#164755)
  drepper-msgrcv (RH#164757)
  alt-qual_syscall (RH#174798)
  alt-qual_flags (RH#173986)

* Thu Nov 17 2005 Dmitry V. Levin <ldv@altlinux.org> 4.5.13-alt4
- Implemented qual_flags support for each personality.

* Tue Nov 15 2005 Dmitry V. Levin <ldv@altlinux.org> 4.5.13-alt3
- Implemented numeric syscall qualifier specification handling.

* Sat Oct 22 2005 Dmitry V. Levin <ldv@altlinux.org> 4.5.13-alt2
- Updated to cvs snapshot 20051021, to fix for potential
  buffer overflow in printpathn().

* Mon Aug 08 2005 Dmitry V. Levin <ldv@altlinux.org> 4.5.13-alt1
- Updated to 4.5.13.
- Applied few ipc patches from Ulrich Drepper.
- Rediffed patches.

* Thu Aug 04 2005 Dmitry V. Levin <ldv@altlinux.org> 4.5.12-alt4
- Updated to cvs snapshot 20050719.
- Merged upstream patches:
  alt-TF (RH#159340)
  alt-TD (RH#159400)

* Sat Jul 16 2005 Dmitry V. Levin <ldv@altlinux.org> 4.5.12-alt3
- Corrected mount(2) deparser (RH#165377).

* Sat Jun 18 2005 Dmitry V. Levin <ldv@altlinux.org> 4.5.12-alt2
- Rewritten quotactl(2) deparser (RH#118696).

* Fri Jun 10 2005 Dmitry V. Levin <ldv@altlinux.org> 4.5.12-alt1
- Updated to 4.5.12.
- Merged upstream patches:
  alt-static (RH#159688).
- Rediffed other patches.

* Sat Jun 04 2005 Dmitry V. Levin <ldv@altlinux.org> 4.5.11-alt6
- Updated to cvs snapshot 20050607.
- Merged upstream patches:
  alt-linkage (RH#158488)
  alt-mem-fixes (RH#159196)
  alt-oom (RH#159308)
  alt-printflags (RH#159310)
- Minor namespace cleanup (RH#159688).
- Rediffed other patches.

* Wed Jun 01 2005 Dmitry V. Levin <ldv@altlinux.org> 4.5.11-alt5
- Removed TRACE_FILE flag from those syscalls
  which have no filename argument (RH#159340).
- Introduced "-e trace=desc" (RH#159400).

* Mon May 30 2005 Dmitry V. Levin <ldv@altlinux.org> 4.5.11-alt4
- Fixed several MM issues (RH#159196).
- Unitized OOM errors reporting (RH#159308).
- Enhanced printflags() semantics (RH#159310).

* Sun May 29 2005 Dmitry V. Levin <ldv@altlinux.org> 4.5.11-alt3
- Updated to cvs snapshot 20050526.

* Sun May 22 2005 Dmitry V. Levin <ldv@altlinux.org> 4.5.11-alt2
- Updated to cvs snapshot 20050509.
- Fixed to build with default kernel headers.

* Thu Mar 24 2005 Dmitry V. Levin <ldv@altlinux.org> 4.5.11-alt1
- Updated to 4.5.11.

* Tue Mar 15 2005 Dmitry V. Levin <ldv@altlinux.org> 4.5.10-alt1
- Updated to 4.5.10.

* Thu Feb 24 2005 Dmitry V. Levin <ldv@altlinux.org> 4.5.9-alt2
- Updated to cvs snapshot 20050204.
- Merged upstream patches:
  alt-fake_execve (RH#143365)

* Sat Feb 05 2005 Dmitry V. Levin <ldv@altlinux.org> 4.5.9-alt1
- Updated to 4.5.9.
- Merged upstream patches:
  alt-qual (RH#143362)
  alt-call_summary (RH#143369)
  alt-gnu_source (RH#143370)

* Mon Dec 20 2004 Dmitry V. Levin <ldv@altlinux.org> 4.5.8-alt2
- Fixed multiply qualifying expression bugs.
- Fixed "strace -i" misbehaviour.
- Fixed segfault in "strace -c".
- Fixed GNU_SOURCE handling.

* Mon Oct 25 2004 Dmitry V. Levin <ldv@altlinux.org> 4.5.8-alt1
- Updated to 4.5.8.
- Merged upstream patches:
  alt-ioctl-scsi (RH#129808)
  rh-printmsghdr-scm (RH#131689)
  alt-ioctl-rtc (RH#58606)

* Mon Sep 13 2004 Dmitry V. Levin <ldv@altlinux.org> 4.5.7-alt3
- Improved rtc ioctls handling.

* Mon Sep 13 2004 Dmitry V. Levin <ldv@altlinux.org> 4.5.7-alt2
- Added SCSI ioctl names.
- Improved sendmsg/recvmsg handling.

* Tue Aug 31 2004 Dmitry V. Levin <ldv@altlinux.org> 4.5.7-alt1
- Updated to 4.5.7.
- Merged upstream patches:
  alt-parse_sigset (RH#128091)

* Sat Jul 17 2004 Dmitry V. Levin <ldv@altlinux.org> 4.5.6-alt1
- Updated to 4.5.6.

* Mon Jul 12 2004 Dmitry V. Levin <ldv@altlinux.org> 4.5.5-alt2
- Fixed signal parser.

* Wed Jun 30 2004 Dmitry V. Levin <ldv@altlinux.org> 4.5.5-alt1
- Updated to 4.5.5.

* Fri Jun 04 2004 Dmitry V. Levin <ldv@altlinux.org> 4.5.4-alt1
- Updated to 4.5.4.
- Merged upstream patches:
  alt-linux-ioctlent (RH#122257)

* Sun May 02 2004 Dmitry V. Levin <ldv@altlinux.org> 4.5.3-alt2
- Added more ioctl names.
- Regenerated ioctl list from linux-2.6.5.

* Sun Apr 18 2004 Dmitry V. Levin <ldv@altlinux.org> 4.5.3-alt1
- Updated to 4.5.3.
- Merged upstream patches:
  alt-quotactl-fix (RH#118694)

* Thu Mar 18 2004 Dmitry V. Levin <ldv@altlinux.org> 4.5.2-alt2
- Fixed output of the quotactl command parser.

* Thu Mar 04 2004 Dmitry V. Levin <ldv@altlinux.org> 4.5.2-alt1
- Updated to 4.5.2.
- Merged upstream patches:
  alt-trace-coredump (RH#112117)

* Mon Dec 15 2003 Dmitry V. Levin <ldv@altlinux.org> 4.5.1-alt1
- Updated to 4.5.1.
- Merged upstream patches:
  owl-ioctl (RH#105358)
  alt-output (except line buffering for piped output)
  alt-ugid32_syscalls (RH#105359)
- Rediffed:
  owl-alt-fixes
  owl-man
  alt-pipe-setlinebuf
  alt-trace-coredump
  alt-keep_status

* Tue Oct 21 2003 Dmitry V. Levin <ldv@altlinux.org> 4.5-alt1
- Updated to 4.5.

* Sat Sep 06 2003 Dmitry V. Levin <ldv@altlinux.org> 4.4.99-alt1
- Updated to 4.4.99.
- Reviewed patches:
  + merged upstream or obsolete:
    all RH patches.
  + reworked:
    owl-alt-fixes
    owl-man
    owl-ioctl
    alt-output
    alt-keep_status
    alt-ugid32_syscalls
- Updated build dependencies.

* Fri Sep 05 2003 Dmitry V. Levin <ldv@altlinux.org> 4.4-alt6
- Corrected strace behaviour in case of piped output redirection.

* Sun Nov 24 2002 Dmitry V. Levin <ldv@altlinux.org> 4.4-alt5
- Fixed kernel-2.4.x specific uid32 syscalls handling.

* Wed Oct 30 2002 Dmitry V. Levin <ldv@altlinux.org> 4.4-alt4
- Reverted signal.c back to revision 1.31 (as in strace-4.4);
  this should fix strace hangups (#0001326).
- Merged RH patches (4.4-8):
  + fixed modify_ldt handling;
  + added/fixed handing for the following syscalls:
    getpmsg, putpmsg, lchown32, getuid32, readahead, sendfile64,
    setxattr, fsetxattr, getxattr, fgetxattr, listxattr, flistxattr,
    removexattr, fremovexattr, sched_setaffinity, sched_getaffinity,
    futex, set_thread_area, get_thread_area;
  + added SA_RESTORER handling.

* Tue Jun 11 2002 Dmitry V. Levin <ldv@altlinux.org> 4.4-alt3
- Updated to current CVS version (post-4.4) with an additional fix for
  displaying all possible ioctl names when there's more than one match,
  some build fixes, and a RH-derived patch for detaches from
  multi-threaded programs (Owl).
- Changed group tag to "Development/Debuggers".

* Thu May 23 2002 Stanislav Ievlev <inger@altlinux.ru> 4.4-alt2
- Added subpackage to remove deps on perl-base in main package.

* Thu Aug 30 2001 Dmitry V. Levin <ldv@altlinux.ru> 4.4-alt1
- 4.4

* Tue Oct 24 2000 Dmitry V. Levin <ldv@fandra.org> 4.2-ipl3mdk
- Enabled all LFS patches and rebuilt with LFS-aware kernel-headers.

* Tue Oct 17 2000 Dmitry V. Levin <ldv@fandra.org> 4.2-ipl2mdk
- Added fcntl64 patch.

* Tue Oct 03 2000 Dmitry V. Levin <ldv@fandra.org> 4.2-ipl1mdk
- Merged in RH patches.
- Added keep_status feature.

* Tue Mar 28 2000 Dmitry V. Levin <ldv@fandra.org>
- 4.2

* Sat Nov 27 1999 Dmitry V. Levin <ldv@fandra.org>
- Fandra adaptions

* Fri Nov 26 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- 4.1.

* Mon Nov 08 1999 John Buswell <johnb@mandrakesoft.com>
- Commented out KERN_SECURELVL from system.c (this is not in sysctl.h in
  2.2.13 kernel)
- Build Release

* Mon Jul 12 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- 4.00.

* Wed Apr 28 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- Update to 3.99.

* Tue Apr 06 1999 Preston Brown <pbrown@redhat.com>
- strip binary

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com>
- auto rebuild in the new build environment (release 16)

* Tue Feb  9 1999 Jeff Johnson <jbj@redhat.com>
- vfork est arrive!

* Tue Feb  9 1999 Christopher Blizzard <blizzard@redhat.com>
- Add patch to follow clone() syscalls, too.

* Sun Jan 17 1999 Jeff Johnson <jbj@redhat.com>
- patch to build alpha/sparc with glibc 2.1.

* Thu Dec 03 1998 Cristian Gafton <gafton@redhat.com>
- patch to build on ARM

* Wed Sep 30 1998 Jeff Johnson <jbj@redhat.com>
- fix typo (printf, not tprintf).

* Sat Sep 19 1998 Jeff Johnson <jbj@redhat.com>
- fix compile problem on sparc.

* Tue Aug 18 1998 Cristian Gafton <gafton@redhat.com>
- buildroot

* Mon Jul 20 1998 Cristian Gafton <gafton@redhat.com>
- added the umoven patch from James Youngman <jay@gnu.org>
- fixed build problems on newer glibc releases

* Mon Jun 08 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr
