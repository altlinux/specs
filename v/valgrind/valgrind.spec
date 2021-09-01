Name: valgrind
Version: 3.17.0
Release: alt3

Summary: Valgrind, an open-source memory debugger for GNU/Linux
License: GPLv2+
Group: Development/Other
URL: http://www.valgrind.org/
Source: https://sourceware.org/pub/valgrind/%name-%version.tar

Patch1: gdbserver_tests-update-filters-for-newer-glibc-gdb.patch
Patch2: helgrind-and-drd-suppression-libc-and-libpthread.patch
Patch3: valgrind-alt-arm.patch
Patch4: valgrind-alt-loongson-is-mips.patch
Patch5: valgrind-alt-vki_siginfo.patch
Patch6: valgrind-rh-cachegrind-improvements.patch
Patch7: valgrind-rh-ldso-supp.patch
Patch8: valgrind-rh-alt-some-stack-protector.patch
Patch9: valgrind-rh-some-Wl-z-now.patch
Patch10: valgrind-rh-ppc64-isa-3.1.patch
Patch11: valgrind-rh-ppc64-isa-3.1-tests.patch
Patch12: valgrind-rh-debuginfod.patch
Patch13: valgrind-rh-clone-parent-res.patch
Patch14: valgrind-rh-clone3.patch
Patch15: valgrind-rh-_start.patch
Patch16: valgrind-rh-ppc64-statfs64.patch
Patch17: valgrind-rh-vgdb-queued-signals.patch
Patch18: valgrind-rh-ppc64-test-isa-3-1.patch
Patch19: valgrind-rh-ppc64-pstxvp.patch

# Apparently, nobody cares whether valgrind works on arm or not.
%ifarch %arm
%def_disable check
%endif

# valgrind needs /proc to work
Requires: /proc
%{?!_disable_check:BuildRequires: /proc gdb-light}

BuildRequires: gcc-c++

%description
Valgrind is an instrumentation framework for building dynamic analysis
tools.  There are Valgrind tools that can automatically detect many
memory management and threading bugs, and profile your programs in
detail.  You can also use Valgrind to build new tools.  The Valgrind
distribution currently includes six production-quality tools: a memory
error detector (memcheck, the default tool), two thread error
detectors (helgrind and drd), a cache and branch-prediction profiler
(cachegrind), a call-graph generating cache and branch-prediction
profiler (callgrind), and a heap profiler (massif).

%package devel
Summary: Development files for %name
License: BSD-style
Group: Development/Other
Requires: %name = %version-%release

%description devel
The valgrind-devel subpackage contains header files with macros to
manipulate and query Valgrind's execution from within the client
program.  The resulting executables will still run without Valgrind,
just a little bit more slowly than they otherwise would, but otherwise
unchanged.

When run on Valgrind with --client-perms=yes, Valgrind observes these
macro calls and takes appropriate action.  When run on Valgrind with
--client-perms=no (the default), Valgrind observes these macro calls
but does not take any action as a result.

%package tool-devel
Summary: Header files and libraries for compiling Valgrind tools
Group: Development/Other
Requires: %name-devel = %version-%release

%description tool-devel
The valgrind-tool-devel subpackage contains header files and libraries
needed to compile Valgrind tools separately from the Valgrind core.


%prep
%setup
%autopatch -p1

%build
# Filter out some flags that cause lots of valgrind test failures.
# Also filter away -O2, valgrind adds it wherever suitable, but
# not for tests which should be -O0, as they aren't meant to be
# compiled with -O2 unless explicitely requested.
%define optflags_optimization %nil

# LTO triggers undefined symbols, and configure --enable-lto doesn't help.
%define optflags_lto %nil

%ifarch %arm
# On arm valgrind explicitly sets -marm -mcpu=cortex-a8.
%remove_optflags -mthumb -march=armv7-a
%endif

autoreconf -vi

# Use gdb-light as gdb.
export ac_cv_path_GDB=%_bindir/gdb-light

# Currently there is no usable MPI implementation in Sisyphus.
%configure \
	--without-mpicc

%make_build

%install
%makeinstall_std

mv %buildroot%_docdir/%name{,-%version}
install -m644 -p AUTHORS FAQ.txt NEWS \
	%buildroot%_docdir/%name-%version/

# Most of ELF objects should not be stripped - see README_PACKAGERS
%brp_strip_none %_libexecdir/%name/*

%check
if [ ! -r /proc/self/exe ]; then
	echo '/proc/self/exe is not available, regression test SKIPPED' >&2
	exit
fi

# Make sure a basic binary runs.
./vg-in-place --error-exitcode=1 /bin/echo

%make_build CFLAGS= check ||:

echo "===============TESTING==================="
make nonexp-regtest ||:
find -type f -name '*.diff' |sort
echo "===============END TESTING==============="

%files
%_bindir/*
%_libexecdir/%name/
%exclude %_libdir/%name/lib*.a
%_docdir/%name-%version/
%exclude %_docdir/%name-%version/valgrind_manual.ps
%_mandir/*/*

%files devel
%dir %_includedir/%name/
%_includedir/%name/valgrind.h
%_includedir/%name/callgrind.h
%_includedir/%name/helgrind.h
%_includedir/%name/memcheck.h

%files tool-devel
%_includedir/%name/
%exclude %_includedir/%name/valgrind.h
%exclude %_includedir/%name/callgrind.h
%exclude %_includedir/%name/helgrind.h
%exclude %_includedir/%name/memcheck.h
%dir %_libdir/%name/
%_libdir/%name/lib*.a
%_pkgconfigdir/%name.pc


%changelog
* Wed Sep 01 2021 Dmitry V. Levin <ldv@altlinux.org> 3.17.0-alt3
- Synced with valgrind-3.17.0-12 from Fedora.

* Mon Jul 19 2021 Dmitry V. Levin <ldv@altlinux.org> 3.17.0-alt2
- Disabled %%check on arm (closes: #40446).

* Fri Jul 09 2021 Dmitry V. Levin <ldv@altlinux.org> 3.17.0-alt1
- 3.16.1 -> 3.17.0.
- Synced with valgrind-3.17.0-6 from Fedora.

* Tue Aug 18 2020 Dmitry V. Levin <ldv@altlinux.org> 3.16.1-alt1
- 3.16.0 -> 3.16.1.
- Synced with valgrind-3.16.1-5 from Fedora.

* Thu May 28 2020 Dmitry V. Levin <ldv@altlinux.org> 3.16.0-alt1
- 3.15.0 -> 3.16.0.
- Synced with valgrind-3.16.0-2 from Fedora.

* Tue Apr 16 2019 Dmitry V. Levin <ldv@altlinux.org> 3.15.0-alt1
- 3.14.0 -> 3.15.0.
- Synced with valgrind-3.15.0-1 from Fedora.

* Fri Mar 08 2019 Dmitry V. Levin <ldv@altlinux.org> 3.14.0-alt3
- Synced with valgrind-3.14.0-16 from Fedora.
- Fixed siginfo_t definition on 64-bit architectures.

* Wed Feb 20 2019 Dmitry V. Levin <ldv@altlinux.org> 3.14.0-alt2
- Made valgrind work on Loongson 3A CPUs
  (at least for mips32r2 binaries; by iv@).
- Merged with valgrind-3.14.0-13 from Fedora.
- %%check: use gdb-light instead of gdb.

* Tue Oct 09 2018 Dmitry V. Levin <ldv@altlinux.org> 3.14.0-alt1
- 3.13.0 -> 3.14.0.

* Sun Nov 05 2017 Dmitry V. Levin <ldv@altlinux.org> 3.13.0-alt1
- Merged with valgrind-3.13.0-10 from Fedora.

* Thu Jul 20 2017 Dmitry V. Levin <ldv@altlinux.org> 3.13.0-alt1
- Updated to 3.13.0.
- Merged with valgrind-3.13.0-4 from Fedora.

* Mon Nov 16 2015 Dmitry V. Levin <ldv@altlinux.org> 3.11.0-alt1
- Updated to 3.11.0.
- Merged with valgrind-3.11.0-5 from Fedora.

* Fri Nov 14 2014 Dmitry V. Levin <ldv@altlinux.org> 3.10.0-alt1
- Updated to 3.10.0.
- Merged with valgrind-3.10.0-5 from Fedora.

* Mon Mar 25 2013 Dmitry V. Levin <ldv@altlinux.org> 3.8.1-alt2
- Fixed build with glibc 2.17.

* Wed Oct 03 2012 Dmitry V. Levin <ldv@altlinux.org> 3.8.1-alt1
- Updated to 3.8.1.
- Merged with valgrind-3.8.1-2 from Fedora.

* Mon Jun 18 2012 Dmitry V. Levin <ldv@altlinux.org> 3.7.0-alt1
- Updated to 3.7.0 release (closes: #27411).
- Backported upstream build fixes.
- Merged with Fedora valgrind-3.7.0-4 (by legion@).

* Thu Dec 08 2011 Dmitry V. Levin <ldv@altlinux.org> 3.6.1-alt3
- Added /proc requirement.

* Fri Dec 02 2011 Dmitry V. Levin <ldv@altlinux.org> 3.6.1-alt2
- Fixed build on Linux 3.x.

* Thu May 05 2011 Dmitry V. Levin <ldv@altlinux.org> 3.6.1-alt1
- Updated to 3.6.1 release.
- Merged with Fedora valgrind-3.6.1-1.

* Fri Nov 12 2010 Dmitry V. Levin <ldv@altlinux.org> 3.6.0-alt1
- Updated to 3.6.0 release.
- Merged with Fedora valgrind-3.6.0-1.

* Thu Nov 26 2009 Dmitry V. Levin <ldv@altlinux.org> 3.5.0-alt1
- Updated to 3.5.0 release.

* Tue May 26 2009 Dmitry V. Levin <ldv@altlinux.org> 3.4.1-alt1
- Updated to 3.4.1 release.

* Fri Feb 20 2009 Dmitry V. Levin <ldv@altlinux.org> 3.4.0-alt1
- Updated to 3.4.0 release.

* Fri Dec 12 2008 Dmitry V. Levin <ldv@altlinux.org> 3.3.1-alt2
- Merged rh-glibc29.patch from FC valgrind-3.3.0-4.

* Sun Nov 09 2008 Sergey Vlasov <vsu@altlinux.ru> 3.3.1-alt1
- 3.3.1 release.
- Removed obsolete patches from SVN:
  - svn-r5966-detect-only64bit
  - svn-r5967-sendto-display-fix
- Removed obsolete alt-xorg-7.0-suppressions patch.
- Updated rh-openat patch from Fedora (valgrind-3.3.0-3).
- Updated alt-fix-only64bit, ald-glibc-suppressions patches.
- Removed -fno-stack-protector addition from spec file (the configure script
  adds this option automatically since 3.0.0).
- Moved %name.pc from %name-devel to %name-tool-devel due to
  library references which cause cyclic dependencies otherwise.

* Sun Mar 11 2007 Sergey Vlasov <vsu@altlinux.ru> 3.2.3-alt1
- 3.2.3 release.
- Removed rh-alt-glibc25 patch (glibc 2.5 support merged upstream).
- Removed rh-makefile patch (VEX/Makefile bug fixed upstream).
- Removed rh-cfa-set-loc patch (fixed upstream).
- Updated alt-pkgconfig patch (upstream fix still is not correct).

* Thu Oct 19 2006 Sergey Vlasov <vsu@altlinux.ru> 3.2.1-alt1
- 3.2.1 release.
- Removed obsolete patches from SVN (merged in 3.2.1 release):
  - svn-r5968-futex-args
  - svn-r5970-more-tty-ioctls
- Added patches from FC6 package:
  + rh-alt-glibc25: add glibc-2.5 support (removed part which patches the
    generated configure script - it is regenerated anyway)
  + rh-makefile: fix broken conditionals in VEX/Makefile
  + rh-openat: fix openat syscall handling
  + rh-cfa-set-loc: fix CFA_set_loc address handling in DWARF reader
- Added patches:
  + alt-pkgconfig: fix unexpanded @VG_PLATFORM@ in valgrind.pc
  + alt-regtest: fix regression test problems:
    - memcheck/tests/x86/scalar: fix getgroups test failure in hasher
      (satellite user has no supplementary groups)
- Use uncompressed tarball in src.rpm.
- Build with -fno-stack-protector (support functions for -fstack-protector are
  in glibc, but core Valgrind parts are not linked with glibc).
- Run regression test after build (can be turned off with --disable check).
  Test failure does not really abort the build now - some tests are broken.
  Stolen from Fedora package by Jakub Jelinek <jakub at redhat dot com>.
  Note: regression test needs /proc in the build environment.

* Thu Jun 15 2006 Sergey Vlasov <vsu@altlinux.ru> 3.2.0-alt1
- 3.2.0 release.
- WARNING: Code sequences used for client requests have been changed by
  upstream developers in an incompatible way!  All programs which were using
  header files from valgrind-devel must be recompiled with new headers.
- Added callgrind.h to valgrind-devel subpackage (new tool in 3.2.0).
- Removed all %%__* macro abuse from spec.
- Explicitly disabled MPI support (configure picks up mpicc from lam-devel,
  which does not really work - current Sisyphus package contains only static
  libraries, and MPI support in Valgrind requires a shared MPI library).
- Removed alt-x86_64-no-biarch patch (obsolete).
- Added patches from upstream SVN repository:
  + svn-r5966-detect-only64bit: automatically detect pure 64 bit systems with
    no 32 bit support
  + svn-r5967-sendto-display-fix: fix display of buffer address in sendto
    system call arguments on x86_64
  + svn-r5968-futex-args: validate futex system call arguments more carefully
    (fixes spurious uninitialized value errors)
  + svn-r5970-more-tty-ioctls: implement some more terminal ioctls
- Added alt-fix-only64bit patch: fix "make regtest" on pure 64 bit systems
  (the regression testing script still attempted to run 32-bit tests).

* Thu Mar 16 2006 Sergey Vlasov <vsu@altlinux.ru> 3.1.1-alt1
- 3.1.1 release.
- Removed obsolete patches from SVN.
- Removed alt-oset-64bit patch (fixed upstream).

* Wed Feb 01 2006 Sergey Vlasov <vsu@altlinux.ru> 3.1.0-alt1
- 3.1.0 release.
- Removed old obsolete patches.
- Added patches from SVN VALGRIND_3_1_BRANCH:
  - svn-r5257-disable-yield-test: disable none/tests/x86/yield test which fails
    randomly
  - svn-r5260-amd64-getpriority: enable getpriority and setpriority syscalls on
    x86_64
  - svn-r5320-cachegrind-misattribution: fix misattributions of counts in
    cachegrind when a function name was used in more than one module
  - svn-r5448-debugger-cmdline: make more space for debugger command line
  - svn-r5449-cg_annotate-sort: cg_annotate: fix broken --sort option
  - svn-r5450-memcheck-reads-freed-mem: fix access to freed memory in memcheck
  - svn-r5451-oset-64bit-fastcmp: fix OSet 64-bit fastcmp bug
  - svn-r5478-internal-error-message: make it clearer that internal errors are
    Valgrind's fault
  - svn-r5479-dwarf2-line-numbers: read dwarf2 line number information even if
    a .debug_str section was not found
  - svn-r5480-leakcheck-assertion: fix wrong assertions in leak checker
  - svn-r5481-gen-suppressions: fix a minor --gen-suppressions output bug
  - svn-r5492-xorg-6.9-suppression: update suppression for Xorg 6.9.0
- Added alt-x86_64-no-biarch patch: disable building of 32-bit (x86) version on
  x86_64 (does not work because 32-bit libgcc is missing).
- Added alt-oset-64bit patch: fix memcheck/tests/oset_test after applying
  svn-r5451-oset-64bit-fastcmp patch.
- Removed %%set_verify_elf_method textrel=relaxed, which is no longer needed
  with valgrind-3.1.0.
- Removed "chstk -e" workaround for ancient buggy versions of the Openwall
  kernel patch.
- Added valgrind-tool-devel subpackage for internal headers and static
  libraries which are useful only for building Valgrind tools; valgrind-devel
  now contains only headers for client-to-Valgrind communication.
- Fixed license for valgrind-devel (these particular headers are BSD-licensed,
  unlike the rest of Valgrind).
- Added alt-xorg-7.0-suppressions patch: suppressions for Xorg 7.0 libraries.
- Added alt-glibc-suppressions patch: more glibc suppressions (workaround for
  broken backtrace from some internal glibc parts).
- Updated BuildRequires.

* Thu May 19 2005 Sergey Vlasov <vsu@altlinux.ru> 2.4.0-alt1
- 2.4.0 release.
- Removed obsolete alt-sigreturn, alt-direct-syscall, alt-pad-check patches.
- Added alt-funobj-suppression patch: allow optional specification of shared
  object name after function name in suppressions (fun:FUNCTION:OBJECT).
- Updated alt-suppressions patch for 2.4.0 and glibc-2.3.5; now using the
  funobj suppression feature for strchr errors in /lib/ld-linux.so.2 (using
  just fun:index hides all errors in strchr/index, using just
  obj:/lib/ld-linux.so.2 hides all errors detected in that object).
- Updated alt-intercept-strmem patch for 2.4.0.
- Removed AutoProv and __find_requires hacks from spec (no longer required).

* Wed Jun 02 2004 Sergey Vlasov <vsu@altlinux.ru> 2.1.2-alt0.3.20040522
- Fixed fcntl F_GETLK64, F_SETLK64, F_SETLKW64 handling in alt-direct-syscall
  patch.
- Added alt-pad-check patch: exit immediately if as_pad fails instead of
  mysteriously crashing later (can happen if hard address space limits are
  configured).

* Sat May 22 2004 Sergey Vlasov <vsu@altlinux.ru> 2.1.2-alt0.2.20040522
- 20040522 CVS snapshot:
  + teach Massif about the 'nothrow' versions of new and new[]
- Added alt-direct-syscall patch: make libpthread wrappers invoke syscalls
  directly instead of using __libc_* wrappers (which are no longer exported in
  recent glibc versions).

* Wed May 05 2004 Sergey Vlasov <vsu@altlinux.ru> 2.1.2-alt0.1.20040505
- 20040505 CVS snapshot.
- Filter out GLIBC_PRIVATE dependencies.
- Enable executable stack (workaround for GCC trampoline handling bug in the
  Openwall kernel patch).
- Added alt-sigreturn patch: workaround for signal return handling bug in the
  Openwall kernel patch.
- Added alt-suppressions patch: suppress false memcheck error in
  /lib/ld-2.3.3.so (strchr is over-optimized, and the intercept mechanism
  cannot replace it that early).
- Added alt-intercept-strmem patch: use the new intercept mechanism instead of
  symbol override for str*/mem* function replacement (symbol override does not
  work with glibc-2.3.3 because of PLT bypassing, and this leads to lots of
  false errors detected by memcheck).
- Updated BuildRequires.

* Sun Jan 04 2004 Sergey Vlasov <vsu@altlinux.ru> 2.0.0-alt1
- 2.0.0 stable release.
- Updated URL.
- Relaxed TEXTREL check (the low-level code cannot be made PIC).
- Updated BuildRequires.

* Wed Oct 08 2003 Sergey Vlasov <vsu@altlinux.ru> 2.0-alt0.20030725
- 20030725 snapshot.
- Added BuildPreReq: kernel-headers-std.

* Thu May 22 2003 Sergey Vlasov <vsu@altlinux.ru> 1.9.6-alt1
- 1.9.6 release.
- Updated BuildRequires.
- Fixed devel subpackage dependencies.
- Spec file cleanup.

* Thu Nov 21 2002 Sergey Vlasov <vsu@altlinux.ru> 1.0.4-alt1
- 1.0.4 release.
- Do not strip shared libraries.
- Added BuildRequires.

* Mon Jul 29 2002 Alexander Bokovoy <ab@altlinux.ru>
- Initial build.

