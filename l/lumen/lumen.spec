%global _unpackaged_files_terminate_build 1

Name: lumen
Version: 2.30.0
Release: alt2
Summary: A fast terminal diff viewer and code review TUI
License: MIT
Group: Development/Other
URL: https://crates.io/crates/lumen
VCS: https://github.com/jnsahaj/lumen

Source: %name-%version.tar
Source1: vendor.tar

ExcludeArch: %ix86

BuildRequires(pre): rpm-macros-rust
BuildRequires: rpm-build-rust
BuildRequires: libssl-devel

Requires: github-cli

%description
Beautiful git diff viewer, generate commits with AI,
get summary of changes, all from the CLI.

%prep
%setup -a 1
%rust_prep

%build
export OPENSSL_NO_VENDOR=1
%rust_build

%install
%rust_install

%check
export OPENSSL_NO_VENDOR=1
%rust_test -- \
           --skip vcs::git::tests::test_get_merge_base_returns_ancestor \
           --skip vcs::git::tests::test_working_copy_parent_ref_returns_head

%files
%_bindir/%name

%changelog
* Wed Jul 01 2026 Alexander Makeenkov <amakeenk@altlinux.org> 2.30.0-alt2
- Added missing runtime require to github-cli.

* Sun Jun 21 2026 Alexander Makeenkov <amakeenk@altlinux.org> 2.30.0-alt1
- Initial build for ALT.
