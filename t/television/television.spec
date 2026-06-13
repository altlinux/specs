%global _unpackaged_files_terminate_build 1
%global bin_name tv
%global bin_path ./target/release/%bin_name

%def_with check

Name: television
Version: 0.15.8
Release: alt1
Summary: A fast, portable and hackable fuzzy finder for the terminal
License: MIT
Group: File tools
Url: https://alexpasmantier.github.io/television
VCS: https://github.com/alexpasmantier/television

Source: %name-%version.tar
Source1: vendor.tar

BuildRequires(pre): rpm-macros-rust
BuildRequires: rpm-build-rust

Requires: bat
Requires: fd
Requires: ripgrep

%if_with check
BuildRequires: /dev/pts
%endif

%description
Television is a fuzzy finder that lets you search through any kind
of data in real-time. It comes with built-in channels for common
tasks like finding files, searching git repositories, browsing
environment variables, and more. You can also create your own
custom channels to search through any data source you need.

%prep
%setup -a 1
%rust_prep
# disable UI integration tests requiring ghostty
sed -i '/phantom-test/d' Cargo.toml
cat >> .cargo/config.toml <<EOF
[source."git+https://github.com/alexpasmantier/nucleo.git?branch=television"]
git = "https://github.com/alexpasmantier/nucleo.git"
branch = "television"
replace-with = "vendored-sources"
EOF

%build
%rust_build
%bin_path completions bash > %bin_name.bash
%bin_path completions fish > %bin_name.fish
%bin_path completions zsh > _%bin_name

%install
%rust_install %bin_name
install -Dm 0644 man/%bin_name.1 %buildroot%_man1dir/%bin_name.1
install -Dm 0644 %bin_name.bash %buildroot%_datadir/bash-completion/completions/%bin_name.bash
install -Dm 0644 %bin_name.fish %buildroot%_datadir/fish/vendor_completions.d/%bin_name.fish
install -Dm 0644 _%bin_name %buildroot/%_datadir/zsh/site-functions/_%bin_name

%check
export TV_BIN_PATH=%bin_path
%rust_test --lib --bin tv --test app

%files
%_bindir/%bin_name
%_man1dir/%bin_name.1.*
%_datadir/bash-completion/completions/%bin_name.bash
%_datadir/fish/vendor_completions.d/%bin_name.fish
%_datadir/zsh/site-functions/_%bin_name
%doc LICENSE

%changelog
* Sat Jun 13 2026 Alexander Makeenkov <amakeenk@altlinux.org> 0.15.8-alt1
- Updated to version 0.15.8.

* Sun Apr 12 2026 Alexander Makeenkov <amakeenk@altlinux.org> 0.15.5-alt1
- Updated to version 0.15.5.

* Fri Mar 27 2026 Alexander Makeenkov <amakeenk@altlinux.org> 0.15.4-alt2
- Added missing runtime requires on bat, fd and ripgrep.

* Sun Mar 22 2026 Alexander Makeenkov <amakeenk@altlinux.org> 0.15.4-alt1
- Updated to version 0.15.4.
- Packaged shell completions for bash, zsh, fish.

* Sat Mar 21 2026 Alexander Makeenkov <amakeenk@altlinux.org> 0.15.3-alt1
- Initial build for ALT.
