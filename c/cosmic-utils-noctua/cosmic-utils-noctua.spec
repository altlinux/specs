%define _unpackaged_files_terminate_build 1
%define oname noctua
%define oname2 org.codeberg.wfx.Noctua

Name: cosmic-utils-noctua
Version: 20260224
Release: alt1

Summary: An image viewer application for the COSMIC desktop
License: GPL-3.0-only
Group: Graphical desktop/Other

Url: https://github.com/cosmic-utils/noctua
VCS: https://github.com/cosmic-utils/noctua

Source0: %name-%version.tar
Source1: vendor.tar

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
%rust_prep
cat >> .cargo/config.toml <<EOF

[source."git+https://github.com/jackpot51/rust-atomicwrites"]
git = "https://github.com/jackpot51/rust-atomicwrites"
replace-with = "vendored-sources"

[source."git+https://github.com/pop-os/cosmic-protocols?rev=d0e95be"]
git = "https://github.com/pop-os/cosmic-protocols"
rev = "d0e95be"
replace-with = "vendored-sources"

[source."git+https://github.com/pop-os/cosmic-text.git"]
git = "https://github.com/pop-os/cosmic-text.git"
replace-with = "vendored-sources"

[source."git+https://github.com/pop-os/dbus-settings-bindings"]
git = "https://github.com/pop-os/dbus-settings-bindings"
replace-with = "vendored-sources"

[source."git+https://github.com/pop-os/freedesktop-icons"]
git = "https://github.com/pop-os/freedesktop-icons"
replace-with = "vendored-sources"

[source."git+https://github.com/pop-os/glyphon.git?tag=iced-0.14-dev"]
git = "https://github.com/pop-os/glyphon.git"
tag = "iced-0.14-dev"
replace-with = "vendored-sources"

[source."git+https://github.com/pop-os/libcosmic.git"]
git = "https://github.com/pop-os/libcosmic.git"
replace-with = "vendored-sources"

[source."git+https://github.com/pop-os/smithay-clipboard?tag=pop-dnd-5"]
git = "https://github.com/pop-os/smithay-clipboard"
tag = "pop-dnd-5"
replace-with = "vendored-sources"

[source."git+https://github.com/pop-os/softbuffer?tag=cosmic-4.0"]
git = "https://github.com/pop-os/softbuffer"
tag = "cosmic-4.0"
replace-with = "vendored-sources"

[source."git+https://github.com/pop-os/window_clipboard.git?tag=pop-0.13-2"]
git = "https://github.com/pop-os/window_clipboard.git"
tag = "pop-0.13-2"
replace-with = "vendored-sources"

[source."git+https://github.com/pop-os/winit.git?tag=iced-xdg-surface-0.13-rc"]
git = "https://github.com/pop-os/winit.git"
tag = "iced-xdg-surface-0.13-rc"
replace-with = "vendored-sources"

[source."git+https://github.com/wash2/accesskit?tag=iced-xdg-surface-0.13-rc"]
git = "https://github.com/wash2/accesskit"
tag = "iced-xdg-surface-0.13-rc"
replace-with = "vendored-sources"

EOF

%build
%rust_build 

%install
install -D target/release/%oname %buildroot%_bindir/%oname
install -Dm 0644 resources/%oname2.metainfo.xml %buildroot%_datadir/metainfo/%oname2.metainfo.xml
install -Dm 0644 resources/icons/hicolor/scalable/apps/%oname2.svg \
    %buildroot%_iconsdir/hicolor/scalable/apps/%oname2.svg
install -Dm 0644 resources/%oname2.desktop %buildroot%_desktopdir/%oname2.desktop

%files
%doc *.md LICENSE
%_bindir/%oname
%_desktopdir/%oname2.desktop
%_datadir/metainfo/%oname2.metainfo.xml
%_iconsdir/hicolor/scalable/apps/%oname2.svg

%changelog
* Mon Aug 24 2026 Aleksandr Shamaraev <shad@altlinux.org> 20260224-alt1
- Initial build.
