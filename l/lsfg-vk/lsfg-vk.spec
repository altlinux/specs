%define _unpackaged_files_terminate_build 1

Name: lsfg-vk
Version: 2.0.0
Release: alt1

Summary: Lossless Scaling Frame Generation on Linux via DXVK/Vulkan

Group: System/Configuration/Hardware
License: MIT
Url: https://github.com/PancakeTAS/lsfg-vk

Source: %name-%version.tar
Source1: submodules-%name-%version.tar

BuildRequires(pre): rpm-build-rust
BuildRequires: cmake ninja-build gcc-c++ llvm
BuildRequires: clang clang-tools clang-devel libcxxabi-devel libcxx-devel
BuildRequires: libvulkan-devel vulkan-headers glslang-devel spirv-headers
BuildRequires: wayland-devel libwayland-client-devel libwayland-cursor-devel libwayland-egl-devel
BuildRequires: libxkbcommon-devel libXrandr-devel libXinerama-devel libXcursor-devel libXi-devel
BuildRequires: libSDL3-devel libffi-devel
BuildRequires: qt6-base-devel qt6-declarative-devel ImageMagick-tools

ExcludeArch: %ix86

%description
%summary

%package ui
Summary: User interface for %name
Group: System/Configuration/Hardware
Requires: %name = %EVR

%description ui
Easy to use configuration editor for %name.

%prep
%setup -a1

%build
%cmake  -B build -G Ninja \
        -DCMAKE_BUILD_TYPE=RelWithDebinfo \
        -DCMAKE_INSTALL_PREFIX=%buildroot/usr \
        -DCMAKE_C_COMPILER=clang \
        -DCMAKE_CXX_COMPILER=clang++ \
        -DCMAKE_INTERPROCEDURAL_OPTIMIZATION=On \
        -DLSFGVK_BUILD_UI=ON \
        %nil

cmake --build build

%install
cmake --install build

install -Dm644 %name-ui/rsc/gay.pancake.%name-ui.desktop %buildroot%_desktopdir/gay.pancake.%name-ui.desktop

for res in 16 32 48 128 256; do
    mkdir -p %buildroot%_iconsdir/hicolor/$res'x'$res/apps/
    convert %name-ui/rsc/gay.pancake.%name-ui.png -resize $res'x'$res %buildroot%_iconsdir/hicolor/$res'x'$res/apps/gay.pancake.%name-ui.png
done

%files
%doc LICENSE.md
%_bindir/%name-cli
%_libdir/lib%name-layer.so
%_datadir/vulkan/implicit_layer.d/VkLayer_LSFGVK_frame_generation.json

%files ui
%_bindir/%name-ui
%_desktopdir/gay.pancake.%name-ui.desktop
%_iconsdir/hicolor/*/apps/gay.pancake.%name-ui.png

%changelog
* Thu Apr 16 2026 Mikhail Tergoev <fidel@altlinux.org> 2.0.0-alt1
- 2.0.0-dev
- Build UI for lsfg-vk (ALT bug: 57109)

* Fri Aug 01 2025 Mikhail Tergoev <fidel@altlinux.org> 1.0.0-alt1
- Initial build for ALT Sisyphus
