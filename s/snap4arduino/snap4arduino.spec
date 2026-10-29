%define _unpackaged_files_terminate_build 1
%define snap_revision 5b561c9b0f643a75e146acfe4b8b1e8ac0f45ffd

Name: snap4arduino
Version: 10.3.6
Release: alt1

Summary: Visual programming environment for Arduino boards
License: AGPL-3.0
Group: Education
URL: https://snap4arduino.rocks
VCS: https://github.com/bromagosa/Snap4Arduino.git

ExcludeArch: %ix86

Source0: %name-%version.tar
Source1: %name-%version-predownloaded.tar
Source2: assemble.py
Source3: snap4arduino.desktop
Source4: snap4arduino.lang.sed

Patch0: %name-%version.patch
Patch1: %name-%version-alt-firmata-desktop.patch
Patch2: %name-%version-alt-serialport-callback.patch

Requires: electron
# SerialPort invokes udevadm for Linux port enumeration.
Requires: /usr/bin/udevadm

BuildRequires: python3
BuildRequires: npm
BuildRequires: node-gyp
BuildRequires: udev
BuildRequires: desktop-file-utils

# Node module scripts are private application resources. The native addon is
# installed separately so RPM still scans its ELF dependencies.
%add_findreq_skiplist %_libdir/%name/app/*

%description
Snap4Arduino combines the Snap! visual programming environment with Arduino
board control through the Firmata protocol.

%prep
%setup -a1
%patch -P 0 -p1
(cd sources && sha256sum -c SHA256SUMS)
(cd npm/tarballs && sha256sum -c ../SHA256SUMS)
tar -xf sources/snap-%snap_revision.tar.gz

export npm_config_cache="$PWD/.npm-cache"
npm cache add --offline --ignore-scripts "$PWD"/npm/tarballs/*.tgz
npm --prefix npm ci --offline --ignore-scripts --omit=dev --no-audit --no-fund

# The addon is compiled locally for the target architecture.
rm -rf npm/node_modules/@serialport/bindings-cpp/prebuilds

%patch -P 1 -p1 -d npm
%patch -P 2 -p1 -d npm

%build
# node-gyp supplies the compiler and Node headers through its dependencies.
(cd npm/node_modules/@serialport/bindings-cpp && \
    CFLAGS="%optflags" CXXFLAGS="%optflags" node-gyp rebuild --nodedir=/usr)

python3 %SOURCE2 --snap Snap-%snap_revision --npm-manifest npm/package.json --output app

cp -a npm/node_modules app/
cp npm/package-lock.json app/

%install
install -d %buildroot%_libdir/%name
cp -a app %buildroot%_libdir/%name/
# Keep the compiled addon outside the JS resource skiplist so RPM scans its ELF
# dependencies and generates debuginfo. A relative link also permits relocation.
addon_dir=%buildroot%_libdir/%name/app/node_modules/@serialport/bindings-cpp
install -m755 "$addon_dir/build/Release/bindings.node" \
    %buildroot%_libdir/%name/serialport.node
rm -rf "$addon_dir/build"
install -d "$addon_dir/build/Release"
ln -s ../../../../../../serialport.node \
    "$addon_dir/build/Release/bindings.node"
install -D -m644 %SOURCE3 %buildroot%_desktopdir/%name.desktop
for size in 16 32 48 128 256; do
    install -D -m644 assets/icons/${size}x${size}x32.png \
        %buildroot%_iconsdir/hicolor/${size}x${size}/apps/%name.png
done

install -d %buildroot%_bindir
cat > %buildroot%_bindir/%name <<'EOF'
#!/bin/sh
exec /usr/bin/electron %_libdir/%name/app "$@"
EOF
chmod 755 %buildroot%_bindir/%name

# Snap! translations are JavaScript files rather than gettext catalogs.
%find_lang --without-mo --custom-file-script=%SOURCE4 %name
# List the other private resources separately to avoid duplicate locale entries.
# Remove ignore files now; brp-cleanup would remove them after this list is made.
find %buildroot%_libdir/%name/app -name .gitignore -delete
find %buildroot%_libdir/%name -type d -printf '"%%p"\n' | \
    sed 's/^/%%dir /' > %name.files
find %buildroot%_libdir/%name ! -type d \
    ! -path '*/locale/lang-*.js' ! -path '*/s4a/lang-*.js' \
    -printf '"%%p"\n' >> %name.files
sed -i 's|%buildroot||' %name.files
cat %name.lang >> %name.files

%check
desktop-file-validate %buildroot%_desktopdir/%name.desktop
test "$(cat %buildroot%_libdir/%name/app/version)" = "%version"
test -f %buildroot%_libdir/%name/app/node_modules/firmata/lib/firmata.js
for module in %buildroot%_libdir/%name/app/desktop/*.js; do
    node --check "$module"
done
node -e 'require("%buildroot%_libdir/%name/app/desktop/serial").list((err) => { if (err) throw err; })'

%files -f %name.files
%doc README.md CHANGELOG.md LICENSE
%_bindir/%name
%_desktopdir/%name.desktop
%_iconsdir/hicolor/*/apps/%name.png

%changelog
* Tue Oct 27 2026 Grant Makyan <karonus@altlinux.org> 10.3.6-alt1
- Initial build for ALT.
