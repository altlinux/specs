%define bname rg

Name: ripgrep
Version: 12.1.1
Release: alt2
Summary: Recursively searches directories for a regex pattern
License: MIT and Unlicense
Group: File tools
Url: https://github.com/BurntSushi/ripgrep
Source: %name-%version.tar
Packager: Alexander Makeenkov <amakeenk@altlinux.org>

BuildRequires: asciidoctor
BuildRequires: rust-cargo
BuildRequires: /proc

%description
ripgrep is a line-oriented search tool that recursively searches
your current directory for a regex pattern.

%prep
%setup
mkdir -p .cargo
cat >> .cargo/config <<EOF
[source.crates-io]
replace-with = "vendored-sources"

[source.vendored-sources]
directory = "vendor"
EOF

%build
cargo build --offline --release --features=pcre2

%install
mkdir -p %buildroot%_bindir
mkdir -p %buildroot%_man1dir
mkdir -p %buildroot%_datadir/bash-completion/completions
install -m 0755 target/release/%bname %buildroot%_bindir
install -m 0644 target/release/build/%name-*/out/%bname.1 %buildroot%_man1dir
install -m 0644 target/release/build/%name-*/out/%bname.bash %buildroot%_datadir/bash-completion/completions

%files
%_bindir/%bname
%_man1dir/%bname.1.xz
%_datadir/bash-completion/completions/%bname.bash
%doc COPYING LICENSE-MIT UNLICENSE

%changelog
* Wed Feb 10 2021 Alexander Makeenkov <amakeenk@altlinux.org> 12.1.1-alt2
- Build with pcre2 support (closes: #39668)

* Fri Jun 12 2020 Alexander Makeenkov <amakeenk@altlinux.org> 12.1.1-alt1
- Initial build for ALT

