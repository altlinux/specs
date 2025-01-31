%define _unpackaged_files_terminate_build 1

Name: alt-chksum
Version: 0.1.4
Release: alt1

Summary: ALT distro checksum downloader
License: %gpl2plus
Group: System/Base
Packager: Paul Wolneykien <manowar@altlinux.org>

Source: %name-%version.tar

BuildRequires(pre): rpm-build-licenses
BuildArch: noarch

Requires: verify-checksums >= 1.0.11

%description
Provides 'alt-chksum' command to download and verify the ALT checksum
repository and also keeps the documentation describing the manual
verification procedure.

%prep
%setup

%build

%install
install -D -m0755 %name %buildroot/%_bindir/%name

%files
%doc README
%_bindir/%name

%changelog
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
