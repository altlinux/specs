Name: gdb
Version: 7.9
Release: alt3

Summary: A GNU source-level debugger for C, C++ and other languages
License: GPLv3+
Group: Development/Debuggers
Url: http://www.gnu.org/software/gdb/

# ftp://sourceware.org/pub/gdb/releases/gdb-%version.tar.bz2
Source: gdb-%version.tar
# Cleanup any leftover testsuite processes as it may stuck hasher builds.
Source2: gdb-orphanripper.c
# Man page for gstack(1).
Source3: gdb-gstack.man

Patch1: gdb-alt-testsuite-version.patch
Patch2: gdb-alt-readline.patch
Patch3: gdb-alt-bfd.patch

### Debian patches
Patch11: dwarf2-cfi-warning.patch
Patch13: linux-clear-thread-list.patch

### Fedora patches
# Work around out-of-date dejagnu that does not have KFAIL
#=drop: That dejagnu is too old to be supported.
Patch101: gdb-6.3-rh-dummykfail-20041202.patch
# Better parse 64-bit PPC system call prologues.
#=maybepush+ppc: Write new testcase.
Patch105: gdb-6.3-ppc64syscall-20040622.patch
# Include the pc's section when doing a symbol lookup so that the
# correct symbol is found.
#=maybepush: Write new testcase.
Patch111: gdb-6.3-ppc64displaysymbol-20041124.patch
# Fix upstream `set scheduler-locking step' vs. upstream PPC atomic seqs.
#=push+work: It is a bit difficult patch, a part is ppc specific.
Patch112: gdb-6.6-scheduler_locking-step-sw-watchpoints2.patch
# Make upstream `set scheduler-locking step' as default.
#=push+work: How much is scheduler-locking relevant after non-stop?
Patch260: gdb-6.6-scheduler_locking-step-is-default.patch
# Add a wrapper script to GDB that implements pstack using the
# --readnever option.
#=push+work: with gdbindex maybe --readnever should no longer be used.
Patch118: gdb-6.3-gstack-20050411.patch
# VSYSCALL and PIE
#=fedoratest
Patch122: gdb-6.3-test-pie-20050107.patch
#=push: May get obsoleted by Tom's unrelocated objfiles patch.
Patch389: gdb-archer-pie-addons.patch
#=push+work: Breakpoints disabling matching should not be based on address.
Patch394: gdb-archer-pie-addons-keep-disabled.patch
# Get selftest working with sep-debug-info
#=fedoratest
Patch125: gdb-6.3-test-self-20050110.patch
# Test support of multiple destructors just like multiple constructors
#=fedoratest
Patch133: gdb-6.3-test-dtorfix-20050121.patch
# Fix to support executable moving
#=fedoratest
Patch136: gdb-6.3-test-movedir-20050125.patch
# Test sibling threads to set threaded watchpoints for x86 and x86-64
#=fedoratest
Patch145: gdb-6.3-threaded-watchpoints2-20050225.patch
# Notify observers that the inferior has been created
#=fedoratest
Patch161: gdb-6.3-inferior-notification-20050721.patch
# Verify printing of inherited members test
#=fedoratest
Patch163: gdb-6.3-inheritancetest-20050726.patch
# Add readnever option
#=push
Patch164: gdb-6.3-readnever-20050907.patch
# Fix debuginfo addresses resolving for --emit-relocs Linux kernels (BZ 203661).
#=push+work: There was some mail thread about it, this patch may be a hack.
Patch188: gdb-6.5-bz203661-emit-relocs.patch
# Support TLS symbols (+`errno' suggestion if no pthread is found) (BZ 185337).
#=push+work: It should be replaced by existing uncommitted Roland's glibc patch for TLS without libpthreads.
Patch194: gdb-6.5-bz185337-resolve-tls-without-debuginfo-v2.patch
# Fix TLS symbols resolving for shared libraries with a relative pathname.
# The testsuite needs `gdb-6.5-tls-of-separate-debuginfo.patch'.
#=fedoratest+work: One should recheck if it is really fixed upstream.
Patch196: gdb-6.5-sharedlibrary-path.patch
# Suggest fixing your target architecture for gdbserver(1) (BZ 190810).
# FIXME: It could be autodetected.
#=push+work: There are more such error cases that can happen.
Patch199: gdb-6.5-bz190810-gdbserver-arch-advice.patch
# Testcase for deadlocking on last address space byte; for corrupted backtraces.
#=fedoratest
Patch211: gdb-6.5-last-address-space-byte-test.patch
# Improved testsuite results by the testsuite provided by the courtesy of BEA.
#=fedoratest+work: For upstream it should be rewritten as a dejagnu test, the test of no "??" was useful.
Patch208: gdb-6.5-BEA-testsuite.patch
# Fix readline segfault on excessively long hand-typed lines.
#=fedoratest
Patch213: gdb-6.5-readline-long-line-crash-test.patch
# Fix bogus 0x0 unwind of the thread's topmost function clone(3) (BZ 216711).
#=fedora
Patch214: gdb-6.5-bz216711-clone-is-outermost.patch
# Test sideeffects of skipping ppc .so libs trampolines (BZ 218379).
#=fedoratest
Patch216: gdb-6.5-bz218379-ppc-solib-trampoline-test.patch
# Fix lockup on trampoline vs. its function lookup; unreproducible (BZ 218379).
#=fedora
Patch217: gdb-6.5-bz218379-solib-trampoline-lookup-lock-fix.patch
# Find symbols properly at their original (included) file (BZ 109921).
#=fedoratest
Patch225: gdb-6.5-bz109921-DW_AT_decl_file-test.patch
# Update PPC unwinding patches to their upstream variants (BZ 140532).
#=fedoratest+ppc
Patch229: gdb-6.3-bz140532-ppc-unwinding-test.patch
# Testcase for exec() from threaded program (BZ 202689).
#=fedoratest
Patch231: gdb-6.3-bz202689-exec-from-pthread-test.patch
# Backported fixups post the source tarball.
#Xdrop: Just backports.
Patch232: gdb-upstream.patch
# Testcase for PPC Power6/DFP instructions disassembly (BZ 230000).
#=fedoratest+ppc
Patch234: gdb-6.6-bz230000-power6-disassembly-test.patch
# Temporary support for shared libraries >2GB on 64bit hosts. (BZ 231832)
#=push+work: Upstream should have backward compat. API: libc-alpha: <20070127104539.GA9444@.*>
Patch235: gdb-6.3-bz231832-obstack-2gb.patch
# Allow running `/usr/bin/gcore' with provided but inaccessible tty (BZ 229517).
#=fedoratest
Patch245: gdb-6.6-bz229517-gcore-without-terminal.patch
# Notify user of a child forked process being detached (BZ 235197).
#=push: This is more about discussion if/what should be printed.
Patch247: gdb-6.6-bz235197-fork-detach-info.patch
# Avoid too long timeouts on failing cases of "annota1.exp annota3.exp".
#=fedoratest
Patch254: gdb-6.6-testsuite-timeouts.patch
# Support for stepping over PPC atomic instruction sequences (BZ 237572).
#=fedoratest
Patch258: gdb-6.6-bz237572-ppc-atomic-sequence-test.patch
# Test kernel VDSO decoding while attaching to an i386 process.
#=fedoratest
Patch263: gdb-6.3-attach-see-vdso-test.patch
# Test leftover zombie process (BZ 243845).
#=fedoratest
Patch271: gdb-6.5-bz243845-stale-testing-zombie-test.patch
# New locating of the matching binaries from the pure core file (build-id).
#=push
Patch274: gdb-6.6-buildid-locate.patch
# Fix loading of core files without build-ids but with build-ids in executables.
#=push
Patch659: gdb-6.6-buildid-locate-solib-missing-ids.patch
#=push
Patch353: gdb-6.6-buildid-locate-rpm.patch
#=push
Patch415: gdb-6.6-buildid-locate-core-as-arg.patch
# Workaround librpm BZ 643031 due to its unexpected exit() calls (BZ 642879).
#=push
Patch519: gdb-6.6-buildid-locate-rpm-librpm-workaround.patch
# Fix displaying of numeric char arrays as strings (BZ 224128).
#=fedoratest: But it is failing anyway, one should check the behavior more.
Patch282: gdb-6.7-charsign-test.patch
# Test PPC hiding of call-volatile parameter register.
#=fedoratest+ppc
Patch284: gdb-6.7-ppc-clobbered-registers-O2-test.patch
# Test hiding unexpected breakpoints on intentional step commands.
#=fedoratest
Patch290: gdb-6.5-missed-trap-on-step-test.patch
# Support DW_TAG_interface_type the same way as DW_TAG_class_type (BZ 426600).
#=fedoratest
Patch294: gdb-6.7-bz426600-DW_TAG_interface_type-test.patch
# Test gcore memory and time requirements for large inferiors.
#=fedoratest
Patch296: gdb-6.5-gcore-buffer-limit-test.patch
# Test debugging statically linked threaded inferiors (BZ 239652).
#  - It requires recent glibc to work in this case properly.
#=fedoratest
Patch298: gdb-6.6-threads-static-test.patch
# Test GCORE for shmid 0 shared memory mappings.
#=fedoratest: But it is broken anyway, sometimes the case being tested is not reproducible.
Patch309: gdb-6.3-mapping-zero-inode-test.patch
# Test a crash on `focus cmd', `focus prev' commands.
#=fedoratest
Patch311: gdb-6.3-focus-cmd-prev-test.patch
# Test various forms of threads tracking across exec() (BZ 442765).
#=fedoratest
Patch315: gdb-6.8-bz442765-threaded-exec-test.patch
# Test a crash on libraries missing the .text section.
#=fedoratest
Patch320: gdb-6.5-section-num-fixup-test.patch
# Fix register assignments with no GDB stack frames (BZ 436037).
#=push+work: This fix is incorrect.
Patch330: gdb-6.8-bz436037-reg-no-longer-active.patch
# Make the GDB quit processing non-abortable to cleanup everything properly.
#=push: It was useful only after gdb-6.8-attach-signalled-detach-stopped.patch .
Patch331: gdb-6.8-quit-never-aborts.patch
# [RHEL5] Workaround kernel for detaching SIGSTOPped processes (BZ 809382).
#=fedora
Patch335: gdb-rhel5-compat.patch
# [RHEL5,RHEL6] Fix attaching to stopped processes.
#=fedora
Patch337: gdb-6.8-attach-signalled-detach-stopped.patch
# Test the watchpoints conditionals works.
#=fedoratest
Patch343: gdb-6.8-watchpoint-conditionals-test.patch
# Fix resolving of variables at locations lists in prelinked libs (BZ 466901).
#=fedoratest
Patch348: gdb-6.8-bz466901-backtrace-full-prelinked.patch
# The merged branch `archer-jankratochvil-fedora15' of:
# http://sourceware.org/gdb/wiki/ProjectArcher
#=push+work
Patch349: gdb-archer.patch
# Fix parsing elf64-i386 files for kdump PAE vmcore dumps (BZ 457187).
# - Turn on 64-bit BFD support, globally enable AC_SYS_LARGEFILE.
#=fedoratest
Patch360: gdb-6.8-bz457187-largefile-test.patch
# New test for step-resume breakpoint placed in multiple threads at once.
#=fedoratest
Patch381: gdb-simultaneous-step-resume-breakpoint-test.patch
# Fix GNU/Linux core open: Can't read pathname for load map: Input/output error.
# Fix regression of undisplayed missing shared libraries caused by a fix for.
#=push+work: It should be in glibc: libc-alpha: <20091004161706.GA27450@.*>
Patch382: gdb-core-open-vdso-warning.patch
# Fix syscall restarts for amd64->i386 biarch.
#=push
Patch391: gdb-x86_64-i386-syscall-restart.patch
# Fix stepping with OMP parallel Fortran sections (BZ 533176).
#=push+work: It requires some better DWARF annotations.
Patch392: gdb-bz533176-fortran-omp-step.patch
# Fix regression by python on ia64 due to stale current frame.
#=push
Patch397: gdb-follow-child-stale-parent.patch
# Workaround ccache making lineno non-zero for command-line definitions.
#=fedoratest: ccache is rarely used and it is even fixed now.
Patch403: gdb-ccache-workaround.patch
# Testcase for "Do not make up line information" fix by Daniel Jacobowitz.
#=fedoratest
Patch407: gdb-lineno-makeup-test.patch
# Test power7 ppc disassembly.
#=fedoratest+ppc
Patch408: gdb-ppc-power7-test.patch
# Fix i386+x86_64 rwatch+awatch before run, regression against 6.8 (BZ 541866).
# Fix i386 rwatch+awatch before run (BZ 688788, on top of BZ 541866).
#=push+work: It should be fixed properly instead.
Patch417: gdb-bz541866-rwatch-before-run.patch
# Workaround non-stop moribund locations exploited by kernel utrace (BZ 590623).
#=push+work: Currently it is still not fully safe.
Patch459: gdb-moribund-utrace-workaround.patch
# Fix follow-exec for C++ programs (bugreported by Martin Stransky).
#=fedoratest
Patch470: gdb-archer-next-over-throw-cxx-exec.patch
# Backport DWARF-4 support (BZ 601887, Tom Tromey).
#=fedoratest
Patch475: gdb-bz601887-dwarf4-rh-test.patch
# [delayed-symfile] Test a backtrace regression on CFIs without DIE (BZ 614604).
#=fedoratest
Patch490: gdb-test-bt-cfi-without-die.patch
# Provide /usr/bin/gdb-add-index for rpm-build (Tom Tromey).
#=fedora: Re-check against the upstream version.
Patch491: gdb-gdb-add-index-script.patch
# Out of memory is just an error, not fatal (uninitialized VLS vars, BZ 568248).
#=drop+work: Inferior objects should be read in parts, then this patch gets obsoleted.
Patch496: gdb-bz568248-oom-is-error.patch
# Verify GDB Python built-in function gdb.solib_address exists (BZ # 634108).
#=fedoratest
Patch526: gdb-bz634108-solib_address.patch
# New test gdb.arch/x86_64-pid0-core.exp for kernel PID 0 cores (BZ 611435).
#=fedoratest
Patch542: gdb-test-pid0-core.patch
# [archer-tromey-delayed-symfile] New test gdb.dwarf2/dw2-aranges.exp.
#=fedoratest
Patch547: gdb-test-dw2-aranges.patch
# [archer-keiths-expr-cumulative+upstream] Import C++ testcases.
#=fedoratest
Patch548: gdb-test-expr-cumulative-archer.patch
# Work around PR libc/13097 "linux-vdso.so.1" warning message.
#=push
Patch627: gdb-glibc-vdso-workaround.patch
# Hack for proper PIE run of the testsuite.
#=fedoratest
Patch634: gdb-runtest-pie-override.patch
# Print reasons for failed attach/spawn incl. SELinux deny_ptrace (BZ 786878).
#=push
Patch653: gdb-attach-fail-reasons-5of5.patch
# Workaround crashes from stale frame_info pointer (BZ 804256).
#=fedora
Patch661: gdb-stale-frame_info.patch
# Workaround PR libc/14166 for inferior calls of strstr.
#=push+work: But push it to glibc.
Patch690: gdb-glibc-strstr-workaround.patch
# Include testcase for `Unable to see a variable inside a module (XLF)' (BZ 823789).
#=fedoratest
#+ppc
Patch698: gdb-rhel5.9-testcase-xlf-var-inside-mod.patch
# Testcase for `Setting solib-absolute-prefix breaks vDSO' (BZ 818343).
#=fedoratest
Patch703: gdb-rhbz-818343-set-solib-absolute-prefix-testcase.patch
# Fix `GDB cannot access struct member whose offset is larger than 256MB'
# (RH BZ 795424).
#=push+work
Patch811: gdb-rhbz795424-bitpos-20of25.patch
Patch812: gdb-rhbz795424-bitpos-21of25.patch
Patch813: gdb-rhbz795424-bitpos-22of25.patch
Patch814: gdb-rhbz795424-bitpos-23of25.patch
Patch816: gdb-rhbz795424-bitpos-25of25.patch
Patch817: gdb-rhbz795424-bitpos-25of25-test.patch
Patch818: gdb-rhbz795424-bitpos-lazyvalue.patch
# Import regression test for `gdb/findvar.c:417: internal-error:
# read_var_value: Assertion `frame' failed.' (RH BZ 947564) from RHEL 6.5.
#=fedoratest
Patch832: gdb-rhbz947564-findvar-assertion-frame-failed-testcase.patch
# Fix crash on 'enable count' (Simon Marchi, BZ 993118).
Patch843: gdb-enable-count-crash.patch
# [rhel6] DTS backward Python compatibility API (BZ 1020004, Phil Muldoon).
Patch848: gdb-dts-rhel6-python-compat.patch
# Fix crash of -readnow /usr/lib/debug/usr/bin/gnatbind.debug (BZ 1069211).
Patch852: gdb-gnat-dwarf-crash-3of3.patch
# VLA (Fortran dynamic arrays) from Intel + archer-jankratochvil-vla tests.
Patch888: gdb-vla-intel.patch
Patch983: gdb-vla-intel-logical-not.patch
Patch889: gdb-vla-intel-stringbt-fix.patch
Patch912: gdb-vla-intel-04of23-fix.patch
Patch887: gdb-archer-vla-tests.patch
# Continue backtrace even if a frame filter throws an exception (Phil Muldoon).
Patch918: gdb-btrobust.patch
# Display Fortran strings in backtraces.
Patch925: gdb-fortran-frame-string.patch
# Fix Python GIL with gdb.execute("continue") (Phil Muldoon, BZ 1116957).
Patch927: gdb-python-gil.patch
# Fix jit-reader.h for multi-lib.
Patch978: gdb-jit-reader-multilib.patch
# Temporarily disable dg-extract-results.py to fix gdb.sum sorting.
Patch982: gdb-no-dg-extract-results-py.patch

%def_enable tui
%def_disable check
%def_with python

BuildRequires: flex libreadline-devel libexpat-devel liblzma-devel zlib-devel
BuildRequires: makeinfo
BuildRequires: %{?_with_python:python-devel} libstdc++6 %{?_enable_tui:libncursesw-devel}
%{?!_without_check:%{?!_disable_check:BuildRequires: dejagnu glibc-devel-static gcc-c++ gcc-fortran gcc-java gcc-objc prelink valgrind /proc /dev/pts}}
%if_with python
Provides: python-module-gdb = %version-%release
%endif
Requires: gdb-common = %version-%release

%description
GDB is a full featured, command driven debugger.  GDB allows you to
trace the execution of programs and examine their internal state at
any time.  The debugger is most effective when used together with a
supported compiler, such as those from the GNU Compiler Collection.

%package light
Summary: A GNU source-level debugger for C, C++ and other languages (light build)
Group: Development/Debuggers
Requires: gdb-common = %version-%release
Conflicts: gdb < 7.5.0.20121002-alt5

%description light
GDB is a full featured, command driven debugger.  GDB allows you to
trace the execution of programs and examine their internal state at
any time.  The debugger is most effective when used together with a
supported compiler, such as those from the GNU Compiler Collection.
This package contains light build of GDB without expat, python and
tui support.

%package common
Summary: GDB common files
Group: Development/Debuggers
BuildArch: noarch
Conflicts: gdb < 7.5.0.20121002-alt5

%description common
This package contains common GDB files.

%package -n libgdb-devel
Summary: GDB static libraries
Group: Development/C
Conflicts: libbfd-devel libiberty-devel

%description -n libgdb-devel
This package contains static GDB libraries required to build other debuggers.

%prep
%setup
# Remove generated bison and flex parser files.
egrep -lZ 'A (Bison parser, made by GNU Bison|lexical scanner generated by flex)' gdb/*.c |
	xargs -r0 rm --
# Remove generated info files.
rm */doc/*.info*
# Somehow readline/doc is needed to build other docs.
mv readline/doc readline-doc

### Fedora patches
%patch349 -p1
%patch101 -p1
%patch105 -p1
%patch111 -p1
%patch112 -p1
%patch118 -p1
%patch122 -p1
%patch125 -p1
%patch133 -p1
%patch136 -p1
%patch145 -p1
%patch161 -p1
%patch163 -p1
%patch164 -p1
%patch188 -p1
%patch194 -p1
%patch196 -p1
%patch199 -p1
%patch208 -p1
%patch211 -p1
%patch213 -p1
%patch214 -p1
%patch216 -p1
%patch217 -p1
%patch225 -p1
%patch229 -p1
%patch231 -p1
%patch234 -p1
%patch235 -p1
%patch245 -p1
%patch247 -p1
%patch254 -p1
%patch258 -p1
%patch260 -p1
%patch263 -p1
%patch271 -p1
%patch274 -p1
%patch659 -p1
#patch353 -p1
#patch276 -p1
%patch282 -p1
%patch284 -p1
#patch287 -p1
%patch290 -p1
%patch294 -p1
%patch296 -p1
%patch298 -p1
%patch309 -p1
%patch311 -p1
%patch315 -p1
%patch320 -p1
#patch329 -p1
%patch330 -p1
%patch331 -p1
%patch343 -p1
%patch348 -p1
%patch360 -p1
%patch381 -p1
%patch382 -p1
%patch391 -p1
%patch392 -p1
%patch397 -p1
%patch403 -p1
#patch404 -p1
#patch405 -p1
%patch389 -p1
%patch394 -p1
%patch407 -p1
%patch408 -p1
%patch417 -p1
%patch459 -p1
%patch470 -p1
%patch475 -p1
%patch415 -p1
#patch519 -p1
%patch490 -p1
%patch491 -p1
%patch496 -p1
#patch504 -p1
%patch526 -p1
%patch542 -p1
%patch547 -p1
%patch548 -p1
#patch618 -p1
%patch627 -p1
%patch634 -p1
#patch643 -p1
%patch653 -p1
#patch657 -p1
%patch661 -p1
%patch690 -p1
%patch698 -p1
%patch703 -p1
#patch811 -p1
#patch812 -p1
#patch813 -p1
#patch814 -p1
#patch816 -p1
#patch817 -p1
#patch818 -p1

%patch832 -p1
%patch843 -p1
%patch852 -p1
%patch887 -p1
%patch918 -p1
%patch925 -p1
%patch927 -p1
%patch978 -p1
%patch982 -p1
%patch848 -p1

%patch337 -p1
%patch335 -p1

# Debian patches
%patch11 -p1
%patch13 -p1

# ALT patches
%patch1 -p1
%patch2 -p1
%patch3 -p1

# We don't need these subdirs.
rm -r gdb/gdbserver readline

find -type f -name \*.orig -delete
xz -9k gdb/{MAINTAINERS,NEWS}

%build
echo '%version-%release (%distribution)' >gdb/version.in

for f in */configure.in; do
	pushd "${f%%/*}"
		[ configure.in -nt configure ] && autoconf
	popd
done
for f in */Makefile.am; do
	pushd "${f%%/*}"
		[ Makefile.am -nt Makefile.in ] && automake
	popd
done

%define _configure_script ../configure
%define configure_opts \\\
	--with-gdb-datadir=%_datadir/gdb \\\
	--with-separate-debug-dir=/usr/lib/debug \\\
	--with-auto-load-dir='$debugdir:%_libdir/gdb/auto-load:$datadir/auto-load' \\\
	--enable-gdb-build-warnings=,-Wno-unused \\\
	--disable-werror \\\
	--disable-sim \\\
	--disable-rpath \\\
	--with-system-readline \\\
	--with-lzma \\\
	--without-libexpat-prefix \\\
	--without-rpm \\\
	--without-libunwind \\\
	--enable-64-bit-bfd \\\
	%nil
export \
	ac_cv_have_x=${ac_cv_have_x='have_x=yes ac_x_includes=%_x11includedir ac_x_libraries=%_x11libdir'} \
	%{?!_enable_tui:ac_cv_search_tgetent='none required'} \
	#

%define buildtarget build-%_target
rm -rf %buildtarget
mkdir %buildtarget
pushd %buildtarget

%configure %configure_opts %{subst_enable tui} %{subst_with python}
%make_build
%make_build -C gdb libgdb.a
%make_build info MAKEINFOFLAGS=--no-split
grep -Fq '#define HAVE_ZLIB_H 1' gdb/config.h

popd #%buildtarget

rm -rf light
mkdir light
pushd light

%configure %configure_opts --disable-tui --without-expat --without-python
%make_build
grep -Fq '#define HAVE_ZLIB_H 1' gdb/config.h

popd #light

%install
%makeinstall_std -C %buildtarget
install -pm755 light/gdb/gdb %buildroot%_bindir/gdb-light

install -pm644 %_sourcedir/gdb-gstack.man %buildroot%_man1dir/gstack.1

# These files are already packaged as a part of binutils.
rm %buildroot%_infodir/bfd*
rm %buildroot%_datadir/locale/*/LC_MESSAGES/{bfd,opcodes}.mo

pushd %buildtarget
mkdir -p %buildroot%_libdir
install -pm644 */lib*.a %buildroot%_libdir/
popd #%buildtarget

mkdir -p %buildroot%_datadir/gdb/auto-load

%if_with python
mkdir -p %buildroot%python_sitelibdir_noarch
mv %buildroot%_datadir/gdb/python/gdb/ %buildroot%python_sitelibdir_noarch/
ln -s ../../../..%python_sitelibdir_noarch/gdb %buildroot%_datadir/gdb/python/gdb
%endif

%check
[ -w /dev/ptmx -a -f /proc/self/maps ] || exit
pushd %buildtarget/gdb
%__cc %optflags -o orphanripper %_sourcedir/gdb-orphanripper.c -lutil
./orphanripper make -k -j%__nprocs check ||:
popd

# contained in gdb binary
%add_python_req_skip _gdb

%files
%_bindir/*
%if_with python
%_datadir/gdb/python
%python_sitelibdir_noarch/*
%endif
%exclude %_bindir/gdb-light

%files light
%_bindir/gdb-light

%files common
%_man1dir/*
%_infodir/*
%_datadir/gdb
%doc gdb/{MAINTAINERS,NEWS}.xz
%exclude %_datadir/gdb/python

%files -n libgdb-devel
%_includedir/*
%_libdir/lib*.a

%changelog
* Mon Aug 29 2016 Andrey Cherepanov <cas@altlinux.org> 7.9-alt3
- Do not distribute desktop file for console program

* Thu Dec 10 2015 Andrey Cherepanov <cas@altlinux.org> 7.9-alt2
- Fix configure by adding makeinfo to build requirements
- Rebuild fixes redundant repl_strstr function in libgdb.a

* Tue Sep 08 2015 Sergey Bolshakov <sbolshakov@altlinux.ru> 7.9-alt1
- 7.9 released, synced with fedora 7.9-11

* Thu Jan 30 2014 Evgeny Sinelnikov <sin@altlinux.ru> 7.5.0.20121002-alt5
- Built with python support (closes: #29759).
- Added separate subpackages gdb-common and gdb-light.
- Changed default auto-load path to /usr/share/gdb directory.

* Tue Nov 19 2013 Gleb F-Malinovskiy <glebfm@altlinux.org> 7.5.0.20121002-alt4
- Fixed build with readline6.

* Fri Feb 15 2013 Dmitry V. Levin <ldv@altlinux.org> 7.5.0.20121002-alt3
- Packaged a lightweigted build of gdb as %_bindir/gdb-light.

* Wed Oct 10 2012 Dmitry V. Levin <ldv@altlinux.org> 7.5.0.20121002-alt2
- Disabled few patches that appeared to be too Fedora specific (closes: #27818).

* Fri Oct 05 2012 Dmitry V. Levin <ldv@altlinux.org> 7.5.0.20121002-alt1
- Updated to 7.5.0.20121002, synced with Fedora and Debian.

* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 7.2-alt2.1
- Rebuild with Python-2.7

* Fri Jun 03 2011 Dmitry V. Levin <ldv@altlinux.org> 7.2-alt2
- Updated desktop categories.

* Tue Feb 01 2011 Dmitry V. Levin <ldv@altlinux.org> 7.2-alt1
- Updated to 7.2, synced with FC gdb-7.2-40 and Debian gdb-7.2-1.
- Changed debug dir from %%_libdir/debug to /usr/lib/debug.

* Fri Oct 15 2010 Kirill A. Shutemov <kas@altlinux.org> 7.0.1-alt3
- Set gdb_datadir to %%_libdir/gdb to move auto-load directory out
  of /usr/share.
- Drop libstdc++ helpers: packaged from gcc now.

* Sun Apr 11 2010 Dmitry V. Levin <ldv@altlinux.org> 7.0.1-alt2
- libgdb-devel: Packaged libdecnumber.a.
- Fixed "gdb --version" output.

* Sun Mar 07 2010 Dmitry V. Levin <ldv@altlinux.org> 7.0.1-alt1
- Updated to 7.0.1 (closes: #19417, #20569, #21761).
- Imported bunch of patches from FC gdb-7.0.1-33.
- Imported bunch of patches from Debian gdb-7.0.1-2.

* Mon Mar 03 2008 Dmitry V. Levin <ldv@altlinux.org> 6.6-alt3
- Fixed build with fresh makeinfo.

* Fri Nov 16 2007 Dmitry V. Levin <ldv@altlinux.org> 6.6-alt2
- Packaged static gdb libraries into libgdb-devel subpackage (at@, #8899).

* Sun Apr 01 2007 Dmitry V. Levin <ldv@altlinux.org> 6.6-alt1
- Updated to 6.6.
- Imported bunch of patches from FC gdb-6.6-8.
- Imported bunch of patches from Debian gdb-6.6.dfsg-1.

* Fri Dec 30 2005 ALT QA Team Robot <qa-robot@altlinux.org> 6.3-alt2.1
- Rebuilt with libreadline.so.5.

* Sun May 29 2005 Dmitry V. Levin <ldv@altlinux.org> 6.3-alt2
- Imported bunch of patches from Debian.
- Applied upstream fix to BFD library (CAN-2005-1704).
- Applied fix for .gdbinit issue (CAN-2005-1705).

* Mon Dec 20 2004 Dmitry V. Levin <ldv@altlinux.org> 6.3-alt1
- Updated to 6.3, updated patches.

* Wed Aug 04 2004 Dmitry V. Levin <ldv@altlinux.org> 6.2-alt1
- Updated to 6.2, updated patches.

* Tue Apr 06 2004 Dmitry V. Levin <ldv@altlinux.org> 6.1-alt1
- Updated to 6.1, updated patches.
- Applied patches from RH's gdb-6.0post-0.20040223.8
- Build with bundled libbfd, libopcodes and libiberty.
- Packaged gcore script.
- Enabled tui by default.

* Sun Aug 10 2003 Dmitry V. Levin <ldv@altlinux.org> 5.3-alt2
- Rebuilt with libbfd-2.14.90.0.5.

* Fri Jun 20 2003 Dmitry V. Levin <ldv@altlinux.org> 5.3-alt1
- Updated to 5.3, rediffed patches.
- Merged with gdb-5.3-23mdk (8 patches added).

* Tue Oct 08 2002 Dmitry V. Levin <ldv@altlinux.org> 5.2.1-alt2
- Avoid build dependencies on XFree86-* (#0001376).
- Fixed build with new rpm-build.

* Mon Aug 26 2002 Dmitry V. Levin <ldv@altlinux.org> 5.2.1-alt1
- 5.2.1
- Patched to link with libtinfo.
- Applied "rh-misc" patch from rh gdb-5.2.1-3.

* Mon Jun 17 2002 Dmitry V. Levin <ldv@altlinux.org> 5.2-alt1
- 5.2
- Built with system libreadline, libbfd, libopcodes and libiberty.

* Thu Feb 14 2002 Dmitry V. Levin <ldv@alt-linux.org> 5.1.1-alt1
- Added menu entry.
- Moved mmaloc to separate subpackage.
- Usual ALT adaptions.

* Thu Jan 24 2002 Trond Eivind Glomsrød <teg@redhat.com> 5.1.1-1
- 5.1.1
- add URL

* Wed Jan 09 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Mon Dec 10 2001 Trond Eivind Glomsrød <teg@redhat.com> 5.1-2
- Fix some thread+fpu problems

* Mon Nov 26 2001 Trond Eivind Glomsrød <teg@redhat.com> 5.1-1
- 5.1

* Mon Nov 19 2001 Trond Eivind Glomsrød <teg@redhat.com> 5.0.94-0.71
- 5.0.94. Almost there....

* Mon Nov 12 2001 Trond Eivind Glomsrød <teg@redhat.com> 5.0.93-2
- Add patch from jakub@redhat.com to improve handling of DWARF

* Mon Nov 12 2001 Trond Eivind Glomsrød <teg@redhat.com> 5.0.93-1
- 5.0.93
- handle missing info pages in post/pre scripts

* Wed Oct 31 2001 Trond Eivind Glomsrød <teg@redhat.com> 5.0.92-1
- 5.0.92

* Fri Oct 26 2001 Trond Eivind Glomsrød <teg@redhat.com> 5.0.91rh-1
- New snapshot
- Use the 5.0.91 versioning from the snapshot

* Wed Oct 17 2001 Trond Eivind Glomsrød <teg@redhat.com> 5.0rh-17
- New snapshot

* Thu Sep 27 2001 Trond Eivind Glomsrød <teg@redhat.com>
- New snapshot

* Wed Sep 12 2001 Trond Eivind Glomsrød <teg@redhat.com> 5.0rh-16
- New snapshot

* Mon Aug 13 2001 Trond Eivind Glomsrød <teg@redhat.com> 5.0rh-15
- Don't buildrequire compat-glibc (#51690)

* Thu Aug  9 2001 Trond Eivind Glomsrød <teg@redhat.com>
- New snapshot, from the stable branch eventually leading to gdb 5.1

* Mon Jul 30 2001 Trond Eivind Glomsrød <teg@redhat.com>
- s/Copyright/License/
- Add texinfo to BuildRequires

* Mon Jun 25 2001 Trond Eivind Glomsrød <teg@redhat.com>
- New snapshot

* Fri Jun 15 2001 Trond Eivind Glomsrød <teg@redhat.com>
- New snapshot
- Add ncurses-devel to buildprereq
- Remove perl from buildprereq, as gdb changed the way
  version strings are generated

* Thu Jun 14 2001 Trond Eivind Glomsrød <teg@redhat.com>
- New snapshot

* Wed May 16 2001 Trond Eivind Glomsrød <teg@redhat.com>
- New snapshot - this had thread fixes for curing #39070
- New way of specifying version

* Tue May  1 2001 Trond Eivind Glomsrød <teg@redhat.com>
- New tarball
- Kevin's patch is now part of gdb

* Mon Apr  9 2001 Trond Eivind Glomsrød <teg@redhat.com>
- Add patch from kevinb@redhat.com to fix floating point + thread
  problem (#24310)
- remove old workarounds
- new snapshot

* Thu Apr  5 2001 Trond Eivind Glomsrød <teg@redhat.com>
- New snapshot

* Sat Mar 17 2001 Bill Nottingham <notting@redhat.com>
- on ia64, there are no old headers :)

* Fri Mar 16 2001 Trond Eivind Glomsrød <teg@redhat.com>
- build with old headers, new compiler

* Wed Mar 16 2001 Trond Eivind Glomsrød <teg@redhat.com>
- new snapshot

* Mon Feb 26 2001 Trond Eivind Glomsrød <teg@redhat.com>
- new snapshot which should fix some more IA64 problems (#29151)
- remove IA64 patch, it's now integrated

* Wed Feb 21 2001 Trond Eivind Glomsrød <teg@redhat.com>
- add IA64 and Alpha patches from Kevin Buettner <kevinb@redhat.com>
- use perl instead of patch for fixing the version string

* Tue Feb 20 2001 Trond Eivind Glomsrød <teg@redhat.com>
- don't use kgcc anymore
- mark it as our own version
- new snapshot

* Mon Jan 22 2001 Bernhard Rosenkraenzer <bero@redhat.com>
- Link with ncurses 5.x even though we're using kgcc.
  No need to drag in requirements on ncurses4 (Bug #24445)

* Fri Jan 19 2001 Trond Eivind Glomsrød <teg@redhat.com>
- new snapshot

* Thu Dec 20 2000 Trond Eivind Glomsrød <teg@redhat.com>
- new snapshot

* Mon Dec 04 2000 Trond Eivind Glomsrød <teg@redhat.com>
- new snapshot
- new alpha patch - it now compiles everywhere. Finally.

* Fri Dec 01 2000 Trond Eivind Glomsrød <teg@redhat.com>
- new snapshot

* Mon Nov 20 2000 Trond Eivind Glomsrød <teg@redhat.com>
- new CVS snapshot
- disable the patches
- don't use %%configure, as it confuses the autoconf script
- enable SPARC, disable Alpha

* Wed Aug 09 2000 Trond Eivind Glomsrød <teg@redhat.com>
- added patch from GDB team for C++ symbol handling

* Mon Jul 25 2000 Trond Eivind Glomsrød <teg@redhat.com>
- upgrade to CVS snapshot
- excludearch SPARC, build on IA61

* Wed Jul 19 2000 Trond Eivind Glomsrød <teg@redhat.com>
- rebuild

* Thu Jul 13 2000 Prospector <bugzilla@redhat.com>
- automatic rebuild

* Sun Jul 02 2000 Trond Eivind Glomsrød <teg@redhat.com>
- rebuild

* Fri Jun 08 2000 Trond Eivind Glomsrød <teg@redhat.com>
- use %%configure, %%makeinstall, %%{_infodir}, %%{_mandir},
  and %%{_tmppath}
- the install scripts  for info are broken(they don't care about
  you specify in the installstep), work around that.
- don't build for IA64

* Mon May 22 2000 Trond Eivind Glomsrød <teg@redhat.com>
- upgraded to 5.0 - dump all patches. Reapply later if needed.
- added the NEWS file to the %%doc files
- don't delete files which doesn't get installed (readline, texinfo)
- let build system handle stripping and gzipping
- don't delete libmmalloc
- apply patch from jakub@redhat.com to make it build on SPARC

* Fri Apr 28 2000 Matt Wilson <msw@redhat.com>
- rebuilt against new ncurses

* Tue Mar  7 2000 Jeff Johnson <jbj@redhat.com>
- rebuild for sparc baud rates > 38400.

* Tue Feb  8 2000 Jakub Jelinek <jakub@redhat.com>
- fix core file handling on i386 with glibc 2.1.3 headers

* Fri Jan 14 2000 Jakub Jelinek <jakub@redhat.com>
- fix reading registers from core on sparc.
- hack around build problems on i386 with glibc 2.1.3 headers

* Thu Oct 7 1999 Jim Kingdon
- List files to install in /usr/info specifically (so we don't pick up
things like info.info from GDB snapshots).

* Thu Oct 7 1999 Jim Kingdon
- Update GDB to 19991004 snapshot.  This eliminates the need for the
sigtramp, sparc, xref, and threads patches.  Update sparcmin patch.

* Mon Aug 23 1999 Jim Kingdon
- Omit readline manpage.

* Tue Aug 7 1999 Jim Kingdon
- Remove H.J. Lu's patches (they had been commented out).
- Add sigtramp patch (from gdb.cygnus.com) and threads patch (adapted
from code fusion CD-ROM).

* Wed Apr 14 1999 Jeff Johnson <jbj@redhat.com>
- merge H.J. Lu's patches into 4.18.

* Mon Apr 05 1999 Cristian Gafton <gafton@redhat.com>
- updated the kern22 patch with stuff from davem

* Thu Apr  1 1999 Jeff Johnson <jbj@redhat.com>
- sparc with 2.2 kernels no longer uses sunos ptrace (davem)

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com>
- auto rebuild in the new build environment (release 3)

* Mon Mar  8 1999 Jeff Johnson <jbj@redhat.com>
- Sparc fiddles for Red Hat 6.0.
