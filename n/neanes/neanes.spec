%define rust_debug 0
%define rust_lto "off"

Name: neanes
Version: 0.5.59
Release: alt1

Summary: Byzantine chant notation editor

License: GPL-3.0-only
Group: Sound
URL: https://github.com/neanes/neanes
# Source-url: https://github.com/neanes/neanes/archive/refs/tags/v%version.tar.gz
Source: %name-%version.tar
Source1: %name-development-%version.tar
# Build-only native modules; no native modules are installed in the RPM.
# Source2-url: https://github.com/tailwindlabs/tailwindcss/archive/refs/tags/v4.3.3.tar.gz
Source2: tailwindcss-4.3.3.tar
# Source3-url: https://github.com/parcel-bundler/lightningcss/archive/refs/tags/v1.32.0.tar.gz
Source3: lightningcss-1.32.0.tar
Source4: neanes.desktop
Source5: neanes.xml
Source6: copy-runtime.py

# Keep RPMs architecture-specific: the Electron runtime is not available on i586.
# The system Electron runtime is not built for 32-bit x86.
ExcludeArch: %ix86
AutoReq: yes,nonodejs,nonodejs_native,nomono
AutoReq: nopython,nolua,nomingw32,nomingw64,noshebang

BuildRequires(pre): rpm-macros-rust
BuildRequires: npm /proc electron rpm-build-rust
BuildRequires: rolldown rollup esbuild node-typescript node-parcel-watcher python3
BuildRequires: desktop-file-utils

%description
Neanes is a scorewriter for notating Byzantine chant. It supports rapid
entry of neumes and multilingual lyrics, automatic alignment and line
breaking, printing, and export to PDF, HTML, PNG and MusicXML.

%prep
%setup -a1 -a2 -a3
# Native builders use the host compiler instead of upstream cross-linker names.
sed -i '/^linker = /d' lightningcss/.cargo/config.toml
# Use the architecture-independent JavaScript interfaces to system build tools.
rm -rf node_modules/rolldown node_modules/rollup node_modules/typescript node_modules/@parcel/watcher
ln -s /usr/lib/node_modules/rolldown node_modules/rolldown
ln -s /usr/lib/node_modules/rollup node_modules/rollup
ln -s /usr/lib/node_modules/typescript node_modules/typescript
mkdir -p node_modules/@parcel
ln -s /usr/lib/node_modules/@parcel/watcher node_modules/@parcel/watcher
for module in tailwindcss lightningcss; do
    mkdir -p "$module/.cargo"
    cat >> "$module/.cargo/config.toml" <<EOF
[source.crates-io]
replace-with = "vendored-sources"
[source.vendored-sources]
directory = "$(pwd)/node_modules/.cargo-vendor-$module"
EOF
done

%build
export PATH="$PWD/node_modules/.bin:$PATH"
export ESBUILD_BINARY_PATH=/usr/bin/esbuild
pushd tailwindcss
%rust_build --locked -p tailwind-oxide
popd
pushd lightningcss
%rust_build --locked -p lightningcss_node
popd
node_arch=$(node -p process.arch)
cp tailwindcss/target/release/libtailwind_oxide.so \
    "node_modules/@tailwindcss/oxide/tailwindcss-oxide.linux-$node_arch-gnu.node"
cp lightningcss/target/release/liblightningcss_node.so \
    "node_modules/lightningcss/lightningcss.linux-$node_arch-gnu.node"
# Do not let Tailwind scan the build-only Rust workspaces for CSS candidates.
rm -rf tailwindcss lightningcss
vue-tsc --noEmit
# Use ALT's esbuild for final CSS minification instead of Vite's additional
# optional native Lightning CSS dependency.
# Inline the bundled OpenType faces so the file:// application does not need
# separate font requests, which fail in the system Electron renderer.
node --input-type=module <<'JS'
import { build } from 'vite';
await build({
  build: {
    cssMinify: false,
    assetsInlineLimit: (filePath) => filePath.endsWith('.otf') ? true : undefined,
  },
});
JS
/usr/bin/esbuild dist/assets/*.css --minify --outdir=dist/assets --allow-overwrite
mkdir runtime
cp -a dist dist-electron package.json runtime/
python3 %SOURCE6

%check
desktop-file-validate %SOURCE4
test -s runtime/dist/index.html
test -s runtime/dist-electron/main/index.js
test -s runtime/dist-electron/preload/index.js
test -z "$(find runtime -name '*.node' -print -quit)"

%install
mkdir -p %buildroot%_datadir/%name
cp -a runtime/. %buildroot%_datadir/%name/
mkdir -p %buildroot%_bindir
cat > %buildroot%_bindir/%name <<'EOF'
#!/bin/sh
exec /usr/bin/electron %_datadir/neanes --no-update "$@"
EOF
chmod 755 %buildroot%_bindir/%name
install -Dm644 %SOURCE4 %buildroot%_desktopdir/%name.desktop
install -Dm644 %SOURCE5 %buildroot%_datadir/mime/packages/%name.xml
for icon in build/icons/*.png; do
    size=$(basename "$icon" .png)
    install -Dm644 "$icon" %buildroot%_iconsdir/hicolor/"$size"/apps/%name.png
done

%files
%doc README.md LICENSE examples
%_bindir/%name
%_datadir/%name/
%_desktopdir/%name.desktop
%_datadir/mime/packages/%name.xml
%_iconsdir/hicolor/*/apps/%name.png

%changelog
* Fri Nov 13 2026 Vitaly Lipatov <lav@altlinux.ru> 0.5.59-alt1
- initial build for ALT Sisyphus
- exclude 32-bit x86 (system Electron is unavailable).

