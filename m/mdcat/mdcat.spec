%global _unpackaged_files_terminate_build 1
%def_with check

Name: mdcat
Version: 2.15.0
Release: alt1
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

%if_with check
BuildRequires: less
%endif

# for mdpick and mdless
Requires: fzf
Requires: less

%description
Fancy cat for Markdown.

%prep
%setup -a1
%rust_prep

%build
%rust_build
ln -s mdcat target/release/mdless
ln -s mdcat target/release/mdpick
asciidoctor -b manpage -a reproducible -o mdcat.1 mdcat.1.adoc
target/release/mdcat --completions bash > mdcat.bash
target/release/mdcat --completions zsh > mdcat.zsh
target/release/mdcat --completions fish > mdcat.fish
target/release/mdless --completions bash > mdless.bash
target/release/mdless --completions zsh > mdless.zsh
target/release/mdless --completions fish > mdless.fish
target/release/mdpick --completions bash > mdpick.bash
target/release/mdpick --completions zsh > mdpick.zsh
target/release/mdpick --completions fish > mdpick.fish

%install
%rust_install
ln -s mdcat %buildroot%_bindir/mdless
ln -s mdcat %buildroot%_bindir/mdpick
install -Dm 0644 mdcat.1 %buildroot%_man1dir/mdcat.1
install -Dm 0644 mdcat.bash %buildroot%_datadir/bash-completion/completions/mdcat
install -Dm 0644 mdcat.zsh %buildroot%_datadir/zsh/site-functions/_mdcat
install -Dm 0644 mdcat.fish %buildroot%_datadir/fish/vendor_completions.d/mdcat.fish
install -Dm 0644 mdless.bash %buildroot%_datadir/bash-completion/completions/mdless
install -Dm 0644 mdless.zsh %buildroot%_datadir/zsh/site-functions/_mdless
install -Dm 0644 mdless.fish %buildroot%_datadir/fish/vendor_completions.d/mdless.fish
install -Dm 0644 mdpick.bash %buildroot%_datadir/bash-completion/completions/mdpick
install -Dm 0644 mdpick.zsh %buildroot%_datadir/zsh/site-functions/_mdpick
install -Dm 0644 mdpick.fish %buildroot%_datadir/fish/vendor_completions.d/mdpick.fish

%check
%rust_test

%files
%_bindir/mdcat
%_bindir/mdless
%_bindir/mdpick
%_man1dir/mdcat.1*
%_datadir/zsh/site-functions/_mdcat
%_datadir/zsh/site-functions/_mdless
%_datadir/zsh/site-functions/_mdpick
%_datadir/bash-completion/completions/mdcat
%_datadir/bash-completion/completions/mdless
%_datadir/bash-completion/completions/mdpick
%_datadir/fish/vendor_completions.d/mdcat.fish
%_datadir/fish/vendor_completions.d/mdless.fish
%_datadir/fish/vendor_completions.d/mdpick.fish

%changelog
* Wed Aug 05 2026 Alexander Makeenkov <amakeenk@altlinux.org> 2.15.0-alt1
- Updated to version 2.15.0.
- Packaged mdless and mdpick binaries.

* Wed Jul 29 2026 Alexander Makeenkov <amakeenk@altlinux.org> 2.14.0-alt2
- Packaged shell completions for bash, zsh, fish.
- Packaged man page.

* Mon Jul 27 2026 Alexander Makeenkov <amakeenk@altlinux.org> 2.14.0-alt1
- Updated to version 2.14.0.

* Fri Jul 24 2026 Alexander Makeenkov <amakeenk@altlinux.org> 2.13.0-alt1
- Initial build for ALT.
