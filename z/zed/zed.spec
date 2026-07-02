%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%define _libexecdir %_prefix/libexec
%define app_id dev.zed.Zed
%define app_cli zed-editor

%define webrtc_basedir %_builddir
# git grep WEBRTC_TAG
%define webrtc_tar webrtc-0001d84-2
%define webrtc_source %SOURCE4
%define webrtc_dir %webrtc_basedir/linux-x64-release

Name: zed
Version: 1.9.0
Release: alt1

Summary: A high-performance, multiplayer code editor from the creators of Atom and Tree-sitter
License: GPL-3.0 and Apache-2.0
Group: Editors
Url: https://zed.dev/
Vcs: https://github.com/zed-industries/zed.git

ExclusiveArch: x86_64

Source0: %name-%version.tar
Source1: %name-%version-vendor.tar
Source2: config.toml
Source3: update-metadata-releases.py
Source4: https://github.com/livekit/rust-sdks/releases/download/%webrtc_tar/webrtc-linux-x64-release.zip
Patch0: %name-%version-alt.patch

BuildRequires(pre): rpm-macros-rust
BuildRequires: rpm-build-rust
BuildRequires: rust-cargo
BuildRequires: cargo-about
BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: libgit2-devel
BuildRequires: libssh2-devel
BuildRequires: libssl-devel
BuildRequires: libzstd-devel
BuildRequires: zlib-devel
BuildRequires: bzip2-devel
BuildRequires: libalsa-devel
BuildRequires: glib2-devel
BuildRequires: libgio-devel
BuildRequires: libexpat-devel
BuildRequires: libxcb-devel
BuildRequires: libxkbcommon-devel
BuildRequires: libxkbcommon-x11-devel
BuildRequires: libX11-devel
BuildRequires: fontconfig-devel
BuildRequires: python3
BuildRequires: unzip
BuildRequires: /usr/bin/protoc
BuildRequires: libprotobuf-devel
BuildRequires: libvulkan-devel
BuildRequires: vulkan-validation-layers
BuildRequires: vulkan-headers
BuildRequires: libwayland-client-devel
BuildRequires: libwayland-cursor-devel
BuildRequires: libwayland-server-devel
BuildRequires: libwayland-egl-devel

%description
Code at the speed of thought - Zed is a high-performance, multiplayer code
editor from the creators of Atom and Tree-sitter.

%prep
%setup -a1
%autopatch -p1
install -vpD %SOURCE2 .cargo/config.toml
install -vp  %SOURCE3 ./update-metadata-releases.py

unzip -o %webrtc_source -d %webrtc_basedir

%build
export RELEASE_VERSION="%version"
export ZED_UPDATE_EXPLANATION="Please update zed using apt-get."
export PROTOC="/usr/bin/protoc"
export PROTOC_INCLUDE="/usr/include"
export OPENSSL_NO_VENDOR=1
export LIBGIT2_NO_VENDOR=1

# Upstream says that licenses should be generated before
# building the binaries. See the following for more info:
# https://github.com/zed-industries/zed/issues/14302
export ALLOW_MISSING_LICENSES=1
./script/generate-licenses

export LK_CUSTOM_WEBRTC="%webrtc_dir"
%rust_build --package zed --package cli

%install
install -pD -m0755 target/release/zed %buildroot%_libexecdir/zed-editor
install -pD -m0755 target/release/cli %buildroot%_bindir/%app_cli
install -pD -m0644 crates/zed/resources/app-icon.png %buildroot%_iconsdir/hicolor/512x512/apps/%app_id.png
install -pD -m0644 crates/zed/resources/app-icon@2x.png %buildroot%_iconsdir/hicolor/1024x1024/apps/%app_id.png

export DO_STARTUP_NOTIFY="true"
export APP_ID="%app_id"
export APP_CLI="%app_cli"
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
%doc LICENSE-APACHE README.md assets/licenses.md
%_libexecdir/zed-editor
%_bindir/%app_cli
%_desktopdir/%app_id.desktop
%_datadir/metainfo/%app_id.metainfo.xml
%_iconsdir/hicolor/*/apps/%app_id.png

%changelog
* Thu Jul 02 2026 Anton Zhukharev <ancieg@altlinux.org> 1.9.0-alt1
- Updated to 1.9.0.

* Tue Jun 30 2026 Anton Zhukharev <ancieg@altlinux.org> 1.8.2-alt2
- Fixed fonts corruption (ALT#59675).

* Mon Jun 29 2026 Anton Zhukharev <ancieg@altlinux.org> 1.8.2-alt1
- Updated to 1.8.2.

* Thu Jun 18 2026 Anton Zhukharev <ancieg@altlinux.org> 1.7.2-alt1
- Updated to 1.7.2.

* Thu Jun 11 2026 Anton Zhukharev <ancieg@altlinux.org> 1.6.3-alt1
- Updated to 1.6.3.

* Thu Jun 04 2026 Anton Zhukharev <ancieg@altlinux.org> 1.5.3-alt1
- Updated to 1.5.3.

* Thu May 28 2026 Anton Zhukharev <ancieg@altlinux.org> 1.4.2-alt1
- Updated to 1.4.2.

* Mon May 25 2026 Anton Zhukharev <ancieg@altlinux.org> 1.3.6-alt1
- Updated to 1.3.6.

* Thu May 07 2026 Anton Zhukharev <ancieg@altlinux.org> 1.1.6-alt1
- Updated to 1.1.6.

* Mon May 04 2026 Anton Zhukharev <ancieg@altlinux.org> 1.0.1-alt1
- Updated to 1.0.1.

* Thu Apr 30 2026 Anton Zhukharev <ancieg@altlinux.org> 1.0.0-alt1
- Updated to 1.0.0 (ALT#58946).

* Thu Mar 12 2026 Alexey Shabalin <shaba@altlinux.org> 0.227.1-alt1
- updated from 0.225.10 to 0.227.1

* Fri Feb 27 2026 Alexey Shabalin <shaba@altlinux.org> 0.225.10-alt1
- updated from 0.223.5 to 0.225.10

* Wed Feb 18 2026 Alexey Shabalin <shaba@altlinux.org> 0.223.5-alt1
- Update to 0.223.5.

* Thu Feb 12 2026 Alexey Shabalin <shaba@altlinux.org> 0.223.3-alt1
- Updated to 0.223.3.

* Sat Feb 07 2026 Alexey Shabalin <shaba@altlinux.org> 0.222.4-alt1
- Updated to 0.222.4.

* Sat Jan 31 2026 Alexey Shabalin <shaba@altlinux.org> 0.221.5-alt1
- Update to 0.221.5.
- Build with system openssl and libgit2.

* Mon Jan 26 2026 Anton Zhukharev <ancieg@altlinux.org> 0.220.6-alt1
- Updated to 0.220.6.
- Excluded aarch64 architecture.

* Mon Dec 22 2025 Anton Zhukharev <ancieg@altlinux.org> 0.217.3-alt1
- Updated to 0.217.3.

* Fri Dec 19 2025 Anton Zhukharev <ancieg@altlinux.org> 0.217.2-alt1
- Updated to 0.217.2.

* Fri Sep 26 2025 Anton Zhukharev <ancieg@altlinux.org> 0.205.5-alt1
- Updated to 0.205.5.

* Thu Sep 25 2025 Anton Zhukharev <ancieg@altlinux.org> 0.205.4-alt1
- Updated to 0.205.4.

* Tue Sep 23 2025 Anton Zhukharev <ancieg@altlinux.org> 0.204.5-alt1
- Updated to 0.204.5.

* Wed Aug 27 2025 Anton Zhukharev <ancieg@altlinux.org> 0.201.4-alt1
- Updated to 0.201.4.

* Mon Aug 25 2025 Anton Zhukharev <ancieg@altlinux.org> 0.200.5-alt1
- Updated to 0.200.5.

* Fri Jul 25 2025 Anton Zhukharev <ancieg@altlinux.org> 0.196.6-alt1
- Updated to 0.196.6.

* Thu Jul 17 2025 Anton Zhukharev <ancieg@altlinux.org> 0.195.3-alt1
- Updated to 0.195.3.

* Tue Jul 15 2025 Anton Zhukharev <ancieg@altlinux.org> 0.194.3-alt1
- Updated to 0.194.3.

* Thu Jul 03 2025 Anton Zhukharev <ancieg@altlinux.org> 0.193.3-alt1
- Updated to 0.193.3.

* Thu Jun 26 2025 Anton Zhukharev <ancieg@altlinux.org> 0.192.6-alt1
- Updated to 0.192.6.

* Mon Jun 23 2025 Anton Zhukharev <ancieg@altlinux.org> 0.191.7-alt1
- Updated to 0.191.7.

* Mon Jun 23 2025 Anton Zhukharev <ancieg@altlinux.org> 0.191.6-alt1
- Updated to 0.191.6.

* Fri May 30 2025 Anton Zhukharev <ancieg@altlinux.org> 0.188.4-alt1
- Updated to 0.188.4.

* Thu May 29 2025 Anton Zhukharev <ancieg@altlinux.org> 0.188.3-alt1
- Updated to 0.188.3.
- Removed dependency on netcat.

* Wed May 28 2025 Anton Zhukharev <ancieg@altlinux.org> 0.187.9-alt1
- Updated to 0.187.9.
- Changed cli name from "zed" to "zed-editor" (closes #54347).

* Mon May 26 2025 Anton Zhukharev <ancieg@altlinux.org> 0.187.8-alt1
- Updated to 0.187.8.

* Mon May 05 2025 Anton Zhukharev <ancieg@altlinux.org> 0.184.10-alt1
- Updated to 0.184.10.

* Thu Apr 24 2025 Anton Zhukharev <ancieg@altlinux.org> 0.183.10-alt1
- Updated to 0.183.10.

* Mon Apr 21 2025 Anton Zhukharev <ancieg@altlinux.org> 0.182.11-alt1
- Updated to 0.182.11.

* Thu Apr 17 2025 Anton Zhukharev <ancieg@altlinux.org> 0.182.9-alt1
- Updated to 0.182.9.

* Thu Apr 10 2025 Anton Zhukharev <ancieg@altlinux.org> 0.181.5-alt1
- Updated to 0.181.5.

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
