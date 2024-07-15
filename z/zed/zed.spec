%define _unpackaged_files_terminate_build 1

%define _libexecdir %_prefix/libexec

Name: zed
Version: 0.143.6
Release: alt3

Summary: A high-performance, multiplayer code editor from the creators of Atom and Tree-sitter
License: GPL-3.0 and AGPL-3.0 and Apache-2.0
Group: Editors
Url: https://zed.dev/
Vcs: https://github.com/zed-industries/zed

ExclusiveArch: x86_64 aarch64

Source0: %name-%version.tar
Source1: %name-%version-vendor.tar
Source2: config.toml
Patch0: %name-%version-alt.patch

BuildRequires(pre): rpm-build-rust
BuildRequires: /proc
BuildRequires: rust
BuildRequires: rust-cargo
BuildRequires: gcc-c++
BuildRequires: cmake
BuildRequires: mold
BuildRequires: libstdc++-devel
BuildRequires: libssl-devel
BuildRequires: libzstd-devel
BuildRequires: libalsa-devel
BuildRequires: libxcb-devel
BuildRequires: libxkbcommon-devel
BuildRequires: libxkbcommon-x11-devel

%description
Code at the speed of thought - Zed is a high-performance, multiplayer code
editor from the creators of Atom and Tree-sitter.

%prep
%setup -a1
%autopatch -p1
install -vpD %SOURCE2 .cargo/config.toml
cat >> .cargo/config.toml << EOF
[install]
root = "%buildroot%_prefix"

[build]
rustflags = ["-Copt-level=3", "-Cdebuginfo=1"]

[profile.release]
strip = false

[target.x86_64-unknown-linux-gnu]
rustflags = ["-C", "link-arg=-fuse-ld=mold"]

[target.aarch64-unknown-linux-gnu]
rustflags = ["-C", "link-arg=-fuse-ld=mold"]
EOF

%build
export RELEASE_VERSION="%version"
export ZED_UPDATE_EXPLANATION="Please update zed using apt-get."
%rust_build --package zed --package cli

%install
install -pD -m0755 target/release/zed %buildroot%_libexecdir/zed-editor
install -pD -m0755 target/release/cli %buildroot%_bindir/zed
install -pD -m0644 crates/zed/resources/app-icon.png %buildroot%_iconsdir/hicolor/512x512/apps/zed.png
install -pD -m0644 crates/zed/resources/app-icon@2x.png %buildroot%_iconsdir/hicolor/1024x1024/apps/zed.png

export DO_STARTUP_NOTIFY="true"
export APP_CLI="zed"
export APP_ICON="zed"
export APP_ARGS="%%U"
export APP_NAME="Zed"
mkdir -p %buildroot%_desktopdir
envsubst < crates/zed/resources/zed.desktop.in > %buildroot%_desktopdir/zed.desktop
sed "/Name=/aStartupWMClass=dev.zed.Zed" %buildroot%_desktopdir/zed.desktop

%files
# some licenses files have copyrights
%doc LICENSE-AGPL LICENSE-APACHE README.md
%_libexecdir/zed-editor
%_bindir/zed
%_desktopdir/zed.desktop
%_iconsdir/hicolor/*/apps/zed.png

%changelog
* Mon Jul 15 2024 Anton Zhukharev <ancieg@altlinux.org> 0.143.6-alt3
- Fixed icons displaying (closes 50897).

* Thu Jul 11 2024 Anton Zhukharev <ancieg@altlinux.org> 0.143.6-alt2
- Fixed version displaying.

* Thu Jul 11 2024 Anton Zhukharev <ancieg@altlinux.org> 0.143.6-alt1
- Built for ALT Sisyphus.

