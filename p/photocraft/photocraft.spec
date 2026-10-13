%define _unpackaged_files_terminate_build 1
%define oname ai.storyteller.photocraft

Name: photocraft
Version: 0.8.2
Release: alt1

Summary: PhotoCraft: An open-source, photo editor
License: MIT OR Apache-2.0
Group: Graphics

Url: https://getartcraft.com/apps/photocraft
VCS: https://github.com/storytold/photocraft

Source: %name-%version.tar

ExcludeArch: %ix86

BuildRequires(pre): rpm-macros-rust
BuildRequires: rpm-build-rust

%description
Image editing; an open-source, clean-room reimplementation of
Adobe Photoshop, rebuilt in pure Rust.

Layers, masks, adjustment layers, layer styles, type, vectors,
brushes and real PSD files,
in a native app written entirely in Rust. Open source, offline,
and yours.

%prep
%setup
%rust_prep
cat >> .cargo/config.toml <<EOF

[source."git+https://github.com/storytold/craft-libs?rev=5c874d51eeb3de70e735c8ce87a59a7dedd47675"]
git = "https://github.com/storytold/craft-libs"
rev = "5c874d51eeb3de70e735c8ce87a59a7dedd47675"
replace-with = "vendored-sources"

EOF

%build
%rust_build
sed -e "s/@VERSION@/%version/g" -e "s/@DATE@/date '+%Y%m%d'/g" packaging/linux/%oname.metainfo.xml.in \
	packaging/linux/%oname.metainfo.xml.in > packaging/linux/%oname.metainfo.xml

%install
%rust_install

install -Dm 0755 target/release/%{name}-cli %buildroot%_bindir/%{name}-cli
install -Dm 0644 packaging/linux/%oname.desktop %buildroot%_desktopdir/%oname.desktop
install -Dm 0644 packaging/linux/%oname.mime.xml %buildroot%_datadir/mime/packages/%oname.mime.xml
install -Dm 0644 packaging/linux/%oname.metainfo.xml %buildroot%_datadir/metainfo/%oname.metainfo.xml
install -d %buildroot%_iconsdir
pushd assets/app-icon
cp -p -r hicolor %buildroot%_iconsdir/
popd

%files
%doc *.md LICENSE*
%_bindir/%{name}*
%_desktopdir/%oname.desktop
%_datadir/mime/packages/%oname.mime.xml
%_datadir/metainfo/%oname.metainfo.xml
%_iconsdir/hicolor/*/apps/%oname.*

%changelog
* Tue Oct 13 2026 Aleksandr Shamaraev <shad@altlinux.org> 0.8.2-alt1
- Initial build for ALT Linux.

