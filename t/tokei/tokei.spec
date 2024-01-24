%define _unpackaged_files_terminate_build 1

Name: tokei
Version: 13.0.0
Release: alt1

Summary: Program that allows you to count your code, quickly
License: MIT and Apache-2.0
Group: File tools
Vcs: https://github.com/XAMPPRocky/tokei
Packager: Michael Chernigin <chernigin@altlinux.ru>

Source0: %name-%version.tar
BuildRequires: rust-cargo
BuildRequires: /proc

%description
Tokei is a program that displays statistics about your code. Tokei will show
the number of files, total lines within those files and code, comments, and
blanks grouped by language.

%prep
%setup -q
mkdir -p .cargo
cat >> .cargo/config <<EOF
[source.crates-io]
replace-with = "vendored-sources"

[source.vendored-sources]
directory = "vendor"
EOF

%build
cargo build --offline --release

%install
mkdir -p %buildroot%_bindir
install -Dm0755 target/release/%name %buildroot%_bindir/

%check
cargo test

%files
%doc LICENCE-APACHE
%doc LICENCE-MIT
%doc README.md
%_bindir/%name

%changelog
* Tue Jun 13 2023 Michael Chernigin <chernigin@altlinux.org> 13.0.0-alt1
- Update to 8a48c475 from upstream, branch master
- Initial build for ALT Linux

