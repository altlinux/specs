# SPDX-License-Identifier: GPL-2.0-only
%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%set_verify_elf_method strict,lint=relaxed

Name: act-github-actions
Version: 0.2.70
Release: alt1
Summary: Run your GitHub Actions locally in Docker
License: MIT
Group: Development/Tools
Url: https://nektosact.com
Vcs: https://github.com/nektos/act
Conflicts: act
Provides: act

Source: %name-%version.tar
BuildRequires: golang

%description
Run your GitHub Actions locally! Why would you want to do this? Two
reasons:

- Fast Feedback - Rather than having to commit/push every time you want
  to test out the changes you are making to your .github/workflows/ files
  (or for any changes to embedded GitHub actions), you can use act to
  run the actions locally. The environment variables and filesystem are
  all configured to match what GitHub provides.

- Local Task Runner - I love make. However, I also hate repeating
  myself. With act, you can use the GitHub Actions defined in your
  .github/workflows/ to replace your Makefile!

%prep
%setup

%build
go build -v -buildmode=pie -ldflags "-X main.version=%version"

%install
install -Dp act -t %buildroot%_bindir

%check
%buildroot%_bindir/act --version | grep -Fx 'act version %version'

%files
%doc CONTRIBUTING.md IMAGES.md LICENSE README.md
%_bindir/act

%changelog
* Wed Dec 04 2024 Vitaly Chikunov <vt@altlinux.org> 0.2.70-alt1
- First import v0.2.70 (2024-12-01).
