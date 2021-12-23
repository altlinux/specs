%define _unpackaged_files_terminate_build 1

Name:     srpm-cleanup
Version:  0.1.4
Release:  alt1

Summary:  Remove unused source files from SRPM packages
License:  GPL-3.0-or-later
Group:    Development/Tools
Url:      http://git.altlinux.org/people/manowar/packages/srpm-cleanup.git

Packager: Paul Wolneykien <manowar@altlinux.org>

Source:   %name-%version.tar

BuildArch: noarch
BuildRequires: ronn perl(Pod/Usage.pm) pandoc >= 2

Requires: make apt-repo-tools rsync time findutils coreutils gear
Requires: %name-parallel = %version-%release
Requires: %name-common = %version-%release

%description
srpm-cleanup(1) removes unused source files from SRPM packages.
The list of unused files can be obtained with hsh-separate-sources(1).

This package should be installed on the main management host.


%package audit
Summary:  Default audit on/off scripts for %name
Group:    Development/Tools
License:  GPL-3.0-or-later
Requires: audit
Requires: %name-common = %version-%release

%description audit
Provides the default audit on/off scripts for %name.

This package should be installed on the hosts that build packages.


%package parallel
Summary:  "GNU" Parallel used in srpm-cleanup scripts
Group:    Development/Tools
License:  GPL-3.0-or-later

%description parallel
A "GNU" Parallel version with special patches used in srpm-cleanup
scripts.


%package common
Summary:  Common files for %name
Group:    Development/Tools
License:  GPL-3.0-or-later

%description common
Provides common files for %name.


%prep
%setup

%build
%autoreconf
%configure
%make_build

%install
%makeinstall_std

%files
%_bindir/hsh-separate-sources
%_bindir/srpm-cleanup
%_datadir/%name/import-logs.pl
%_datadir/%name/main.mk
%_datadir/%name/exceptions.list
%_datadir/%name/exclude.list
%_datadir/%name/nprofile
%_man1dir/hsh-separate-sources.1*
%_man1dir/srpm-cleanup.1*
%_man7dir/make-srpm-cleanup.7*
%dir %_docdir/%name
%_docdir/%name/*

%files audit
%_datadir/%name/audit_on
%_datadir/%name/audit_off

%files parallel
%_bindir/parallel_alt

%files common
%dir %_datadir/%name


%changelog
* Thu Dec 23 2021 Paul Wolneykien <manowar@altlinux.org> 0.1.4-alt1
- Package base names in exclude.list (was --- regexp).
- Added 'bind', 'libaom', 'vlc' and 'bind-dyndb-ldap' to the list of
  packages that shouldn't be cleaned.
- export-repo: Do not follow the symbolic links.
- Fixed 'clean-stage4-unused-*' targets.
- Specify the digest for base Docker images
  (alt@sha256:c4eb4ad40440b7c3297c14c91048aa07cbe2534f9e629f4bc9b0d113ca57821f).
- Added 'wpa_supplicant' to exclude.list and install the list
  to pkgdatadir.
- Support regular expressions in exclude.list.
- Pass the time-stamp to the pre and post scripts.
- Introduce file checksumming and checksum verification.
- Fixed copying srpm-cleanup-common to the node directory.
- Fixed building the containers with srpm-cleanup-common.
- Fix: Rebuild the original SRPMs for packages that have failed on
  Stage IV on any arch.
- Fix/improve the 'check-disttags' target.
- Fix: Include 'noinode' into stage III and IV retry categories.

* Mon Nov 08 2021 Paul Wolneykien <manowar@altlinux.org> 0.1.3-alt2
- Fix: Own %_datadir/%name and %_docdir/%name.

* Mon Nov 08 2021 Paul Wolneykien <manowar@altlinux.org> 0.1.3-alt1
- Added --init-cmds=<CMDS>: Execute <CMDS> before the Hasher run.
- vm/Makefile: Mount EXPORT_DIR to /export on the manager node.
- Support custom dist-tags.
- Fix: vm/srpm-cleanup-node: Don't limit the stack size by default.
- Fix: Mount the standard points when building SRPMs (/proc).
- Set MAX_SILENCE = 300 in the default configuration.
- main.mk: Register unknown terminations in Stage IV.
- hsh-separate-sources: Introduce --max-silence=SECS: an option to
  kill frozen Hashers.
- main.mk: Fix: Explicitly touch output directories after a stage
  build.
- srpm-cleanup: Fixed file transfer (and return) caused by *.tar
  input.
- main.mk: Check the 'done' statistics against the actually
  present files.
- srpm-cleanup: Apply the --limit= early.
- srpm-cleanup: Process TAR archives, specified on the command line
  in --with-tars mode.
- Allow to pass additional options to rsync(1) via --rsync-opts=.
- vm/srpm-cleanup-node: Allow to override the stack size from
  the environment.
- vm/Makefile: Allow to pass additional arguments to the container
  endpoints.
- vm/srpm-cleanup-manager: Install 'screen'.
- main.mk: Allow to override NPROCS.
- Added clean-stage<N>-unused targets.
- Fix: Don't mute the Hasher log if verbose but when is in dry-run
  mode.
- Automatic SRPM lists with subdirectories.
- Fix: Abort building early in the case of an error.
- Added 'relook-pkgs', 'relook-and-reclean-pkgs' and
  'relook-and-rebuild-pkgs' targets.
- Improve: Output the workdir's mount options.
- Check the workdir's mount options before building and abort if the
  workdir's mount options are bad.
- FIX: Use 'strictatime' on the build node!
- Fixed show-stage2-pkg-status and show-stage3-pkg-status targets:
  no arch!
- Improve: Check that Stage II and III went OK in reclean targets.
- Added support for regular expressions in the exceptions.list.
- Fix: Calculate Stage IV noatts from Stage I--III lists.
- Add 'show-srpm-lists' and 'update-srpm-versions' targets.
- srpm-cleanup: Fix: Make architecture selected on the command line
  be preferred over detected one.
- Make --debug imply --verbose.
- Detect debug and dry-run modes early and print the command line.
- Re-allow to dry-run srpm-cleanup in single host/package mode.
- Fixed package group (arch) concatenation: remove the trailing '+'.
- vm/Makefile: Fixed building of an updated unreleased version.

* Wed Sep 29 2021 Paul Wolneykien <manowar@altlinux.org> 0.1.2-alt1
- Allow to override builder/cleaner slots with SLOTS=.
- Run the tools with --limit if LIMIT= is specified with make.
- Add --limit option to limit the work plan by N packages.
- Fix: Importing the log with existing or empty status file.
- Fix: Initialize the temporary log file instead of the garbage one.
- Fix: Delete .included-all.list on 'statclean'.
- Fix: Delete stage skiplists on 'statclean'.
- Configure to work in temporary directory on remote by default.
- Fix: Remove rpms/ on 'stage4-clean'.
- audit_on: Deduce the arch from the prefix.
- audit_on: Delete rules (with the current key) on error.
- audit_on: Add rules for the specified arch only.
- Fixed rebuild lists for stages V/1 and V/2.
- Require gear (for srpm-cleanup).
- main.mk: Fix: Use different set of common options with build and
  with clean targets.
- Allow to select arches for stage I and IV with FOR_ARCHES.
- Fixed COMMON_OPTS override in the example Makefile.
- GNU Parallel: Substitute '{host}' in rsync transfers (patch).
- Fixed BIN_LIST usage when producing 'update-versions.sed'.
- Initialize the default NPROC profile when adding a new builder
  with 'add-builder.
- Copy NPROC profile files to remote hosts.
- Fix/improve handling of the empty SRPM list for all status targets.
- Add comments about the initial variables in the example Makefile.
- Added 'show-repo-dir' and 'set-repo-dir' targets.
- Display warnings if no SRPM lists are defined.
- Set the default repo path to /repo/sisyphus.
- Introduce automatic SRPM lists.
- Make the example configuration ready for use with the default Docker
  containers.
- Added targets to self-edit the configuration Makefile.
- Define variables for most of the path defaults.
- Fixed the update-versions.sed target hardcode.
- Require findutils, coreutils, time, rsync, apt-repo-tools.
- Fixed basefile transfer (with --selfie) option.
- Fixed duplicate rules for creating the log directories.
- Create log directories on demand.
- Fixed documentation path: docdir is already a pkgdocdir.
- Automatic build of the Docker containers from vm/ dir.
- Let the 'audit' subpackage require 'audit'.
- Added a Docker container for a cleanup node.
- Added a Docker container for the cleanup manager
- Fix/improve SRPM indicies and export.
- Fix: Return 1 if the specified CPU profile file isn't readable.
- Added -dry-run[-dun] targets for stage V generalized targets.
- Fix: Added the missing Done and NoAtt columns to the stage III
  status report.
- Update: Build arch-included packages only.
- Added 'clean-and-verify-noatt' target.
- Fix: Use double quotation in the template regexps.
- Fix: Use single quotes in find expressions.
- Fixed status filter: allow more than one digit in the try number.

* Wed May 26 2021 Paul Wolneykien <manowar@altlinux.org> 0.1.1-alt3
- Package parallel_alt --- a special version of "GNU" Parallel used
  in srpm-cleanup scripts.

* Wed May 26 2021 Paul Wolneykien <manowar@altlinux.org> 0.1.1-alt2
- Added README in Russian (Quick start).

* Fri May 14 2021 Paul Wolneykien <manowar@altlinux.org> 0.1.1-alt1
- Initial version for Sisyphus.
