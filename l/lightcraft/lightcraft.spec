%define _unpackaged_files_terminate_build 1
%define oname ai.storyteller.lightcraft

Name: lightcraft
Version: 0.7.1
Release: alt1

Summary: LightCraft: An open-source non-destructive photo editor
License: MIT OR Apache-2.0
Group: Graphics

Url: https://getartcraft.com/apps/lightcraft
VCS: https://github.com/storytold/lightcraft

Source: %name-%version.tar
Source1: vendor.tar

ExcludeArch: %ix86

BuildRequires(pre): rpm-macros-rust
BuildRequires: rpm-build-rust

%description
Photo library and raw development; an open-source, clean-room
reimplementation of Adobe Lightroom, rebuilt in pure Rust.

Native on macOS, Windows and Linux. In the browser via WebAssembly.
Drivable end to end by AI agents over MCP.

%prep
%setup -a1
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
* Wed Oct 14 2026 Aleksandr Shamaraev <shad@altlinux.org> 0.7.1-alt1
- Initial build for ALT Linux.

