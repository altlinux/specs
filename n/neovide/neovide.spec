%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1

Name: neovide
Version: 0.16.2
Release: alt1

Summary: No Nonsense Neovim Gui
License: MIT
Group: Editors
Url: https://neovide.dev/
Vcs: https://github.com/neovide/neovide

Source0: %name-%version.tar
Source1: %name-%version-vendor.tar
Source2: skia-m145-0.92.0.tar
Source3: wuffs-e3f919ccfe3ef542cfc983a82146070258fb57f8.tar
Source4: cargo-config.toml
Patch0: %name-%version-alt.patch

# from website/docs/installation.md
Requires: neovim >= 0.10

BuildRequires: rust-cargo
BuildRequires: python3
BuildRequires: clang-devel
BuildRequires: gcc-c++
BuildRequires: gn
BuildRequires: ninja-build
BuildRequires: pkg-config
BuildRequires: libexpat-devel
BuildRequires: libicu-devel
BuildRequires: fontconfig-devel
BuildRequires: libfreetype-devel
BuildRequires: libharfbuzz-devel
BuildRequires: libjpeg-devel
BuildRequires: libpng-devel
BuildRequires: zlib-devel

%description
This is a simple graphical user interface for Neovim (an aggressively refactored
and updated Vim editor). Where possible there are some graphical improvements,
but functionally it should act like the terminal UI.

To checkout all the cool features, installation instructions, configuration
settings and much more, head on over to https://neovide.dev.

%prep
%setup -a1 -a2 -a3
%autopatch -p1
[ -d .cargo ] || mkdir -p .cargo
cat %_sourcedir/cargo-config.toml >> .cargo/config.toml

# just for pretty for in %%install
mv assets/neovide-1024.png assets/neovide-1024x1024.png

%build
export SKIA_SOURCE_DIR="$PWD/skia"
export SKIA_GN_COMMAND=gn
export SKIA_NINJA_COMMAND=ninja
export SKIA_USE_SYSTEM_LIBRARIES=true
%ifarch i586
export SKIA_GN_ARGS='target_cpu="x86"'
%endif
%ifarch loongarch64
export SKIA_GN_ARGS='target_cpu="loong64"'
%endif
export CARGO_PROFILE_RELEASE_LTO=thin
export CARGO_PROFILE_RELEASE_OPT_LEVEL=3
export CARGO_PROFILE_RELEASE_CODEGEN_UNITS=1
export CARGO_PROFILE_RELEASE_DEBUG=true
export CARGO_PROFILE_RELEASE_STRIP=none
cargo build --release %{?_smp_mflags} --offline --verbose

%install
install -vpDm0755 target/release/neovide -t %buildroot%_bindir
install -vpDm0644 assets/neovide.desktop -t %buildroot%_desktopdir
install -vpDm0644 assets/neovide.svg -t %buildroot%_iconsdir/hicolor/scalable/apps
for size in 16 32 48 256 1024; do
    install -vpDm0644 "assets/neovide-${size}x${size}.png" \
        "%buildroot%_iconsdir/hicolor/${size}x${size}/apps/neovide.png"
done

%files
%_bindir/neovide
%_desktopdir/neovide.desktop
%_iconsdir/hicolor/*/apps/neovide.*

%changelog
* Tue Oct 27 2026 Anton Zhukharev <ancieg@altlinux.org> 0.16.2-alt1
- Packaged for ALT Sisyphus.
