%define _unpackaged_files_terminate_build 1

Name: lapce
Version: 0.2.7
Release: alt2

Summary: Lightning-fast and Powerful Code Editor written in Rust
License: Apache-2.0
Group: Development/Other
Url: https://lapce.dev
Vcs: https://github.com/lapce/lapce

Source: %name-%version.tar

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

# lapce is used for rust development
# see: https://bugzilla.altlinux.org/46242
Requires: gcc
Requires: rust-analyzer
Requires: rust-cargo
Requires: rust-src

%description
Lapce is written in pure Rust with a UI in Druid (which is also written
in Rust). It is designed with Rope Science from the Xi-Editor which
makes for lightning-fast computation, and leverages OpenGL for
rendering. More information about the features of Lapce can be found on
the main website and user documentation can be found on GitBook.

%prep
%setup
mkdir .cargo
cp {.gear,.cargo}/config.toml

# fix path to lapce.svg icon
sed -i '/Icon=/s/=.*/=%name/' extra/linux/dev.lapce.lapce.desktop

%build
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

%files
%doc LICENSE README.md CHANGELOG.md
%_bindir/%name
%_bindir/%name-proxy
%_desktopdir/%name.desktop
%_iconsdir/hicolor/scalable/apps/%name.svg

%changelog
* Wed May 24 2023 Anton Zhukharev <ancieg@altlinux.org> 0.2.7-alt2
- Packaged desktop file (ALT 46243).
- Packaged lapce-proxy.
- Set dependency on gcc, rust-analyzer, rust-cargo and rust-src (ALT 46242).

* Thu May 11 2023 Anton Zhukharev <ancieg@altlinux.org> 0.2.7-alt1
- Initial build for ALT Sisyphus.

