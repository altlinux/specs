%global handylibdir %_libdir/handy
%global handydatadir %_datadir/handy

Name: handy
Version: 0.9.5
Release: alt1

Summary: A speech-to-text application that works completely offline
License: MIT
Group: Accessibility
URL: https://handy.computer/
VCS: https://github.com/cjpais/Handy.git

Source0: %name-%version.tar
Source1: vendor.tar
Source2: node_modules.tar
Source3: ferrous-opencc.tar
Source4: transcribe-cpp-sys.tar
Source5: tauri-utils.tar
Source6: Cargo.lock
Source7: package-lock.json
Source8: handy.desktop
Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-macros-rust
BuildRequires: rpm-build-rust
BuildRequires: rpm-build-nodejs

BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: pkgconf
BuildRequires: glslang-devel
BuildRequires: glslc
BuildRequires: libdbus-devel
BuildRequires: libspirv-tools-devel
BuildRequires: libvulkan-devel
BuildRequires: spirv-headers
BuildRequires: libappindicator-gtk3
BuildRequires: libayatana-appindicator3-devel
BuildRequires: libgtk+3-devel
BuildRequires: libgtk-layer-shell-devel
BuildRequires: librsvg-devel
BuildRequires: libwebkit2gtk4.1-devel
BuildRequires: libalsa-devel
BuildRequires: libssl-devel
BuildRequires: libXi-devel
BuildRequires: libXtst-devel
BuildRequires: xdotool-devel
BuildRequires: node-typescript

#
# Use our libraries from the repository instead of vendored binaries and libraries
#
# Replace a vendored source from the transcribe-cpp-sys crate
BuildRequires: libllama-devel
# Replace a binary from the ort-sys crate
BuildRequires: libonnxruntime-devel

#
# Additional build-time dependencies
#
# Install and validate handy desktop file
BuildRequires: desktop-file-utils
# Generate and install handy man page
BuildRequires: help2man

ExcludeArch: %ix86

%description
Handy is a cross-platform desktop application that provides simple,
privacy-focused speech transcription. Press a shortcut, speak, and have
your words appear in any text field. This happens on your own computer
without sending any information to the cloud.

%prep
%setup -a1 -a2 -a3 -a4 -a5
%autopatch -p1
cp -vf %SOURCE6 src-tauri/Cargo.lock
cp -vf %SOURCE7 package-lock.json

pushd src-tauri
%rust_prep
cat >> .cargo/config.toml << EOF
[source."git+https://github.com/ahkohd/tauri-nspanel?branch=v2.1"]
git = "https://github.com/ahkohd/tauri-nspanel"
branch = "v2.1"
replace-with = "vendored-sources"

[source."git+https://github.com/cjpais/hf-hub?branch=cancellable-downloads"]
git = "https://github.com/cjpais/hf-hub"
branch = "cancellable-downloads"
replace-with = "vendored-sources"

[source."git+https://github.com/cjpais/rodio.git"]
git = "https://github.com/cjpais/rodio.git"
replace-with = "vendored-sources"

[source."git+https://github.com/cjpais/tao?rev=c3bee28c1d446d95f08c95c3b6f8d4bde052b876"]
git = "https://github.com/cjpais/tao"
rev = "c3bee28c1d446d95f08c95c3b6f8d4bde052b876"
replace-with = "vendored-sources"

[source."git+https://github.com/cjpais/vad-rs"]
git = "https://github.com/cjpais/vad-rs"
replace-with = "vendored-sources"

[source."git+https://github.com/rustdesk-org/rdev"]
git = "https://github.com/rustdesk-org/rdev"
replace-with = "vendored-sources"

[patch.crates-io]
ferrous-opencc = { path = "ferrous-opencc" }
transcribe-cpp-sys = { path = "transcribe-cpp-sys" }
tauri-utils = { path = "tauri-utils" }
EOF

# Use the `%%handylibdir` macro instead of hardened `/usr/lib`
sed -i 's|@HANDYLIBDIR@|%handylibdir|g' build.rs

# Use the `%%handydatadir` macro instead of hardened `/usr/lib/Handy/resources`
sed -i 's|@HANDYDATADIR@|%handydatadir|g' tauri-utils/src/platform.rs
popd

%build
export TAURI_SKIP_DEPS_CHECK=1
npm run build

pushd src-tauri
# Link with the system ggml instead of vendored library
export RUSTFLAGS="-C link-arg=-lggml"
# Link with the system onnx runtime instead of vendored binary
export ORT_STRATEGY=system
export ORT_LIB_LOCATION=%_libdir
export ORT_PREFER_DYNAMIC_LINK=1
%rust_build
popd

%install
pushd src-tauri
%rust_install

# Install handy runtime dependency
install -Dpm 0644 -t %buildroot%handylibdir/ transcribe-libs/*

# Install handy resources
mkdir -p %buildroot%handydatadir
cp -rv resources %buildroot%handydatadir

# Install handy icons
install -Dpm 0644 icons/32x32.png %buildroot%_niconsdir/%name.png
install -Dpm 0644 icons/128x128.png %buildroot%_iconsdir/hicolor/128x128/apps/%name.png
popd

# Install and validate desktop file
desktop-file-install --dir=%buildroot%_desktopdir %SOURCE8
desktop-file-validate %buildroot%_desktopdir/%name.desktop

# Generate and install man page
export LD_LIBRARY_PATH=%buildroot%handylibdir
mkdir -p %buildroot%_man1dir
help2man --no-discard-stderr \
	-N \
	-s 1 \
	--version-string %version \
	-o %buildroot%_man1dir/%name.1 \
	%buildroot%_bindir/%name

%files
%doc README.md
%_bindir/%name
%_desktopdir/%name.desktop
%handydatadir
%handylibdir
%_man1dir/%name.1.*
%_niconsdir/%name.png
%_iconsdir/hicolor/128x128/apps/%name.png

%changelog
* Wed Sep 02 2026 Ulysses Apokin <ulysses@altlinux.org> 0.9.5-alt1
- Initial build for Sisyphus.
