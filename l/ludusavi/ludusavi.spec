Name:    ludusavi
Version: 0.31.0
Release: alt1

Summary: Backup tool for PC game saves
License: MIT
Group:   Games/Other
Url:     https://github.com/mtkennerly/ludusavi
VCS:     https://github.com/mtkennerly/ludusavi.git

Source: %name-%version.tar
Source1: %name-development-%version.tar

BuildRequires: rpm-build-rust
BuildRequires: glib2-devel libgio-devel libatk-devel libgtk+3-devel
BuildRequires: libappstream-devel

ExclusiveArch: x86_64

%description
Ludusavi is a tool for backing up your PC video game save data, written
in Rust. It is cross-platform and supports multiple game stores.

%prep
%setup -a1
%rust_prep

sed -i -e 's/"files":{[^}]*}/"files":{}/' \
    ./vendor/*/.cargo-checksum.json

%build
CFLAGS+=" -ffat-lto-objects"
export RUSTUP_TOOLCHAIN=stable
export CARGO_TARGET_DIR=target

%rust_build

%check
appstreamcli validate --no-net "assets/linux/com.mtkennerly.ludusavi.metainfo.xml"
desktop-file-validate "assets/linux/com.mtkennerly.ludusavi.desktop"

%install
%rust_install

install -Dm644 assets/linux/com.mtkennerly.ludusavi.metainfo.xml -t %buildroot%_datadir/metainfo/
install -Dm644 assets/icon.png %buildroot%_iconsdir/hicolor/64x64/apps/com.mtkennerly.ludusavi.png
install -Dm644 assets/icon.svg %buildroot%_iconsdir/hicolor/scalable/apps/com.mtkennerly.ludusavi.svg
install -Dm644 assets/linux/com.mtkennerly.ludusavi.desktop -t %buildroot%_desktopdir/

%files
%doc LICENSE README.md
%_bindir/%name
%_datadir/metainfo/com.mtkennerly.ludusavi.metainfo.xml
%_desktopdir/com.mtkennerly.ludusavi.desktop
%_iconsdir/hicolor/64x64/apps/com.mtkennerly.ludusavi.png
%_iconsdir/hicolor/scalable/apps/com.mtkennerly.ludusavi.svg

%changelog
* Sun Jun 07 2026 Sergey Palcheh <minergenon@altlinux.org> 0.31.0-alt1
- new version 0.31.0

* Thu Mar 20 2025 Sergey Palcheh <minergenon@altlinux.org> 0.28.0-alt1
- Initial build for Sisyphus
