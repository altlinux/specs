%define _unpackaged_files_terminate_build 1
%define app_id com.vscodium.codium
%define ms_commit 08d4889f9ec4a1685d257b9b95de036c8e1ce1e5
%ifarch x86_64
%define vscode_arch x64
%endif
%ifarch aarch64
%define vscode_arch arm64
%endif
%define vscode_output VSCode-linux-%vscode_arch

Name: codium
Version: 1.135.06055
Release: alt1

Summary: Community build of the Visual Studio Code editor
License: MIT
Group: Development/Other
Url: https://vscodium.com/
VCS: https://github.com/VSCodium/vscodium.git

Source0: %name-%version.tar
Source1: %name-%version-predownloaded.tar.zst
Patch0: offline-build.patch
Patch1: system-electron.patch

ExcludeArch: %ix86

BuildRequires: /proc
BuildRequires: gcc-c++
BuildRequires: make
BuildRequires: pkg-config
BuildRequires: python3
BuildRequires: node
BuildRequires: node-devel
BuildRequires: node-gyp
BuildRequires: npm
BuildRequires: git-core
BuildRequires: jq
BuildRequires: patchelf
BuildRequires: ripgrep
BuildRequires: zip
BuildRequires: electron
BuildRequires: libcurl4-openssl
BuildRequires: libkrb5-devel
BuildRequires: libsecret
BuildRequires: libwebkit2gtk4.1
BuildRequires: libX11-devel
BuildRequires: libxkbfile-devel

Requires: electron

%add_findprov_skiplist %_libdir/%name/resources/app/node_modules/*
%add_findreq_skiplist %_libdir/%name/resources/app/node_modules/*

%description
VSCodium is a community build of Visual Studio Code with the VSCodium
product configuration and Open VSX extension registry.

%prep
%setup -a1
%autopatch -p1

test "$(jq -r .commit upstream/stable.json)" = "%ms_commit"

%build
export GLOBAL_DIRNAME=codium
export OS_NAME=linux
export VSCODE_QUALITY=stable
export VSCODE_ARCH=%vscode_arch
export RELEASE_VERSION=%version
export DISABLE_UPDATE=yes
export BUILD_SOURCEVERSION=%ms_commit
export MAX_OLD_SPACE_SIZE=8192

export npm_config_offline=true

. ./prepare_vscode.sh

# Recreate the release VSIX files from unpacked sources and register them.
mkdir -p vscode/.build-vsix
for source in vscode/.build-vsix-sources/*; do
    metadata="$source/extension/package.json"
    extension=$(jq -er '.publisher + "." + .name' "$metadata")
    version=$(jq -er .version "$metadata")
    vsix="$extension.$version.vsix"
    (cd "$source" && zip -q -r "../../.build-vsix/$vsix" .)
    hash=$(sha256sum "vscode/.build-vsix/$vsix" | cut -d' ' -f1)
    jq --arg extension "$extension" --arg vsix "$vsix" --arg hash "$hash" '
        (.builtInExtensions[] | select(.name == $extension)) += {
            vsix: (".build-vsix/" + $vsix), sha256: $hash
        }' vscode/product.json > vscode/product.json.new
    mv vscode/product.json.new vscode/product.json
done

pushd vscode
for module in \
    @parcel/watcher \
    @vscode/native-watchdog \
    @vscode/spdlog \
    @vscode/sqlite3 \
    @vscodium/native-keymap \
    @vscodium/policy-watcher \
    kerberos; do
    (cd "node_modules/$module" && node-gyp configure && node-gyp build)
done
npm run gulp vscode-min-prepack
rm -f .build/extensions/ms-vscode.js-debug/src/win32-app-container-tokens.*.node
npm run copy-policy-dto --prefix build
node build/lib/policies/policyGenerator.ts build/lib/policies/policyData.jsonc linux
npm run gulp vscode-linux-%vscode_arch-min-packing
popd

%install
install -d %buildroot%_libdir/%name/resources %buildroot%_bindir
cp -a %vscode_output/resources/app %buildroot%_libdir/%name/resources/
appdir=%buildroot%_libdir/%name/resources/app

# Microsoft's authentication runtime uses the OpenSSL flavor of libcurl.
%ifarch x86_64
patchelf --replace-needed libcurl.so.4 libcurl-openssl.so.4 \
    "$appdir/extensions/microsoft-authentication/dist/libmsalruntime.so"
%endif

find "$appdir/node_modules.asar.unpacked/node-pty/prebuilds" \
    -mindepth 1 -maxdepth 1 ! -name linux-%vscode_arch -exec rm -rf -- {} +
find "$appdir/node_modules.asar.unpacked/@vscode/ripgrep-universal/bin" \
    -mindepth 1 -maxdepth 1 -type d ! -name linux-%vscode_arch -exec rm -rf -- {} +
find "$appdir/node_modules.asar.unpacked/@microsoft/mxc-sdk/bin" \
    -mindepth 1 -maxdepth 1 ! -name %vscode_arch -exec rm -rf -- {} +
find "$appdir/node_modules.asar.unpacked/@microsoft/mxc-sdk/bin/%vscode_arch" \
    -type f \( -name '*.exe' -o -name '*-mac' \) -delete

%ifarch aarch64
for helper in lxc-exec linux-test-proxy; do
    patchelf --set-interpreter /lib64/ld-linux-aarch64.so.1 \
        "$appdir/node_modules.asar.unpacked/@microsoft/mxc-sdk/bin/arm64/$helper"
done
%endif

cat > %buildroot%_bindir/codium <<'SH'
#!/bin/sh
ELECTRON_RUN_AS_NODE=1 exec %_bindir/electron \
    %_libdir/%name/resources/app/out/cli.js "$@"
SH
chmod 755 %buildroot%_bindir/codium
ln -s codium %buildroot%_bindir/vscodium

sed -e 's|@@NAME_LONG@@|VSCodium|g' \
    -e 's|@@EXEC@@|/usr/bin/codium|g' \
    -e 's|@@ICON@@|codium|g' \
    -e 's|@@NAME_SHORT@@|VSCodium|g' \
    -e 's|@@NAME@@|codium|g' \
    src/stable/resources/linux/code.desktop > %app_id.desktop
install -Dm644 %app_id.desktop %buildroot%_desktopdir/%app_id.desktop

sed -e 's|@@NAME_LONG@@|VSCodium|g' \
    -e 's|@@EXEC@@|/usr/bin/codium|g' \
    -e 's|@@ICON@@|codium|g' \
    -e 's|@@URLPROTOCOL@@|vscodium|g' \
    src/stable/resources/linux/code-url-handler.desktop > codium-url-handler.desktop
install -Dm644 codium-url-handler.desktop %buildroot%_desktopdir/codium-url-handler.desktop

sed -e 's|@@NAME@@|com.vscodium.codium|g' \
    -e 's|@@LICENSE@@|MIT|g' \
    -e 's|@@NAME_LONG@@|VSCodium|g' \
    src/stable/resources/linux/code.appdata.xml > %app_id.metainfo.xml
install -Dm644 %app_id.metainfo.xml %buildroot%_datadir/metainfo/%app_id.metainfo.xml
install -Dm644 src/stable/resources/linux/code.svg \
    %buildroot%_iconsdir/hicolor/scalable/apps/codium.svg

%check
app="$PWD/%vscode_output/resources/app"
test "$(ELECTRON_RUN_AS_NODE=1 /usr/bin/electron "$app/out/cli.js" --version | head -n1)" = "%version"

for native in \
    @parcel/watcher/build/Release/watcher.node \
    @vscode/native-watchdog/build/Release/watchdog.node \
    @vscode/spdlog/build/Release/spdlog.node \
    @vscode/sqlite3/build/Release/vscode-sqlite3.node \
    @vscodium/native-keymap/build/Release/keymapping.node \
    @vscodium/policy-watcher/build/Release/vscodium-policy-watcher.node \
    kerberos/build/Release/kerberos.node \
    @vscode/os-proxy-resolver-linux-%vscode_arch-gnu/os_proxy_resolver.node \
    node-pty/prebuilds/linux-%vscode_arch/pty.node; do
    ELECTRON_RUN_AS_NODE=1 /usr/bin/electron -e \
        'require(process.argv[1])' "$app/node_modules.asar.unpacked/$native"
done

%files
%doc LICENSE README.md
%_bindir/codium
%_bindir/vscodium
%_libdir/%name/resources/app
%_desktopdir/%app_id.desktop
%_desktopdir/codium-url-handler.desktop
%_iconsdir/hicolor/scalable/apps/codium.svg
%_datadir/metainfo/%app_id.metainfo.xml

%changelog
* Tue Sep 29 2026 Grant Makyan <karonus@altlinux.org> 1.135.06055-alt1
- Update to VSCodium 1.135.06055.
- Use system Electron runtime.
- Add aarch64 build support.

* Tue Aug 05 2025 Semen Fomchenkov <armatik@altlinux.org> 1.101.14098-alt2
- Use patchelf for change interpreter.

* Wed Jun 25 2025 Semen Fomchenkov <armatik@altlinux.org> 1.101.14098-alt1
- 1.101.14098

* Tue Apr 22 2025 Semen Fomchenkov <armatik@altlinux.org> 1.99.32562-alt1
- 1.99.32562

* Fri Feb 14 2025 Semen Fomchenkov <armatik@altlinux.org> 1.97.2.25045-alt1
- 1.97.2.25045
- add url-handler .desktop file

* Sat Feb 01 2025 Semen Fomchenkov <armatik@altlinux.org> 1.96.4.25026-alt2
- add Wayland support (Closes: 47792)
- add appstream-data (Closes: 52900)
- remove gitlab-ci dependency (Closes: 52896)
- new .svg icon instead of the old .png
- add Vcs tag to spec-file (Closes: 52899)

* Thu Jan 30 2025 Semen Fomchenkov <armatik@altlinux.org> 1.96.4.25026-alt1
- new version (1.96.4.25026) (Closes: 50953, 52311)
- drop arm-32bit version

* Sun Sep 10 2023 Evgeniy Kukhtinov <neurofreak@altlinux.org> 1.82.0.23250-alt1
- new version (1.82.0.23250) (Closes: 46710)

* Thu Oct 13 2022 Evgeniy Kukhtinov <neurofreak@altlinux.org> 1.72.1.22284-alt1
-  new version (1.72.1.22284) (Closes: 43921)

* Mon Aug 08 2022 Evgeniy Kukhtinov <neurofreak@altlinux.org> 1.70.0-alt1
- new version (1.70.0)

* Fri Jun 03 2022 Evgeniy Kukhtinov <neurofreak@altlinux.org> 1.67.2-alt1
- new version (1.67.2)
- added Provides: vscodium

* Thu Apr 28 2022 Evgeniy Kukhtinov <neurofreak@altlinux.org> 1.66.2-alt1
- changed build from source to packing from binaries
- new version (1.66.2) ALT #42144

* Sat Mar 05 2022 Evgeniy Kukhtinov <neurofreak@altlinux.org> 1.63.2-alt2
- set ExclusiveArch: x86_64

* Sat Mar 05 2022 Evgeniy Kukhtinov <neurofreak@altlinux.org> 1.63.2-alt1
- initial version (1.63.2) with rpmgs script
  + import sources from codium-1.63.2.tar
  + import sources from code-1.63.2.tar
  + workaround "python: command not found" error
  + workaround "Error: Command failed: git config pull.rebase merges"
  + add predownloaded node_modules for vscode
  + add predownloaded node_modules for extensions
  + disable download marketplace builtin extensions during the build
  + workaround to download electron and ffmpeg
  + fixed aarch64 and armh packing
  + sandbox mode is disabled to avoid a startup error
  + add icons and desktop files
  + packing README.md
