Name: fd
Version: 9.0.0
Release: alt1
Summary: A simple, fast and user-friendly alternative to 'find'
License: MIT and Apache-2.0
Group: File tools
Url: https://github.com/sharkdp/fd
Source: %name-%version.tar
Source1: vendor.tar

BuildRequires(pre): rpm-build-rust
BuildRequires: rust-cargo

%ifarch i586 armh
%filter_from_requires /libc.so.6(GLIBC_PRIVATE)/d
%endif

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
%setup -a 1
mkdir -p .cargo
cat >> .cargo/config <<EOF
[source.crates-io]
replace-with = "vendored-sources"

[source.vendored-sources]
directory = "vendor"
EOF

%build
%rust_build
target/release/%name --gen-completions bash > %name.bash
target/release/%name --gen-completions fish > %name.fish

%install
%rust_install
install -Dm 0644 doc/%name.1 %buildroot%_man1dir/%name.1
install -Dm 0644 %name.bash %buildroot%_datadir/bash-completion/completions/%name
install -Dm 0644 %name.fish %buildroot%_datadir/fish/vendor_completions.d/%name.fish
install -Dm 0644 contrib/completion/_%name %buildroot%_datadir/zsh/site-functions/_%name

%check
%rust_test

%files
%_bindir/%name
%_man1dir/%name.1.xz
%_datadir/zsh/site-functions/_%name
%_datadir/bash-completion/completions/%name
%_datadir/fish/vendor_completions.d/%name.fish

%changelog
* Tue Dec 19 2023 Alexander Makeenkov <amakeenk@altlinux.org> 9.0.0-alt1
- Updated to version 9.0.0.

* Sun Oct 22 2023 Alexander Makeenkov <amakeenk@altlinux.org> 8.7.1-alt1
- Updated to version 8.7.1.

* Fri Feb 24 2023 Alexander Makeenkov <amakeenk@altlinux.org> 8.7.0-alt1
- Updated to version 8.7.0

* Sat Dec 17 2022 Alexander Makeenkov <amakeenk@altlinux.org> 8.6.0-alt1
- Updated to version 8.6.0

* Mon May 30 2022 Alexander Makeenkov <amakeenk@altlinux.org> 8.4.0-alt1
- Updated to version 8.4.0

* Sat May 14 2022 Alexander Makeenkov <amakeenk@altlinux.org> 8.3.2-alt1
- Updated to version 8.3.2

* Sun Jan 23 2022 Alexander Makeenkov <amakeenk@altlinux.org> 8.3.1-alt1
- Updated to version 8.3.1

* Sat Jan 09 2021 Alexander Makeenkov <amakeenk@altlinux.org> 8.2.0-alt1
- Updated to version 8.2.0

* Sat Jun 13 2020 Alexander Makeenkov <amakeenk@altlinux.org> 8.1.1-alt1
- Initial build for ALT

