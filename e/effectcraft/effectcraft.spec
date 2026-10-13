%define _unpackaged_files_terminate_build 1
%define oname ai.storyteller.effectcraft

Name: effectcraft
Version: 0.9.2
Release: alt1

Summary: EffectCraft: An open-source motion graphics and compositing tool
License: MIT OR Apache-2.0
Group: Video

Url: https://getartcraft.com/apps/effectcraft
VCS: https://github.com/storytold/effectcraft

Source: %name-%version.tar
Source1: vendor.tar

ExcludeArch: %ix86

BuildRequires(pre): rpm-macros-rust
BuildRequires: rpm-build-rust
BuildRequires: pkgconfig(alsa)

%description
Motion graphics and visual effects; an open-source, clean-room
reimplementation of Adobe After Effects, rebuilt in pure Rust.

A free, open-source compositor in the spirit of After Effects:
compositions, layers, keyframes, 306 effects, layer styles, expressions,
3D cameras and lights, and a render queue, native on macOS, Windows and
Linux, and in the browser. Young, moving fast, and already usable.

%prep
%setup -a1
%rust_prep
cat >> .cargo/config.toml <<EOF

[source."git+https://github.com/storytold/craft-libs?rev=5c874d51eeb3de70e735c8ce87a59a7dedd47675"]
git = "https://github.com/storytold/craft-libs"
rev = "5c874d51eeb3de70e735c8ce87a59a7dedd47675"
replace-with = "vendored-sources"

[source."git+https://github.com/storytold/filmcraft?rev=2c5ba7a72619935f0481f99d59409e0d1844b234"]
git = "https://github.com/storytold/filmcraft"
rev = "2c5ba7a72619935f0481f99d59409e0d1844b234"
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
* Wed Oct 14 2026 Aleksandr Shamaraev <shad@altlinux.org> 0.9.2-alt1
- Initial build for ALT Linux.

