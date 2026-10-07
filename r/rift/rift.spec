%define _unpackaged_files_terminate_build 1

Name: rift
Version: 2.9.0
Release: alt2
Summary: Terminal coding agent for local and cloud language models
License: MIT
Group: Development/Tools
Url: https://github.com/exYze/rift
Vcs: https://github.com/exYze/rift.git

Source: %name-%version.tar
Source1: %name-predownloaded-%version.tar
Source2: %name-predownloaded-desktop-%version.tar
Source3: %name-desktop.desktop
Patch1: %name-%version-%release.patch

BuildRequires(pre): rpm-macros-rust
BuildRequires: rpm-build-rust
BuildRequires: gcc-c++
BuildRequires: pkgconfig(gtk+-3.0)
BuildRequires: pkgconfig(webkit2gtk-4.1)
BuildRequires: pkgconfig(ayatana-appindicator3-0.1)
BuildRequires: pkgconfig(librsvg-2.0)
BuildRequires: pkgconfig(dbus-1)
BuildRequires: pkgconfig(openssl)
BuildRequires: xdotool-devel
BuildRequires: desktop-file-utils

# git is the only hard runtime dependency (swarm/github); clipboard, LSP
# and MCP servers are optional features with graceful fallbacks.
Requires: git-core

%description
Rift is a terminal coding agent built in Rust. It supports local Ollama and
OpenAI-compatible servers, with optional cloud providers.

%package desktop
Summary: Desktop interface for Rift
Group: Graphical desktop/Other
Requires: %name = %version-%release
Requires: fonts-otf-google-noto-cjk-common

%description desktop
Rift Desktop is a native graphical interface for Rift. It manages sessions
and starts the Rift coding agent through its serve protocol.

%prep
%setup -a1 -a2
%patch1 -p1
%rust_prep
pushd desktop/src-tauri
%rust_prep
popd

%build
%rust_build -p rift-tui --bin rift
%ifarch %ix86
# Fat LTO with one codegen unit exhausts the 32-bit rustc address space.
export CARGO_PROFILE_RELEASE_LTO=off
export CARGO_PROFILE_RELEASE_CODEGEN_UNITS=16
%endif
pushd desktop/src-tauri
%rust_build --bin rift-desktop
popd

%install
%rust_install rift
pushd desktop/src-tauri
%rust_install rift-desktop
popd
install -Dm644 %SOURCE3 %buildroot%_desktopdir/%name-desktop.desktop
install -Dm644 desktop/src-tauri/icons/icon.png \
    %buildroot%_iconsdir/hicolor/256x256/apps/%name-desktop.png

%check
export RIFT_NO_UPDATE_CHECK=1
%rust_test --workspace
%ifarch %ix86
export CARGO_PROFILE_RELEASE_LTO=off
export CARGO_PROFILE_RELEASE_CODEGEN_UNITS=16
%endif
pushd desktop/src-tauri
%rust_test
popd
desktop-file-validate %SOURCE3

%files
%doc README.md CHANGELOG.md LICENSE
%_bindir/rift

%files desktop
%doc desktop/README.md
%_bindir/rift-desktop
%_desktopdir/rift-desktop.desktop
%_iconsdir/hicolor/256x256/apps/rift-desktop.png

%changelog
* Wed Oct 07 2026 Alexey Shabalin <shaba@altlinux.org> 2.9.0-alt2
- Add support built-in Kimi Code provider.

* Tue Oct 06 2026 Alexey Shabalin <shaba@altlinux.org> 2.9.0-alt1
- Initial build for Sisyphus with terminal and desktop interfaces.

