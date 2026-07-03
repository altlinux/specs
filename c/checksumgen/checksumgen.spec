%define _unpackaged_files_terminate_build 1

Name:     checksumgen
Version:  0.4.7
Release:  alt1

Summary:  Generates checksum file for an RPM repo slice
License:  GPLv2
Group:    Monitoring
Vcs:      http://git.altinux.org:packages/checksumgen.git

Packager: Paul Wolneykien <manowar@altlinux.org>
Source:   %name-%version.tar

BuildArch: noarch

BuildRequires: bats /proc apt-repo-tools rpmpeek fakeroot gostsum shellcheck

Requires: apt-repo-tools rpmpeek fakeroot gostsum

%description
Generates checksum file for an RPM repo slice.

%package -n checksumbot
Summary: A script for RPM checksum repository maintenance
Group:    Monitoring

%description -n checksumbot
A script to update and commit RPM checksum files.

%prep
%setup

%build
%make_build

%install
%makeinstall_std sysconfdir=%_sysconfdir unitdir=%_unitdir logrotatedir=%_logrotatedir bindir=%_bindir libexecdir=%_prefix/libexec mandir=%_mandir

%check
%make_build syntax
%make_build check

%files
%doc checksumgen/README
%dir %_prefix/libexec/%name
%_prefix/libexec/%name/*.sh
%_bindir/%name
%_bindir/checksumdiff
%_bindir/checksummerge
%_man1dir/%name.1.*
%_man1dir/checksumdiff.1.*
%_man1dir/checksummerge.1.*

%files -n checksumbot
%_bindir/checksumbot
%_man1dir/checksumbot.1.*

%changelog
* Fri Jul 03 2026 Paul Wolneykien <manowar@altlinux.org> 0.4.7-alt1
- Make CHKSUMPATH be 'chksum' by default.
- Added --init option (and others) to initialize the checksum
  Git repository.
- checksumbot: Fix: Don't show last commit if no new commit was made.

* Thu Dec 18 2025 Paul Wolneykien <manowar@altlinux.org> 0.4.6-alt1
- Make data processing independent of the current locale
  (Fixes: OVE-20251218-0001).
- Fixed sum_files.sh: Skip find in the case of an empty $INCLUDE.

* Wed Dec 17 2025 Paul Wolneykien <manowar@altlinux.org> 0.4.5-alt1
- Untabify all help pages.
- checksumbot: Added --cb option to override CHKSUMBRANCH
  configuration option.
- checksumgen: Fixed shellcheck SC2317.

* Tue Dec 16 2025 Paul Wolneykien <manowar@altlinux.org> 0.4.4-alt1
- checksumbot: Include checksumdiff report in the output.
- checksumbot: Include RPM names diff in the output.
- checksumbot: Added configuration option to include RPM package
  lists into the checksum repository.
- Added option to send checksumdiff statistic report to a file.
- Make checksumdiff report statistics in verbose mode.
- Make checksumdiff check the total record counters.
- checksumdiff: Verify per-task checksum files using one-line
  checksum views.
- Always replace per-task *.chksum files when checksumdiff.
- Make checksummerge support inplace file update.

* Tue Dec 09 2025 Paul Wolneykien <manowar@altlinux.org> 0.4.3-alt1
- checksumgen: Improved job control: reap all processes when
  interrupted.
- checksumgen: Fix: Exit with error if one of the jobs exited
  with error.
- checksumgen: Fix: Exclude directories from file list
  (Fixes: OVE-20251209-0001).
- checksumgen: Only trace xargs if DEBUG > 1.
- checksumgen: Print the TODO list of packages in DEBUG mode.
- checksumgen: Output the command line in DEBUG mode.
- Don't enable shell trace (-x) if DEBUG < 3.
- checksumbot: Run mkimage-profiles with REPORT=1 in debug mode.
- checksumbot: Added -r, --ref command-line option.
- checksumbot: Fix: Use LANG=C for log file timestamps.

* Wed Nov 26 2025 Paul Wolneykien <manowar@altlinux.org> 0.4.2-alt1.1
- Note, that v0.3.0-alt1 fixes missing checksum data for *.ko.zst files
  by including *.ko.zst by default (Fixes: OVE-20251204-0001).

* Wed Nov 26 2025 Paul Wolneykien <manowar@altlinux.org> 0.4.2-alt1
- setup.sh: Fix: Verify the actually written configuration.
- setup.sh: Fixed reading ${...} config values.
- checksumbot: Use apt.$BRANCH.$ARCH.conf for update and
  apt.$DISTROVER.$ARCH.conf for release.
- Let `make setup` accept CONFIG=path-to-config.
- Fix: Revert back to a non-override-values config.
- setup.sh: Added `Dir::Etc::parts "/var/empty";` to the default
  APT config.
- setup.sh: Added `Dir::Etc::main "/dev/null";` to the default
  APT config.

* Mon Nov 24 2025 Paul Wolneykien <manowar@altlinux.org> 0.4.1-alt1
- checksumbot: Sync version with the main package.
- Fixed license.
- Make checksumdiff support packages with no dist-tags.
- Fix checksumbot: Use FETCH_HEAD to checkout mkimage-profiles
  (MKIPREF might be a branch now).
- setup.sh: Fixed APT conf generation.
- Fixed checksumbot: Add empty line before MKIPKEY in the default
  config.

* Fri Nov 14 2025 Paul Wolneykien <manowar@altlinux.org> 0.4.0-alt1
- Added setup script for checksumbot (setup.sh).
- Added manual pages for 'checksumbot' and all new utils.
- Fixed -p, --prev option description in 'checksumgen'.
- Added the 'checksummerge' utility.
- Added new 'checksumdiff' utility.
- Reworked version of checksumbot (0.2.0): Rely on mkimage-profiles
  and 'alt-sp-common-update.tar' profile).

* Tue Aug 12 2025 Paul Wolneykien <manowar@altlinux.org> 0.3.1-alt1
- Updated the README file.
- Switch license to GNU GPL v2.
- Removed list_rpms.sh.
- Added the manual page.

* Tue Aug 12 2025 Paul Wolneykien <manowar@altlinux.org> 0.3.0-alt1
- Include all files under /lib/firmware by default.
- Added -I | --include options, include *.ko.zst by default.

* Mon May 26 2025 Paul Wolneykien <manowar@altlinux.org> 0.2.2-alt1
- Added tests.
- Fixed RPM signature key listing.
- Replace --isodir with --pkglist option.
- Display warning when the todo list is empty.
- Fixed delsed generation.
- Fix/improve the baselist grep (closes: 54438).
- Fix: Sort the todo list.
- Fixed prevlist grep patterns: use fixed strings.
- Fixed \t (tab) in query format string.
- Fix: Own %_prefix/libexec/checksumgen.

* Wed May 21 2025 Paul Wolneykien <manowar@altlinux.org> 0.2.1-alt1
- Add -n | --no-fakeroot option.
- Added the first basic unit-test.
- Fixed RPM-list check in repo mode

* Tue May 20 2025 Paul Wolneykien <manowar@altlinux.org> 0.2.0-alt1
- Renamed to 'checksumgen'.
- Support a list of RPM filenames in -l | --rpmlist argument.
- Parallel multiprocessing of RPM packages.

* Sun Jul 14 2024 Paul Wolneykien <manowar@altlinux.org> 0.1.2-alt1
- Added notes about usage with 'mkimage-profiles'.
- Truncate existing default or specified missings file.
- Allow to specify missings filename with -m, --missings.
- Fix: Don't overwrite "$workdir"/rpmlist
- Added -I, --isodir option.
- Always include 'noarch' when searching and filtering RPM packages.
- Added list_rpms.sh.
- Added README.md symlink (for GitLab).
- Added `make local` to configure the CLI to be run from the
  current directory.

* Wed Jul 10 2024 Paul Wolneykien <manowar@altlinux.org> 0.1.1-alt1
- Updated the README.
- Make generate-checksum a CLI interface to underlying utils.
- Make pkg_list_get_executables_checksums.sh able to output to stdout.

* Sun Jul 07 2024 Paul Wolneykien <manowar@altlinux.org> 0.1.0-alt1
- Initial version for C10F2.
