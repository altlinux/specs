%define _unpackaged_files_terminate_build 1
%define oname noctua
%define oname2 org.codeberg.wfx.Noctua

Name: cosmic-utils-noctua
Version: 20260918
Release: alt1

Summary: An image viewer application for the COSMIC desktop
License: GPL-3.0-or-later
Group: Graphical desktop/Other

Url: https://github.com/cosmic-utils/noctua
VCS: https://github.com/cosmic-utils/noctua

Source0: %name-%version.tar
Source1: vendor.tar
Source2: Cargo.lock

BuildRequires(pre): rpm-macros-rust
BuildRequires: rpm-build-rust
BuildRequires: libxkbcommon-devel
BuildRequires: pkgconfig(glib-2.0)
BuildRequires: pkgconfig(gio-2.0)
BuildRequires: pkgconfig(cairo)
BuildRequires: pkgconfig(cairo-gobject)
BuildRequires: libpoppler-glib-devel

%description
%summary.

%prep
%setup -a1
cp -a %SOURCE2 Cargo.lock
%rust_prep
cat >> .cargo/config.toml <<EOF

[source."git+https://github.com/iced-rs/cryoglyph.git?rev=e429a025df36ab8145708acb309080ae3deec17a"]
git = "https://github.com/iced-rs/cryoglyph.git"
rev = "e429a025df36ab8145708acb309080ae3deec17a"
replace-with = "vendored-sources"

[source."git+https://github.com/jackpot51/rust-atomicwrites"]
git = "https://github.com/jackpot51/rust-atomicwrites"
replace-with = "vendored-sources"

[source."git+https://github.com/pop-os/cosmic-protocols?rev=c0cff4d"]
git = "https://github.com/pop-os/cosmic-protocols"
rev = "c0cff4d"
replace-with = "vendored-sources"

[source."git+https://github.com/pop-os/dbus-settings-bindings"]
git = "https://github.com/pop-os/dbus-settings-bindings"
replace-with = "vendored-sources"

[source."git+https://github.com/pop-os/freedesktop-icons"]
git = "https://github.com/pop-os/freedesktop-icons"
replace-with = "vendored-sources"

[source."git+https://github.com/pop-os/libcosmic.git?rev=87ab8179e1bd9880239c340855ae8862034bd0e8"]
git = "https://github.com/pop-os/libcosmic.git"
rev = "87ab8179e1bd9880239c340855ae8862034bd0e8"
replace-with = "vendored-sources"

[source."git+https://github.com/pop-os/smithay-clipboard?tag=sctk-0.20"]
git = "https://github.com/pop-os/smithay-clipboard"
tag = "sctk-0.20"
replace-with = "vendored-sources"

[source."git+https://github.com/pop-os/softbuffer?tag=cosmic-4.0"]
git = "https://github.com/pop-os/softbuffer"
tag = "cosmic-4.0"
replace-with = "vendored-sources"

[source."git+https://github.com/pop-os/window_clipboard.git?tag=sctk-0.20"]
git = "https://github.com/pop-os/window_clipboard.git"
tag = "sctk-0.20"
replace-with = "vendored-sources"

[source."git+https://github.com/pop-os/winit.git?tag=cosmic-0.14"]
git = "https://github.com/pop-os/winit.git"
tag = "cosmic-0.14"
replace-with = "vendored-sources"

[source."git+https://github.com/wash2/accesskit?tag=cosmic-0.14"]
git = "https://github.com/wash2/accesskit"
tag = "cosmic-0.14"
replace-with = "vendored-sources"

EOF

%build
%rust_build 

%install
install -D target/release/%oname %buildroot%_bindir/%oname
install -Dm 0644 ui/cosmic/resources/%oname2.metainfo.xml %buildroot%_datadir/metainfo/%oname2.metainfo.xml
install -Dm 0644 ui/cosmic/resources/icons/hicolor/scalable/apps/%oname2.svg \
    %buildroot%_iconsdir/hicolor/scalable/apps/%oname2.svg
install -Dm 0644 ui/cosmic/resources/%oname2.desktop %buildroot%_desktopdir/%oname2.desktop

%files
%doc *.md
%_bindir/%oname
%_desktopdir/%oname2.desktop
%_datadir/metainfo/%oname2.metainfo.xml
%_iconsdir/hicolor/scalable/apps/%oname2.svg

%changelog
* Sat Sep 19 2026 Aleksandr Shamaraev <shad@altlinux.org> 20260918-alt1
- updated to git.8668c428b7
- changed license

* Mon Aug 24 2026 Aleksandr Shamaraev <shad@altlinux.org> 20260224-alt1
- Initial build.
