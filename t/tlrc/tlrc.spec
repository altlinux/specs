%global _unpackaged_files_terminate_build 1

%def_with check

Name: tlrc
Version: 1.13.0
Release: alt1

Summary: A tldr client written in Rust
License: MIT
Group: Documentation
Url: https://tldr.sh/tlrc
Vcs: https://github.com/tldr-pages/tlrc

Source: %name-%version.tar
# prepare using
# $ cargo-vendor-alt --exclude-crate-path '*#tests'
Source1: vendor.tar

BuildRequires(pre): rpm-macros-rust
BuildRequires: rpm-build-rust

Conflicts: python3-module-tldr tealdeer

%description
%summary.

%prep
%setup -a 1
%rust_prep

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
* Fri Apr 10 2026 Alexander Stepchenko <geochip@altlinux.org> 1.13.0-alt1
- 1.12.0 -> 1.13.0.

* Mon Oct 27 2025 Alexander Stepchenko <geochip@altlinux.org> 1.12.0-alt1
- 1.11.1 -> 1.12.0.

* Thu Aug 14 2025 Alexander Stepchenko <geochip@altlinux.org> 1.11.1-alt1
- Update to 1.11.1.

* Tue Aug 06 2024 Alexander Stepchenko <geochip@altlinux.org> 1.9.3-alt1
- 1.9.2 -> 1.9.3

* Fri Jul 12 2024 Alexander Stepchenko <geochip@altlinux.org> 1.9.2-alt1
- Initial build for ALT.
