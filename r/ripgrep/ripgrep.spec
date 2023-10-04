%define bname rg

Name: ripgrep
Version: 13.0.0
Release: alt3
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
# XXX: help pcre2-sys to disable JIT on LoongArch
export TARGET="%{_arch}-unknown-linux-gnu"
cargo build --offline --release --features=pcre2

%install
mkdir -p %buildroot%_bindir
mkdir -p %buildroot%_man1dir
mkdir -p %buildroot%_datadir/bash-completion/completions
mkdir -p %buildroot/%_datadir/zsh/site-functions
mkdir -p %buildroot%_datadir/fish/vendor_completions.d
install -m 0755 target/release/%bname %buildroot%_bindir
install -m 0644 target/release/build/%name-*/out/%bname.1 %buildroot%_man1dir
install -m 0644 target/release/build/%name-*/out/%bname.bash %buildroot%_datadir/bash-completion/completions
install -m 0644 complete/_%bname %buildroot/%_datadir/zsh/site-functions
install -m 0644 target/release/build/%name-*/out/%bname.fish %buildroot%_datadir/fish/vendor_completions.d

%files
%_bindir/%bname
%_man1dir/%bname.1.xz
%_datadir/bash-completion/completions/%bname.bash
%_datadir/zsh/site-functions/_%bname
%_datadir/fish/vendor_completions.d/%bname.fish
%doc COPYING LICENSE-MIT UNLICENSE

%changelog
* Wed Oct 04 2023 Alexey Sheplyakov <asheplyakov@altlinux.org> 13.0.0-alt3
- Support LoongArch architecture

* Tue Jul 20 2021 Mikhail Gordeev <obirvalger@altlinux.org> 13.0.0-alt2
- Add zsh and fish completions

* Sun Jun 13 2021 Alexander Makeenkov <amakeenk@altlinux.org> 13.0.0-alt1
- Updated to version 13.0.0

* Wed Feb 10 2021 Alexander Makeenkov <amakeenk@altlinux.org> 12.1.1-alt2
- Build with pcre2 support (closes: #39668)

* Fri Jun 12 2020 Alexander Makeenkov <amakeenk@altlinux.org> 12.1.1-alt1
- Initial build for ALT

