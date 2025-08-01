%define _unpackaged_files_terminate_build 1

%def_without ui

Name: lsfg-vk
Version: 1.0.0
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

%if_with ui
BuildRequires: libadwaita-devel
BuildRequires: ImageMagick-tools
%endif

ExcludeArch: %ix86

%description
%summary


%package ui
Summary: User interface for %name
Group: System/Configuration/Hardware
Requires: %name = %EVR

%description ui
%summary

%prep
%setup -a1

%build
# build library
%cmake  -B build -G Ninja \
        -DCMAKE_BUILD_TYPE=RelWithDebinfo \
        -DCMAKE_INSTALL_PREFIX=/usr \
        -DCMAKE_C_COMPILER=clang \
        -DCMAKE_CXX_COMPILER=clang++ \
        -DCMAKE_INTERPROCEDURAL_OPTIMIZATION=On \
        %nil

cmake --build build

%if_with ui
# build UI
cd ui
cargo build --release --locked
%endif

%install

# base library and config
install -Dm644 VkLayer_LS_frame_generation.json %buildroot%_datadir/vulkan/implicit_layer.d/VkLayer_LS_frame_generation.json
install -Dm644 build/liblsfg-vk.so %buildroot%_libdir/liblsfg-vk.so

%if_with ui
# UI binary, desktop file and icon
install -Dm755 ui/target/release/%name-ui %buildroot%_bindir/%name-ui
install -Dm644 ui/rsc/gay.pancake.%name-ui.desktop %buildroot%_desktopdir/%name-ui.desktop

for res in 16 32 48 128 256; do
    mkdir -p %buildroot%_iconsdir/hicolor/$res'x'$res/apps/
    convert ui/rsc/icon.png -resize $res'x'$res %buildroot%_iconsdir/hicolor/$res'x'$res/apps/gay.pancake.%name-ui.png
done
%endif

%files
%doc LICENSE.md
%_libdir/liblsfg-vk.so
%_datadir/vulkan/implicit_layer.d/VkLayer_LS_frame_generation.json

%if_with ui
%files ui
%_bindir/%name-ui
%_desktopdir/%name-ui.desktop
%_iconsdir/hicolor/*/apps/gay.pancake.%name-ui.png
%endif

%changelog
* Fri Aug 01 2025 Mikhail Tergoev <fidel@altlinux.org> 1.0.0-alt1
- Initial build for ALT Sisyphus
