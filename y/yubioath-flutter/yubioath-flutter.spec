%define _unpackaged_files_terminate_build 1
%define app_id com.yubico.yubioath
%define flutter_arch x64
%define yubioath_home %_libdir/yubioath-flutter

%set_verify_elf_method normal,lint=relaxed
%add_debuginfo_skiplist %yubioath_home/* %yubioath_home/lib/*

Name: yubioath-flutter
Version: 7.4.0
Release: alt1

Summary: Yubico Authenticator for Desktop
License: Apache-2.0
Group: System/Configuration/Hardware
Url: https://developers.yubico.com/yubioath-flutter/
Vcs: https://github.com/Yubico/yubioath-flutter

# Sync with flutter archs
ExclusiveArch: x86_64

Source0: %name-%version.tar
Source1: %name-%version-pub-cache.tar
Patch: %name-%version-alt.patch

AutoProv: no
Provides: yubioath-desktop = %EVR
Obsoletes: yubioath-desktop <= 5.1.0-alt4
Conflicts: yubioath-desktop <= 5.1.0-alt4

%add_python3_path %yubioath_home
Requires: flutter-gtk

BuildRequires(pre): rpm-build-python3
BuildRequires: /proc
BuildRequires: /dev/pts
BuildRequires: ninja-build
BuildRequires: flutter-tool
BuildRequires: flutter-gtk
BuildRequires: flutter-desktop
BuildRequires: clang-devel
BuildRequires: libstdc++-devel
BuildRequires: pkgconfig(libnotify)
BuildRequires: pkgconfig(ayatana-appindicator3-0.1)
BuildRequires: patchelf

%description
Manage your YubiKey and access one-time passwords with this
full-featured companion app to the YubiKey.

Features include:
* Display information about your YubiKey such as serial number,
  firmware version, and supported capabilities
* Manage and access OATH one-time passwords stored securely on your
  YubiKey
* Configure PIN, fingerprints, and manage passkeys for WebAuthn/FIDO
* Configure PIN/PUK/Management key, and manage private keys and
  certificates for PIV
* Provision Yubico OTP, static passwords, and other YubiKey slot-based
  credentials
* Configure enabled features, and factory reset YubiKey data
* Compatible with any USB or NFC-enabled YubiKey

Store your unique credential on a hardware-backed security key and take
it wherever you go from mobile to desktop. No more storing sensitive
secrets on your mobile phone, leaving your accounts vulnerable to
takeovers. With the YubiKey and Yubico Authenticator you can raise the
bar for security. No connectivity needed!

%prep
%setup -a1
%autopatch -p1
# Embed flutter-gtk
install -vD /usr/lib/flutter/icudtl.dat -t linux/flutter/ephemeral
install -vD /usr/lib/libflutter_linux_gtk.so -t linux/flutter/ephemeral

%build
# Build helper (piece from ./build-helper.sh)
# pushd helper
#     pyinstaller authenticator-helper.spec --distpath ../build/linux
#     uv build --no-build-isolation
#     find ../build/linux/helper -type f -exec chmod a-x {} +
#     chmod a+x ../build/linux/helper/authenticator-helper
# popd

# Workaround for building helper via pyinstaller to avoid a lot of system package
# modules bunching (and entire python3 with its stdlib too).
install -vD -m755 helper/authenticator-helper.py build/linux/helper/authenticator-helper
cp -rv helper/helper build/linux/helper

export PUB_CACHE="$PWD/pub-cache"
flutter build linux --no-pub --verbose --obfuscate --split-debug-info=debuginfo

%install
cd build/linux/%flutter_arch/release/bundle

# Install whole compiled data
mkdir -p %buildroot%yubioath_home
cp -rv {authenticator,helper,lib,data} %buildroot%yubioath_home/

install -vD -m0644 -t %buildroot%_desktopdir linux_support/%app_id.desktop
install -vD -m0644 -t %buildroot%_iconsdir/hicolor/256x256/apps linux_support/%app_id.png

# Do not package platform embedding file from flutter-gtk (it is in Requires)
rm -v %buildroot/%yubioath_home/lib/libflutter_linux_gtk.so

# Fix RPATH values in plugins
find %buildroot%yubioath_home/lib -name 'lib*_plugin.so' -exec patchelf --set-rpath '$ORIGIN' {} \;

# Strip ELFs to deacrease total package size
strip %buildroot%yubioath_home/authenticator
find %buildroot%yubioath_home/lib -name '*.so' -exec strip {} \;

# Fix desktop file
sed -i %buildroot%_desktopdir/%app_id.desktop \
    -e 's|@EXEC_PATH/authenticator|%yubioath_home/authenticator|' \
    -e 's|@EXEC_PATH/linux_support/%app_id|%app_id|'

%files
%_desktopdir/%app_id.desktop
%_iconsdir/hicolor/256x256/apps/%app_id.png
%yubioath_home/

%changelog
* Thu Jun 18 2026 Anton Zhukharev <ancieg@altlinux.org> 7.4.0-alt1
- Updated to 7.4.0.

* Fri Apr 17 2026 Anton Zhukharev <ancieg@altlinux.org> 7.3.3-alt1
- Updated to 7.3.3.

* Fri Apr 03 2026 Anton Zhukharev <ancieg@altlinux.org> 7.3.2-alt1
- Packaged for ALT Sisyphus as a replacement for yubioath-desktop (ALT#54773).
