%define _unpackaged_files_terminate_build 1

Name: eza
Version: 0.18.23
Release: alt1

Summary: A modern, maintained replacement for ls
License: MIT
Group: System/Base
Url: https://eza.rocks/

VCS: https://github.com/eza-community/eza.git
Source: %name-%version.tar
Source1: %name-%version-vendor.tar
Patch0: %name-%version-alt.patch

BuildRequires: /proc
BuildRequires: rust
BuildRequires: rust-cargo
BuildRequires: libgit2-devel
BuildRequires: pandoc

Provides: exa = %EVR
Obsoletes: exa

%description
eza is a modern, maintained replacement for the venerable file-listing
command-line  program ls  that  ships with  Unix  and Linux  operating
systems, giving it more features  and better defaults. It uses colours
to  distinguish file  types  and metadata.  It  knows about  symlinks,
extended  attributes, and  Git. And  it's  small, fast,  and just  one
single binary.

%prep
%setup -a1
%patch0 -p1

sed -i -e '/^strip = true$/ s/true/false/' Cargo.toml

mkdir -p .cargo
cat > .cargo/config <<EOF
[source.crates-io]
replace-with = "vendored-sources"

[source.vendored-sources]
directory = "vendor"
EOF

%build
cargo build --release %{?_smp_mflags} --all-targets --offline

mkdir -p target/man
for manpage in eza.1 eza_colors.5 eza_colors-explanation.5; do
    pandoc --standalone -f markdown -t man "man/${manpage}.md" > "target/man/${manpage}"
done

%install
install -D -m755 target/release/eza %buildroot%_bindir/eza
ln -s eza %buildroot%_bindir/exa

# install completions
install -Dm 0644 completions/bash/eza %buildroot%_datadir/bash-completion/completions/eza
install -Dm 0644 completions/zsh/_eza %buildroot%_datadir/zsh/site-functions/_eza
install -Dm 0644 completions/fish/eza.fish %buildroot%_datadir/fish/vendor_completions.d/eza.fish

# install man pages
install -Dm644 target/man/*.1 -t %buildroot%_man1dir
install -Dm644 target/man/*.5 -t %buildroot%_man5dir

%check
cargo test --release --offline

%files
%doc LICENCE README.md
%_bindir/*
%_man1dir/*
%_man5dir/*
%_datadir/bash-completion/completions/eza
%_datadir/zsh/site-functions/_eza
%_datadir/fish/vendor_completions.d/eza.fish

%changelog
* Tue Jul 30 2024 Egor Ignatov <egori@altlinux.org> 0.18.23-alt1
- 0.18.23

* Fri Apr 05 2024 Egor Ignatov <egori@altlinux.org> 0.18.9-alt1
- 0.18.9

* Tue Mar 26 2024 Egor Ignatov <egori@altlinux.org> 0.18.8-alt1
- 0.18.8

* Mon Mar 18 2024 Egor Ignatov <egori@altlinux.org> 0.18.7-alt1
- 0.18.7

* Thu Mar 07 2024 Egor Ignatov <egori@altlinux.org> 0.18.6-alt1
- 0.18.6 

* Sun Mar 03 2024 Egor Ignatov <egori@altlinux.org> 0.18.5-alt1
- Replace exa with maintained fork eza
- 0.18.5

* Mon May 30 2022 Egor Ignatov <egori@altlinux.org> 0.10.1-alt2
- Fix FTBFS on rust 1.61.0

* Wed Apr 14 2021 Egor Ignatov <egori@altlinux.org> 0.10.1-alt1
- First build for ALT
