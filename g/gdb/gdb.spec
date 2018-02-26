Name: gdb
Version: 7.2
Release: alt2.1

Summary: A GNU source-level debugger for C, C++ and other languages
License: GPLv3+
Group: Development/Debuggers
Url: http://www.gnu.org/software/gdb/

# ftp://sourceware.org/pub/gdb/releases/gdb-%version.tar.bz2
Source: gdb-%version.tar
Source1: gdb.desktop
# Cleanup any leftover testsuite processes as it may stuck hasher builds.
Source2: gdb-orphanripper.c
# Man page for gstack(1).
Source3: gdb-gstack.man

Patch1: gdb-7.2-alt-testsuite-version.patch
Patch2: gdb-7.2-alt-readline.patch

### Debian patches
Patch11: dwarf2-cfi-warning.patch
Patch12: gdb-fortran-main.patch
Patch13: linux-clear-thread-list.patch
Patch14: man-page-args.patch
Patch15: man-page-order.patch

### RedHat patches
# Work around out-of-date dejagnu that does not have KFAIL
#=drop: That dejagnu is too old to be supported.
Patch101: gdb-6.3-rh-dummykfail-20041202.patch
# Check that libunwind works - new test then fix
#=ia64
Patch103: gdb-6.3-rh-testlibunwind-20041202.patch
# Use convert_from_func_ptr_addr on the solib breakpoint address;
# simplifies and makes more consistent the logic.
#=maybepush+ppc: Write new testcase.
Patch104: gdb-6.3-ppcdotsolib-20041022.patch
# Better parse 64-bit PPC system call prologues.
#=maybepush+ppc: Write new testcase.
Patch105: gdb-6.3-ppc64syscall-20040622.patch
# Stop a backtrace when a zero PC is encountered.
#=maybepush: Write new testcase.
Patch106: gdb-6.3-framepczero-20040927.patch
# Include the pc's section when doing a symbol lookup so that the
# correct symbol is found.
#=maybepush: Write new testcase.
Patch111: gdb-6.3-ppc64displaysymbol-20041124.patch
# Fix upstream `set scheduler-locking step' vs. upstream PPC atomic seqs.
#=maybepush+work: It is a bit difficult patch, a part is ppc specific.
Patch112: gdb-6.6-scheduler_locking-step-sw-watchpoints2.patch
# Make upstream `set scheduler-locking step' as default.
#=maybepush+work: How much is scheduler-locking relevant after non-stop?
Patch260: gdb-6.6-scheduler_locking-step-is-default.patch
# Add a wrapper script to GDB that implements pstack using the
# --readnever option.
#=push+work: with gdbindex maybe --readnever should no longer be used.
Patch118: gdb-6.3-gstack-20050411.patch
# VSYSCALL and PIE
#=fedoratest
Patch122: gdb-6.3-test-pie-20050107.patch
#=maybepush: May get obsoleted by Tom's unrelocated objfiles patch.
Patch389: gdb-archer-pie-addons.patch
#=push+work: Breakpoints disabling matching should not be based on address.
Patch394: gdb-archer-pie-addons-keep-disabled.patch
# Get selftest working with sep-debug-info
#=maybepush
Patch125: gdb-6.3-test-self-20050110.patch
# Test support of multiple destructors just like multiple constructors
#=fedoratest
Patch133: gdb-6.3-test-dtorfix-20050121.patch
# Fix to support executable moving
#=fedoratest
Patch136: gdb-6.3-test-movedir-20050125.patch
# Fix gcore for threads
#=ia64
Patch140: gdb-6.3-gcore-thread-20050204.patch
# Stop while intentionally stepping and the thread exit is met.
#=push
Patch141: gdb-6.6-step-thread-exit.patch
#=push
Patch259: gdb-6.3-step-thread-exit-20050211-test.patch
# Prevent gdb from being pushed into background
#=maybepush
Patch142: gdb-6.3-terminal-fix-20050214.patch
# Test sibling threads to set threaded watchpoints for x86 and x86-64
#=fedoratest
Patch145: gdb-6.3-threaded-watchpoints2-20050225.patch
# Fix printing of inherited members
#=maybepush
Patch148: gdb-6.3-inheritance-20050324.patch
# Do not issue warning message about first page of storage for ia64 gcore
#=ia64
Patch153: gdb-6.3-ia64-gcore-page0-20050421.patch
# Security errata for untrusted .gdbinit
#=push
Patch157: gdb-6.3-security-errata-20050610.patch
# IA64 sigtramp prev register patch
#=ia64
Patch158: gdb-6.3-ia64-sigtramp-frame-20050708.patch
# IA64 gcore speed-up patch
#=ia64
Patch160: gdb-6.3-ia64-gcore-speedup-20050714.patch
# Notify observers that the inferior has been created
#=fedoratest
Patch161: gdb-6.3-inferior-notification-20050721.patch
# Fix ia64 info frame bug
#=ia64
Patch162: gdb-6.3-ia64-info-frame-fix-20050725.patch
# Verify printing of inherited members test
#=fedoratest
Patch163: gdb-6.3-inheritancetest-20050726.patch
# Add readnever option
#=push
Patch164: gdb-6.3-readnever-20050907.patch
# Fix ia64 gdb problem with user-specified SIGILL handling
#=ia64
Patch169: gdb-6.3-ia64-sigill-20051115.patch
# Allow option to continue backtracing past a zero pc value
#=maybepush
Patch170: gdb-6.3-bt-past-zero-20051201.patch
# Use bigger numbers than int.
#=push
Patch176: gdb-6.3-large-core-20051206.patch
# Fix debuginfo addresses resolving for --emit-relocs Linux kernels (BZ 203661).
#=push+work: There was some mail thread about it, this patch may be a hack.
Patch188: gdb-6.5-bz203661-emit-relocs.patch
# Security patch: avoid stack overflows in dwarf expression computation.
# CVE-2006-4146
#=push
Patch190: gdb-6.5-dwarf-stack-overflow.patch
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
#=fedoratest
Patch214: gdb-6.5-bz216711-clone-is-outermost.patch
# Test sideeffects of skipping ppc .so libs trampolines (BZ 218379).
#=fedoratest
Patch216: gdb-6.5-bz218379-ppc-solib-trampoline-test.patch
# Fix lockup on trampoline vs. its function lookup; unreproducible (BZ 218379).
#=push
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
#=drop: Just backports.
Patch232: gdb-upstream.patch
# Testcase for PPC Power6/DFP instructions disassembly (BZ 230000).
#=fedoratest+ppc
Patch234: gdb-6.6-bz230000-power6-disassembly-test.patch
# Temporary support for shared libraries >2GB on 64bit hosts. (BZ 231832)
#=push+work: Upstream should have backward compat. API: libc-alpha: <20070127104539.GA9444@.*>
Patch235: gdb-6.3-bz231832-obstack-2gb.patch
# Fix debugging GDB itself - the compiled in source files paths (BZ 225783).
#=push
Patch241: gdb-6.6-bz225783-gdb-debuginfo-paths.patch
# Allow running `/usr/bin/gcore' with provided but inaccessible tty (BZ 229517).
#=fedoratest: Drop the obsoleted gdb_gcore.sh change.
Patch245: gdb-6.6-bz229517-gcore-without-terminal.patch
# Notify user of a child forked process being detached (BZ 235197).
#=push: This is more about discussion if/what should be printed.
Patch247: gdb-6.6-bz235197-fork-detach-info.patch
# Avoid too long timeouts on failing cases of "annota1.exp annota3.exp".
#=push
Patch254: gdb-6.6-testsuite-timeouts.patch
# Support for stepping over PPC atomic instruction sequences (BZ 237572).
#=fedoratest
Patch258: gdb-6.6-bz237572-ppc-atomic-sequence-test.patch
# Link with libreadline provided by the operating system.
#=push
Patch261: gdb-6.6-readline-system.patch
# Test kernel VDSO decoding while attaching to an i386 process.
#=fedoratest
Patch263: gdb-6.3-attach-see-vdso-test.patch
# Do not hang on exit of a thread group leader (BZ 247354).
#=push
Patch265: gdb-6.6-bz247354-leader-exit-fix.patch
#=push
Patch266: gdb-6.6-bz247354-leader-exit-test.patch
# Test leftover zombie process (BZ 243845).
#=fedoratest
Patch271: gdb-6.5-bz243845-stale-testing-zombie-test.patch
# New locating of the matching binaries from the pure core file (build-id).
#=push
Patch274: gdb-6.6-buildid-locate.patch
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
# Testsuite fixes for more stable/comparable results.
#=push
Patch287: gdb-6.7-testsuite-stable-results.patch
# Test ia64 memory leaks of the code using libunwind.
#=fedoratest
Patch289: gdb-6.5-ia64-libunwind-leak-test.patch
# Test hiding unexpected breakpoints on intentional step commands.
#=fedoratest
Patch290: gdb-6.5-missed-trap-on-step-test.patch
# Support DW_TAG_interface_type the same way as DW_TAG_class_type (BZ 426600).
#=maybepush
Patch293: gdb-6.7-bz426600-DW_TAG_interface_type-fix.patch
#=fedoratest
Patch294: gdb-6.7-bz426600-DW_TAG_interface_type-test.patch
# Test gcore memory and time requirements for large inferiors.
#=fedoratest
Patch296: gdb-6.5-gcore-buffer-limit-test.patch
# Test debugging statically linked threaded inferiors (BZ 239652).
#  - It requires recent glibc to work in this case properly.
#=fedoratest
Patch298: gdb-6.6-threads-static-test.patch
# Fix #include <asm/ptrace.h> on kernel-headers-2.6.25-0.40.rc1.git2.fc9.x86_64.
#=push
Patch304: gdb-6.7-kernel-headers-compat.patch
# Test GCORE for shmid 0 shared memory mappings.
#=fedoratest: But it is broken anyway, sometimes the case being tested is not reproducible.
Patch309: gdb-6.3-mapping-zero-inode-test.patch
# Test a crash on `focus cmd', `focus prev' commands.
#=fedoratest
Patch311: gdb-6.3-focus-cmd-prev-test.patch
# Test various forms of threads tracking across exec() (BZ 442765).
#=fedoratest
Patch315: gdb-6.8-bz442765-threaded-exec-test.patch
# Silence memcpy check which returns false positive (sparc64)
#=push: But it is just a GCC workaround, look up the existing GCC PR for it.
Patch317: gdb-6.8-sparc64-silence-memcpy-check.patch
# Fix memory trashing on binaries from GCC Ada (workaround GCC PR 35998).
#=push
Patch318: gdb-6.8-gcc35998-ada-memory-trash.patch
# Test a crash on libraries missing the .text section.
#=fedoratest
Patch320: gdb-6.5-section-num-fixup-test.patch
# Fix compatibility with recent glibc headers.
#=push
Patch324: gdb-6.8-glibc-headers-compat.patch
# Create a single binary `gdb' autodetecting --tui by its argv[0].
#=push+work: IIRC Tom told argv[0] should not be used by GNU programs, also drop libgdb.a.
Patch326: gdb-6.8-tui-singlebinary.patch
# Fix PRPSINFO in the core files dumped by gcore (BZ 254229).
#=push
Patch329: gdb-6.8-bz254229-gcore-prpsinfo.patch
# Fix register assignments with no GDB stack frames (BZ 436037).
#=push+work: This fix is incorrect.
Patch330: gdb-6.8-bz436037-reg-no-longer-active.patch
# Make the GDB quit processing non-abortable to cleanup everything properly.
#=push: Useful only after gdb-6.8-attach-signalled-detach-stopped.patch .
Patch331: gdb-6.8-quit-never-aborts.patch
# Support DW_TAG_constant for Fortran in recent Fedora/RH GCCs.
#=push
Patch332: gdb-6.8-fortran-tag-constant.patch
# Fix attaching to stopped processes and/or pending signals.
#=push+work
Patch337: gdb-6.8-attach-signalled-detach-stopped.patch
# Test the watchpoints conditionals works.
#=fedoratest
Patch343: gdb-6.8-watchpoint-conditionals-test.patch
# Fix resolving of variables at locations lists in prelinked libs (BZ 466901).
#=fedoratest
Patch348: gdb-6.8-bz466901-backtrace-full-prelinked.patch
# The merged branch `archer' of: http://sourceware.org/gdb/wiki/ProjectArcher
#=push
#archer-jankratochvil-vla
#=push
#archer-jankratochvil-watchpoint3
#=push
#archer-jankratochvil-ifunc
#=push
#archer-pmuldoon-next-over-throw2
#=maybepush
#archer-tromey-python
#=maybepush
#archer-tromey-optional-psymtab
Patch349: gdb-archer.patch
#=maybepush
Patch420: gdb-archer-ada.patch
# Fix parsing elf64-i386 files for kdump PAE vmcore dumps (BZ 457187).
# - Turn on 64-bit BFD support, globally enable AC_SYS_LARGEFILE.
#=fedoratest
Patch360: gdb-6.8-bz457187-largefile-test.patch
# New test for step-resume breakpoint placed in multiple threads at once.
#=fedoratest
Patch381: gdb-simultaneous-step-resume-breakpoint-test.patch
# Fix GNU/Linux core open: Can't read pathname for load map: Input/output error.
#=push+work: It should be in glibc: libc-alpha: <20091004161706.GA27450@.*>
Patch382: gdb-core-open-vdso-warning.patch
# Fix callback-mode readline-6.0 regression for CTRL-C (for RHEL-6.0).
Patch390: gdb-readline-6.0-signal.patch
# Fix syscall restarts for amd64->i386 biarch.
#=push
Patch391: gdb-x86_64-i386-syscall-restart.patch
# Fix stepping with OMP parallel Fortran sections (BZ 533176).
#=push+work: It requires some better DWARF annotations.
Patch392: gdb-bz533176-fortran-omp-step.patch
# Disable warning messages new for gdb-6.8+ for RHEL-5 backward compatibility.
# Workaround RHEL-5 kernels for detaching SIGSTOPped processes (BZ 498595).
#=fedoratest
Patch335: gdb-rhel5-compat.patch
# Fix regression by python on ia64 due to stale current frame.
#=push
Patch397: gdb-follow-child-stale-parent.patch
# Workaround ccache making lineno non-zero for command-line definitions.
#=drop: ccache is rarely used and it is even fixed now.
Patch403: gdb-ccache-workaround.patch
# Implement `info common' for Fortran.
#=push
Patch404: gdb-fortran-common-reduce.patch
#=push
Patch405: gdb-fortran-common.patch
# Testcase for "Do not make up line information" fix by Daniel Jacobowitz.
#=fedoratest
Patch407: gdb-lineno-makeup-test.patch
# Test power7 ppc disassembly.
#=fedoratest+ppc
Patch408: gdb-ppc-power7-test.patch
# Revert: Add -Wunused-function to compile flags.
#=drop
Patch412: gdb-unused-revert.patch
# Fix i386+x86_64 rwatch+awatch before run, regression against 6.8 (BZ 541866).
#=push+work: It should be fixed properly instead.
Patch417: gdb-bz541866-rwatch-before-run.patch
# Fix crash on C++ types in some debug info files (BZ 575292, Keith Seitz).
# Temporarily workaround the crash of BZ 575292 as there was now BZ 585445.
# Re-enable the BZ 575292 and BZ 585445 C++ fix using an updated patch.
#=maybepush: Not sure if all the parts are upstream.
Patch451: gdb-bz575292-delayed-physname.patch
# Fix crash when using GNU IFUNC call from breakpoint condition.
#=drop: After archer-jankratochvil-ifunc gets in this one gets obsoleted.
Patch454: gdb-bz539590-gnu-ifunc-fix-cond.patch
# Workaround non-stop moribund locations exploited by kernel utrace (BZ 590623).
#=push+work: Currently it is still not fully safe.
Patch459: gdb-moribund-utrace-workaround.patch
# Remove core file when starting a process (BZ 594560).
#=maybepush
Patch461: gdb-bz594560-core-vs-process.patch
# Fix follow-exec for C++ programs (bugreported by Martin Stransky).
#=fedoratest
Patch470: gdb-archer-next-over-throw-cxx-exec.patch
# Backport DWARF-4 support (BZ 601887, Tom Tromey).
#=fedoratest
Patch475: gdb-bz601887-dwarf4-rh-test.patch
# Print 2D C++ vectors as matrices (BZ 562763, sourceware10659, Chris Moller).
#=push+work: There are some outstanding issues, check the mails.
Patch486: gdb-bz562763-pretty-print-2d-vectors.patch
# Fix prelinked executables with sepdebug and copy relocations (BZ 614659).
#=drop: Upstreamed.
Patch489: gdb-bz614659-prelink-dynbss.patch
# [delayed-symfile] Test a backtrace regression on CFIs without DIE (BZ 614604).
#=fedoratest
Patch490: gdb-test-bt-cfi-without-die.patch
# Provide /usr/bin/gdb-add-index for rpm-build (Tom Tromey).
#=drop: Re-check against the upstream version.
Patch491: gdb-gdb-add-index-script.patch
# Fix gcore from very small terminal windows (BZ 555076).
#=drop: Upstreamed.
Patch493: gdb-bz555076-gcore-small-height.patch
# Out of memory is just an error, not fatal (uninitialized VLS vars, BZ 568248).
#=drop+work: Inferior objects should be read in parts, then this patch gets obsoleted.
Patch496: gdb-bz568248-oom-is-error.patch
# Workaround false GCC warning(s).
#=push
Patch497: gdb-false-gcc-warning.patch
# Do not crash on broken separate debuginfo due to old elfutils (BZ 631575).
#=drop: Upstreamed.
Patch499: gdb-bz631575-gdb-index-nobits.patch
# Fix symbol lookup misses methods of current class (BZ 631158, Sami Wagiaalla).
#=maybepush
Patch500: gdb-bz631158-cxx-this-lookup.patch
# Fix Ada regression when any .gdb_index library is present.
#=drop: Upstreamed.
Patch501: gdb-gdbindex-ada-regression.patch
# python: load *-gdb.py for shlibs during attach (BZ 634660).
#=drop: Upstreamed.
Patch502: gdb-bz634660-gdbpy-load-on-attach.patch
# Fix double free crash during overload resolution (PR 12028, Sami Wagiaalla).
#=drop: Upstreamed.
Patch503: gdb-pr12028-double-free.patch
# Fix gcore writer for -Wl,-z,relro (PR corefiles/11804).
#=push: There is different patch on gdb-patches, waiting now for resolution in kernel.
Patch504: gdb-bz623749-gcore-relro.patch
# Fix infinite loop crash on self-referencing class (BZ 627432).
#=drop: Upstreamed.
Patch506: gdb-bz627432-loop-static-self-class.patch
# Fix lost siginfo_t in linux-nat (BZ 592031).
#=drop: Upstreamed.
Patch507: gdb-bz592031-siginfo-lost-1of5.patch
#=drop: Upstreamed.
Patch508: gdb-bz592031-siginfo-lost-2of5.patch
#=drop: Upstreamed.
Patch509: gdb-bz592031-siginfo-lost-3of5.patch
#=push
Patch510: gdb-bz592031-siginfo-lost-4of5.patch
#=push
Patch511: gdb-bz592031-siginfo-lost-5of5.patch
# Fix .gdb_index for big-endian hosts (Tom Tromey).
#=drop: Upstreamed.
Patch514: gdb-gdbindex-v1-to-v2.patch
#=drop: Upstreamed.
Patch512: gdb-gdbindex-bigendian.patch
#=drop: Upstreamed.
Patch515: gdb-gdbindex-v2-to-v3.patch
# [ifunc] Fix crash on deleting watchpoint of an autovariable (BZ 637770).
#=drop: A part of archer-jankratochvil-ifunc work.
Patch513: gdb-bz637770-ifunc-watchpoint-delete.patch
# Fix python stale error state, also fix its save/restore (BZ 639089).
#=drop: Just a backport.
Patch518: gdb-testsuite-lib-python.patch
#=drop: Upstreamed.
Patch516: gdb-python-error-state.patch
# Fix inferior exec of new PIE x86_64 (BZ 638979).
#=drop: Upstreamed.
Patch517: gdb-exec-pie-amd64.patch
# Fix crash on CTRL-C while reading an ELF symbol file (BZ 642879).
#=push
Patch520: gdb-bz642879-elfread-sigint-stale.patch
# Fix .gdb_index memory corruption (BZ 653644).
#=drop
Patch527: gdb-bz653644-gdbindex-double-free.patch
# Fix crash on stale bpstat (BZ 661773).
Patch529: gdb-stale-bpstat-2of3.patch
Patch530: gdb-stale-bpstat-3of3.patch
# Backport gdb.base/break-interp.exp test (+prelink fix) on PPC (BZ 663449).
#=drop
Patch533: gdb-ppc-test-break-interp-1of6.patch
#=drop
Patch534: gdb-ppc-test-break-interp-2of6.patch
#=drop
Patch535: gdb-ppc-test-break-interp-3of6.patch
#=drop
Patch536: gdb-ppc-test-break-interp-4of6.patch
#=drop
Patch537: gdb-ppc-test-break-interp-5of6.patch
#=drop
Patch538: gdb-ppc-test-break-interp-6of6.patch
# Backport gdb.cp/infcall-dlopen.exp test (BZ 639645).
#=drop
Patch539: gdb-test-infcall-dlopen-1of2.patch
#=drop
Patch540: gdb-test-infcall-dlopen-2of2.patch
# New testcase py-prettyprint.exp:print hint_error (for BZ 611569, BZ 629236).
#=fedoratest
Patch541: gdb-test-pp-hint-error.patch
# New test gdb.arch/x86_64-pid0-core.exp for kernel PID 0 cores (BZ 611435).
#=fedoratest
Patch542: gdb-test-pid0-core.patch
# Backport support of template parameters (Tom Tromey, BZ 562758).
#=drop
Patch543: gdb-template-arguments-1of3.patch
#=drop
Patch544: gdb-template-arguments-2of3.patch
#=drop
Patch545: gdb-template-arguments-3of3.patch
# New test gdb.base/gnu-ifunc.exp:"static gnu_ifunc" (BZ 632259).
# =drop
Patch546: gdb-test-ifunc-static-start.patch
# [archer-tromey-delayed-symfile] New test gdb.dwarf2/dw2-aranges.exp.
# =fedoratest
Patch547: gdb-test-dw2-aranges.patch
# [archer-keiths-expr-cumulative+upstream] Import C++ testcases.
# =fedoratest
Patch548: gdb-test-expr-cumulative-archer.patch
# [vla] Support Fortran vector slices and subsets (BZ 609782).
# =drop
Patch549: gdb-archer-vla-misc.patch
# =drop
Patch550: gdb-archer-vla-subarray.patch
# Fix discontiguous address ranges in .gdb_index - v3->v4 (BZ 672281).
# =drop
Patch551: gdb-gdbindex-v4-1of3.patch
# =drop
Patch552: gdb-gdbindex-v4-2of3.patch
# =drop
Patch553: gdb-gdbindex-v4-3of3.patch
# [ifunc] Fix possible crash on deleting breakpoints (BZ 673483).
Patch558: gdb-ifunc-unchain.patch
# Display pthread_t for threads even from core files (PR 8210, BZ 673696).
Patch559: gdb-core-threads-1of5.patch 
Patch560: gdb-core-threads-2of5.patch
Patch561: gdb-core-threads-3of5.patch
Patch562: gdb-core-threads-4of5.patch
Patch563: gdb-core-threads-5of5.patch
# Fix crash on static method with no parameters.
Patch564: gdb-crash-noparam.patch

%def_enable tui
%def_disable check

BuildRequires: flex libreadline-devel libexpat-devel zlib-devel
BuildRequires: python-devel libstdc++4.4 %{?_enable_tui:libncursesw-devel}
%{?!_without_check:%{?!_disable_check:BuildRequires: dejagnu glibc-devel-static gcc-c++ gcc-fortran gcc-java gcc-objc prelink valgrind /proc /dev/pts}}

%description
GDB is a full featured, command driven debugger.  GDB allows you to
trace the execution of programs and examine their internal state at
any time.  The debugger is most effective when used together with a
supported compiler, such as those from the GNU Compiler Collection.

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

### RedHat patches
%patch232 -p1
%patch349 -p1
%patch420 -p1
%patch101 -p1
%patch103 -p1
%patch104 -p1
%patch105 -p1
%patch106 -p1
%patch111 -p1
%patch112 -p1
%patch118 -p1
%patch122 -p1
%patch125 -p1
%patch133 -p1
%patch136 -p1
%patch140 -p1
%patch141 -p1
%patch259 -p1
%patch142 -p1
%patch145 -p1
%patch148 -p1
%patch153 -p1
%patch157 -p1
%patch158 -p1
%patch160 -p1
%patch161 -p1
%patch162 -p1
%patch163 -p1
%patch164 -p1
%patch169 -p1
%patch170 -p1
%patch176 -p1
%patch188 -p1
%patch190 -p1
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
%patch241 -p1
%patch245 -p1
%patch247 -p1
%patch254 -p1
%patch258 -p1
%patch260 -p1
%patch261 -p1
%patch263 -p1
%patch265 -p1
%patch266 -p1
%patch271 -p1
%patch274 -p1
%patch353 -p1
%patch282 -p1
%patch284 -p1
%patch287 -p1
%patch289 -p1
%patch290 -p1
%patch293 -p1
%patch294 -p1
%patch296 -p1
%patch298 -p1
%patch304 -p1
%patch309 -p1
%patch311 -p1
%patch315 -p1
%patch317 -p1
%patch318 -p1
%patch320 -p1
%patch324 -p1
%patch326 -p1
%patch329 -p1
%patch330 -p1
%patch331 -p1
%patch332 -p1
%patch337 -p1
%patch343 -p1
%patch348 -p1
%patch360 -p1
%patch381 -p1
%patch382 -p1
%patch391 -p1
%patch392 -p1
%patch397 -p1
%patch403 -p1
%patch404 -p1
%patch405 -p1
%patch389 -p1
%patch394 -p1
%patch407 -p1
%patch408 -p1
%patch412 -p1
%patch417 -p1
%patch451 -p1
%patch454 -p1
%patch459 -p1
%patch461 -p1
%patch470 -p1
%patch475 -p1
%patch486 -p1
%patch415 -p1
%patch519 -p1
%patch489 -p1
%patch490 -p1
%patch491 -p1
%patch493 -p1
%patch496 -p1
%patch497 -p1
%patch499 -p1
%patch500 -p1
%patch501 -p1
%patch502 -p1
%patch503 -p1
%patch504 -p1
%patch506 -p1
%patch507 -p1
%patch508 -p1
%patch509 -p1
%patch510 -p1
%patch511 -p1
%patch514 -p1
%patch512 -p1
%patch515 -p1
%patch513 -p1
%patch516 -p1
%patch517 -p1
%patch518 -p1
%patch520 -p1
%patch527 -p1
%patch533 -p1
%patch534 -p1
%patch535 -p1
%patch536 -p1
%patch537 -p1
%patch538 -p1
%patch539 -p1
%patch540 -p1
%patch529 -p1
%patch530 -p1
%patch541 -p1
%patch542 -p1
%patch543 -p1
%patch544 -p1
%patch545 -p1
%patch546 -p1
%patch547 -p1
%patch548 -p1
%patch549 -p1
%patch550 -p1
%patch551 -p1
%patch552 -p1
%patch553 -p1
%patch558 -p1
%patch559 -p1
%patch560 -p1
%patch561 -p1
%patch562 -p1
%patch563 -p1
%patch564 -p1
%patch335 -p1

# Debian patches
%patch11 -p1
%patch12 -p1
%patch13 -p1
%patch14 -p1
%patch15 -p1

# ALT patches
%patch1 -p1
%patch2 -p1

# We don't need these subdirs.
rm -r gdb/gdbserver readline

find -type f -name \*.orig -delete
bzip2 -9k gdb/{MAINTAINERS,NEWS,PROBLEMS}

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

%define buildtarget build-%_target
rm -rf %buildtarget
mkdir %buildtarget
pushd %buildtarget

%define _configure_script ../configure
export \
	ac_cv_have_x=${ac_cv_have_x='have_x=yes ac_x_includes=%_x11includedir ac_x_libraries=%_x11libdir'} \
	%{?!_enable_tui:ac_cv_search_tgetent='none required'} \
	#
%configure \
	--with-gdb-datadir=%_libdir/gdb \
	--with-pythondir=%_datadir/gdb/python \
	--with-separate-debug-dir=/usr/lib/debug \
	--enable-gdb-build-warnings=,-Wno-unused \
	--disable-werror \
	--disable-sim \
	--disable-rpath \
	--with-system-readline \
	--without-libexpat-prefix \
	--without-rpm \
	--without-libunwind \
	--enable-64-bit-bfd \
	%subst_enable tui \
	#

%make_build
make info
grep -q '#define HAVE_ZLIB_H 1' gdb/config.h

popd #%buildtarget

%install
%makeinstall_std -C %buildtarget

install -pm755 gdb/gdb_gcore.sh %buildroot%_bindir/gcore
install -pm644 %_sourcedir/gdb-gstack.man %buildroot%_man1dir/gstack.1
install -pDm644 %_sourcedir/gdb.desktop %buildroot%_desktopdir/gdb.desktop

# This file is not needed.
%{?_enable_tui:rm %buildroot%_bindir/gdbtui; ln -sf gdb.1 %buildroot%_man1dir/gdbtui.1}

# These files are already packaged as a part of binutils.
rm %buildroot%_infodir/{bfd,configure,standard}*
rm %buildroot%_datadir/locale/*/LC_MESSAGES/{bfd,opcodes}.mo

pushd %buildtarget
mkdir -p %buildroot%_libdir
install -pm644 bfd/libbfd.a libiberty/libiberty.a opcodes/libopcodes.a \
	gdb/libgdb.a libdecnumber/libdecnumber.a \
	%buildroot%_libdir/
popd #%buildtarget

mkdir -p %buildroot%_libdir/gdb/auto-load

%check
[ -w /dev/ptmx -a -f /proc/self/maps ] || exit
pushd %buildtarget/gdb
%__cc %optflags -o orphanripper %_sourcedir/gdb-orphanripper.c -lutil
./orphanripper make -k check ||:
popd

%files
%_bindir/*
%_man1dir/*
%_infodir/*
%_datadir/gdb
%_libdir/gdb
%_desktopdir/*
%doc gdb/{MAINTAINERS,NEWS,PROBLEMS}.bz2

%files -n libgdb-devel
%_includedir/*
%_libdir/lib*.a

%changelog
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
