%define _unpackaged_files_terminate_build 1

Name: fresh
Version: 0.1.88
Release: alt1

Summary: Text editor for your terminal: easy, powerful and fast

License: GPL-2.0
Group: Editors
Url: https://sinelaw.github.io/fresh/

# Source-url: https://github.com/sinelaw/fresh/archive/refs/tags/v%version.tar.gz
Source: %name-%version.tar

Source1: %name-development-%version.tar

ExcludeArch: i586

BuildRequires(pre): rpm-macros-rust
BuildRequires: rpm-build-rust
BuildRequires: clang-devel llvm-devel

%description
%summary.

%prep
%setup -a1
mkdir -p .cargo
cat >.cargo/config <<EOF
[source.crates-io]
replace-with = "vendored-sources"
[source.vendored-sources]
directory = "vendor"
EOF

%build
%rust_build

%install
# Binary (installed alongside plugins, symlinked from /usr/bin)
install -d %buildroot%_bindir
install -Dm755 target/release/fresh %buildroot%_libexecdir/fresh/fresh
ln -s %_libexecdir/fresh/fresh %buildroot%_bindir/fresh

cp -r crates/fresh-editor/plugins %buildroot%_libexecdir/%name/
cp -r crates/fresh-editor/keymaps %buildroot%_libexecdir/%name/
cp -r crates/fresh-editor/queries %buildroot%_libexecdir/%name/
cp -r crates/fresh-editor/themes %buildroot%_libexecdir/%name/

install -Dm644 crates/fresh-editor/flatpak/io.github.sinelaw.fresh.svg %buildroot%_iconsdir/hicolor/scalable/apps/io.github.sinelaw.fresh.svg
install -Dm644 crates/fresh-editor/flatpak/io.github.sinelaw.fresh.desktop %buildroot%_desktopdir/io.github.sinelaw.fresh.desktop
install -Dm644 crates/fresh-editor/flatpak/io.github.sinelaw.fresh.metainfo.xml %buildroot%_datadir/metainfo/io.github.sinelaw.fresh.metainfo.xml

%files
%doc LICENSE README.md CHANGELOG.md
%_bindir/fresh
%_libexecdir/fresh
%_iconsdir/hicolor/scalable/apps/io.github.sinelaw.fresh.svg
%_desktopdir/io.github.sinelaw.fresh.desktop
%_datadir/metainfo/io.github.sinelaw.fresh.metainfo.xml

%changelog
* Sat Jan 24 2026 Boris Yumankulov <boria138@altlinux.org> 0.1.88-alt1
- initial build for ALT Sisyphus

