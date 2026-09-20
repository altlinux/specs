%define _unpackaged_files_terminate_build 1

%define __find_requires_filter grep -vF -e 'debug64(libGlassSDK.so)' -e '/usr/lib/debug/usr/lib64/xr-driver/viture/libglasses.so.debug' -e '/usr/lib/debug/usr/lib64/xr-driver/viture/libusb-1.0.so.0.debug'

Name:    breezy-desktop
Version: 2.12.2
Release: alt1

Summary: XR virtual desktop for KWin 6 and GNOME (XR glasses mirror)
License: GPL-3.0-only AND MIT AND BSD-3-Clause AND CC0-1.0
Group:   Graphical desktop/Other
URL:     https://github.com/wheaney/breezy-desktop
VCS:     https://github.com/wheaney/breezy-desktop

Source: %name-%version.tar
Source1: %name-postsubmodules-%version.tar
Source2: %name-development-%version.tar
Source3: %name-packaging-vulkan-%version.tar

BuildRequires(pre): rpm-macros-cmake rpm-macros-meson rpm-macros-systemd
BuildRequires(pre): rpm-macros-rust
BuildRequires: cmake meson ninja-build pkgconf
BuildRequires: gcc gcc-c++ extra-cmake-modules patchelf
BuildRequires: rpm-build-rust rpm-build-python3
BuildRequires: kwin-devel kf6-kconfig-devel kf6-kconfigwidgets-devel
BuildRequires: kf6-kcolorscheme-devel kf6-kcoreaddons-devel kf6-kglobalaccel-devel
BuildRequires: kf6-ki18n-devel kf6-kcmutils-devel kf6-kwindowsystem-devel
BuildRequires: kf6-kxmlgui-devel qt6-base-devel qt6-declarative-devel qt6-quick3d
BuildRequires: libX11-devel libxcb-devel libepoxy-devel wayland-devel
BuildRequires: libusb-devel libevdev-devel libudev-devel
BuildRequires: openssl-devel libcurl-devel libjson-c-devel
BuildRequires: libgio-devel gettext-tools desktop-file-utils gtk4-update-icon-cache
BuildRequires: libvulkan-devel glslang spirv-headers

Requires: /usr/bin/env

ExclusiveArch: x86_64

%description
Breezy Desktop turns XR glasses into a virtual desktop: a full-screen mirror
of whatever the host GPU renders, with a head-tracked view, a virtual display
behind the glasses, and built-in virtual displays for external monitors.

The XR glasses driver (breezy-desktop-driver) runs as a user session service
and talks to the hardware (XREAL Air/One, VITURE, Rokid, RayNeo); the common
breezy-desktop package ships the management UI; breezy-desktop-kwin and
breezy-desktop-gnome provide the KWin 6 effect and the GNOME Shell extension
respectively.

%package driver
Summary: XR glasses user-space driver for Breezy Desktop
Group:   System/Configuration/Hardware
Requires(post): systemd
Requires(preun): systemd

%description driver
User-space driver for XR glasses (XREAL Air/One, VITURE, Rokid, RayNeo) used
by Breezy Desktop. Runs as a systemd user service, exposes xrDriver to the
Breezy UI and applications, and ships the vendor SDKs for supported
devices under %_libdir/xr-driver.

%package kwin
Summary: Breezy Desktop KWin 6 effect and settings module
Group:   Graphical desktop/KDE
Requires: kwin breezy-desktop-driver qt6-quick3d /usr/bin/kcmshell6

%description kwin
KWin 6 full-screen effect that mirrors the desktop onto XR glasses through
the Breezy Desktop driver, with the settings KCM for display and tracking
options.

%package gnome
Summary: Breezy Desktop GNOME Shell extension
Group:   Graphical desktop/GNOME
BuildArch: noarch
Requires: gnome-shell

%description gnome
GNOME Shell extension (breezydesktop@xronlinux.com) that mirrors the desktop
onto XR glasses, using the same driver and virtual displays as the rest of
the Breezy Desktop stack.

%package vulkan
Summary: Breezy Desktop Vulkan post-processing layer
Group:   System/Configuration/Hardware
Requires: breezy-desktop-driver

%description vulkan
Breezy Desktop Vulkan post-processing layer: a 64-bit vkBasalt build with
runtime uniform support and the Sombrero ReShade effect, used to render the
XR glasses view for native Vulkan and gamescope applications.  The per-user
layer definition and shader files are installed by the breezy_vulkan_setup
command; the layer is enabled with ENABLE_BREEZY_VKBASALT=1.

%prep
%setup -a1 -a2 -a3

# ALT installs the KWin headers under /usr/include/KF6/kwin, while upstream
# hardcodes the /usr/include/kwin layout (and reads effect.h from there):
sed -i 's|/usr/include/kwin/effect/effect.h|%_includedir/KF6/kwin/effect/effect.h|' \
    kwin/cmake/info.cmake
sed -i 's|/usr/include/kwin|%_includedir/KF6|' kwin/src/CMakeLists.txt

# Build assets upstream keeps out of git (ignored files, provided from their
# real locations in this vendored tree):
cp VERSION kwin/VERSION
cp ui/modules/PyXRLinuxDriverIPC/xrdriveripc.py kwin/src/xrdriveripc/xrdriveripc.py
cp vulkan/custom_banner.png kwin/src/qml/custom_banner.png
cp modules/sombrero/calibrating.png kwin/src/qml/calibrating.png
cp ui/data/icons/hicolor/scalable/apps/com.xronlinux.BreezyDesktop.svg \
   kwin/src/kcm/com.xronlinux.BreezyDesktop.svg

# Driver systemd unit carries template placeholders; the LD_LIBRARY_PATH line
# is dropped because the SDKs are found via the installed RUNPATH and
# /etc/ld.so.conf.d/xr-driver.conf:
sed -i -e "s|ExecStart={bin_dir}/xrDriver|ExecStart=%{_bindir}/xrDriver|" \
       -e "/Environment=/d" \
    modules/XRLinuxDriver/systemd/xr-driver.service

# The XReal One driver module is Rust and is driven by its own Cargo/CMake
# target.  Its crate lives in a git submodule, so the vendored crate (Source2)
# is unpacked next to it and the cargo source replacement is generated here,
# the way the Rust build macros do it for top-level crates:
xod=modules/XRLinuxDriver/modules/xrealOneDeviceKit/modules/xreal_one_driver
mv vendor "$xod/vendor"
pushd "$xod"
%rust_prep
popd

%build
# The driver's XReal One module is Rust and is driven by its own CMake target;
# build it offline against the vendored crate placed during the prep step:
export CARGO_HOME="$PWD/.cargo-home"
export CARGO_NET_OFFLINE=true

# Breezy XR driver (vendored device modules; SDKs linked/dlopen'ed from the
# /usr/lib64/xr-driver RUNPATH below, so the install RPATH is kept on):
pushd modules/XRLinuxDriver
%cmake \
    -DCMAKE_BUILD_TYPE=Release \
    -DCMAKE_SKIP_INSTALL_RPATH:BOOL=off \
    -DCMAKE_INSTALL_RPATH=%_libdir/xr-driver
%cmake_build
popd

# KWin 6 effect plugin + KCM:
pushd kwin
%cmake \
    -DCMAKE_BUILD_TYPE=Release \
    -DCMAKE_INSTALL_LIBDIR=%_lib
%cmake_build
popd

# UI application and virtualdisplay helper:
pushd ui
%meson
%meson_build
popd

# Breezy Vulkan layer: the vendored vkBasalt fork adds runtime uniforms.
# Built 64-bit only from this tree; a 32-bit layer would need an i586 build
# of the whole source package.
pushd vulkan/modules/vkBasalt
%meson -Dappend_libdir_vkbasalt=true
%meson_build
popd

%install
# Breezy XR driver
install -Dm755 modules/XRLinuxDriver/%_cmake__builddir/xrDriver %buildroot%_bindir/xrDriver
# Installed by hand (no cmake_install), so the build-tree RPATH survives; rewrite it.
# The vendored VITURE SDK (libglasses.so, xr_device_provider_*) lives in the
# viture/ subdir, hence both private dirs.
patchelf --set-rpath %_libdir/xr-driver:%_libdir/xr-driver/viture %buildroot%_bindir/xrDriver
install -Dm755 modules/XRLinuxDriver/bin/xr_driver_cli %buildroot%_bindir/xr_driver_cli
install -Dm755 modules/XRLinuxDriver/bin/xr_driver_logs %buildroot%_bindir/xr_driver_logs

install -dm755 %buildroot%_libdir/xr-driver
cp -a modules/XRLinuxDriver/lib/%_arch/. %buildroot%_libdir/xr-driver/
# Prebuilt SDK blobs carry RPATHs "/usr/local/lib" and "./"; the ALT ELF check
# accepts only $ORIGIN (or system paths), and the libs' siblings sit next to them.
find %buildroot%_libdir/xr-driver -type f -name '*.so*' -exec patchelf --set-rpath '$ORIGIN' {} +
# The VITURE SDK ships the SONAME as a hard link to the same library; keep one
# real file and point the SONAME at it (otherwise it is packaged twice).
if [ -e %buildroot%_libdir/xr-driver/viture/libusb-1.0.so.0.3.0 ]; then
    ln -sf libusb-1.0.so.0.3.0 %buildroot%_libdir/xr-driver/viture/libusb-1.0.so.0
fi

install -Dm644 modules/XRLinuxDriver/systemd/xr-driver.service %buildroot%_userunitdir/xr-driver.service
install -dm755 %buildroot%_udevrulesdir
install -m644 modules/XRLinuxDriver/udev/70-*.rules %buildroot%_udevrulesdir/
install -dm755 %buildroot%_sysconfdir/ld.so.conf.d
echo "%_libdir/xr-driver" > %buildroot%_sysconfdir/ld.so.conf.d/xr-driver.conf
install -dm755 %buildroot%_modules_loaddir
echo "uinput" > %buildroot%_modules_loaddir/uinput.conf

# UI application (meson)
pushd ui
%meson_install
popd
rm -rf %buildroot%_datadir/breezydesktop/breezydesktop/lib
sed -i -e 's|^Exec=.*|Exec=env APPDIR=%_datadir BINDIR=%_bindir breezydesktop|' \
    %buildroot%_desktopdir/com.xronlinux.BreezyDesktop.desktop

# The UI looks for a verify helper next to the binary ($BINDIR/breezy_gnome_verify)
# and exits when it is absent.  The tarball installs a per-user copy; for the RPM
# install a system-wide one that checks the pieces provided by the subpackages.
cat > %buildroot%_bindir/breezy_gnome_verify <<'VERIFY_EOF'
#!/bin/sh
set -e
fail() { echo "Verification failed: $1" >&2; exit 1; }
[ -x %_bindir/xrDriver ] || fail "the XR driver (breezy-desktop-driver) is not installed"
[ -d %_datadir/gnome-shell/extensions/breezydesktop@xronlinux.com ] || \
    fail "the Breezy GNOME Shell extension (breezy-desktop-gnome) is not installed"
echo "Verification succeeded"
VERIFY_EOF
chmod 755 %buildroot%_bindir/breezy_gnome_verify

# KWin effect + KCM
pushd kwin
%cmake_install
popd
install -Dm755 kwin/bin/breezy_kwin_logs %buildroot%_bindir/breezy_kwin_logs

# GNOME Shell extension.  The source tree keeps Sombrero.frag, the textures
# and the GSettings schema as symlinks into sibling submodules; dereference
# them, or the extension ships dangling links (and file Requires on the
# /usr/share/gnome-shell paths they would have pointed to):
install -dm755 %buildroot%_datadir/gnome-shell/extensions/breezydesktop@xronlinux.com
cp -rL gnome/src/. %buildroot%_datadir/gnome-shell/extensions/breezydesktop@xronlinux.com/
install -Dm755 gnome/bin/breezy_gnome_logs %buildroot%_bindir/breezy_gnome_logs

# Breezy Vulkan layer: private 64-bit vkBasalt plus the Sombrero/ReShade
# assets and the per-user setup command.  Everything stays under /usr; the
# per-user files are created by breezy_vulkan_setup, not by an RPM scriptlet.
install -dm755 %buildroot%_libdir/breezy-desktop/vkbasalt
install -m755 vulkan/modules/vkBasalt/%_target_platform/src/libvkbasalt.so \
    %buildroot%_libdir/breezy-desktop/vkbasalt/libvkbasalt.so

vulkan_dir=%buildroot%_datadir/breezy-desktop/vulkan
install -dm755 "$vulkan_dir"
install -m644 modules/sombrero/*.frag modules/sombrero/*.png "$vulkan_dir"/
install -m644 vulkan/custom_banner.png "$vulkan_dir"/
install -m644 vulkan/config/vkBasalt.conf "$vulkan_dir"/
install -m644 packaging-vulkan/ReShade.fxh packaging-vulkan/ReShadeUI.fxh "$vulkan_dir"/
sed 's|@LIB_PATH@|%_libdir/breezy-desktop/vkbasalt/libvkbasalt.so|' \
    packaging-vulkan/breezy_vkBasalt.json > "$vulkan_dir"/breezy_vkBasalt.json

sed 's|@ASSET_DIR@|%_datadir/breezy-desktop/vulkan|' \
    packaging-vulkan/breezy_vulkan_setup > %buildroot%_bindir/breezy_vulkan_setup
chmod 755 %buildroot%_bindir/breezy_vulkan_setup
install -m755 packaging-vulkan/breezy_vulkan_uninstall %buildroot%_bindir/breezy_vulkan_uninstall
install -m755 vulkan/bin/breezy_vulkan_logs %buildroot%_bindir/breezy_vulkan_logs

# Canonical ALT python shebang fix (rpm-macros-python3, via rpm-build-python3):
%python3_fix_shebang %buildroot%_bindir

# ALT has no macro for shell shebangs; make the interpreters absolute.
find %buildroot%_bindir -type f -exec sed -i \
    -e '1s|^#!/usr/bin/env bash$|#!/bin/bash|' {} +

# These data modules are installed non-executable and run via an explicit
# python3; a shebang there is dead weight (rpmlint: non-executable-script).
sed -i '1{/^#!/d}' \
    %buildroot%_datadir/breezydesktop/breezydesktop/virtualdisplay.py \
    %buildroot%_datadir/kwin/effects/breezy_desktop/xrdriveripc_runner.py

%find_lang breezydesktop

%post driver
%systemd_user_post xr-driver.service
%udev_rules_update
modprobe uinput 2>/dev/null || :
:; exit 0

%preun driver
%systemd_user_preun xr-driver.service
:; exit 0

%postun driver
%udev_rules_update
:; exit 0

%files -f breezydesktop.lang
%doc LICENSE README.md
%_bindir/breezydesktop
%_bindir/virtualdisplay
%_bindir/breezy_gnome_verify
%_datadir/breezydesktop/
%_desktopdir/com.xronlinux.BreezyDesktop.desktop
%_datadir/metainfo/com.xronlinux.BreezyDesktop.metainfo.xml
%_datadir/glib-2.0/schemas/com.xronlinux.BreezyDesktop.gschema.xml
%_iconsdir/hicolor/scalable/apps/com.xronlinux.BreezyDesktop.svg

%files driver
%doc LICENSE
%_bindir/xrDriver
%_bindir/xr_driver_cli
%_bindir/xr_driver_logs
%dir %_libdir/xr-driver
%_libdir/xr-driver/*.so*
%dir %_libdir/xr-driver/viture
%_libdir/xr-driver/viture/*.so*
%_userunitdir/xr-driver.service
%_udevrulesdir/70-xreal-xr.rules
%_udevrulesdir/70-viture-xr.rules
%_udevrulesdir/70-uinput-xr.rules
%_udevrulesdir/70-rokid-xr.rules
%_udevrulesdir/70-rayneo-xr.rules
%_sysconfdir/ld.so.conf.d/xr-driver.conf
%_modules_loaddir/uinput.conf

%files kwin
%doc LICENSE
%_libdir/qt6/plugins/kwin/effects/plugins/
%dir %_datadir/kwin/effects
%_datadir/kwin/effects/breezy_desktop/
%_libdir/qt6/plugins/plasma/kcms/
%_desktopdir/breezy_desktop.desktop
%_bindir/breezy_kwin_logs

%files gnome
%doc LICENSE
%dir %_datadir/gnome-shell/extensions
%_datadir/gnome-shell/extensions/breezydesktop@xronlinux.com/
%_bindir/breezy_gnome_logs

%files vulkan
%doc LICENSE
%dir %_libdir/breezy-desktop
%dir %_libdir/breezy-desktop/vkbasalt
%_libdir/breezy-desktop/vkbasalt/libvkbasalt.so
%dir %_datadir/breezy-desktop
%_datadir/breezy-desktop/vulkan/
%_bindir/breezy_vulkan_setup
%_bindir/breezy_vulkan_uninstall
%_bindir/breezy_vulkan_logs

%changelog
* Sat Sep 19 2026 Sergey Palcheh <minergenon@altlinux.org> 2.12.2-alt1
- Initial build for Sisyphus.
