%define debug_package %nil

%define commit bc1b1259146db61cebba389eff0f3df2bf6edce5
%define commit_short %(echo %commit | head -c6)

Name: armorpaint
Version: 0.9.1
Release: alt1

Summary: Software for 3D PBR texture painting

License: zlib
Group: Graphics
Url: https://github.com/armory3d/armortools/tree/main/armorpaint

# Source0-url: https://github.com/armory3d/armortools/commit/%commit
Source0: %name-%version.tar
Source1: armorpaint_wrapper
Source2: armorpaint.desktop

BuildRequires: git-core
BuildRequires: clang
BuildRequires: ninja-build
BuildRequires: libstdc++-devel
BuildRequires: pkgconfig(alsa)
#BuildRequires: mesa-common-devel
BuildRequires: pkgconfig(gtk+-3.0)
BuildRequires: pkgconfig(xkbcommon)
BuildRequires: pkgconfig(xcursor)
BuildRequires: pkgconfig(xrandr)
BuildRequires: pkgconfig(xinerama)
BuildRequires: pkgconfig(xi)
BuildRequires: pkgconfig(vulkan)
BuildRequires: pkgconfig(wayland-protocols)
BuildRequires: pkgconfig(udev)

# aarch64 build not supported, upstream say^ may be in future
ExclusiveArch: x86_64

%description
ArmorPaint is a stand-alone software designed for physically-based texture painting.
Drag & drop your 3D models and start painting. Receive instant visual feedback
in the viewport as you paint.

%prep
%setup
subst 's/-static-libgcc -static-libstdc++//' base/tools/make.js

%build
pushd armorpaint
../base/make --graphics vulkan --run
popd

%install
# install wrapper script
install -d %buildroot%_bindir
install -m0755 %SOURCE1 %buildroot%_bindir/%name

cd %name/build/out
# install main binary and krom
install -d %buildroot%_libdir/%name/
install -m0755 ArmorPaint %buildroot%_libdir/%name/
cp -r data %buildroot%_libdir/%name/

# install desktop file and icon
install -d %buildroot%_desktopdir/
install -d %buildroot%_pixmapsdir/
install -m0644 %SOURCE2 %buildroot%_desktopdir
install -m0644 icon.png %buildroot%_pixmapsdir/%name.png


%files
%doc license.md
%_bindir/%name
%_desktopdir/*.desktop
%_pixmapsdir/*.png
%_libdir/%name/


%changelog
* Thu Feb 27 2025 Vitaly Lipatov <lav@altlinux.ru> 0.9.1-alt1
- initial build for ALT Sisyphus

