%global _unpackaged_files_terminate_build 1

Name: goose
Version: 1.44.0
Release: alt1
Summary: An open source, extensible AI agent
License: Apache-2.0
Group: Development/Tools
Url: https://block.github.io/goose
VCS: https://github.com/block/goose

Source: %name-%version.tar
Source1: vendor-alt.tar
Source2: cargo-vendor-config.toml

ExcludeArch: i586

BuildRequires(pre): rpm-macros-rust
BuildRequires: rpm-build-rust
BuildRequires: libsqlite3-devel
BuildRequires: libxcb-devel

%description
goose is your on-machine AI agent, capable of automating complex
development tasks from start to finish. More than just code
suggestions, goose can build entire projects from scratch,
write and execute code, debug failures, orchestrate workflows,
and interact with external APIs - autonomously.

%prep
%setup -a 1
%rust_prep
# Upstream ships its own vendor/v8 - a [patch.crates-io] path dependency and a
# workspace member - so the ALT vendored crates go to vendor-alt/ instead:
# cargo refuses a vendored-sources directory holding anything that is not a
# vendored crate ("failed to load checksum .cargo-checksum.json of v8").
# NB: %%rust_prep emits the line with a trailing space, so do not anchor on $.
sed -i 's|directory = "vendor"|directory = "vendor-alt"|' .cargo/config.toml
grep -q 'directory = "vendor-alt"' .cargo/config.toml
# Source replacements for the git dependencies of this release, regenerated
# together with the vendor tree by .gear/up.d/10-cargo-vendor.
cat %SOURCE2 >> .cargo/config.toml

%build
# Two of goose-cli's default features cannot be built offline from a hasher
# chroot: code-mode drags in deno_core -> v8, whose build script downloads a
# prebuilt librusty_v8 archive from GitHub (or needs a full gn/ninja V8 build
# from source), and local-inference drags in candle plus the llama.cpp bindings.
# portable-default is upstream's own feature set for portable builds and leaves
# both out; system-keyring is added back so key storage keeps using the system
# keyring over D-Bus, as it did before 1.44.0.
#
# TODO: bring code-mode back. It needs v8-goose (a rusty_v8 fork carrying V8
# 145) packaged for ALT on its own, built from source with gn/ninja instead of
# pulling denoland's prebuilt librusty_v8_release_*.a. Once that package exists,
# this build can point RUSTY_V8_SRC_BINDING_PATH/RUSTY_V8_ARCHIVE at it and add
# code-mode back to --features. Note code-mode ran on the pure-Rust boa engine
# through 1.23; commit 8631caa890 "Use Port of Context (pctx) for code mode",
# released in 1.24.0, is what moved it to deno_core/V8 - so there is no lighter
# path back within 1.44.0 itself.
%rust_build -p goose-cli --no-default-features --features portable-default,system-keyring

%install
%rust_install

%files
%_bindir/goose
%doc LICENSE

%changelog
* Tue Jul 28 2026 Alexey Shabalin <shaba@altlinux.org> 1.44.0-alt1
- updated from 1.16.1 to 1.44.0

* Fri Dec 12 2025 Alexander Makeenkov <amakeenk@altlinux.org> 1.16.1-alt1
- Updated to version 1.16.1.

* Thu Nov 27 2025 Alexander Makeenkov <amakeenk@altlinux.org> 1.15.0-alt1
- Initial build for ALT.

