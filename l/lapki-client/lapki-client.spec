%define _unpackaged_files_terminate_build 1
%define electron_ver 28

Name:    lapki-client
Version: 0.6.0
Release: alt1
Summary: The client part of Lapki IDE
Summary(ru_RU.UTF-8): Клиентская часть Lapki IDE
License: GPL-3.0-or-later
Group:   Development/Tools
Url:     https://github.com/kruzhok-team/lapki-client

Source0: %name-%version.tar
Source1: node_modules.tar.xz
Source2: lapki-compiler.tar
Source3: docserver.tar

ExclusiveArch: x86_64

BuildRequires(pre): rpm-build-nodejs

BuildRequires: nodejs 
BuildRequires: electron%electron_ver 
BuildRequires: desktop-file-utils

Requires: electron%electron_ver 
Requires: avrdude 
Requires: nodejs

AutoReq: no
AutoProv: no
%set_verify_elf_method unresolved=ignore
%add_findreq_skiplist %_libdir/%name/**/*

%description
The client part of Lapki IDE, a programming environment for
extended hierarchical state machines.

%description -l ru_RU.UTF-8
Клиентская часть Lapki IDE, среды программирования расширенных
иерархических машин состояний.

%prep
%setup
tar -xf %SOURCE1
tar -xf %SOURCE2
tar -xf %SOURCE3

%build
export PATH=$(pwd)/node_modules/.bin:$PATH
export ELECTRON_SKIP_BINARY_DOWNLOAD=1
export NODE_ENV=production
electron-vite build --outDir out

%install
mkdir -p %buildroot%_libdir/%name
mkdir -p %buildroot%_bindir
mkdir -p %buildroot%_iconsdir/hicolor/48x48/apps

cp -pr out            %buildroot%_libdir/%name/
cp -pr resources      %buildroot%_libdir/%name/
cp -pr node_modules   %buildroot%_libdir/%name/
cp -pr docserver      %buildroot%_libdir/%name/
cp -pr lapki-compiler %buildroot%_libdir/%name/
cp -p  package.json   %buildroot%_libdir/%name/
cp -pr demos          %buildroot%_libdir/%name/
cp -pr extensions     %buildroot%_libdir/%name/
cp -pr schema         %buildroot%_libdir/%name/

rm -rf %buildroot%_libdir/%name/resources/docserver
rm -rf %buildroot%_libdir/%name/resources/lapki-compiler
ln -s ../docserver      %buildroot%_libdir/%name/resources/docserver
ln -s ../lapki-compiler %buildroot%_libdir/%name/resources/lapki-compiler

node -e "
const pkg = require('./package.json');
const dev = Object.keys(pkg.devDependencies || {});
const fs = require('fs');
dev.forEach(name => {
  const p = '%buildroot%_libdir/%name/node_modules/' + name;
  if (fs.existsSync(p)) {
    fs.rmSync(p, {recursive: true, force: true});
  }
});
"

find %buildroot%_libdir/%name/node_modules -type f \
    \( -name "*.md" \
    -o -name "*.markdown" \
    -o -name "CHANGELOG*" \
    -o -name "LICENCE*" \
    -o -name "LICENSE*" \
    -o -name "*.ts" ! -name "*.d.ts" \
    -o -name ".travis.yml" \
    -o -name ".eslintrc*" \
    -o -name "Makefile" \
    -o -name "Gruntfile*" \
    -o -name "*.js.map" \
    -o -name "*.css.map" \) -delete

for testdir in test tests __tests__ example examples; do
    find %buildroot%_libdir/%name/node_modules \
        -type d -name "$testdir" -exec rm -rf {} + 2>/dev/null || true
done

find %buildroot%_libdir/%name -type f \
    \( -name "*.exe" -o -name "*.dll" \
    -o -name "*.bat" -o -name "*.cmd" \
    -o -name "*.dylib" \) -delete

find %buildroot%_libdir/%name -type f -name "lapki-flasher" -exec chmod 755 {} +
find %buildroot%_libdir/%name -type f -name "*.sh"          -exec chmod 755 {} +

install -D -m 0644 %buildroot%_libdir/%name/resources/icon.png \
    %buildroot%_iconsdir/hicolor/48x48/apps/%name.png

mkdir -p %buildroot%_desktopdir
cat > %buildroot%_desktopdir/%name.desktop << 'DESKTOP'
[Desktop Entry]
Name=Lapki IDE
Name[ru]=Lapki IDE
Comment=Graphical IDE for cyber-physical systems
Comment[ru]=Графическая среда разработки для киберфизических систем
Exec=lapki-client
Icon=lapki-client
Terminal=false
Type=Application
Categories=Development;IDE;
DESKTOP

desktop-file-validate %buildroot%_desktopdir/%name.desktop

cat > %buildroot%_bindir/%name << 'WRAPPER'
#!/bin/sh
export ELECTRON_IS_DEV=0
export NODE_ENV=production
export NODE_PATH=%_libdir/%name/node_modules
export ELECTRON_EXTENSIONS_PATH="${XDG_CACHE_HOME:-$HOME/.cache}/lapki-ide/extensions"
mkdir -p "$ELECTRON_EXTENSIONS_PATH"
cd %_libdir/%name
exec %_bindir/electron%electron_ver . "$@"
WRAPPER
chmod 0755 %buildroot%_bindir/%name

%files
%_bindir/%name
%_libdir/%name
%_desktopdir/%name.desktop
%_iconsdir/hicolor/48x48/apps/%name.png
%doc README.md

%changelog
* Thu Jun 30 2026 Dina Tagantseva <dinchik@altlinux.org> 0.6.0-alt1
- Initial build for Sisyphus.
