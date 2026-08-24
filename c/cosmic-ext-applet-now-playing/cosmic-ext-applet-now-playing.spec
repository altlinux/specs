%define _unpackaged_files_terminate_build 1
%define oname com.github.DiegoMMR.CosmicExtAppletNowPlaying

Name: cosmic-ext-applet-now-playing
Version: 0.2.0
Release: alt1

Summary: A small COSMIC panel applet that shows what is currently playing
License: GPL-3.0-only
Group: Graphical desktop/Other

Url: https://github.com/cosmic-utils/cosmic-ext-applet-now-playing
VCS: https://github.com/cosmic-utils/cosmic-ext-applet-now-playing

Source0: %name-%version.tar
Source1: vendor.tar

BuildRequires(pre): rpm-macros-rust
BuildRequires: rpm-build-rust
BuildRequires: libxkbcommon-devel
BuildRequires: pkgconfig(dbus-1)

%description
A small COSMIC panel applet that shows what is currently playing via MPRIS.

It displays:

- Current track title and artist in the panel.
- A popup with album art and media controls.
- Album-color inspired panel button styling.

%prep
%setup -a1
%rust_prep
cat >> .cargo/config.toml <<EOF

[source."git+https://github.com/iced-rs/cryoglyph.git?rev=e429a025df36ab8145708acb309080ae3deec17a"]
git = "https://github.com/iced-rs/cryoglyph.git"
rev = "e429a025df36ab8145708acb309080ae3deec17a"
replace-with = "vendored-sources"

[source."git+https://github.com/jackpot51/rust-atomicwrites"]
git = "https://github.com/jackpot51/rust-atomicwrites"
replace-with = "vendored-sources"

[source."git+https://github.com/pop-os/cosmic-panel"]
git = "https://github.com/pop-os/cosmic-panel"
replace-with = "vendored-sources"

[source."git+https://github.com/pop-os/cosmic-protocols?rev=32283d7"]
git = "https://github.com/pop-os/cosmic-protocols"
rev = "32283d7"
replace-with = "vendored-sources"

[source."git+https://github.com/pop-os/dbus-settings-bindings"]
git = "https://github.com/pop-os/dbus-settings-bindings"
replace-with = "vendored-sources"

[source."git+https://github.com/pop-os/freedesktop-icons"]
git = "https://github.com/pop-os/freedesktop-icons"
replace-with = "vendored-sources"

[source."git+https://github.com/pop-os/libcosmic.git"]
git = "https://github.com/pop-os/libcosmic.git"
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
%rust_install
install -Dm 0644 res/%oname.metainfo.xml %buildroot%_datadir/metainfo/%oname.metainfo.xml
install -Dm 0644 res/icons/hicolor/48x48/apps/%oname.svg \
    %buildroot%_iconsdir/hicolor/48x48/apps/%oname.svg
install -Dm 0644 res/%oname.desktop %buildroot%_desktopdir/%oname.desktop

%files
%doc *.md LICENSE
%_bindir/%name
%_datadir/metainfo/%oname.metainfo.xml
%_iconsdir/hicolor/48x48/apps/%oname.svg
%_desktopdir/%oname.desktop

%changelog
* Mon Aug 24 2026 Aleksandr Shamaraev <shad@altlinux.org> 0.2.0-alt1
- Initial build.

