%define _unpackaged_files_terminate_build 1

Name: alt-chksum
Version: 0.1.8
Release: alt1

Summary: ALT distro checksum downloader
License: %gpl2plus
Group: System/Base
Packager: Paul Wolneykien <manowar@altlinux.org>

Source: %name-%version.tar

BuildRequires(pre): rpm-build-licenses
BuildRequires: shellcheck
BuildArch: noarch

Requires: verify-checksums >= 1.0.19

%description
Provides 'alt-chksum' command to download and verify the ALT checksum
repository and also keeps the documentation describing the manual
verification procedure.

%prep
%setup

%build

%install
install -D -m0755 %name %buildroot/%_bindir/%name

%check
shellcheck %name

%files
%doc README
%_bindir/%name

%changelog
* Mon Jul 06 2026 Paul Wolneykien <manowar@altlinux.org> 0.1.8-alt1
- Require verify-checksums >= 1.0.19.
- Call verify-checksums with --dir and --list for each branch.
- Validate branches before calling verify-checksums.
- New and updated GPG trusted keys (Fixes: OVE-20260706-0002).
- Added ALT SP Bot public key.
- Updated manowar@ public key.
- Updated checksumbot's public key.
- Fix: Run git init with advice.defaultBranchName=false.

* Mon Nov 17 2025 Paul Wolneykien <manowar@altlinux.org> 0.1.7-alt1
- Notify the users about new security updates (Fixes: OVE-20251117-0001).
- Display EOL.txt on validate if it exists.

* Fri Nov 14 2025 Paul Wolneykien <manowar@altlinux.org> 0.1.6-alt1
- Updated expired GPG keys (Fixes: OVE-20251114-0001).
- Updated README.

* Fri Feb 21 2025 Paul Wolneykien <manowar@altlinux.org> 0.1.5-alt1
- Fix: Don't pull extra branches when update.

* Fri Nov 01 2024 Paul Wolneykien <manowar@altlinux.org> 0.1.4-alt1
- Change the default URL to https://checksum.altsp.su/alt-checksum/checksums.git.

* Mon Sep 30 2024 Paul Wolneykien <manowar@altlinux.org> 0.1.3-alt1
- Run "git gc" after a branch is deleted.
- Verify git commit signatures too.
- Fix: Fetch using plain "git pull" (without the branch name).
- Fix: Don't use --set-upstream option with "git fetch".
- Switch the default URL to
  https://gitlab.basealt.space/alt-checksum/checksums.git.
- Require verify-checksums >= 1.0.11.

* Thu Sep 05 2024 Paul Wolneykien <manowar@altlinux.org> 0.1.2-alt1
- Invoke verify-checksums with --dir <branch> argument for each
  branch.
- Fix: Remove worktree with --force on 'del'.
- Fix: Check git status when validate.
- Make 'validate' report error when the repo is uninitialized or
  there is no branches.

* Mon Sep 02 2024 Paul Wolneykien <manowar@altlinux.org> 0.1.1-alt1
- Version: 0.1.1
- Updated README.
- Automatically validate new branches and updates.
- Added 'log' command.
- Track remote branches on 'add', delete local branches on 'del'.
- Added per-command help.
- Show public key metadata with 'keys \?'.
- Add public key for Checksum Test <checksumtest@localhost>.
- Adapted for multiple git worktrees.
- Print validation error about untagged HEAD.
- Use gpg.conf borrowed from alt-gpgkeys.

* Fri Aug 16 2024 Paul Wolneykien <manowar@altlinux.org> 0.1.0-alt1
- Initial release.
