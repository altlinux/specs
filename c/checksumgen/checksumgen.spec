%define _unpackaged_files_terminate_build 1

Name:     checksumgen
Version:  0.2.1
Release:  alt1

Summary:  Generates checksum file for an RPM repo slice
License:  MIT
Group:    Monitoring
Vcs:      http://git.altinux.org:packages/checksumgen.git

Packager: Paul Wolneykien <manowar@altlinux.org>
Source:   %name-%version.tar

BuildArch: noarch

BuildRequires: bats /proc apt-repo-tools rpmpeek fakeroot gostsum

Requires: apt-repo-tools rpmpeek fakeroot gostsum

%description
Generates checksum file for an RPM repo slice.

%prep
%setup

%build
%make_build

%install
%makeinstall_std sysconfdir=%_sysconfdir unitdir=%_unitdir logrotatedir=%_logrotatedir bindir=%_bindir libexecdir=%_prefix/libexec

%check
%make_build check

%files
%doc README
%_prefix/libexec/%name/*.sh
%_bindir/%name

%changelog
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
