Name: fd
Version: 8.3.1
Release: alt1
Summary: A simple, fast and user-friendly alternative to 'find'
License: MIT and Apache-2.0
Group: File tools
Url: https://github.com/sharkdp/fd
Source: %name-%version.tar
Packager: Alexander Makeenkov <amakeenk@altlinux.org>

BuildRequires: rust-cargo
BuildRequires: /proc

%description
fd is an alternative to GNU find. It features:
- Colorized terminal output (similar to ls).
- The search is case-insensitive by default. It switches to
  case-sensitive if the pattern contains an uppercase character.
- By default, ignores patterns from .gitignore, and ignores hidden
  directories and files.
- Supports regular expressions and Unicode awareness.
- A parallel execution similar to GNU Parallel is available.

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
mkdir -p %buildroot%_datadir/bash-completion/completions
install -m 0755 target/release/%name %buildroot%_bindir
install -m 0644 doc/%name.1 %buildroot%_man1dir
install -m 0644 target/release/build/%name-find-*/out/%name.bash %buildroot%_datadir/bash-completion/completions

%files
%_bindir/%name
%_man1dir/%name.1.xz
%_datadir/bash-completion/completions/%name.bash
%doc LICENSE-MIT LICENSE-APACHE

%changelog
* Sun Jan 23 2022 Alexander Makeenkov <amakeenk@altlinux.org> 8.3.1-alt1
- Updated to version 8.3.1

* Sat Jan 09 2021 Alexander Makeenkov <amakeenk@altlinux.org> 8.2.0-alt1
- Updated to version 8.2.0

* Sat Jun 13 2020 Alexander Makeenkov <amakeenk@altlinux.org> 8.1.1-alt1
- Initial build for ALT

