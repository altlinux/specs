Name: cc-switch
Version: 4.0.25
Release: alt1

Summary: All-in-One Assistant for Claude Code, Codex and Gemini CLI

License: MIT
Group: Development/Other
# Rollup (via Vite) ships native bindings only for x86_64 and aarch64;
# there is no linux-ia32 build, so i586 cannot build the frontend.
ExcludeArch: %{ix86}
URL: https://github.com/farion1231/cc-switch

# Source-url: https://github.com/farion1231/cc-switch/archive/refs/tags/v%version.tar.gz
Source: %name-%version.tar
Source1: %name-development-%version.tar
Source2: %name-node-%version.tar

BuildRequires(pre): rpm-macros-rust
BuildRequires: rpm-build-rust /proc
BuildRequires: /usr/bin/node
BuildRequires: libwebkit2gtk4.1-devel libsoup3.0-devel
BuildRequires: libayatana-appindicator3-devel
BuildRequires: libgtk+3-devel libcairo-devel libpango-devel libgdk-pixbuf-devel
BuildRequires: libssl-devel
BuildRequires: pkg-config

# Tauri dlopens libayatana-appindicator3.so.1 for the tray icon at runtime;
# auto-deps don't catch dlopened libs, so declare it explicitly.
Requires: libayatana-appindicator3-1

%description
CC Switch is a cross-platform desktop app for managing and switching provider
configurations for Claude Code, Codex, Gemini CLI, and other AI coding agents.

Features:
- Manage multiple provider configurations and endpoints
- One-click switch and sync to client live configurations
- MCP servers and Prompt/Skills management

%prep
%setup -a1 -a2

# Remove rust-toolchain pin (use system rust)
rm -f rust-toolchain.toml

# Set up cargo vendor config (old format, not config.toml)
mkdir -p .cargo
cat > .cargo/config <<'EOF'
[source.crates-io]
replace-with = "vendored-sources"

[source.vendored-sources]
directory = "vendor"
EOF

%build
# Fix for static linking issues (from AUR)
unset CFLAGS CXXFLAGS LDFLAGS

# Upstream [profile.release] has strip="symbols" and debug=false by default,
# which yields an empty -debuginfo subpackage. Override via env (don't mutate
# Cargo.toml): emit debug info and let the RPM find-debuginfo stage split it off
# and strip the main binary.
export CARGO_PROFILE_RELEASE_DEBUG=true
export CARGO_PROFILE_RELEASE_STRIP=none

export PATH=$(pwd)/node_modules/.bin:$PATH

# Build frontend (vite build -> dist/)
vite build

# Build Rust binary with embedded frontend
# tauri/custom-protocol enables embedded-asset serving via tauri://localhost
cargo build --release --manifest-path src-tauri/Cargo.toml \
    --bin cc-switch --features tauri/custom-protocol

%install
install -Dm755 src-tauri/target/release/cc-switch %buildroot%_bindir/cc-switch

# Icons
install -Dm644 src-tauri/icons/32x32.png %buildroot%_iconsdir/hicolor/32x32/apps/com.ccswitch.desktop.png
install -Dm644 src-tauri/icons/128x128.png %buildroot%_iconsdir/hicolor/128x128/apps/com.ccswitch.desktop.png
install -Dm644 src-tauri/icons/128x128@2x.png %buildroot%_iconsdir/hicolor/256x256/apps/com.ccswitch.desktop.png

# Desktop file
install -Dm644 flatpak/com.ccswitch.desktop.desktop %buildroot%_desktopdir/com.ccswitch.desktop.desktop

# Metainfo
install -Dm644 flatpak/com.ccswitch.desktop.metainfo.xml %buildroot%_datadir/metainfo/com.ccswitch.desktop.metainfo.xml

%files
%_bindir/cc-switch
%_iconsdir/hicolor/*/apps/com.ccswitch.desktop.png
%_desktopdir/com.ccswitch.desktop.desktop
%_datadir/metainfo/com.ccswitch.desktop.metainfo.xml
%doc LICENSE

%changelog
* Thu Nov 05 2026 Vitaly Lipatov <lav@altlinux.ru> 4.0.25-alt1
- New version 4.0.25

* Sat Jul 04 2026 Vitaly Lipatov <lav@altlinux.ru> 3.16.5-alt1
- Initial build for ALT Sisyphus

