%define _unpackaged_files_terminate_build 1

# no debuginfo for the native module
%add_debuginfo_skiplist %_libdir/rolldown/*.so

Name: rolldown
Version: 1.2.13
Release: alt1

Summary: Fast JavaScript bundler written in Rust
License: MIT
Group: Development/Tools
URL: https://rolldown.rs/
VCS: https://github.com/rolldown/rolldown

Source0: %name-%version.tar
Source1: %name-%version-vendor-rust.tar
Source2: %name-%version-vendor-node.tar
Patch: %name-%version-alt.patch
Patch1: %name-native-binding.patch
Patch2: %name-global-resolve.patch

Requires: node

BuildRequires(pre): rpm-macros-rust
BuildRequires(pre): rpm-macros-nodejs
BuildRequires: rpm-build-rust
BuildRequires: cmake
BuildRequires: gcc-c++

%description
A tool that combines multiple source files and project dependencies into one
or more ready-to-use files (bundles) optimized for the browser.

%prep
%setup -a1 -a2
%patch -p1
# load the native module from the package directory on every architecture
# (upstream loader only knows platform-specific .node names)
%patch1 -p1
# resolve bare imports in configs from the global node_modules
# (Node's ESM resolver ignores global paths)
%patch2 -p1
%rust_prep

%build
export CARGO_PROFILE_RELEASE_DEBUG=0
cargo build --release --offline %_smp_mflags -p rolldown_binding

%install
mkdir -p %buildroot%nodejs_sitelib/%name %buildroot%_bindir
cp -a -- npm/. %buildroot%nodejs_sitelib/%name/
install -Dm644 target/release/librolldown_binding.so \
    %buildroot%_libdir/%name/librolldown_binding.so
ln -rs %buildroot%nodejs_sitelib/%name/bin/cli.mjs %buildroot%_bindir/%name
ln -rs %buildroot%_libdir/%name/librolldown_binding.so \
    %buildroot%nodejs_sitelib/%name/librolldown_binding.so

%files
%_libdir/%name/
%_bindir/%name
%nodejs_sitelib/%name/

%changelog
* Wed Oct 14 2026 Tatyana Gagina <treza@altlinux.org> 1.2.13-alt1
- Packaged for Sisyphus.
