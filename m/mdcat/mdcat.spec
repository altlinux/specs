%global _unpackaged_files_terminate_build 1
%def_with check

Name: mdcat
Version: 2.14.0
Release: alt2
Summary: cat for markdown
License: MPL-2.0
Group: Text tools
URL: https://crates.io/crates/mdcat
VCS: https://github.com/BIRSAx2/mdcat

Source: %name-%version.tar
Source1: vendor.tar

BuildRequires(pre): rpm-macros-rust
BuildRequires: rpm-build-rust
BuildRequires: pkgconfig(openssl)
BuildRequires: asciidoctor

%description
Fancy cat for Markdown.

%prep
%setup -a1
%rust_prep

%build
%rust_build
asciidoctor -b manpage -a reproducible -o %name.1 %name.1.adoc
target/release/%name --completions bash > %name.bash
target/release/%name --completions zsh > %name.zsh
target/release/%name --completions fish > %name.fish

%install
%rust_install
install -Dm 0644 %name.1 %buildroot%_man1dir/%name.1
install -Dm 0644 %name.bash %buildroot%_datadir/bash-completion/completions/%name
install -Dm 0644 %name.zsh %buildroot%_datadir/zsh/site-functions/_%name
install -Dm 0644 %name.fish %buildroot%_datadir/fish/vendor_completions.d/%name.fish

%check
%rust_test

%files
%_bindir/%name
%_man1dir/%name.1*
%_datadir/zsh/site-functions/_%name
%_datadir/bash-completion/completions/%name
%_datadir/fish/vendor_completions.d/%name.fish

%changelog
* Wed Jul 29 2026 Alexander Makeenkov <amakeenk@altlinux.org> 2.14.0-alt2
- Packaged shell completions for bash, zsh, fish.
- Packaged man page.

* Mon Jul 27 2026 Alexander Makeenkov <amakeenk@altlinux.org> 2.14.0-alt1
- Updated to version 2.14.0.

* Fri Jul 24 2026 Alexander Makeenkov <amakeenk@altlinux.org> 2.13.0-alt1
- Initial build for ALT.
