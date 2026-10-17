%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1

# doesn't work on girar
%def_without check

%define bash_completionsdir %_datadir/bash-completion/completions
%define fish_completionsdir %_datadir/fish/vendor_completions.d
%define zsh_completionsdir %_datadir/zsh/site-functions

Name: kache
Version: 1.2.2
Release: alt1

Summary: Compiler cache for Rust, C/C++ and CUDA, with S3, GCS, shared-filesystem and OCI remotes
License: Apache-2.0
Group: Development/Tools
Url: https://ninja.kunobi.com/kache
Vcs: https://github.com/kunobi-ninja/kache

ExcludeArch: %ix86

Source0: %name-%version.tar
Source1: %name-%version-vendor.tar
Source2: cargo-config.toml
Patch0: %name-%version-alt.patch

BuildRequires: rust-cargo
BuildRequires: mold
BuildRequires: pkgconfig(libzstd)
BuildRequires: pkgconfig(sqlite3)

%description
Build once. Reuse the work.

Kache is a compiler cache for Rust, C/C++, and CUDA on Linux, macOS, and
Windows. It restores matching compiler outputs across worktrees and CI runs, so
you spend less time rebuilding and less disk space storing the same bytes.

%prep
%setup -a1
%autopatch -p1
[ -d .cargo ] || mkdir -p .cargo
cat %_sourcedir/cargo-config.toml >> .cargo/config.toml

%build
export CARGO_PROFILE_RELEASE_LTO=thin
export CARGO_PROFILE_RELEASE_OPT_LEVEL=3
export CARGO_PROFILE_RELEASE_CODEGEN_UNITS=1
export CARGO_PROFILE_RELEASE_DEBUG=true
export CARGO_PROFILE_RELEASE_STRIP=none
export ZSTD_SYS_USE_PKG_CONFIG=true
export LIBSQLITE3_SYS_USE_PKG_CONFIG=true
export RUSTFLAGS="-Clinker=gcc -Clink-arg=-fuse-ld=mold -Clink-arg=-Wl,--icf=safe"
cargo build --release %{?_smp_mflags} --offline --verbose

%install
install -vpDm0755 target/release/kache -t %buildroot%_bindir

mkdir -p %buildroot%bash_completionsdir
mkdir -p %buildroot%fish_completionsdir
mkdir -p %buildroot%zsh_completionsdir

%buildroot%_bindir/kache completions bash > %buildroot%bash_completionsdir/kache
%buildroot%_bindir/kache completions fish > %buildroot%fish_completionsdir/kache.fish
%buildroot%_bindir/kache completions zsh > %buildroot%zsh_completionsdir/_kache

%check
cargo test --locked --bin kache

%files
%_bindir/kache
%bash_completionsdir/kache
%fish_completionsdir/kache.fish
%zsh_completionsdir/_kache

%changelog
* Sat Oct 17 2026 Anton Zhukharev <ancieg@altlinux.org> 1.2.2-alt1
- Packaged for ALT Sisyphus.
