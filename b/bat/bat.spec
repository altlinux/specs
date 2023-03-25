Name: bat
Version: 0.23.0
Release: alt1
Summary: A cat(1) clone with syntax highlighting and Git integration
License: MIT or Apache-2.0
Group: File tools
Url: https://github.com/sharkdp/bat
Source: %name-%version.tar

BuildRequires: rust-cargo
Conflicts: bacula9-bat
Conflicts: bacula11-bat

%description
A cat(1) clone which supports syntax highlighting for a large number of
programming and markup languages. It has git integration and automatic paging.

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
cargo build --offline --release

%install
mkdir -p %buildroot%_bindir
mkdir -p %buildroot%_man1dir
install -m 0755 target/release/%name %buildroot%_bindir
install -m 0644 target/release/build/%name-*/out/assets/manual/%name.1 %buildroot%_man1dir
install -Dm 0644 target/release/build/%name-*/out/assets/completions/bat.bash %buildroot%_datadir/bash-completion/completions/bat
install -Dm 0644 target/release/build/%name-*/out/assets/completions/bat.zsh %buildroot%_datadir/zsh/site-functions/_bat
install -Dm 0644 target/release/build/%name-*/out/assets/completions/bat.fish %buildroot%_datadir/fish/vendor_completions.d/bat.fish

%check
# Test no_args_doesnt_break failed in hasher with error "Couldn't open pty"
cargo test -- --skip no_args_doesnt_break

%files
%_bindir/%name
%_man1dir/%name.1.xz
%_datadir/bash-completion/completions/bat
%_datadir/zsh/site-functions/_bat
%_datadir/fish/vendor_completions.d/bat.fish
%doc README.md LICENSE-MIT LICENSE-APACHE

%changelog
* Sat Mar 25 2023 Alexander Makeenkov <amakeenk@altlinux.org> 0.23.0-alt1
- Updated to version 0.23.0
- Enabled tests

* Fri Oct 07 2022 Alexander Makeenkov <amakeenk@altlinux.org> 0.22.1-alt1
- Updated to version 0.22.1

* Sat May 14 2022 Alexander Makeenkov <amakeenk@altlinux.org> 0.21.0-alt1
- Updated to version 0.21.0

* Sun Jan 23 2022 Alexander Makeenkov <amakeenk@altlinux.org> 0.19.0-alt1
- Updated to version 0.19.0

* Tue Sep 21 2021 Alexander Makeenkov <amakeenk@altlinux.org> 0.18.3-alt1
- Updated to version 0.18.3
- Added conflict with bacula11-bat package

* Thu Aug 12 2021 Egor Ignatov <egori@altlinux.org> 0.18.2-alt1
- Update to version 0.18.2
- add bash, zsh and fish completions

* Sun Jun 06 2021 Alexander Makeenkov <amakeenk@altlinux.org> 0.18.1-alt1
- Updated to version 0.18.1

* Wed Apr 21 2021 Egor Ignatov <egori@altlinux.org> 0.18.0-alt1
- Update to version 0.18.0

* Sat Jan 09 2021 Alexander Makeenkov <amakeenk@altlinux.org> 0.17.1-alt1
- Updated to version 0.17.1

* Wed Jun 24 2020 Alexander Makeenkov <amakeenk@altlinux.org> 0.15.4-alt2
- Added conflict with bacula9-bat package

* Sat Jun 13 2020 Alexander Makeenkov <amakeenk@altlinux.org> 0.15.4-alt1
- Initial build for ALT

