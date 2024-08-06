%global _unpackaged_files_terminate_build 1

%def_with check

Name: tlrc
Version: 1.9.3
Release: alt1

Summary: A tldr client written in Rust
License: MIT
Group: Documentation
Url: https://tldr.sh/tlrc
Vcs: https://github.com/tldr-pages/tlrc

Source: %name-%version.tar
Source1: vendor.tar

BuildRequires(pre): rpm-macros-rust
BuildRequires: rpm-build-rust

Conflicts: python3-module-tldr tealdeer

%description
%summary.

%prep
%setup -a 1
mkdir -p .cargo
cat >> .cargo/config.toml <<EOF
[source.crates-io]
replace-with = "vendored-sources"

[source.vendored-sources]
directory = "vendor"
EOF

%build
%rust_build

%install
%rust_install tldr

install -Dpm 644 completions/tldr.bash %buildroot%_datadir/bash-completion/completions/tldr
install -Dpm 644 completions/_tldr %buildroot%_datadir/zsh/site-functions/_tldr
install -Dpm 644 completions/tldr.fish %buildroot%_datadir/fish/vendor_completions.d/tldr.fish

mkdir -p %buildroot%_man1dir/
install -Dpm 644 tldr.1 %buildroot%_man1dir/

%check
%rust_test

%files
%doc *.md
%_bindir/tldr
%_datadir/bash-completion/completions/tldr
%_datadir/zsh/site-functions/_tldr
%_datadir/fish/vendor_completions.d/tldr.fish
%_man1dir/tldr.*

%changelog
* Tue Aug 06 2024 Alexander Stepchenko <geochip@altlinux.org> 1.9.3-alt1
- 1.9.2 -> 1.9.3

* Fri Jul 12 2024 Alexander Stepchenko <geochip@altlinux.org> 1.9.2-alt1
- Initial build for ALT.
