%define _unpackaged_files_terminate_build 1

%def_with check

Name: herdr
Version: 0.8.2
Release: alt1

Summary: Terminal workspace manager for AI coding agents
License: Apache-2.0
Group: Terminals

Url: https://herdr.dev
Vcs: https://github.com/herdrdev/herdr

Source: %name-%version.tar
Source1: vendor-alt.tar
Source2: vendor-zig.tar
Patch0: %name-%version-alt.patch

ExclusiveArch: %zig_arches

BuildRequires(pre): rpm-macros-zig
BuildRequires: zig
BuildRequires: rpm-build-rust

BuildRequires: /proc, /dev/pts

%if_with check
BuildRequires: git
BuildRequires: curl
%endif

%description
herdr is a terminal workspace manager built for running several AI coding
agents side by side.

The terminals live inside a background server, so agents keep working when the
client goes away and sessions come back after a detach, a lost network
connection or a reboot.  Every pane is marked working, blocked or idle, so a
stuck agent is visible instead of hidden in another tab.  Panes, tabs and
workspaces are driven both from tmux-style prefix keys and from the mouse, and
agents themselves can drive herdr through its command line and socket API.

%prep
%setup -a 1 -a 2
%patch0 -p1

rm -f rust-toolchain.toml

mkdir -p .cargo
cat > .cargo/config.toml <<EOF
[source.crates-io]
replace-with = "vendored-sources"

[source.vendored-sources]
directory = "vendor-alt"
EOF

%build
export CARGO_HOME="$PWD/.cargo-home"

export ZIG=%_bindir/zig
export ZIG_GLOBAL_CACHE_DIR="$PWD/.zig-global-cache"
export ZIG_LOCAL_CACHE_DIR="$PWD/.zig-local-cache"
mkdir -p "$ZIG_GLOBAL_CACHE_DIR" "$ZIG_LOCAL_CACHE_DIR"
cp -a vendor-zig/p "$ZIG_GLOBAL_CACHE_DIR/p"
export LIBGHOSTTY_VT_OPTIMIZE=ReleaseFast
export LIBGHOSTTY_VT_SIMD=true

%rust_build

%install
%rust_install

export HOME="$PWD"
install -d %buildroot%_datadir/bash-completion/completions \
	%buildroot%_datadir/zsh/site-functions \
	%buildroot%_datadir/fish/vendor_completions.d \
	%buildroot%_datadir/elvish/lib
./target/release/herdr completion bash \
	> %buildroot%_datadir/bash-completion/completions/herdr
./target/release/herdr completion zsh \
	> %buildroot%_datadir/zsh/site-functions/_herdr
./target/release/herdr completion fish \
	> %buildroot%_datadir/fish/vendor_completions.d/herdr.fish
./target/release/herdr completion elvish \
	> %buildroot%_datadir/elvish/lib/herdr.elv
chmod 0644 %buildroot%_datadir/bash-completion/completions/herdr \
	%buildroot%_datadir/zsh/site-functions/_herdr \
	%buildroot%_datadir/fish/vendor_completions.d/herdr.fish \
	%buildroot%_datadir/elvish/lib/herdr.elv

install -Dm0644 skills/herdr/SKILL.md \
	%buildroot%_datadir/herdr/skills/herdr/SKILL.md

install -Dm0644 docs/next/api/herdr-api.schema.json \
	%buildroot%_datadir/herdr/api/herdr-api.schema.json

./target/release/herdr --default-config > config.toml.example

%check
export CARGO_HOME="$PWD/.cargo-home"
export RUSTFLAGS="${RUSTFLAGS-} -g"
export ZIG=%_bindir/zig
export ZIG_GLOBAL_CACHE_DIR="$PWD/.zig-global-cache"
export ZIG_LOCAL_CACHE_DIR="$PWD/.zig-local-cache"
export LIBGHOSTTY_VT_OPTIMIZE=ReleaseFast
export LIBGHOSTTY_VT_SIMD=true

isolated=workspace::tests::generated_workspace_ids_are_short_base32_handles
cargo test --release --offline %{?_smp_mflags} --bins -- \
	--test-threads=1 --skip "$isolated"
cargo test --release --offline %{?_smp_mflags} --bins -- \
	--exact "$isolated"

%files
%doc LICENSE README.md CHANGELOG.md config.toml.example website/agent-guide.md
%_bindir/herdr
%_datadir/bash-completion/completions/herdr
%_datadir/zsh/site-functions/_herdr
%_datadir/fish/vendor_completions.d/herdr.fish
%_datadir/elvish/lib/herdr.elv
%_datadir/herdr

%changelog
* Thu Aug 27 2026 Egor Ignatov <egori@altlinux.org> 0.8.2-alt1
- First build for ALT.
