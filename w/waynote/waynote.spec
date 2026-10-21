%define cargo_prep %nil
%define cargo_build %rust_build
%define cargo_install %rust_install

Name: waynote
Version: 0.1.6
Release: alt1

Summary: Wayland-native Markdown sticky notes

License: MIT
Group: Office
URL: https://github.com/mryll/waynote
# Source-url: https://github.com/mryll/waynote/archive/refs/tags/v%version.tar.gz
Source: %name-%version.tar
Source1: %name-development-%version.tar
Source2: config.toml

BuildRequires(pre): rpm-macros-rust
BuildRequires: rpm-build-rust /proc
BuildRequires: libgtk4-devel libgtk4-layer-shell-devel

%description
Waynote displays Markdown sticky notes on a Wayland desktop using the
wlr-layer-shell protocol. Notes are stored as plain Markdown files and
refresh automatically when edited externally. The application supports
multiple monitors, colors, checkboxes, and a system tray icon.

%prep
%setup -a1
%cargo_prep
install -vD %SOURCE2 .cargo/config.toml

%build
%cargo_build

%install
install -Dm755 target/release/%name %buildroot%_bindir/%name
install -Dm644 assets/%name.svg %buildroot%_iconsdir/hicolor/scalable/apps/%name.svg
install -Dm644 packaging/%name.desktop %buildroot%_desktopdir/%name.desktop
install -Dm644 packaging/%name.service %buildroot%_userunitdir/%name.service

%check
%rust_test

%files
%_bindir/%name
%_desktopdir/%name.desktop
%_iconsdir/hicolor/scalable/apps/%name.svg
%_userunitdir/%name.service
%doc README.md LICENSE

%changelog
* Wed Oct 21 2026 Vitaly Lipatov <lav@altlinux.ru> 0.1.6-alt1
- initial build for ALT Linux.

