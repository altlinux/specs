%define _unpackaged_files_terminate_build 1

%define _libexecdir %_prefix/libexec

Name: zed
Version: 0.149.6
Release: alt1

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
BuildRequires: cargo-about
BuildRequires: clang
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

%build
export CC=clang
export CXX=clang++

export RELEASE_VERSION="%version"
export ZED_UPDATE_EXPLANATION="Please update zed using apt-get."

# Upstream says that licenses should be generated before
# building the binaries. See the following for more info:
# https://github.com/zed-industries/zed/issues/14302
./script/generate-licenses

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
sed -i "/Name=/aStartupWMClass=dev.zed.Zed" %buildroot%_desktopdir/zed.desktop

%files
# some licenses files have copyrights
%doc LICENSE-AGPL LICENSE-APACHE README.md assets/licenses.md
%_libexecdir/zed-editor
%_bindir/zed
%_desktopdir/zed.desktop
%_iconsdir/hicolor/*/apps/zed.png

%changelog
* Wed Aug 28 2024 Anton Zhukharev <ancieg@altlinux.org> 0.149.6-alt1
- Updated to 0.149.6.

* Mon Aug 26 2024 Anton Zhukharev <ancieg@altlinux.org> 0.149.5-alt1
- Updated to 0.149.5.

* Thu Aug 08 2024 Anton Zhukharev <ancieg@altlinux.org> 0.147.2-alt1
- Updated to 0.147.2.
- Disabled telemetry by default.

* Mon Aug 05 2024 Anton Zhukharev <ancieg@altlinux.org> 0.146.5-alt1
- Updated to 0.146.5.

* Fri Aug 02 2024 Anton Zhukharev <ancieg@altlinux.org> 0.146.4-alt1
- Updated to 0.146.4.

* Thu Aug 01 2024 Anton Zhukharev <ancieg@altlinux.org> 0.146.3-alt1
- Updated to 0.146.3.

* Thu Jul 25 2024 Anton Zhukharev <ancieg@altlinux.org> 0.145.1-alt1
- Updated to 0.145.1.

* Thu Jul 18 2024 Anton Zhukharev <ancieg@altlinux.org> 0.144.3-alt1
- Updated to 0.144.3.

* Wed Jul 17 2024 Anton Zhukharev <ancieg@altlinux.org> 0.143.7-alt1
- Updated to 0.143.7.

* Tue Jul 16 2024 Anton Zhukharev <ancieg@altlinux.org> 0.143.6-alt5
- Fixed opening licenses from the menu (closes 50900).

* Mon Jul 15 2024 Anton Zhukharev <ancieg@altlinux.org> 0.143.6-alt4
- Really fixed icons displaying (closes 50897).

* Mon Jul 15 2024 Anton Zhukharev <ancieg@altlinux.org> 0.143.6-alt3
- Fixed icons displaying (closes 50897).

* Thu Jul 11 2024 Anton Zhukharev <ancieg@altlinux.org> 0.143.6-alt2
- Fixed version displaying.

* Thu Jul 11 2024 Anton Zhukharev <ancieg@altlinux.org> 0.143.6-alt1
- Built for ALT Sisyphus.

