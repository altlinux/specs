%define _unpackaged_files_terminate_build 1

Name: lapce
Version: 0.4.5
Release: alt1

Summary: Lightning-fast and Powerful Code Editor
License: Apache-2.0
Group: Development/Other
Url: https://lapce.dev
Vcs: https://github.com/lapce/lapce.git

Source0: %name-%version.tar
Source1: config.toml
Patch: %name-%version.patch

BuildRequires(pre): rpm-macros-rust
BuildRequires: rpm-build-rust
BuildRequires: libssl-devel perl(IPC/Cmd.pm)
BuildRequires: libgit2-devel
BuildRequires: libssh2-devel
BuildRequires: zlib-devel libzstd-devel
#BuildRequires: pkgconfig(libdrm) pkgconfig(wayland-scanner) pkgconfig(wayland-cursor)
#BuildRequires: pkgconfig(wayland-client) pkgconfig(wayland-server) pkgconfig(wayland-egl)
# build only for supported architectures
ExclusiveArch: x86_64 aarch64

%description
Lapce is written in pure Rust, with a UI in Floem.
It is designed with Rope Science from the Xi-Editor, enabling lightning-fast
computation, and leverages wgpu for rendering. More information about
the features of Lapce can be found on the main website and
user documentation can be found on GitBook.

# lapce-rust is used for rust development
# see: https://bugzilla.altlinux.org/46242
%package rust
Summary: Lapce for Rust development
Group: Development/Other
Requires: %name = %EVR
Requires: gcc
Requires: rust-analyzer
Requires: rust-cargo
Requires: rust-src

%description rust
%summary.

%prep
%setup
%patch -p1
%rust_prep
cat %SOURCE1 >> .cargo/config.toml

# fix path to lapce.svg icon
sed -i '/Icon=/s/=.*/=%name/' extra/linux/dev.lapce.lapce.desktop

# rust library path
echo "export RUST_SRC_PATH=%_libdir/rustlib/src/rust/library" > lapce-rust.sh

%build
export RELEASE_TAG_NAME="v%version"
export CARGO_PKG_VERSION="%version"
export OPENSSL_NO_VENDOR=1
export LIBGIT2_NO_VENDOR=1
%rust_build

%install
%rust_install

# also install lapce-proxy
install -m755 -pD target/release/%name-proxy %buildroot%_bindir/%name-proxy

# install desktop file and icon
install -m644 -pD extra/linux/dev.lapce.lapce.desktop \
                  %buildroot%_desktopdir/%name.desktop
install -m644 -pD extra/linux/dev.lapce.lapce.metainfo.xml \
                  %buildroot%_datadir/metainfo/dev.lapce.lapce.metainfo.xml
install -m644 -pD extra/images/logo.svg \
                  %buildroot%_iconsdir/hicolor/scalable/apps/%name.svg

# install shell profile file
install -m755 -pD lapce-rust.sh \
                  %buildroot%_sysconfdir/profile.d/lapce-rust.sh

%check
%rust_test

%files
%doc LICENSE README.md CHANGELOG.md
%_bindir/%name
%_bindir/%name-proxy
%_desktopdir/%name.desktop
%_datadir/metainfo/*.xml
%_iconsdir/hicolor/scalable/apps/%name.svg

%files rust
%config(noreplace) %_sysconfdir/profile.d/lapce-rust.sh

%changelog
* Fri Dec 19 2025 Alexey Shabalin <shaba@altlinux.org> 0.4.5-alt1
- 0.4.5.
- Cleanup BR.
- Build with system openssl and libgit2.

* Tue Sep 12 2023 Anton Zhukharev <ancieg@altlinux.org> 0.2.8-alt1
- Updated to 0.2.8.

* Wed May 31 2023 Anton Zhukharev <ancieg@altlinux.org> 0.2.7-alt3
- Separated lapce-rust for Rust developemnt (ALT 46242).

* Wed May 24 2023 Anton Zhukharev <ancieg@altlinux.org> 0.2.7-alt2
- Packaged desktop file (ALT 46243).
- Packaged lapce-proxy.
- Set dependency on gcc, rust-analyzer, rust-cargo and rust-src (ALT 46242).

* Thu May 11 2023 Anton Zhukharev <ancieg@altlinux.org> 0.2.7-alt1
- Initial build for ALT Sisyphus.

