%global _unpackaged_files_terminate_build 1

%define appdir %_datadir/%name

Name: goose-desktop
Version: 1.44.0
Release: alt1
Summary: Desktop application for goose, an open source AI agent
License: Apache-2.0
Group: Development/Tools
Url: https://block.github.io/goose
VCS: https://github.com/block/goose

Source: %name-%version.tar
# The ui/ workspace with its dependency tree, resolved from ui/pnpm-lock.yaml by
# .gear/up.d/10-pnpm-install at `zoryn up` time, because the build chroot has no
# network.
Source1: ui-deps.tar

# The app runs off the shared Electron runtime rather than a bundle of its own,
# which Electron reports as default-app mode. Two places assume otherwise.
Patch1: alt-tray-icon-next-to-app.patch
Patch2: alt-no-devtools-autoinstall.patch

#BuildArch: noarch
#ExclusiveArch: x86_64 aarch64

ExcludeArch: i586

BuildRequires: node
BuildRequires: pnpm
# Not linked against, but electron-forge is pointed at this Electron
# distribution instead of downloading one - see %%build.
BuildRequires: electron
# Used in %%build to repack the Electron distribution for @electron/packager.
BuildRequires: zip

# The desktop app has no agent of its own: it spawns `goose serve` and talks ACP
# to it over loopback. The ACP surface is stable across CLI releases, so this is
# deliberately an unversioned dependency - the two packages may be updated
# independently.
Requires: goose
Requires: electron

%description
goose is your on-machine AI agent, capable of automating complex
development tasks from start to finish.

This package provides the desktop (Electron) front-end. It drives the
goose command-line agent, which it starts as a local ACP server.

%prep
%setup -a 1
%patch1 -p1
%patch2 -p1

# @electron/packager takes a local Electron distribution only through
# packagerConfig.electronZipDir, which upstream's forge config does not set and
# the CLI does not expose. ELECTRON_OVERRIDE_DIST_PATH does not help: that one is
# read by the electron npm package, not by the packager.
grep -q '^module.exports = {' ui/desktop/forge.config.ts
sed -i 's|^module.exports = {|cfg.electronZipDir = process.env.ALT_ELECTRON_ZIP_DIR;\n\nmodule.exports = {|' \
	ui/desktop/forge.config.ts
grep -q 'ALT_ELECTRON_ZIP_DIR' ui/desktop/forge.config.ts

%build
# Repack the packaged Electron under the name @electron/packager would have
# downloaded, so it unpacks that instead of reaching for github.com. Both the
# version and the architecture spelling have to match what the packager derives
# from the electron devDependency and from node, hence asking node rather than
# guessing. The distribution is thrown away again in %%install: only the
# application payload next to it is packaged.
#
# chrome-sandbox is left out: the electron package ships it setuid 4711 root, so
# an unprivileged build cannot even read it, and nothing we keep needs it.
electron_version=$(node -p "require('./ui/node_modules/electron/package.json').version")
electron_arch=$(node -p "process.arch")
mkdir -p electron-zip
(cd %_libdir/electron && \
	zip -qry "$OLDPWD/electron-zip/electron-v$electron_version-linux-$electron_arch.zip" . \
		-x ./chrome-sandbox)
export ALT_ELECTRON_ZIP_DIR="$PWD/electron-zip"

# @aaif/goose-sdk is a workspace dependency of the app and ships no dist/:
# upstream builds it from a postinstall hook, which never runs here because the
# dependency tree arrives unpacked rather than installed. Generate its
# TypeScript from the committed crates/goose/acp-{schema,meta}.json and compile
# it before the app build, or the renderer bundle fails to resolve the import.
(cd ui/sdk && ../node_modules/.bin/tsx generate-schema.ts && ../node_modules/.bin/tsc)

# Call the toolchain binaries directly rather than through `pnpm exec`: pnpm
# verifies node_modules against the workspace config before running anything,
# decides the committed tree is stale (the hook narrows supportedArchitectures
# for the install and restores the file afterwards) and tries to re-run
# `pnpm install`, which cannot work without network.
(cd ui/desktop && ../node_modules/.bin/electron-forge package)

%install
# Take only the application payload from the forge output; the Electron runtime
# next to it belongs to the electron package.
mkdir -p %buildroot%appdir
cp -a ui/desktop/out/*/resources/. %buildroot%appdir/

# Upstream's extraResource carries helper wrappers (jbang, node, npx, uvx) for
# the self-contained bundle it ships itself. Here they only pull bogus
# dependencies out of the script scanner - node, npx, even ImageMagick-tools -
# while the wrapper below points the app at the packaged goose and the system
# tools are the ones actually used. The directory is also where a packaged build
# would look for the agent binary, which is moot: this one is launched through
# /usr/bin/electron and resolves the CLI from $GOOSE_BINARY instead.
rm -rf %buildroot%appdir/bin

# inspector_overlay comes from the Electron distribution that %%build repacked
# for the packager, not from the app - it belongs to the electron package.
rm -rf %buildroot%appdir/inspector_overlay

# An upstream helper that regenerates the menu bar icons with ImageMagick at
# development time; shipping it only adds ImageMagick-tools and coreutils to the
# runtime dependencies.
rm -f %buildroot%appdir/images/prepare.sh

# findGooseBinaryPath() honours $GOOSE_BINARY whenever app.isPackaged is false,
# and it always is here: Electron reports "default app" mode when started with a
# path argument, which is exactly how the wrapper below launches us. That gives
# a clean way to point the app at the packaged CLI without patching it.
mkdir -p %buildroot%_bindir
cat > %buildroot%_bindir/%name <<EOF
#!/bin/sh
export GOOSE_BINARY=%_bindir/goose
exec %_bindir/electron %appdir/app.asar "\$@"
EOF
chmod 755 %buildroot%_bindir/%name

mkdir -p %buildroot%_desktopdir
cat > %buildroot%_desktopdir/%name.desktop <<EOF
[Desktop Entry]
Name=goose
Comment=On-machine AI agent
Exec=%_bindir/%name %%U
Icon=%name
Terminal=false
Type=Application
Categories=Development;
MimeType=x-scheme-handler/goose;
EOF

mkdir -p %buildroot%_iconsdir/hicolor/512x512/apps
install -pm644 ui/desktop/src/images/icon.png \
	%buildroot%_iconsdir/hicolor/512x512/apps/%name.png

%files
%_bindir/%name
%appdir/
%_desktopdir/%name.desktop
%_iconsdir/hicolor/512x512/apps/%name.png
%doc LICENSE

%changelog
* Wed Jul 29 2026 Alexey Shabalin <shaba@altlinux.org> 1.44.0-alt1
- Initial build for ALT.
