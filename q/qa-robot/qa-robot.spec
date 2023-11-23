Name: qa-robot
Version: 0.3.10
Release: alt1

Summary: Simple notification system
License: GPL
Group: File tools

Source: %name-%version.tar

BuildArch: noarch

# for `grep -o'
Requires: grep >= 2.5
# for packages and unexpanded_macros
Requires: perl(RPM/Header.pm), perl(RPM/Vercmp.pm)

# Automatically added by buildreq on Mon Nov 15 2010 (-bi)
BuildRequires: perl-Lingua-EN-Inflect perl-Text-CSV_XS perl-devel perl-podlators

%description
qa-robot reports various state changes, in terms of new, old,
and (possibly) updated entries.  See qa-robot(1) for details.

%package -n tmpdir.sh
Summary: tmpdir.sh and trap.sh helpers for shell programming
Group: Development/Other
# qa-robot included {tmpdir,trap}.sh before
Conflicts: qa-robot < 0.3.9-alt2

%description -n tmpdir.sh
%summary.

Usage example:

    . tmpdir.sh

%package -n rpmpeek
Summary: Peek inside an rpm file by running a command in the unpacked tree
Group: File tools

%description -n rpmpeek
%summary.

%prep
%setup

%build
%perl_vendor_build INSTALLMAN1DIR=%_man1dir

%install
%perl_vendor_install
pushd %buildroot
mkdir ./bin
mv .%_bindir/{tmpdir,trap}.sh -t ./bin/
popd

%files
%_bindir/*
%_man1dir/*.*
%exclude /bin/tmpdir.sh
%exclude /bin/trap.sh
%exclude %_man1dir/tmpdir.sh*
%exclude %_man1dir/trap.sh*
%exclude %_bindir/rpmpeek
%exclude %_man1dir/rpmpeek*

%files -n tmpdir.sh
/bin/tmpdir.sh
/bin/trap.sh
%_man1dir/tmpdir.sh*
%_man1dir/trap.sh*

%files -n rpmpeek
%_bindir/rpmpeek
%_man1dir/rpmpeek*

%changelog
* Thu Nov 23 2023 Vitaly Chikunov <vt@altlinux.org> 0.3.10-alt1
- rpmpeek: Add (bash) user-friendly mode.

* Wed Mar 27 2019 Ivan Zakharyaschev <imz@altlinux.org> 0.3.9-alt2
- Splitted subpkgs off: tmpdir.sh, rpmpeek.

* Mon Oct 10 2016 Igor Vlasenko <viy@altlinux.ru> 0.3.9-alt1
- fix for mutt 1.5 (thanks to glebfm@)

* Mon Oct 10 2016 Igor Vlasenko <viy@altlinux.ru> 0.3.8-alt1
- proper workdir definition

* Fri Oct 07 2016 Igor Vlasenko <viy@altlinux.ru> 0.3.7-alt1
- rpm 404 -> 413 migration: use portable subset of perl-RPM

* Tue Dec 17 2013 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.3.6-alt1
- rpmsodiff:
  + Return 1 if packages differ (RH#1004450).
  + Treat "A", "B", "V", and "i" symbols as "defs".

* Fri Sep 13 2013 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.3.5-alt1
- packages: canonicalize rpms directory and %%packager.
- buildlog_deps: trim very long lines
- unmets: add -l option to add APT::Cache-Limit to apt.conf

* Wed Feb 27 2013 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.3.4-alt1
- unmets: add -a option to work with unnative arches.

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
