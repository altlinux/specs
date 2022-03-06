Name:    codium
Version: 1.63.2
Release: alt2

Summary: Visual Studio Code without MS branding/telemetry/licensing

License: MIT 
Group:   Development/Other
Url:     https://github.com/VSCodium/vscodium

# Source0-url:  https://github.com/VSCodium/vscodium/archive/refs/tags/%{version}.tar.gz
Source0: %name-%version.tar

# Source1-url: https://github.com/microsoft/vscode/archive/refs/tags/%{version}.tar.gz
Source1: code-%version.tar

# sources predownloaded for offline build
#
# predownload vscode/node_modules and vscode/build/node_modules
# $ cd vscode
# $ yarn install
# $ yarn add vscode-gulp-watch esbuild
# $ cp ../vscode/node_modules $alt_git_codium_repository/.gear/predownloaded_sources/
# $ cd vscode/build
# $ cp ../vscode/build/node_modules $alt_git_codium_repository/.gear/predownloaded_sources/build/node_modules
#
# predownload node_modules for vscode/extensions
# $ cd vscode
# $ yarn add markdown-it
#
# then added to .gear/predownloded_sources/extensions by script(Thanx @gbIMoBou):
#
# #!/bin/bash
#
# VERSION="current_version"
#
# BASE="home_dir"
# BUILDROOT_EXT=$BASE/hasher/chroot/usr/src/RPM/BUILD/codium-$VERSION/vscode/extensions
# GIT_EXT=$BASE/sources/codium/.gear/predownloaded_sources/extensions
# SUBDIR=node_modules
#
# for SRC in `find $BUILDROOT_EXT -type d -name "$SUBDIR" | sed "s|^.*$BUILDROOT_EXT||;s|$SUBDIR.*||" | uniq`; do
# 	TGT=$GIT_EXT/$SRC
# 	mkdir -p $TGT
#	cp -rf $BUILDROOT_EXT/$SRC/$SUBDIR $TGT
# done
# end of script
#
# predownload $HOME/.cache/electron while online build
# $ cd vscode
# $ yarn gulp vscode-linux-x64-min-ci
# $ yarn gulp vscode-linux-armhf-min-ci
# $ yarn gulp vscode-linux-arm64-min-ci
# $ cp -r $build_home_dir/.cache/electron $alt_git_codium_repository/.gear/predownloaded_sources/electron
Source2: %name-predownloaded_sources-%version.tar

Source3: codium.desktop
Source4: codium.png

# disable download marketplace builtin extensions during the build
Patch1: vscode-marketplace-extensions-download-disabling.patch

# disable download electron 
Patch2: electron-download-disable.patch

BuildRequires: npm
BuildRequires: yarn
BuildRequires: node-gyp
BuildRequires: libX11-devel
BuildRequires: libxkbfile-devel
BuildRequires: gcc-c++
BuildRequires: python3-base
BuildRequires: libsecret-devel
BuildRequires: jq
BuildRequires: libxshmfence-devel
BuildRequires: libnss
BuildRequires: libnspr
BuildRequires: libatk-devel
BuildRequires: at-spi2-atk-devel
BuildRequires: libdbus-devel
BuildRequires: libdrm-devel
BuildRequires: libgdk-pixbuf-devel
BuildRequires: libgtk+3-devel
BuildRequires: libpango-devel
BuildRequires: libcairo-devel
BuildRequires: libXcomposite-devel
BuildRequires: libXdamage-devel
BuildRequires: libXext-devel
BuildRequires: libXfixes-devel
BuildRequires: libXrandr-devel
BuildRequires: libxkbcommon-devel
BuildRequires: libgbm-devel
BuildRequires: libalsa-devel
BuildRequires: libat-spi2-core-devel
BuildRequires: libcups-devel
BuildRequires: /proc

ExclusiveArch: x86_64

%description
Community-driven, freely-licensed binary distribution of Microsoft's editor VSCode
without MS branding/telemetry/licensing.
Visual Studio Code is a new choice of tool that combines the simplicity
of a code editor with what developers need for the core edit-build-debug cycle.
See FAQ at https://code.visualstudio.com/docs/setup/linux .

%prep
%setup -a1 -a2

mv code-%version vscode

# workaround error: /bin/sh: python: command not found
# choose python3 to build
mv .npmrc vscode/

# workaround "Error: Command failed: git config pull.rebase merges"
# see https://github.com/microsoft/vscode/issues/133544
sed -i "/cp.execSync('git config pull.rebase merges');/d" vscode/build/npm/postinstall.js
sed -i "/cp.execSync('git config blame.ignoreRevsFile .git-blame-ignore');/d" vscode/build/npm/postinstall.js

# add predownloaded node_modules for vscode
mv node_modules vscode/node_modules
mv build/node_modules vscode/build/node_modules
# disable node_modules preinstall
sed -i -e 's/yarn --frozen-lockfile//g' prepare_vscode.sh

# add predownloaded node_modules for extensions
for SRC in `find extensions -type d -name "node_modules" | sed "s|^.*extensions||;s|node_modules.*||" | uniq`; do
	TGT=vscode/extensions/$SRC
	mkdir -p $TGT
	cp -rf extensions/$SRC/node_modules $TGT
done
rm -rf extensions

# disable download marketplace builtin extensions during the build
%patch1 -p1

# workaround to download electron and ffmpeg
%patch2 -p1
mv electron $HOME/.cache/electron

%build
%ifarch x86_64
    _vscode_arch=x64
%endif
%ifarch aarch64
    _vscode_arch=arm64
%endif
%ifarch armh
    _vscode_arch=arm
%endif

# Export some environment variables
export SHOULD_BUILD="yes"
export VSCODE_ARCH="${_vscode_arch}"
export OS_NAME="linux"
export LATEST_MS_COMMIT=$(git rev-list --tags --max-count=1)
export LATEST_MS_TAG=$(git describe --tags "${LATEST_MS_COMMIT}")

# Disable building rpm, deb, and AppImage packages
export SKIP_LINUX_PACKAGES="True"

# build script
./build.sh

%install
mkdir -p %buildroot%_libdir/%name/
%ifarch x86_64
	cp -r %_builddir/%name-%version/VSCode-linux-x64/* %buildroot%_libdir/%name/
%endif
%ifarch aarch64
	cp -r %_builddir/%name-%version/VSCode-linux-arm64/* %buildroot%_libdir/%name/
%endif
%ifarch armh
	cp -r %_builddir/%name-%version/VSCode-linux-armhf/* %buildroot%_libdir/%name/
%endif
mkdir -p %buildroot%_bindir/
# sandbox mode is disabled to avoid a startup error
sed -i -e 's|ELECTRON_RUN_AS_NODE=1 "$ELECTRON" "$CLI" --ms-enable-electron-run-as-node "$@"|ELECTRON_RUN_AS_NODE=1 "$ELECTRON" "$CLI" --ms-enable-electron-run-as-node --no-sandbox "$@"|g' %buildroot%_libdir/%name/bin/codium
ln -rs %buildroot%_libdir/%name/bin/codium %buildroot/%_bindir/codium
ln -rs %buildroot%_libdir/%name/bin/codium %buildroot/%_bindir/vscodium

install -m644 -D %SOURCE3 %buildroot%_desktopdir/%name.desktop
install -m644 -D %SOURCE4 %buildroot%_pixmapsdir/codium.png

%files
%doc README.md
%_bindir/%name
%_bindir/vs%name
%_libdir/%name/
%_desktopdir/%name.desktop
%_pixmapsdir/codium.png 

%changelog
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

