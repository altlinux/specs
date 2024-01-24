%define _unpackaged_files_terminate_build 1

Name: difftastic
Version: 0.47.0
Release: alt1

Summary: A structural diff that understands syntax
License: MIT
Group: File tools
Vcs: https://github.com/Wilfred/difftastic
Packager: Michael Chernigin <chernigin@altlinux.ru>

Source0: %name-%version.tar
BuildRequires: rust-cargo
BuildRequires: /proc
BuildRequires: gcc-c++

%description
Difftastic is a structural diff tool that compares files based on their syntax.

%global bin_name difft

%prep
%setup -q
mkdir -p .cargo
cat >> .cargo/config <<EOF
[source.crates-io]
replace-with = "vendored-sources"

[source."https://github.com/Wilfred/tree_magic"]
git = "https://github.com/Wilfred/tree_magic"
branch = "fix-panic-for-empty-strings"
replace-with = "vendored-sources"

[source.vendored-sources]
directory = "vendor"
EOF

%build
cargo build --offline --release

%install
mkdir -p %buildroot%_bindir
install -Dm0755 target/release/%bin_name %buildroot%_bindir/

%check
cargo test

%files
%doc LICENSE
%doc README.md
%_bindir/%bin_name

%changelog
* Tue Jul 17 2023 Michael Chernigin <chernigin@altlinux.org> 0.47.0-alt1
- Update to b6895d42 from upstream, branch master
- Initial build for ALT Linux

