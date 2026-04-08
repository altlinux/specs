%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1

Name: gamescope
Version: 3.16.20
Release: alt2

Summary: Micro-compositor for video games on Wayland

Group: System/X11
License: BSD-2-Clause
Url: https://github.com/ValveSoftware/gamescope
Vcs: https://github.com/ValveSoftware/gamescope.git

Source: %name-%version.tar
Source1: submodules-%name-%version.tar

Patch1: gamescope-alt-NestedRefresh60.patch
Patch2: 0001-cstdint.patch
Patch3: Allow-to-use-system-wlroots.patch
Patch4: gamescope-3.16.19-alt-use-system-glm.patch
Patch5: gamescope-3.16.19-alt-use-system-stb.patch
Patch6: Update-wlroots-dependency-to-0.19.patch

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson
BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: libstb-devel
BuildRequires: libliftoff-devel
BuildRequires: libbenchmark-devel
BuildRequires: libglm-devel
BuildRequires: hwdata-devel
BuildRequires: libwlroots-devel
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
BuildRequires: libei-devel
BuildRequires: git-core
BuildRequires: libluajit-devel
BuildRequires: libudev-devel

ExclusiveArch: %ix86 x86_64 aarch64

%description
Gamescope is the micro-compositor optimized for running video games on Wayland.

%prep
%setup -a1
%autopatch -p1

# set version without git
sed -i "s/vcs_tag = .*/vcs_tag = '%version'/" src/meson.build

# use system spirv headers
sed -i 's^../thirdparty/SPIRV-Headers/include/spirv/^/usr/include/spirv/^' src/meson.build
rm -rv thirdparty/SPIRV-Headers

# use system libraries
rm -rv subprojects/{libdisplay-info,libliftoff,openvr,wlroots}

%build
%meson \
    -Davif_screenshots=enabled \
    -Dbenchmark=enabled \
    -Ddrm_backend=enabled \
    -Denable_gamescope=true \
    -Denable_gamescope_wsi_layer=true \
    -Denable_openvr_support=true \
    -Dforce_fallback_for=[] \
    -Dinput_emulation=enabled \
    -Dpipewire=enabled \
    -Drt_cap=disabled \
    -Dsdl2_backend=enabled \
    %nil

%meson_build -v

%install
DESTDIR=%buildroot meson install -C %_cmake__builddir --skip-subprojects

%files
%doc LICENSE README.md
%_bindir/gamescope
%_bindir/gamescopectl
%_bindir/gamescopereaper
%_bindir/gamescopestream
%_bindir/gamescope-type
%_libdir/libVkLayer_FROG_gamescope_wsi_*.so
%_datadir/vulkan/implicit_layer.d/VkLayer_FROG_gamescope_wsi.*.json
%_datadir/%name/

%changelog
* Wed Apr 08 2026 Mikhail Tergoev <fidel@altlinux.org> 3.16.20-alt2
- Update BR and fix build with wlroots-0.19

* Fri Feb 13 2026 Ilya Sorochan <k0tran@altlinux.org> 3.16.20-alt1
- 3.16.20
- Update Url and add Vcs tag.
- Use %%version in the build process (ALT bug: 55085).

* Mon Jan 12 2026 Ilya Sorochan <k0tran@altlinux.org> 3.16.19-alt1
- 3.16.19

* Mon May 12 2025 Mikhail Tergoev <fidel@altlinux.org> 3.16.4-alt1
- 3.16.4

* Wed Nov 13 2024 Mikhail Tergoev <fidel@altlinux.org> 3.15.14-alt1
- 3.15.14
- Added build for aarch64 and i586. 

* Wed May 29 2024 Mikhail Tergoev <fidel@altlinux.org> 3.14.18-alt1
- 3.14.18
- Nested refresh = 60 and unfocused = 30 by default (ALT bug: 50107)

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
