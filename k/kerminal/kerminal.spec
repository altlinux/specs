Name:    kerminal
Version: 2.6.5
Release: alt1

Summary: Modern Terminal Emulator & SSH Manager
License: GPL-3.0-or-later
Group:   Terminals
URL:     https://klpod221.com/kerminal/
VCS:     https://github.com/klpod221/kerminal

Source:  %name-%version.tar
Source1: %name-development-%version.tar

ExclusiveArch: x86_64

BuildRequires(pre): rpm-macros-rust
BuildRequires: rpm-build-rust node gcc pkg-config
BuildRequires: libwebkit2gtk4.1-devel libjavascriptcoregtk4.1-devel
BuildRequires: libssl-devel

%description
Kerminal is a modern, high-performance terminal emulator that combines the
power of a full-featured local terminal with advanced SSH connection
management. Built with security-first architecture using Tauri (Rust) for
native performance and Vue 3 for a responsive UI, Kerminal offers everything
from basic terminal operations to complex SSH workflows with encrypted
profile management, tunneling, and multi-device synchronization-all in a
beautiful native desktop application.

Perfect for developers, DevOps engineers, system administrators, and anyone
who lives in the terminal and values security, organization, and productivity.

%prep
%setup -a1
%rust_prep

%build
# Frontend: tauri embeds ../dist into the binary at compile time,
# so it must be built before cargo build
node node_modules/vite/bin/vite.js build

cd src-tauri
# --features tauri/custom-protocol is what `tauri build` passes implicitly:
# without it tauri sets cfg(dev) and the webview tries to load devUrl
# (http://localhost:1420) instead of the embedded frontend
# --bin Kerminal: skip the cdylib/staticlib crate-types, they are only
# needed for the mobile (Android/iOS) targets
export RUSTFLAGS="${RUSTFLAGS} -g"
cargo build --release %_smp_mflags --offline --features tauri/custom-protocol --bin Kerminal

%install
install -Dm755 src-tauri/target/release/Kerminal %buildroot%_bindir/%name

for size in 32x32 64x64 128x128; do
    install -Dm644 src-tauri/icons/$size.png \
        %buildroot%_iconsdir/hicolor/$size/apps/%name.png
done
install -Dm644 src-tauri/icons/icon.png \
    %buildroot%_iconsdir/hicolor/512x512/apps/%name.png

mkdir -p %buildroot%_desktopdir
cat > %buildroot%_desktopdir/%name.desktop <<'EOF'
[Desktop Entry]
Type=Application
Name=Kerminal
Comment=%summary
Exec=%name
Icon=%name
StartupWMClass=%name
Categories=System;TerminalEmulator;
EOF

%files
%doc LICENSE README.md
%_bindir/%name
%_desktopdir/%name.desktop
%_iconsdir/hicolor/*/apps/%name.png

%changelog
* Thu Aug 20 2026 Sergey Palcheh <minergenon@altlinux.org> 2.6.5-alt1
- Initial build for Sisyphus
