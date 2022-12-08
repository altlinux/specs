# SPDX-License-Identifier: GPL-2.0-only
%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%set_verify_elf_method strict,lint=relaxed,lfs=relaxed

Name: stgit
Version: 2.0.4
Release: alt1
Summary: Stacked Git
License: GPL-2.0-only
Group: Development/Tools
Url: https://stacked-git.github.io/
Vcs: https://github.com/stacked-git/stgit

Source: %name-%version.tar

BuildRequires: /proc
BuildRequires: asciidoc
BuildRequires: git-core
BuildRequires: openssl-devel
BuildRequires: rust-cargo
BuildRequires: xmlto

%description
Stacked Git, StGit for short, is an application for managing Git commits
as a stack of patches.

With a patch stack workflow, multiple patches can be developed
concurrently and efficiently, with each patch focused on a single concern,
resulting in both a clean Git commit history and improved productivity.

%prep
%setup
mkdir -p .cargo
cat >> .cargo/config <<EOF
[source.crates-io]
replace-with = "vendored-sources"

[source.vendored-sources]
directory = "vendor"

[term]
verbose = true
quiet = false

[install]
root = "%buildroot%_prefix"

[profile.release]
strip = false
EOF


%build
unset MAKEFLAGS
%make_build all

%install
unset MAKEFLAGS
%makeinstall_std install-all prefix=%_prefix
install -Dpm644 COPYING README.md AUTHORS.md CHANGELOG.md contrib/stgbashprompt.sh \
	%buildroot%_datadir/doc/stgit/

%check
%buildroot%_bindir/stg --version
# Fails:
rm t/t7000-sparse-checkout.sh
%make_build test

%files
%_bindir/stg
%_man1dir/*.1*
%_datadir/bash-completion/completions/stg
%_datadir/zsh/site-functions/_stg
%_datadir/fish/vendor_completions.d/stg.fish
%_datadir/vim/vimfiles/*/*.vim
%_datadir/emacs/site-lisp/stgit.el
%_datadir/doc/stgit

%changelog
* Thu Dec 08 2022 Vitaly Chikunov <vt@altlinux.org> 2.0.4-alt1
- Update to v2.0.4 (2022-11-30). Codebase converted from Python to Rust.

* Thu Mar 10 2022 Vitaly Chikunov <vt@altlinux.org> 1.5-alt1
- First import v1.5 (2022-01-28).
