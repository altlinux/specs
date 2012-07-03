Name: qa-robot
Version: 0.3.3
Release: alt1

Summary: Simple notification system
License: GPL
Group: File tools

Source: %name-%version.tar

BuildArch: noarch

# for `grep -o'
Requires: grep >= 2.5

# Automatically added by buildreq on Mon Nov 15 2010 (-bi)
BuildRequires: perl-Lingua-EN-Inflect perl-Text-CSV_XS perl-devel perl-podlators

%description
qa-robot reports various state changes, in terms of new, old,
and (possibly) updated entries.  See qa-robot(1) for details.

%prep
%setup

%build
%perl_vendor_build INSTALLMAN1DIR=%_man1dir

%install
%perl_vendor_install

%files
%_bindir/*
%_man1dir/*.*

%changelog
* Wed Aug 31 2011 Dmitry V. Levin <ldv@altlinux.org> 0.3.3-alt1
- trap.sh: fixed signal handling.
- rpmpeek -n: changed to ensure that unpacked tree is readable.
- rpmpeek: documented -h and -n options.

* Mon Nov 15 2010 Dmitry V. Levin <ldv@altlinux.org> 0.3.2-alt1
- packages: Fixed SERIAL check.
- qa-robot: Added notion of branch, added -b option to override
  default branch.
- rpmsodiff: Changed to treat "R" and "u" symbols as "defs".
- cmdcache_hash: Updated for coreutils-8.6.
- rpmpeek: Added -n option.
- rpmelfneed, rpmelfsym, rpmfile: Use "rpmpeek -n".
- Fixed build with new perl.

* Tue Nov 27 2007 Alexey Tourbin <at@altlinux.ru> 0.3.1-alt1
- rpmsoname, rpmsodiff: fixed soname detection on x86_64
- many other minor changes; note that some files are not part
  of the package but still developed in the git repo
  http://git.altlinux.org/people/at/packages/qa-robot.git

* Sat May 27 2006 Alexey Tourbin <at@altlinux.ru> 0.3-alt1
- this release includes some general-purpose shell tools:
  + cmdcache - simple cache for command output
  + tmpdir.sh - manage $TMPDIR
  + trap.sh - manage exit traps
- this release includes some auxiliary tools for RPM processing:
  + rpmargs - process RPM packages (iterator for other scripts)
  + rpmpeek - unpack and execute command within RPM contents
  + rpmfile - list file modes and types in RPM packages
  + rpmelfsym - list symbols from object files in RPM packages
  + rpmsoname - list files that provide sonames in RPM package
  + rpmelfneed - extract DT_NEEDED entries
  (these tools are the basis for building data models)
- this release also includes some tools for higher-level repo analysis:
  + bad_elf_symbols - list unresolved symbols within the repo
  + dup_elf_symbols - list binary code duplication
  + linkage_problems - list possible linkage problems
  + abi_drift - analyze new apps/old libraries problem
- (should be packaged elsewhere) rpmsodiff: auxiliary tool for analyzing
  ABI changes and producing version scripts for linker
- TODO: complete docs; all the sutff is released under the GPL
- other changes:
  + bugs: implemented bwk, awk-based domain-specific lang for processing bugs
  + bugs: use GET instead of wget... sucko! really sucko!!
  + qa-robot: introduced dump.log (for possible roll-backs etc.)
  + qa-robot: Dmitry Levin introduced -a option (for arch-specific workdirs)

* Wed Sep 07 2005 Alexey Tourbin <at@altlinux.ru> 0.2-alt1
- %_bindir/csv2tab: new conversion utility
- %_bindir/inflect: new utility for plural inlections
- dropped %_datadir/%name, all scripts now installed under %_bindir
- %_bindir/bugs:
  + added `reporter' and `assigned_to' fields (e-mail addresses)
  + added section for reopened bugs
  + added section for 10 random bugs (critical bugs have higher priority)
- %_bindir/packages:
  + added `packager' field
  + implemented rpm_recent_changes() for new packages
  + implemented rpm_changes_since() for updated packages
- %_bindir/unmets
  + added options for custom apt.conf and sources.list
  + written manual page (so have at it!)

* Wed Aug 03 2005 Alexey Tourbin <at@altlinux.ru> 0.1-alt1
- initial revision
