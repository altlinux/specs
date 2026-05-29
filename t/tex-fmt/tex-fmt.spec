%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1

%define bash_completionsdir %_datadir/bash-completion/completions
%define fish_completionsdir %_datadir/fish/vendor_completions.d
%define zsh_completionsdir %_datadir/zsh/site-functions

Name: tex-fmt
Version: 0.5.7
Release: alt1

Summary: An extremely fast LaTeX formatter written in Rust
License: MIT
Group: Development/Tools
Url: https://wgunderwood.github.io/tex-fmt/
Vcs: https://github.com/WGUNDERWOOD/tex-fmt

Source0: %name-%version.tar
Source1: %name-%version-vendor.tar
Source2: config.toml
Patch0: %name-%version-alt.patch

BuildRequires: rust-cargo

%description
Indentation, line wrapping and other formatting for LaTeX source code.

%prep
%setup -a1
%autopatch -p1
install -vpD %SOURCE2 .cargo/config.toml

%build
cargo build %_smp_mflags --release --offline

%install
install -vpD -m0755 target/release/tex-fmt -t %buildroot%_bindir

mkdir -p %buildroot%_man1dir
mkdir -p %buildroot%bash_completionsdir
mkdir -p %buildroot%fish_completionsdir
mkdir -p %buildroot%zsh_completionsdir

%buildroot%_bindir/tex-fmt --man \
    > %buildroot%_man1dir/tex-fmt.1
%buildroot%_bindir/tex-fmt --completion bash \
    > %buildroot%bash_completionsdir/tex-fmt
%buildroot%_bindir/tex-fmt --completion fish \
    > %buildroot%fish_completionsdir/tex-fmt.fish
%buildroot%_bindir/tex-fmt --completion bash \
    > %buildroot%zsh_completionsdir/_tex-fmt

%files
%doc LICENSE NEWS.md README.md
%_bindir/tex-fmt
%_man1dir/tex-fmt.1*
%bash_completionsdir/tex-fmt
%fish_completionsdir/tex-fmt.fish
%zsh_completionsdir/_tex-fmt

%changelog
* Fri May 29 2026 Anton Zhukharev <ancieg@altlinux.org> 0.5.7-alt1
- Packaged for ALT Sisyphus.
