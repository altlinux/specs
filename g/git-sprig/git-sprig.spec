%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1

%define bash_completionsdir %_datadir/bash-completion/completions
%define fish_completionsdir %_datadir/fish/vendor_completions.d
%define zsh_completionsdir %_datadir/zsh/site-functions

Name: git-sprig
Version: 0.1.1
Release: alt1

Summary: Materialize git submodules as plain files, recursively, without their history
License: GPL-3.0-or-later
Group: Development/Tools
Url: https://crates.io/crates/git-sprig
Vcs: https://github.com/ancieg/git-sprig

Source0: %name-%version.tar
Source1: %name-%version-vendor.tar
Source2: config.toml
Patch0: %name-%version-alt.patch

BuildRequires: rust-cargo

%description
git-sprig fills in a project's git submodules with plain files. Its git-sprig
command takes every submodule at exactly the commit your project points to,
writes out its files, and does the same for submodules inside submodules.
No history is downloaded and no .git folders are left behind - you get just the
source code.

That comes in handy whenever you need a project's complete sources but not its
repositories: release tarballs, distribution packages, container images,
CI builds, or copying a dependency into another tree.

%prep
%setup -a1
%autopatch -p1
install -vpD %SOURCE2 .cargo/config.toml

%build
export CARGO_PROFILE_RELEASE_CODEGEN_UNITS=1
export CARGO_PROFILE_RELEASE_DEBUG=1
export CARGO_PROFILE_RELEASE_DEBUG_ASSERTIONS=false
export CARGO_PROFILE_RELEASE_INCREMENTAL=false
export CARGO_PROFILE_RELEASE_LTO=fat
export CARGO_PROFILE_RELEASE_OPT_LEVEL=3
export CARGO_PROFILE_RELEASE_OVERFLOW_CHECKS=false
export CARGO_PROFILE_RELEASE_STRIP=none
cargo build %_smp_mflags --release --offline

%install
install -vpD -m0755 target/release/git-sprig -t %buildroot%_bindir

mkdir -p %buildroot%_man1dir
mkdir -p %buildroot%bash_completionsdir
mkdir -p %buildroot%fish_completionsdir
mkdir -p %buildroot%zsh_completionsdir

%buildroot%_bindir/git-sprig --generate-man \
    > %buildroot%_man1dir/git-sprig.1
%buildroot%_bindir/git-sprig --generate-completions bash \
    > %buildroot%bash_completionsdir/git-sprig
%buildroot%_bindir/git-sprig --generate-completions fish \
    > %buildroot%fish_completionsdir/git-sprig.fish
%buildroot%_bindir/git-sprig --generate-completions zsh \
    > %buildroot%zsh_completionsdir/_git-sprig

%files
%_bindir/git-sprig
%_man1dir/git-sprig.1*
%bash_completionsdir/git-sprig
%fish_completionsdir/git-sprig.fish
%zsh_completionsdir/_git-sprig

%changelog
* Wed Sep 16 2026 Anton Zhukharev <ancieg@altlinux.org> 0.1.1-alt1
- Packaged for ALT Sisyphus.
