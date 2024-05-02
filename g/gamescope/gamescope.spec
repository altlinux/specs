%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%set_verify_elf_method strict

Name: gamescope
Version: 3.14.11
Release: alt1

Summary: SteamOS session compositing window manager

Group: System/X11
License: BSD-2-Clause
Url: https://github.com/Plagman/gamescope

Source: %name-%version.tar
Source1: submodules-%name-%version.tar
Source2: stb.pc

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson
BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: libstb-devel
BuildRequires: libliftoff-devel
BuildRequires: libbenchmark-devel
BuildRequires: libglm-devel
BuildRequires: hwdata-devel
# subprojects: Use Joshua-Ashton personal wlroots fork for with branch for now
# BuildRequires: libwlroots-devel
BuildRequires: pipewire-libs-devel
BuildRequires: libX11-devel
BuildRequires: libXdamage-devel
BuildRequires: libXcomposite-devel
BuildRequires: libXrender-devel
BuildRequires: libXext-devel
BuildRequires: libXfixes-devel
BuildRequires: libXxf86vm-devel
BuildRequires: libXtst-devel
BuildRequires: libXres-devel
BuildRequires: libdrm-devel
BuildRequires: libvulkan-devel
BuildRequires: libwayland-server-devel
BuildRequires: libwayland-client-devel
BuildRequires: wayland-protocols
BuildRequires: libxkbcommon-devel
BuildRequires: libcap-devel
BuildRequires: libSDL2-devel
BuildRequires: glslang-devel
BuildRequires: libinput-devel
BuildRequires: libXmu-devel
BuildRequires: libdisplay-info-devel
BuildRequires: libXcursor-devel
BuildRequires: libavif-devel
BuildRequires: spirv-headers
BuildRequires: libopenvr-devel
BuildRequires: libpixman-devel
BuildRequires: libseat1-devel
BuildRequires: xorg-xwayland-devel
BuildRequires: libxcbutil-devel
BuildRequires: libxcbutil-errors-devel
BuildRequires: pkgconfig(libdecor-0)
BuildRequires: pkgconfig(xcb-ewmh)

ExclusiveArch: x86_64

%description
In an embedded session usecase, gamescope does the same thing as steamcompmgr,
but with less extra copies and latency:
*   It's getting game frames through Wayland by way of Xwayland,
    so there's no copy within X itself before it gets the frame.
*   It can use DRM/KMS to directly flip game frames to the screen,
    even when stretching or when notifications are up, removing another copy.
*   When it does need to composite with the GPU, it does so with async Vulkan
    compute, meaning you get to see your frame quick even if the game already
    has the GPU busy with the next frame.

It also runs on top of a regular desktop,
the 'nested' usecase steamcompmgr didn't support.
*   Because the game is running in its own personal Xwayland sandbox desktop,
    it can't interfere with your desktop and your desktop can't interfere with it.
*   You can spoof a virtual screen with a desired resolution and refresh rate
    as the only thing the game sees, and control/resize the output as needed.
    This can be useful in exotic display configurations like ultrawide
    or multi-monitor setups that involve rotation.

It runs on Mesa + AMD or Intel, and could be made to run
on other Mesa/DRM drivers with minimal work.
AMD requires Mesa 20.3+, Intel requires Mesa 21.2+.
Can support NVIDIA if/when they support
atomic KMS + accelerated Xwayland + Vulkan DMA-BUF extensions.
See https://github.com/Plagman/gamescope/issues/151 for NVIDIA support state.

If running RadeonSI clients with older cards (GFX8 and below),
currently have to set R600_DEBUG=nodcc,
or corruption will be observed until the stack picks up DRM modifiers support.

%prep
%setup -a1

mkdir -p pkgconfig
cp -v %SOURCE2 pkgconfig/stb.pc

# use system spirv headers
sed -i 's^../thirdparty/SPIRV-Headers/include/spirv/^/usr/include/spirv/^' src/meson.build

%build
export PKG_CONFIG_PATH=pkgconfig
%meson \
	-Dpipewire=enabled \
	-Dbenchmark=enabled \
	-Ddrm_backend=enabled \
	-Dsdl2_backend=enabled \
	-Davif_screenshots=enabled \
	\
	-Denable_gamescope=true \
	-Denable_openvr_support=true \
	-Denable_gamescope_wsi_layer=true \
	\
	-Drt_cap=disabled \
	\
	-Dforce_fallback_for=[] \
	%nil

%meson_build -v

%install
DESTDIR=%buildroot meson install -C %_cmake__builddir --skip-subprojects

%files
%doc LICENSE README.md
%_bindir/gamescope
%_libdir/libVkLayer_FROG_gamescope_wsi_*.so
%_datadir/vulkan/implicit_layer.d/VkLayer_FROG_gamescope_wsi.*.json

%changelog
* Thu May 02 2024 Mikhail Tergoev <fidel@altlinux.org> 3.14.11-alt1
- 3.14.11

* Wed Apr 17 2024 Mikhail Tergoev <fidel@altlinux.org> 3.14.3-alt1
- 3.14.3

* Mon Mar 18 2024 Mikhail Tergoev <fidel@altlinux.org> 3.14.2-alt2
- Added support OpenVR.
- Used system spirv headers.

* Mon Mar 11 2024 Mikhail Tergoev <fidel@altlinux.org> 3.14.2-alt1
- 3.14.2

* Thu Sep 14 2023 Mikhail Tergoev <fidel@altlinux.org> 3.12.5-alt1
- 3.12.5
- Revert to git.

* Tue Aug 01 2023 Mikhail Tergoev <fidel@altlinux.org> 3.12.0-alt1
- New version (3.12.0) with rpmgs script.
- Moved to update from tarball.

* Wed Mar 02 2022 Aleksei Nikiforov <darktemplar@altlinux.org> 3.11.26-alt1
- Updated to upstream version 3.11.26.

* Mon Feb 28 2022 Aleksei Nikiforov <darktemplar@altlinux.org> 3.11.25-alt1
- Updated to upstream version 3.11.25.

* Tue Feb 22 2022 Aleksei Nikiforov <darktemplar@altlinux.org> 3.11.23-alt1
- Initial build for ALT.
