%define _unpackaged_files_terminate_build 1

Name: gwm
Version: 1.5.0
Release: alt1
Summary: Worktree manager for the terminal.
License: MIT
Group: Development/Other
Url: https://github.com/kbrdn1/gwm-cli

Source0: %name-%version.tar
Source1: vendor.tar

BuildRequires(pre): rpm-macros-rust
BuildRequires: rpm-build-rust
BuildRequires: rust-cargo
BuildRequires: git

%description
Git worktree manager for the terminal: CLI + TUI in Rust.
Creates the worktree, runs your project setup, links the GitHub issue.
Single binary, no git CLI needed.

%prep
%setup -a 1
%autopatch -p1
rm tests/tui_state_pty_overlay_tests.rs
rm tests/worktree_integration.rs

%build
mkdir -p .cargo
cat > .cargo/config.toml <<EOF
[source.crates-io]
replace-with = "vendored-sources"

[source.vendored-sources]
directory = "vendor"
EOF

%rust_build

%install
%rust_install

%check
%rust_test 

%files
%doc *.md
%_bindir/%name

%changelog
* Fri Jul 31 2026 Pavel Shilov <zerospirit@altlinux.org> 1.5.0-alt1
- Initial build for Sisyphus.