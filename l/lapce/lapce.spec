%define _unpackaged_files_terminate_build 1

Name: lapce
Version: 0.2.8
Release: alt1

Summary: Lightning-fast and Powerful Code Editor written in Rust
License: Apache-2.0
Group: Development/Other
Url: https://lapce.dev
Vcs: https://github.com/lapce/lapce

Source0: %name-%version.tar
Source1: config.toml

BuildRequires(pre): rpm-macros-rust
BuildRequires(pre): /proc
BuildRequires: rust-cargo
BuildRequires: gcc-c++
BuildRequires: glib2-devel
BuildRequires: libgio-devel
BuildRequires: libgdk-pixbuf-devel
BuildRequires: libcairo-devel
BuildRequires: libcairo-gobject-devel
BuildRequires: libpango-devel
BuildRequires: libatk-devel
BuildRequires: libgtk+3-devel
BuildRequires: libssl-devel
BuildRequires: perl-Pod-Usage

# build only for supported architectures
ExclusiveArch: x86_64 aarch64

%description
Lapce is written in pure Rust with a UI in Druid (which is also written
in Rust). It is designed with Rope Science from the Xi-Editor which
makes for lightning-fast computation, and leverages OpenGL for
rendering. More information about the features of Lapce can be found on
the main website and user documentation can be found on GitBook.

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

install -D %SOURCE1 .cargo/config.toml

# fix path to lapce.svg icon
sed -i '/Icon=/s/=.*/=%name/' extra/linux/dev.lapce.lapce.desktop

# rust library path
echo "export RUST_SRC_PATH=%_libdir/rustlib/src/rust/library" > lapce-rust.sh

%build
export RELEASE_TAG_NAME="v%version"
export CARGO_PKG_VERSION="%version"
%rust_build

%install
%rust_install

# also install lapce-proxy
%__install -m755 -pD target/release/%name-proxy %buildroot%_bindir/%name-proxy

# install desktop file and icon
%__install -m644 -pD extra/linux/dev.lapce.lapce.desktop \
                     %buildroot%_desktopdir/%name.desktop
%__install -m644 -pD extra/images/logo.svg \
                     %buildroot%_iconsdir/hicolor/scalable/apps/%name.svg

# install shell profile file
%__install -m755 -pD lapce-rust.sh \
                     %buildroot%_sysconfdir/profile.d/lapce-rust.sh

%files
%doc LICENSE README.md CHANGELOG.md
%_bindir/%name
%_bindir/%name-proxy
%_desktopdir/%name.desktop
%_iconsdir/hicolor/scalable/apps/%name.svg

%files rust
%config(noreplace) %_sysconfdir/profile.d/lapce-rust.sh

%changelog
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

