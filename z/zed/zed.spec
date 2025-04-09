%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%define _libexecdir %_prefix/libexec
%define app_id dev.zed.Zed

%define webrtc_basedir %_builddir
%ifarch x86_64
%define webrtc_source %SOURCE4
%define webrtc_dir %webrtc_basedir/linux-x64-release
%else
%define webrtc_source %SOURCE5
%define webrtc_dir %webrtc_basedir/linux-arm64-release
%endif

Name: zed
Version: 0.180.4
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
Source3: update-metadata-releases.py
Source4: https://github.com/zed-industries/webrtc/releases/download/m114_release_patched/webrtc-linux-x64-release.zip
Source5: https://github.com/livekit/rust-sdks/releases/download/webrtc-dac8015-6/webrtc-linux-arm64-release.zip
Patch0: %name-%version-alt.patch

# zed needs netcat to do `git fetch'
# see https://bugzilla.altlinux.org/53668
Requires: netcat

BuildRequires: /proc
BuildRequires: rust-cargo
BuildRequires: cargo-about
BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: libssl-devel
BuildRequires: libzstd-devel
BuildRequires: libalsa-devel
BuildRequires: libxcb-devel
BuildRequires: libxkbcommon-devel
BuildRequires: libxkbcommon-x11-devel
BuildRequires: python3
BuildRequires: unzip

%description
Code at the speed of thought - Zed is a high-performance, multiplayer code
editor from the creators of Atom and Tree-sitter.

%prep
%setup -a1
%autopatch -p1
install -vpD %SOURCE2 .cargo/config.toml
install -vp  %SOURCE3 ./update-metadata-releases.py

unzip %webrtc_source -d %webrtc_basedir

%build
export RELEASE_VERSION="%version"
export ZED_UPDATE_EXPLANATION="Please update zed using apt-get."

# Upstream says that licenses should be generated before
# building the binaries. See the following for more info:
# https://github.com/zed-industries/zed/issues/14302
export ALLOW_MISSING_LICENSES=1
./script/generate-licenses

export LK_CUSTOM_WEBRTC="%webrtc_dir"
cargo build %_smp_mflags --release --offline --package zed --package cli

%install
install -pD -m0755 target/release/zed %buildroot%_libexecdir/zed-editor
install -pD -m0755 target/release/cli %buildroot%_bindir/zed
install -pD -m0644 crates/zed/resources/app-icon.png %buildroot%_iconsdir/hicolor/512x512/apps/%app_id.png
install -pD -m0644 crates/zed/resources/app-icon@2x.png %buildroot%_iconsdir/hicolor/1024x1024/apps/%app_id.png

export DO_STARTUP_NOTIFY="true"
export APP_ID="%app_id"
export APP_CLI="zed"
export APP_ICON="%app_id"
export APP_ARGS="%%U"
export APP_NAME="Zed"
export BRANDING_LIGHT="#99c1f1"
export BRANDING_DARK="#1a5fb4"
mkdir -p %buildroot%_desktopdir %buildroot%_datadir/metainfo
envsubst < crates/zed/resources/zed.desktop.in > %buildroot%_desktopdir/%app_id.desktop
envsubst < crates/zed/resources/flatpak/zed.metainfo.xml.in > %buildroot%_datadir/metainfo/%app_id.metainfo.xml
./update-metadata-releases.py %_specdir/%name.spec %buildroot%_datadir/metainfo/%app_id.metainfo.xml

%files
# some licenses files have copyrights
%doc LICENSE-AGPL LICENSE-APACHE README.md assets/licenses.md
%_libexecdir/zed-editor
%_bindir/zed
%_desktopdir/%app_id.desktop
%_datadir/metainfo/%app_id.metainfo.xml
%_iconsdir/hicolor/*/apps/%app_id.png

%changelog
* Wed Apr 09 2025 Anton Zhukharev <ancieg@altlinux.org> 0.180.4-alt1
- Updated to 0.180.4.

* Mon Apr 07 2025 Anton Zhukharev <ancieg@altlinux.org> 0.180.3-alt1
- Updated to 0.180.3.

* Thu Apr 03 2025 Anton Zhukharev <ancieg@altlinux.org> 0.180.2-alt1
- Updated to 0.180.2.

* Tue Apr 01 2025 Anton Zhukharev <ancieg@altlinux.org> 0.179.5-alt1
- Updated to 0.179.5.

* Mon Mar 31 2025 Anton Zhukharev <ancieg@altlinux.org> 0.179.4-alt2
- Added dependency on netcat to fix `git fetch' (closes 53668).

* Fri Mar 28 2025 Anton Zhukharev <ancieg@altlinux.org> 0.179.4-alt1
- Updated to 0.179.4.

* Fri Mar 28 2025 Anton Zhukharev <ancieg@altlinux.org> 0.179.3-alt1
- Updated to 0.179.3 (closes 53551).

* Thu Dec 12 2024 Anton Zhukharev <ancieg@altlinux.org> 0.165.4-alt1
- Updated to 0.165.4.

* Thu Dec 05 2024 Anton Zhukharev <ancieg@altlinux.org> 0.164.2-alt1
- Updated to 0.164.2.

* Fri Nov 29 2024 Anton Zhukharev <ancieg@altlinux.org> 0.163.2-alt1
- Updated to 0.163.2.

* Fri Nov 22 2024 Anton Zhukharev <ancieg@altlinux.org> 0.162.5-alt1
- Updated to 0.162.5.

* Thu Nov 21 2024 Anton Zhukharev <ancieg@altlinux.org> 0.162.3-alt1
- Updated to 0.162.3.

* Fri Nov 15 2024 Anton Zhukharev <ancieg@altlinux.org> 0.161.2-alt1
- Updated to 0.161.2.

* Thu Nov 14 2024 Anton Zhukharev <ancieg@altlinux.org> 0.160.7-alt2
- Shipped /usr/share/metainfo/dev.zed.Zed.metainfo.xml.

* Tue Nov 12 2024 Anton Zhukharev <ancieg@altlinux.org> 0.160.7-alt1
- Updated to 0.160.7.

* Thu Oct 24 2024 Anton Zhukharev <ancieg@altlinux.org> 0.158.1-alt1
- Updated to 0.158.1.

* Thu Oct 17 2024 Anton Zhukharev <ancieg@altlinux.org> 0.157.5-alt1
- Updated to 0.157.5.

* Tue Oct 15 2024 Anton Zhukharev <ancieg@altlinux.org> 0.156.2-alt1
- Updated to 0.156.2.

* Thu Oct 10 2024 Anton Zhukharev <ancieg@altlinux.org> 0.156.1-alt1
- Updated to 0.156.1.

* Thu Oct 10 2024 Anton Zhukharev <ancieg@altlinux.org> 0.156.0-alt1
- Updated to 0.156.0.

* Thu Oct 03 2024 Anton Zhukharev <ancieg@altlinux.org> 0.155.2-alt1
- Updated to 0.155.2.

* Mon Sep 30 2024 Anton Zhukharev <ancieg@altlinux.org> 0.154.3-alt1
- Updated to 0.154.3.

* Thu Sep 26 2024 Anton Zhukharev <ancieg@altlinux.org> 0.154.2-alt1
- Updated to 0.154.2.

* Wed Sep 25 2024 Anton Zhukharev <ancieg@altlinux.org> 0.154.1-alt1
- Updated to 0.154.1.

* Wed Sep 25 2024 Anton Zhukharev <ancieg@altlinux.org> 0.153.7-alt1
- Updated to 0.153.7.

* Fri Sep 20 2024 Anton Zhukharev <ancieg@altlinux.org> 0.153.6-alt1
- Updated to 0.153.6.

* Tue Sep 17 2024 Anton Zhukharev <ancieg@altlinux.org> 0.152.4-alt1
- Updated to 0.152.4.

* Wed Sep 11 2024 Anton Zhukharev <ancieg@altlinux.org> 0.152.3-alt1
- Updated to 0.152.3.

* Mon Sep 09 2024 Anton Zhukharev <ancieg@altlinux.org> 0.151.2-alt1
- Updated to 0.151.2.

* Fri Sep 06 2024 Anton Zhukharev <ancieg@altlinux.org> 0.151.1-alt1
- Updated to 0.151.1.

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

