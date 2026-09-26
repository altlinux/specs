%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1

Name: disktree
Version: 0.9.1
Release: alt1

Summary: GPUI treemap explorer for disk usage, in Omarchy's visual language
License: MIT
Group: Development/Tools
Url: https://github.com/tobi/disktree
Vcs: https://github.com/tobi/disktree

ExcludeArch: %ix86

Source0: %name-%version.tar
Source1: %name-%version-vendor.tar
Source2: config.toml
Patch0: %name-%version-alt.patch

BuildRequires: rust-cargo
BuildRequires: gcc-c++
BuildRequires: pkgconfig(fontconfig)
BuildRequires: pkgconfig(xkbcommon)
BuildRequires: pkgconfig(xkbcommon-x11)

%description
Find what is filling a disk, mark what should go, and remove it - with the
volume's free space in view the whole time.

%prep
%setup -a1
%autopatch -p1
install -vpD %SOURCE2 .cargo/config.toml

%build
export CARGO_PROFILE_RELEASE_CODEGEN_UNITS=1
export CARGO_PROFILE_RELEASE_OPT_LEVEL=3
export CARGO_PROFILE_RELEASE_DEBUG=true
export CARGO_PROFILE_RELEASE_STRIP=none
export CARGO_PROFILE_RELEASE_LTO=fat
export CARGO_PROFILE_RELEASE_DEBUG_ASSERTIONS=false
export CARGO_PROFILE_RELEASE_INCREMENTAL=false
export CARGO_PROFILE_RELEASE_OVERFLOW_CHECKS=false
cargo build %_smp_mflags --release --offline

%install
install -vpD -m0755 target/release/disktree -t %buildroot%_bindir
install -vpD -m0644 assets/disktree.svg -t %buildroot%_iconsdir/hicolor/scalable/apps

mkdir -p %buildroot%_desktopdir
sed -e "s|@BINDIR@|%_bindir|" -e "s|@VERSION@|%version|" \
    packaging/disktree.desktop.in > %buildroot%_desktopdir/disktree.desktop

%files
%_bindir/disktree
%_iconsdir/hicolor/scalable/apps/disktree.svg
%_desktopdir/disktree.desktop

%changelog
* Fri Sep 25 2026 Anton Zhukharev <ancieg@altlinux.org> 0.9.1-alt1
- Packaged for ALT Sisyphus.
