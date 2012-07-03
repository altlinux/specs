Name: prelink
Version: 0.4.4
Release: alt2

Summary: An ELF prelinking utility
License: GPLv2+
Group: System/Base

# http://pkgs.fedoraproject.org/repo/pkgs/prelink/prelink-20101123.tar.bz2/f207dafd3f87f9ffc9cf2c6f8016e3b9/prelink-20101123.tar.bz2
Source: prelink-20101123.tar
Source2: prelink.conf
Source3: prelink.cron
Source4: prelink.sysconfig

# Automatically added by buildreq on Sat Nov 18 2006
BuildRequires: gcc-c++ libelf-devel

ExclusiveArch: %ix86 alpha sparc sparc64 s390 s390x x86_64 ppc ppc64

%description
This package contains a utility which modifies ELF shared libraries and
executables, so that far less relocations need to be resolved at runtime
and thus programs come up faster.

%prep
%setup -n prelink
sed -i 's/-Wl,--dynamic/-Wl,--no-as-needed,--dynamic/' \
	testsuite/{functions,Makefile}.*
sed -i 's/ -shared /&-Wl,--no-as-needed /' testsuite/*.sh

%build
%add_optflags -D_GNU_SOURCE
%configure --enable-shared
sed -i 's,-all-static,,' src/Makefile
%make_build
make -k -C testsuite check-harder ||:
make -k -C testsuite check-cycle ||:

%install
%makeinstall

mkdir -p %buildroot%_man5dir
ln -s ../man8/prelink.8 %buildroot%_man5dir/prelink.conf.5

mkdir -p %buildroot/etc/{sysconfig,prelink.conf.d,cron.daily,rpm/macros.d}
install -pm644 %_sourcedir/prelink.conf %buildroot/etc/
install -pm700 %_sourcedir/prelink.cron %buildroot/etc/cron.daily/prelink
install -pm644 %_sourcedir/prelink.sysconfig %buildroot/etc/sysconfig/prelink

cat > %buildroot/etc/rpm/macros.d/prelink <<"EOF"
# rpm verifies prelinked libraries using a prelink undo helper.
#     Note: The 2nd token is used as argv[0] and "library" is a
#     placeholder that will be deleted and replaced with the appropriate
#     library file path.
%%__prelink_undo_cmd     %_sbindir/prelink prelink -y library
EOF
chmod 644 %buildroot/etc/rpm/macros.d/prelink

mkdir -p %buildroot/var/{lib,log}/prelink
touch %buildroot/var/lib/prelink/full
touch %buildroot/var/lib/prelink/quick
touch %buildroot/var/lib/prelink/force
touch %buildroot/var/log/prelink/prelink.log

%post
touch /var/lib/prelink/force

%files
%doc AUTHORS doc/prelink.pdf
%verify(not md5 size mtime) %config(noreplace) /etc/prelink.conf
%verify(not md5 size mtime) %config(noreplace) /etc/sysconfig/prelink
/etc/rpm/macros.d/prelink
%dir %_sysconfdir/prelink.conf.d/
/etc/cron.daily/prelink
%_sbindir/prelink
%_bindir/execstack
%_man5dir/prelink.*
%_man8dir/prelink.*
%_man8dir/execstack.*
%dir /var/lib/prelink/
%attr(0644,root,root) %verify(not md5 size mtime) %ghost %config(missingok,noreplace) /var/lib/prelink/full
%attr(0644,root,root) %verify(not md5 size mtime) %ghost %config(missingok,noreplace) /var/lib/prelink/quick
%attr(0644,root,root) %verify(not md5 size mtime) %ghost %config(missingok,noreplace) /var/lib/prelink/force
%attr(0750,root,adm) %dir /var/log/prelink/
%attr(0644,root,root) %verify(not md5 size mtime) %ghost %config(missingok,noreplace) /var/log/prelink/prelink.log

%changelog
* Wed Feb 16 2011 Dmitry V. Levin <ldv@altlinux.org> 0.4.4-alt2
- Made /etc/sysconfig/prelink readable for everyone.

* Mon Feb 07 2011 Dmitry V. Levin <ldv@altlinux.org> 0.4.4-alt1
- Updated to 0.4.4 (20101123).
- Relocated /var/lib/misc/prelink.* to /var/lib/prelink/.

* Fri Nov 16 2007 Dmitry V. Levin <ldv@altlinux.org> 0.3.10-alt1
- Updated to 0.3.10 (20061201).
- Fixed testsuite and reenabled it.
- Relocated prelink.log to /var/log/prelink/.
- Build with -D_GNU_SOURCE to get off64_t definition
  which is necessary for libelf-0.130.

* Sat Nov 18 2006 Vitaly Lipatov <lav@altlinux.ru> 0.3.9-alt1
- restore from orphaned, fix Source URL
- new version from FC6
- remove static build, update buildreq
- disable tests (broken linking)

* Tue Jan 24 2006 Anton D. Kachalov <mouse@altlinux.org> 0.3.6-alt3
- build shared and static version of prelink (#8856)

* Tue Oct 18 2005 Kachalov Anton <mouse@altlinux.ru> 0.3.6-alt2
- added RPM-macros

* Fri Oct 14 2005 Kachalov Anton <mouse@altlinux.ru> 0.3.6-alt1
- first build for Sisyphus

* Thu Sep  1 2005 Jakub Jelinek <jakub@redhat.com> 0.3.6-1
- remove kernel requires - installed kernel doesn't imply running
  kernel anyway and in FC5 kernels older than 2.4.20 can't be used
  anyway, as LinuxThreads are no longer included
- don't relocate stabs N_{B,D,}SLINE (reported by Ashley Pittman)

* Fri Jul 29 2005 Jakub Jelinek <jakub@redhat.com> 0.3.5-2
- on ppc32 handle -mbss-plt .got sections created with -msecure-plt
  capable binutils (#164615)

* Fri Jun 10 2005 Jakub Jelinek <jakub@redhat.com> 0.3.5-1
- support for ppc32 -msecure-plt libraries and binaries
- don't crash if d_tag is invalid (#155605)
- rebuilt against robustified libelf (CAN-2005-1704)
- fix handling of libraries and binaries given on command
  line without any / characters in the filename

* Mon Mar 14 2005 Jakub Jelinek <jakub@redhat.com> 0.3.4-3
- fix relocation of .debug_loc (#150194)

* Sat Mar  5 2005 Jakub Jelinek <jakub@redhat.com> 0.3.4-2
- rebuilt with GCC 4

* Mon Feb  7 2005 Jakub Jelinek <jakub@redhat.com> 0.3.4-1
- fix prelink -uo when linked against libselinux (#146637)
  and when the -o argument filename is on a different filesystem
  than the object that needs undoing

* Tue Nov 23 2004 Jakub Jelinek <jakub@redhat.com> 0.3.3-1
- if layout code needs to re-prelink some library, make sure
  all libraries that depend on it are re-prelinked too (#140081)
- add several more checks before deciding it is ok to prelink a binary
  (even if another bug like #140081 was in, these checks should hopefully
  catch it and refuse to (re-)prelink the binary)
- added new PRELINK_NONRPM_CHECK_INTERVAL variable to %_sysconfdir/prelink,
  defaulting to 7 days.  Prelink nightly job will not do anything
  if that interval has not elapsed since last prelinking and
  and the rpm database has not been modified since that prelinking.
  This is useful if you rely on rpm/up2date/yum/apt-rpm for library
  and binary updates.  If you combine it with other means (installs
  from source, tarballs etc.), you probably want to
  set PRELINK_NONRPM_CHECK_INTERVAL=0.
- update prelink man page (#126468)

* Tue Oct 12 2004 Jakub Jelinek <jakub@redhat.com> 0.3.2-11
- update PT_PHDR program header if present when adding new program
  headers (#133734)

* Sat Oct  2 2004 Jakub Jelinek <jakub@redhat.com> 0.3.2-10
- support for non-absolute blacklist glob patterns (e.g. -b *.la)
- cache information about non-prelinkable files (non-ELF, statically linked,
  too small .dynamic, DT_TEXTREL with conflicts against it; #132056)
- other speedups for prelink -aq
- for --verify, make sure only read-only fd's are opened for the
  unprelinked temporary file, otherwise a kernel might ETXTBUSY on it
  (#133317)
- change warning message if some object's dependencies can't be found
- add buildrequires libselinux-devel and use %%{_tmppath} instead
  of /var/tmp in Buildroot (#132879)

* Wed Sep  8 2004 Jakub Jelinek <jakub@redhat.com> 0.3.2-8
- handle overlapping .opd sections on ppc64

* Tue Sep  7 2004 Jakub Jelinek <jakub@redhat.com> 0.3.2-7
- fix warning messages if setting of security context fails

* Wed Jul  7 2004 Jakub Jelinek <jakub@redhat.com> 0.3.2-6
- change sed separator in testsuite scripts from | to , if \|
  is present in regexps, as that invokes undefined behaviour
  which changed between GNU sed 4.0.9 and 4.1

* Wed Jul  7 2004 Jakub Jelinek <jakub@redhat.com> 0.3.2-5
- skip vDSO in ldd /sbin/init output when determining if /sbin/telinit -u
  should be run (#127350)

* Tue Jun 15 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Thu May 20 2004 Jakub Jelinek <jakub@redhat.com> 0.3.2-3
- 4 SPARC 64-bit fixes
- use $CC instead of gcc when checking for TLS support in tls*.sh

* Thu May 20 2004 Jakub Jelinek <jakub@redhat.com> 0.3.2-2
- add 2 new TLS testcases (one that fails e.g. with glibc < 2.3.3-28
  on IA-32)
- SPARC TLS support

* Wed May  5 2004 Jakub Jelinek <jakub@redhat.com> 0.3.2-1
- fix cxx.c:68: find_cxx_sym: Assertive `n < ndeps' failed problem
  on 32-bit architectures (#118522)
- build prelink.cache into temporary file and atomically rename over
  (#121109)

* Wed Mar 17 2004 Jakub Jelinek <jakub@redhat.com> 0.3.1-2
- unlink temporary files if renaming to the destination or setting of
  security context failed (#118251)
- fix bi-architecture prelinking (#118226)
- if prelink called from the cron script fails, note the exit status
  into /var/log/prelink.log

* Thu Mar  4 2004 Jakub Jelinek <jakub@redhat.com> 0.3.1-1
- add prelink documentation (PDF format)
- fix assertion failures on PPC (.sdynbss related, #115925)
- fix prelink --help (#115202)
- avoid free on uninitialized variable in one error path (#117332)
- s/i386/%%{ix86}/ to make mharris happy

* Mon Feb 16 2004 Jakub Jelinek <jakub@redhat.com> 0.3.0-21
- fix prelink abort in certain cases where a new PT_LOAD segment
  needs to be added (seen on AMD64)

* Thu Jan 29 2004 Jakub Jelinek <jakub@redhat.com> 0.3.0-20
- clearify message about unlisted dependencies
- don't do SELinux context copying if is_selinux_enabled () < 0

* Tue Jan 27 2004 Jakub Jelinek <jakub@redhat.com> 0.3.0-19
- refuse to prelink objects whose dependencies as reported by
  ldd don't include all dependencies transitively (this can
  happen when using RPATH and a shared library with the same
  SONAME exists both in that RPATH and either another RPATH
  or standard library directories)
- add testcase for this
- rework .dynsym/.symtab STT_SECTION translation, so that it works
  with binutils which put only sections not generated by the linker
  into .dynsym for shared libraries
- fix make check, so that it is not confused by 2.6.x kernel
  VDSOs

* Thu Jan 15 2004 Jakub Jelinek <jakub@redhat.com> 0.3.0-18
- allow R_*_JU?MP_SLOT relocs to point also into .got.plt
  sections on IA32/AMD64/ARM/s390/s390x/SH

* Tue Dec  9 2003 Jakub Jelinek <jakub@redhat.com> 0.3.0-17
- set SELinux security context immediately before renaming,
  not before

* Tue Nov 18 2003 Jakub Jelinek <jakub@redhat.com> 0.3.0-15
- blacklist support
- use FTW_ACTIONRETVAL if available to avoid even stating of
  files in blacklisted directory trees
- SELinux support

* Tue Oct 28 2003 Jakub Jelinek <jakub@redhat.com> 0.3.0-13
- added execstack.8 manpage
- changed order of columns in execstack --query output

* Tue Oct 28 2003 Jakub Jelinek <jakub@redhat.com> 0.3.0-12
- added execstack tool
- added -o option, to be used together with -u
- free temp_filename in close_dso

* Mon Oct 27 2003 Jakub Jelinek <jakub@redhat.com> 0.3.0-11
- fix adjustement of DT_VALRNGLO .. DT_VALRNGHI and
  DT_ADDRRNGLO .. DT_ADDRRNGHI dynamic tags when relocating shared
  libraries
- never adjust p_vaddr/p_paddr/p_offset of PT_GNU_STACK segment
- allow shell wildcards in %_sysconfdir/prelink.conf
- fix REL->RELA conversion of shared libraries if .rel.dyn
  or .rel.plt are last sections in readonly PT_LOAD segment
- force full reprelinking on prelink upgrades (well, first time
  the cron job is run after the upgrade)
- require coreutils, findutils, util-linux, gawk and grep

* Fri Oct 24 2003 Jakub Jelinek <jakub@redhat.com> 0.3.0-10
- avoid removing PT_GNU_STACK segment if decreasing first PT_LOAD segment's
  p_vaddr on IA-32

* Mon Oct 13 2003 Jakub Jelinek <jakub@redhat.com> 0.3.0-9
- avoid prelink crash if first dependency is to be prelinked because
  of address space overlaps

* Thu Oct  9 2003 Jakub Jelinek <jakub@redhat.com> 0.3.0-8
- use /var/lib/misc/prelink.full instead of /var/run/prelink.full for last
  full prelink timestamp (#106721)
- warn about UPX compressed binaries or libraries/binaries without section
  headers (neither can be prelinked obviously)

* Mon Oct  6 2003 Jakub Jelinek <jakub@redhat.com> 0.3.0-7
- don't rely on malloc/calloc/realloc with size 0 returning a unique pointer
- fix testsuite, so that it works even if installed glibc/libstdc++
  is already prelinked

* Wed Sep 17 2003 Jakub Jelinek <jakub@redhat.com> 0.3.0-6
- fix comment in %_sysconfdir/sysconfig/prelink (#106217)

* Tue Sep  2 2003 Jakub Jelinek <jakub@redhat.com> 0.3.0-5
- fix prelink segfault on -z nocombreloc libraries (#103404)
- run one make check round with -Wl,-z,nocombreloc to test handling
  of nocombreloc binaries and libraries

* Fri Aug 15 2003 Jakub Jelinek <jakub@redhat.com> 0.3.0-4
- redirect prelink's stderr from the cron job to prelink.log (#102456)

* Mon Aug 11 2003 Jakub Jelinek <jakub@redhat.com> 0.3.0-3
- fix DT_CHECKSUM computation - do STT_LOCAL symbol frobbing and .mdebug
  updates write_dso would do also before checksum computation (#89953)

* Fri Aug  8 2003 Jakub Jelinek <jakub@redhat.com> 0.3.0-2
- avoid assertion failures when changing PROGBITS .bss back into
  NOBITS .bss (#101813)
- add 2 new tests for it

* Tue Aug  5 2003 Jakub Jelinek <jakub@redhat.com> 0.3.0-1
- run prelink from cron automatically, add %_sysconfdir/sysconfig/prelink
  to configure it
- update manual page

* Tue Jul  1 2003 Jakub Jelinek <jakub@redhat.com> 0.2.1-2
- fix a thinko in the library path checking code
- change R_386_GLOB_DAT into R_386_32 in .gnu.conflict, similarly
  R_X86_64_GLOB_DAT and R_X86_64_64
- fix a bug in find_free_space which caused
  "section file offsets not monotonically increasing" errors on some
  IA-32 binaries
- add --md5 and --sha options
- use mmap during --verify if possible
- add */lib64 directories to prelink.conf

* Mon Jun 30 2003 Jakub Jelinek <jakub@redhat.com> 0.2.1-1
- make sure binaries prelinked for the second and later time without
  unprelinking in between verify correctly
- make sure DT_CHECKSUM computation is the same for newly prelinked
  and second or later time prelinked libraries
- dwarf2 abbrev hash bugfix
- don't allow prelinking libraries outside directories specified
  in config file or on the command line
- several new tests for reprelinking
- pack non-alloced sections and section header table tightly after the
  last alloced section

* Wed Jun 18 2003 Jakub Jelinek <jakub@redhat.com> 0.2.0-28
- finish and enable ppc64
- fix ppc BR{,N}TAKEN reloc handling
- fix up sh_offset values of zero-sized or SHT_NOBITS section
  if ld messed them up
- issue error about bogus library dependency chains instead of
  segfaulting (plus testcases for it)

* Fri Jun 13 2003 Jakub Jelinek <jakub@redhat.com> 0.2.0-27
- add --quick mode
- new test for --quick mode and also reprelinking of binary against
  upgraded shared library which needs more conflicts

* Mon Jun  2 2003 Jakub Jelinek <jakub@redhat.com> 0.2.0-26
- don't segfault in C++ optimizations if a conflict from undefined
  to defined value is seen
- some more ppc64 work

* Fri May 30 2003 Jakub Jelinek <jakub@redhat.com> 0.2.0-25
- exec-shield support
- with -R, don't randomize just base address from which all libs
  are layed out, but also slightly randomize order of libraries
  in the layout queue
- add check-harder and check-cycle makefile goals in testsuite/,
  use it during rpm building

* Fri May 23 2003 Jakub Jelinek <jakub@redhat.com> 0.2.0-24
- optimize out conflicts in G++ 3+ virtual tables if they are just
  because some method has been called from a binary and thus there
  is a .plt slot in the binary. This change not only kills lots of conflicts
  on some KDE programs, but also should speed up runtime (not just startup
  time), since the hop through .plt is bypassed
- added new C++ test
- fix a bug in ppc64 fixup .plt code

* Thu May 22 2003 Jakub Jelinek <jakub@redhat.com> 0.2.0-23
- when updating dynamic tags for executable after section reshuffling,
  check section type as well, so that 0 sized sections don't get the
  tags attached instead of the proper ones
- when an address space conflict is found between libraries for the same
  executable during layouting, check properly for all remaining conflicts
  as well

* Thu May 15 2003 Jakub Jelinek <jakub@redhat.com> 0.2.0-22
- don't adjust DT_REL{,A} if it is 0
- allow prelinking of libraries with no dependencies
- fix handling of libraries with no lazy relocs, no normal relocs or no
  relocs at all
- some new tests
- fix SH (Daniel Jacobowitz)

* Mon May  5 2003 Jakub Jelinek <jakub@redhat.com> 0.2.0-21
- fix prelink on AMD64
- 2 new testcases
- fix for debugging prelink_entry_dump/restore

* Fri May  2 2003 Jakub Jelinek <jakub@redhat.com> 0.2.0-20
- ppc TLS
- some ppc64 work
- avoid using trampolines for nested functions
- fix typo in prelink man page (#89247)

* Tue Apr 15 2003 Jakub Jelinek <jakub@redhat.com> 0.2.0-19
- fix find_readonly_space bug which caused doxygen not to be prelinked

* Mon Feb 17 2003 Jakub Jelinek <jakub@redhat.com> 0.2.0-18
- fix section indices in .symtab if non-alloced sections weren't
  originally monotonically increasing
- s390, s390x and Alpha TLS support

* Mon Feb 10 2003 Jakub Jelinek <jakub@redhat.com> 0.2.0-17
- never try to prelink or relocate stripped-to-file debuginfo

* Tue Jan 21 2003 Jakub Jelinek <jakub@redhat.com> 0.2.0-16
- x86-64 TLS support
- added one more tls testcase

* Fri Dec 13 2002 Jakub Jelinek <jakub@redhat.com> 0.2.0-15
- hopefully finished IA-32 TLS support
- require elfutils 0.72 for various data-swapping fixes

* Wed Dec 11 2002 Jakub Jelinek <jakub@redhat.com> 0.2.0-14
- rebuilt against elfutils 0.69 to fix a make check failure on Alpha

* Mon Dec  9 2002 Jakub Jelinek <jakub@redhat.com> 0.2.0-13
- use ELF_F_PERMISSIVE if defined
- be permissive even when doing --reloc-only
- fix up .plt section sh_entsize on Alpha

* Wed Dec  4 2002 Jakub Jelinek <jakub@redhat.com> 0.2.0-12
- some more fixes for elfutils

* Tue Dec  3 2002 Jakub Jelinek <jakub@redhat.com> 0.2.0-11
- make it work with elfutils instead of libelf 0.[78]
- update to newer auto*/libtool
- some more steps towards TLS support, at least --reloc-only should work

* Thu Oct  3 2002 Jakub Jelinek <jakub@redhat.com> 0.2.0-10
- x86-64, s390x and testsuite fixes

* Sun Sep 29 2002 Jakub Jelinek <jakub@redhat.com> 0.2.0-9
- enable on ppc and x86_64
- fix ppc far PLT slot prelink
- support --undo on ppc
- for bug-compatibility with some unnamed OS changed R_SPARC_RELATIVE
  --undo
- tiny steps towards TLS support on IA-32, more will come

* Tue Aug 27 2002 Jakub Jelinek <jakub@redhat.com> 0.2.0-8
- avoid putting garbage into executable's .gnu.liblist sh_link
  if we did not have to grow .dynstr
- don't segfault on bogus sh_link and sh_info values (#72705)

* Mon Aug 26 2002 Jakub Jelinek <jakub@redhat.com> 0.2.0-7
- when growing allocated shared lib sections (for REL->RELA
  conversion), make sure !PF_W and PF_W segments don't end up
  on the same page
- when finding space for sections in an executable, make sure
  it is not included in between two reloc sections
- for non-zero SHN_ABS symbols on 32-bit arches mask high
  32-bits of st_value (libelf 0.8.x is strict here)

* Fri Aug 23 2002 Jakub Jelinek <jakub@redhat.com> 0.2.0-6
- make it work with libelf 0.8.2

* Fri Jun 21 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Fri Jun 21 2002 Jakub Jelinek <jakub@redhat.com> 0.2.0-4
- add %_sysconfdir/rpm/macros.prelink

* Mon Jun 17 2002 Jakub Jelinek <jakub@redhat.com> 0.2.0-1
- added --undo and --verify mode
- new architectures s390, s390x, arm, sh
- handle binaries/shared libraries with non-allocated sections
  without monotonically increasing sh_offsets
- handle .sbss and .sdynbss
- fixed a bug in 64-bit LE/BE read routines
- removed .rel{,a}.dyn reloc conversion/sorting, it was duplicating
  ld's -z combreloc and complicated lots of things
- fixed STB_LOCAL/STT_SECTION symbol adjusting
- use mkstemp for temporary files, allow --verify for binaries/libs
  on read-only filesystems
- added DWARF-2 .debug_ranges adjustement, special case GCC's
  "set base to 0 and make things absolute instead of relative" trick
- allow arches to override default layout mechanism (for ppc)
- added some new tests, test --undo and --verify modes in the testsuite
- alpha: adjust what R_ALPHA_GLOB_DAT points to too
- i386: apply _32 and _PC32 REL relocs, as apply_rel can be called
  for C++ optimizations before REL->RELA conversion
- ppc: layout strategy to satisfy ppc lib location preferences
- sparc64: handle R_SPARC_DISP64
- x86-64: adjust what R_X86_64_RELATIVE points to too
- link prelink statically, esp. because of --verify mode
- run make check during build process

* Mon Oct  1 2001 Jakub Jelinek <jakub@redhat.com> 0.1.3-7
- fix layout code so that -R works
- on IA-32, when there are no R_386_PC32 relocs and no R_386_32 relocs
  with non-zero addend (= memory content), don't convert REL->RELA,
  only switch R_386_32 relocs to R_386_GLOB_DAT
- support creating a new PT_LOAD segment if necessary, if SHT_NOBITS
  sections are small, instead of adding new PT_LOAD segment just add file
  backing to those NOBITS sections
- added testsuite
- new supported architectures (Alpha including .mdebug section support,
  Sparc, Sparc 64-bit, X86_64 (the last one untested)), beginning of PPC
  support

* Thu Sep  6 2001 Jakub Jelinek <jakub@redhat.com> 0.1.3-6
- make sure lib base is always ELF page size aligned

* Wed Aug 29 2001 Jakub Jelinek <jakub@redhat.com> 0.1.3-5
- fix sorting of .rel*.dyn sections, so that all RELATIVE relocs really
  come first
- when DT_RELCOUNT already exists and conversion REL->RELA is done,
  convert it into DT_RELACOUNT
- set conflict lookupent and conflictent to 0 for undefineds
- don't bother with DT_REL*COUNT for apps, they cannot have any RELATIVE
  relocs

* Tue Aug 28 2001 Jakub Jelinek <jakub@redhat.com> 0.1.3-4
- brown paper bag time: when determining if conversion from REL to RELA
  is needed, check all non-PLT rel sections, including last.
  This caused prelinking to fail with -z combreloc compiled libraries.

* Mon Aug 27 2001 Jakub Jelinek <jakub@redhat.com> 0.1.3-3
- don't use .gnu.reloc section, use .rel.dyn or .rela.dyn instead
- put RELATIVE relocs first, not last, so that DT_REL{,A}COUNT
  works
- put in updated glibc patch
- no need for special binutils patch - all is done in the -z combreloc
  patchset

* Tue Jul 24 2001 Jakub Jelinek <jakub@redhat.com> 0.1.3-2
- use the new DT_GNU_CONFLICT/DT_GNU_LIBLIST/SHT_GNU_LIBLIST constants
- unlink *.#prelink# files if necessary

* Wed Jul 18 2001 Jakub Jelinek <jakub@redhat.com> 0.1.3-1
- fix layout.c
- create .gnu.prelink_undo section, --undo and --verify modes will use that
- some more C++ specific optimizations

* Fri Jul 13 2001 Jakub Jelinek <jakub@redhat.com> 0.1.2-1
- bail out early if ELF object does not have sh_offsets
  monotonically increasing
- disallow prelinking if there are conflicts against read-only
  segments in shared libraries (ie. non-pic shared libraries
  - this is better than bailing out for all non-pic shared libraries)
- add some C++ specific optimizations to reduce number of conflicts,
  more to come

* Tue Jul 10 2001 Jakub Jelinek <jakub@redhat.com> 0.1.1-2
- fix incremental prelinking

* Tue Jul 10 2001 Jakub Jelinek <jakub@redhat.com> 0.1.1-1
- relocate stabs and dwarf-2 debugging formats
- support both --all and incremental prelinking
- handle hardlinks
- limit to libraries in %_sysconfdir/prelink.conf directories or
  directories from command line

* Tue Jul  3 2001 Jakub Jelinek <jakub@redhat.com> 0.1.0-1
- new package
