%define _vklib amdvlk
%define _vkdir %_datadir/vulkan/icd.d
%define _vkldir %_datadir/vulkan/implicit_layer.d
# Decrease debuginfo verbosity to reduce memory consumption during final library linking
%define optflags_debug -g1
# As ubuntu
%define gcc_ver 9

%define _vk_api_version 1.3.292

%def_with clang
%def_with wayland
%def_with shader_cache

%define optflags_lto %nil

%ifarch x86_64
%define bits 64
%endif
%ifarch %ix86
%define bits 32
%endif

Name: vulkan-amdgpu
Version: 2024.Q3.1
Release: alt1
License: MIT
Url: https://github.com/GPUOpen-Drivers/AMDVLK
Summary: AMD Open Source Driver For Vulkan
Group: System/X11

ExclusiveArch: x86_64 %ix86

Requires: vulkan-filesystem

BuildRequires(pre): rpm-macros-cmake /proc
BuildRequires: cmake ninja-build python3-devel python3-module-jinja2 curl libxcb-devel libssl-devel llvm-devel
BuildRequires: libX11-devel libxshmfence-devel libXrandr-devel glslang libdxcompiler-devel python3-module-ruamel-yaml
%if_with wayland
BuildRequires: wayland-devel libwayland-server-devel libwayland-client-devel libwayland-cursor-devel libwayland-egl-devel
BuildRequires: libffi-devel
%endif
%if_with clang
BuildRequires: clang mold llvm-devel gcc-c++ libstdc++-devel-static
%else
BuildRequires: gcc%{gcc_ver}-c++ libstdc++%{gcc_ver}-devel-static
%endif

Source0: xgl.tar
Source1: pal.tar
Source2: llpc.tar
Source3: gpurt.tar
Source4: llvm.tar
Source5: metrohash.tar
Source6: amd_icd.json
Source7: cwpack.tar
Source8: VK_LAYER_AMD_switchable_graphics.json
Source9: llvm-dialects.tar

%description
The AMD Open Source Driver for Vulkan(r) is an open-source Vulkan driver for
Radeon(tm) graphics adapters on Linux(r). It is built on top of AMD's Platform
Abstraction Library (PAL), a shared component that is designed to encapsulate
certain hardware and OS-specific programming details for many of AMD's 3D and
compute drivers. Leveraging PAL can help provide a consistent experience across
platforms, including support for recently released GPUs and compatibility with
AMD developer tools.

%prep
%setup -n xgl -b0 -b1 -b2 -b3 -b4 -b5 -b7 -b9
mkdir -p %_builddir/llvm-project
mv %_builddir/llvm/llvm %_builddir/llvm-project
cp -ar %_builddir/llvm/{cmake,third-party} %_builddir/llvm-project/
# llvm-dialects hack
rm -rf %_builddir/llpc/imported/llvm-dialects && ln -s %_builddir/llvm-dialects %_builddir/llpc/imported/llvm-dialects

%build
# build amdvlk.so
# according https://github.com/GPUOpen-Drivers/AMDVLK#build-driver-and-generate-json-files
%if_with clang
%cmake \
	-DXGL_USE_CLANG=ON \
%else	
export GCC_VERSION=%{gcc_ver} \
%cmake \
	-GNinja \
%endif
%if_with wayland
	-DBUILD_WAYLAND_SUPPORT=ON \
%endif
%if_with shader_cache
	-DLLPC_ENABLE_SHADER_CACHE=1 \
%endif
	-DCMAKE_BUILD_TYPE=RelWithDebInfo \
%if_with clang
	-DLLVM_USE_LINKER=mold \
	-DCMAKE_CXX_LINK_FLAGS="-fuse-ld=mold -Wl,--thinlto-jobs=all" \
%endif
        -DXGL_METROHASH_PATH=%_builddir/metrohash \
        -DXGL_CWPACK_PATH=%_builddir/cwpack \
        -DCMAKE_VERBOSE_MAKEFILE:BOOL=ON
%cmake_build

%install
mkdir -p %buildroot{%_vkdir,%_vkldir,%_libdir,%_sysconfdir/amd}
touch %buildroot%_sysconfdir/amd/amdVulkanSettings.cfg

install -p -m644 %_builddir/xgl/%_cmake__builddir/icd/%_vklib%bits.so %buildroot%_libdir/%_vklib.so
for f in %buildroot%_vkdir/$(basename %SOURCE6) %buildroot%_vkldir/$(basename %SOURCE8); do install -pD -m644 /dev/null "$f"; done
sed -e 's|@API_VERSION@|%_vk_api_version|g' %SOURCE6 > %buildroot%_vkdir/$(basename %SOURCE6)
sed -e 's|@API_VERSION@|%_vk_api_version|g' %SOURCE8 > %buildroot%_vkldir/$(basename %SOURCE8)

%files
%_libdir/*.so
%_vkdir/*.json
%_vkldir/*.json
%dir %_sysconfdir/amd
%ghost %attr(644,root,root) %config(missingok) %_sysconfdir/amd/*.cfg

%changelog
* Wed Aug 21 2024 L.A. Kostis <lakostis@altlinux.ru> 2024.Q3.1-alt1
- .spec: try to keep debugging symbols.
- 2024-08-13 update:
  + icd: bump vulkan version
  + llvm-dialects: Updated to 6ff7d39046e2
  + llvm-project: Updated to eb619c26c273
  + gpurt: Updated to c5b10793bd96
  + llpc: Updated to 5278a3ff4f18
  + pal: Updated to d3bfe509cd33
  + xgl: Updated to 8bf20dd1ca8b

* Fri Aug 09 2024 L.A. Kostis <lakostis@altlinux.ru> 2024.Q2.3-alt1.1
- Enable %%ix86 build again.

* Thu Jun 27 2024 L.A. Kostis <lakostis@altlinux.ru> 2024.Q2.3-alt1
- 2024-06-26 update:
  + icd: bump vulkan version
  + llvm-dialects: Updated to ed4b46e84250
  + llvm-project: Updated to 72a6d2843ca0
  + gpurt: Updated to 6ca06bbba1c0
  + llpc: Updated to f64d106c023e
  + pal: Updated to 695337aa8131
  + xgl: Updated to 5dd432ade872

* Tue Jun 18 2024 L.A. Kostis <lakostis@altlinux.ru> 2024.Q2.2-alt1
- 2024-06-05 update:
  + icd: bump vulkan version
  + llvm-project: Updated to c3793ad7bf21
  + gpurt: Updated to c0196c83e76c
  + llpc: Updated to 6c770c7d276d
  + pal: Updated to 2076667db1fa
  + xgl: Updated to 3abea9dfab5a

* Mon Jun 03 2024 L.A. Kostis <lakostis@altlinux.ru> 2024.Q2.1-alt1
- BR: added python3-module-ruamel-yaml (for gpurt).
- 2024-05-15 update:
  + icd: bump vulkan version
  + llvm-dialects: Updated to 55e176fb88bc
  + llvm-project: Updated to 45cdb88c143d
  + gpurt: Updated to e0f12d951395
  + llpc: Updated to 8252cfa83e03
  + pal: Updated to c789abc769d2
  + xgl: Updated to f6a447e31ae7

* Thu Apr 11 2024 L.A. Kostis <lakostis@altlinux.ru> 2024.Q1.3-alt1
- gpurt: fix compile with recent DXC (upstream PR#8).
- 2024-03-26 update:
  + icd: bump vulkan version
  + llvm-dialects: Updated to 3f9e17f5f44e
  + llvm-project: Updated to da55e9e39bc7
  + gpurt: Updated to 2e6d528610f4
  + llpc: Updated to 14535c028dc7
  + pal: Updated to 42e29f4d3d52
  + xgl: Updated to b7100c18eb2d

* Sat Feb 24 2024 L.A. Kostis <lakostis@altlinux.ru> 2024.Q1.2-alt1
- xgl: built with static libstdc++.
- 2024-02-23 update:
  + icd: bump vulkan version
  + llvm-dialects: Updated to 69e114f9d886
  + llvm-project: Updated to 3d1ed0c398ba
  + gpurt: Updated to 8d50dc6e9c45
  + llpc: Updated to d4c8845341ff
  + pal: Updated to abb22ae22308
  + xgl: Updated to ccc121a22ad0

* Fri Jan 05 2024 L.A. Kostis <lakostis@altlinux.ru> 2023.Q4.3-alt1
- 2023-12-28 update:
  + BR: added jinja2 module
  + icd: bump vulkan version
  + llvm-project: Updated to 021d89eb80d2
  + gpurt: Updated to 6808afe3c8a3
  + llpc: Updated to 0c23ae955060
  + pal: Updated to 6353b182d28f
  + xgl: Updated to 53656ff75237

* Sun Dec 03 2023 L.A. Kostis <lakostis@altlinux.ru> 2023.Q4.2-alt1
- 2023-11-24 update:
  + icd: bump vulkan version
  + llvm-dialects: Updated to 16a0e9331797
  + llvm-project: Updated to 9ddf09e97e9e
  + gpurt: Updated to 86360020040c
  + llpc: Updated to e51543dc524c
  + pal: Updated to 6bdc69412b3c
  + xgl: Updated to 565dce2c570c

* Sat Sep 30 2023 L.A. Kostis <lakostis@altlinux.ru> 2023.Q3.3-alt1
- 2023-9-29 update:
  + icd: bump vulkan version
  + llvm-dialects: Updated to 8c54ca076fbf
  + llvm-project: Updated to 92bd7b3505d4
  + gpurt: Updated to 7a3d1d10f98a
  + llpc: Updated to e9a336171294
  + pal: Updated to 2de164b431f8
  + xgl: Updated to 5f4c7d9498c6

* Fri Aug 18 2023 L.A. Kostis <lakostis@altlinux.ru> 2023.Q3.1-alt1
- 2023-8-7 update:
  + icd: bump vulkan version
  + llvm-dialects: Updated to b5c7de36efa5
  + llvm-project: Updated to b2b27cdd9f04
  + gpurt: Updated to a0415aa237c8
  + llpc: Updated to ce2c12c412bd
  + pal: Updated to 9a07f5b7883e
  + xgl: Updated to bc0587c273e5

* Fri Jun 16 2023 L.A. Kostis <lakostis@altlinux.ru> 2023.Q2.3-alt2
- Disable 32-bit (again).
- Use mold for linking.

* Fri Jun 16 2023 L.A. Kostis <lakostis@altlinux.ru> 2023.Q2.3-alt1
- switch to llvm15.
- enable gpurt back on 32-bit (fingers crossed).
- 2023-6-15 update:
  + icd: bump vulkan version
  + llvm-dialects: Updated to e7464fe63735
  + llvm-project: Updated to 02394516f587
  + gpurt: Updated to a1103572dfcc
  + llpc: Updated to f44e737f5e13
  + pal: Updated to f01505f7fe4b
  + xgl: Updated to 6288905587fa

* Thu May 25 2023 L.A. Kostis <lakostis@altlinux.ru> 2023.Q2.2-alt1
- 2023-5-22 update:
  + icd: bump vulkan version
  + llvm-dialects: Updated to b716b5679d2d
  + llvm-project: Updated to 9b82edca7fa3
  + gpurt: Updated to a1220a7d201d
  + llpc: Updated to 298e95edad06
  + pal: Updated to 3efba26966a3
  + xgl: Updated to 02e867e81626

* Mon Apr 24 2023 L.A. Kostis <lakostis@altlinux.ru> 2023.Q2.1-alt1
- 2023-4-18 update:
  + icd: bump vulkan version
  + llvm-dialects: Updated to ef2e7bfe83fb
  + llvm-project: Updated to 6053b88f3401
  + gpurt: Updated to 2c399b3971c1
  + llpc: Updated to 6527fd70d704
  + pal: Updated to 4b53bc00c4d3
  + xgl: Updated to 5301cf5222c6

* Sun Mar 26 2023 L.A. Kostis <lakostis@altlinux.ru> 2023.Q1.3-alt1.1
- gpurt: disable on 32-bit due unstable compilation with recent dxc
  (see gpurt issue #5).

* Thu Mar 16 2023 L.A. Kostis <lakostis@altlinux.ru> 2023.Q1.3-alt1
- 2023-3-14 update:
  + icd: bump vulkan version
  + llvm-dialects: Updated to 17aafecff46b
  + llvm-project: Updated to fdc6165b081b
  + gpurt: Updated to 714a028e920c
  + llpc: Updated to 1ecd9997579b
  + pal: Updated to 4640888b579b
  + xgl: Updated to 997225355d7f

* Mon Feb 20 2023 L.A. Kostis <lakostis@altlinux.ru> 2023.Q1.2-alt1.1
- Fix .icd files generation.

* Mon Feb 20 2023 L.A. Kostis <lakostis@altlinux.ru> 2023.Q1.2-alt1
- 2023-2-17 update:
  + icd: bump vulkan version
  + gpurt: Updated to 172e852f9036
  + llpc: Updated to 522365aa657f
  + pal: Updated to ac9ff8bd2260
  + xgl: Updated to b72c7accced0

* Wed Feb 01 2023 L.A. Kostis <lakostis@altlinux.ru> 2023.Q1.1-alt1.1
- Added llvm-dialects repo.

* Wed Feb 01 2023 L.A. Kostis <lakostis@altlinux.ru> 2023.Q1.1-alt1
- 2023-1-31 update:
  + icd: bump vulkan version
  + llvm-project: Updated to 916f05c15939
  + gpurt: Updated to e19c8ceca056
  + llpc: Updated to ffc49b2a07de
  + pal: Updated to 042362399cda
  + xgl: Updated to 67cd9d1d3016

* Thu Dec 15 2022 L.A. Kostis <lakostis@altlinux.ru> 2022.Q4.4-alt1
- 2022-12-15 update:
  + gpurt: Updated to 1f0c4f7e9cea
  + llpc: Updated to 37dcb2e5cedb
  + pal: Updated to 287ef684bc36
  + xgl: Updated to 8aa0e76a110f

* Sat Dec 10 2022 L.A. Kostis <lakostis@altlinux.ru> 2022.Q4.3-alt1
- 2022-12-9 update:
  + icd: bump vulkan version
  + llvm-project: Updated to 42a4d92d3c68
  + gpurt: Updated to 385af58e0f1b
  + llpc: Updated to 6c817737b654
  + pal: Updated to 4a23f7ca61e2
  + xgl: Updated to b358df546081

* Wed Nov 23 2022 L.A. Kostis <lakostis@altlinux.ru> 2022.Q4.2-alt5
- Add implicit switchable_graphics layers, apparently, libvulkan doesn't read
  it from ICD json.
- Disable excessive optimisation.
- Restore i586 build (as dxc fixed now).

* Mon Nov 21 2022 L.A. Kostis <lakostis@altlinux.ru> 2022.Q4.2-alt4
- Use upstream switches for clang.

* Mon Nov 21 2022 L.A. Kostis <lakostis@altlinux.ru> 2022.Q4.2-alt3
- Rebuild w/ llvm 13.0 (to be in pair with mesa).

* Sun Nov 20 2022 L.A. Kostis <lakostis@altlinux.ru> 2022.Q4.2-alt2
- Disable LTO (it uses own LTO flags).

* Sat Nov 12 2022 L.A. Kostis <lakostis@altlinux.ru> 2022.Q4.2-alt1
- 2022-11-10 update:
  + icd: bump vulkan version
  + llvm-project: Updated to 3c87d1ffe0db
  + gpurt: Updated to 889dd8db7228
  + llpc: Updated to 83e59f978821
  + pal: Updated to 0f44ced5384c
  + xgl: Updated to 0387177d6143

* Sat Oct 22 2022 L.A. Kostis <lakostis@altlinux.ru> 2022.Q4.1-alt1
- 2022-10-21 update:
  + icd: bump vulkan API version
  + llvm-project: Updated to d2b67605e4dd
  + gpurt: Updated to 2874e509b677
  + llpc: Updated to 9db0ba4c968b
  + pal: Updated to c2af6fc4c14e
  + xgl: Updated to 8a67c76eedb8

* Fri Oct 21 2022 L.A. Kostis <lakostis@altlinux.ru> 2022.Q3.5-alt1.1
- disable i586 build (it's broken now).

* Sat Oct 15 2022 L.A. Kostis <lakostis@altlinux.ru> 2022.Q3.5-alt1
- Update build scheme.
- BR: add dxcompiler dependency.
- 2022-9-30 update:
  + icd: bump vulkan API version
  + xgl: Updated to 4118707939c2f4783d28ce2a383184a3794ca477
  + pal: Updated to ae55b19b7553bf204b4945de9c11c5b05bc0e167
  + llpc: Updated to 7857f2e209fc65374f2891be52e3a4a22fbae483
  + gpurt: Updated to b89f22aadd0a335be632055434a7f8ba152fcb37
  + llvm-project: Updated to 5c82ef808fd269c95f5bd166d1846149e3afadc2

* Tue Jul 12 2022 L.A. Kostis <lakostis@altlinux.ru> 2022.Q2.3-alt1
- .spec: play with optlevel on x86_64
- .spec: remove llvm optflags hack
- spvgen: update -alt-shared patch
- 2022-6-21 update:
  + icd: bump vulkan API version
  + llvm-project: Updated to ff4dc0eccd74
  + spvgen: Updated to eaa8c1dafbdb
  + llpc: Updated to 61aabddf65ae
  + pal: Updated to a40241a1e6f5
  + xgl: Updated to a9a73115ee5c

* Sun May 29 2022 L.A. Kostis <lakostis@altlinux.ru> 2022.Q2.2-alt1
- try build with clang.
- 2022-5-20 update:
  + icd: bump vulkan API version
  + llvm-project: Updated to 219f568b0b60
  + cwpack: Updated to 4f8cf0584442
  + metrohash: Updated to 18893fb28601
  + spvgen: Updated to cd629c08af16
  + llpc: Updated to be276de91f44
  + pal: Updated to ca98822bbccc
  + xgl: Updated to 9478a913fc7d

* Sat Apr 09 2022 L.A. Kostis <lakostis@altlinux.ru> 2022.Q2.1-alt1
- update spvgen-shared patch.
- fix llvm build.
- 2022-4-3 update:
  + icd: bump vulkan API version
  + llvm: Updated to 219f568b0b60
  + spvgen: Updated to 87983dba34c2
  + llpc: Updated to c0dbc976ccae
  + pal: Updated to 1ff58cafbae0
  + xgl: Updated to 25569e8bf7ad

* Fri Nov 05 2021 L.A. Kostis <lakostis@altlinux.ru> 2021.Q4.1-alt1
- 2021-11-4 update:
  + icd: bump vulkan API version
  + cwpack: Updated to 39f8940199e6
  + llvm: Updated to 3ced1fbbcda4
  + spvgen: Updated to e0855d9a0370
  + llpc: Updated to c937b09ac21a
  + pal: Updated to d5826cb5d1a3
  + xgl: Updated to 477361f6a225

* Tue Aug 31 2021 L.A. Kostis <lakostis@altlinux.ru> 2021.Q3.5-alt1
- 2021-8-24 update:
  + llvm: Updated to e32a5e65b5a2
  + spvgen: Updated to 985d66ad5f62
  + llpc: Updated to 72c9697660a9
  + pal: Updated to cd4f8b28b5d9
  + xgl: Updated to e6ae9d1025c8

* Mon Aug 16 2021 L.A. Kostis <lakostis@altlinux.ru> 2021.Q3.4-alt2
- add llvm build workaround (-Wno-error=return-type).

* Mon Aug 16 2021 L.A. Kostis <lakostis@altlinux.ru> 2021.Q3.4-alt1
- 2021-8-11 update:
  + icd: bump vulkan version to 1.2.185.
  + llvm: Updated to d3ad9a01687d
  + spvgen: Updated to 051b6997c7c3
  + llpc: Updated to 9a3ae083e740
  + pal: Updated to f2be9e29a870
  + xgl: Updated to ec89b84f0b8a

* Mon Jun 14 2021 L.A. Kostis <lakostis@altlinux.ru> 2021.Q2.5-alt2
- .spec: update cmake macros
- update spvgen -alt-shared patch.

* Sun Jun 13 2021 L.A. Kostis <lakostis@altlinux.ru> 2021.Q2.5-alt1
- 2021-6-10 update:
  + icd: bump vulkan API version to 1.2.179.
  + llvm: Updated to a85ea7baf890
  + spvgen: Updated to faf9ff1722d3
  + llpc: Updated to c89f405e3632
  + pal: Updated to 02ac99ba650a
  + xgl: Updated to 14397c77fbc0

* Tue May 04 2021 L.A. Kostis <lakostis@altlinux.ru> 2021.Q2.2-alt1
- 2021-4-28 update (closes #40022):
  + update spvgen BR
  + json: bump vulkan API version to 1.2.174.
  + llvm: Updated to d2e97f487956
  + spvgen: Updated to 59823e6c3557
  + llpc: Updated to 28c4e99487eb
  + pal: Updated to 0168557a0715
  + xgl: Updated to f1467f0dfd3d

* Wed Feb 24 2021 L.A. Kostis <lakostis@altlinux.ru> 2021.Q1.3-alt2
- Fix wayland client BR.

* Wed Feb 24 2021 L.A. Kostis <lakostis@altlinux.ru> 2021.Q1.3-alt1
- 2021-2-8 update:
  + icd: bump vulkan API version to 1.2.168
  + llvm: Updated to 97bea7830b74
  + spvgen: Updated to 6b84106b7e10
  + llpc: Updated to ca7003a056d3
  + pal: Updated to 5262df4eae03
  + xgl: Updated to a2c6ddfd9063

* Mon Dec 28 2020 L.A. Kostis <lakostis@altlinux.ru> 2020.Q4.6-alt2
- Rebuild w/ gcc9.

* Tue Dec 15 2020 L.A. Kostis <lakostis@altlinux.ru> 2020.Q4.6-alt1
- 2020-12-14 update:
  + icd: bump vulkan API version to 1.2.162
  + metrohash: Updated to 3c566dd9cda4
  + llvm: Updated to a0777f490501
  + spvgen: Updated to fb798cb760a4
  + llpc: Updated to e2d38b0c8042
  + pal: Updated to f92844ecbba3
  + xgl: Updated to 86f61a31988a

* Sun Sep 06 2020 L.A. Kostis <lakostis@altlinux.ru> 2020.Q3.4-alt1
- 2020-8-24 update:
  + xgl: 598c6832a4983f5b75b38a589fca5be80a2f3bb0
  + pal: bebb2b0d0d70625d825cd386a1360154709487f2
  + llpc: 9b5cb15acc8ff789420ed9ed593e35c81303d10c
  + spvgen: 1813b88297ef56f56d5f851886257cac79179705
  + llvm: 30cb97a1d0efebb4317f9abeec8d90a5a83d4837
  + metrohash: 712f76fee75d69b23a1ea8f6465752c3ccaaf9a2
  + cwpack: 7387247eb9889ddcabbc1053b9c2052e253b088e
- icd: bump vulkan version api version to 1.2.150.

* Thu May 07 2020 L.A. Kostis <lakostis@altlinux.ru> 2020.Q2.2-alt1
- 2020-4-30 update:
  + xgl: d8c926b86b1245badc67e5d55b0eaa45d4a910a0
  + pal: e1b2dde021a2efd34da6593994f87317a803b065
  + llpc: 3864fc733e437a6e6ae729c6858b92b39194eada
  + spvgen: d4817ab957f79762da83b7fc1d3f2816dbdc13fd
  + llvm: a1299ba9c8e2337f00bdec73e2031144d9811ed7
- icd: bump vulkan version api version to 1.2.135.
- update BR.

* Wed Feb 12 2020 L.A. Kostis <lakostis@altlinux.ru> 2020.Q1.1-alt1
- 2020-1-21 update:
  + llvm: 08268e9955d48ca075b239ae46328694ddff2413
  + spvgen: 6c9a5cf8789681e31b9cd3df8af245b9aaa2c259
  + llpc: 93f91d8e6258aec02369b63c3248c9fab15c6956
  + pal: 9fab16015e522fff05890a045a1e9d8d3c23a636
  + xgl: 5ee2a33520138966eb5e2745dd3f2e5401d2f3b6
- icd.json: bump vulkan api version.

* Sat Jan 18 2020 L.A. Kostis <lakostis@altlinux.ru> 2019.Q4.5-alt1
- added cwpack library.
- 2019-12-19 update:
  + llvm: cc0df5ace776584f5f7c0c20704d28f445f0e074
  + spvgen: ce06cb5e3116ba77a22c3278dfeadfd865a8977c
  + cwpack: b601c88aeca7a7b08becb3d32709de383c8ee428
  + xgl: 7e13a8bd0bb57d3cfb3bc014f6b26a8c9bb8bfd9
  + pal: 40af910391fb8c287cb37bf520c41310bf88d405
  + llpc: 2efe41812964c88aa38a80c66939ce44ae493fd4
- icd.json: bump vulkan api version.

* Thu Aug 29 2019 L.A. Kostis <lakostis@altlinux.ru> 2019.Q3.5-alt1
- added modified metrohash library.
- 2019-8-26 update:
  + llpc: 4fa48ef1cf0f81eafdb56df91c2f2180d4865101
  + llvm: 9bc5dd4450a6361faf5c5661056a7ee494fad830
  + metrohash: 2b6fee002db6cc92345b02aeee963ebaaf4c0e2f
  + pal: 68b57dba33a4d922e8f1ef1b3781c2f659ffbd1c
  + spvgen: 68b57dba33a4d922e8f1ef1b3781c2f659ffbd1c
  + xgl: 331558e93794068a786bf699d3fe23bb11bac021
- icd.json: bump vulkan api version.

* Wed Jul 03 2019 L.A. Kostis <lakostis@altlinux.ru> 2019.Q3.1-alt1
- 2019-6-30 update:
  + llpc: aa8a9d7f2b7ad7b81b70e7959e99e3f31f85c211
  + llvm: 8118692e8aefbd95f791ff49beddb8ce90e8927c
  + pal:6c8eaa257e6216437fdfe3f17d418eccfe42e0bd
  + spvgen: 53245b96b7a647743f50b9d841751f9755002661
  + xgl: eee58c8e482ac4a6fdc40452cb4ad744395d0f74
- icd.json: bump vulkan api version.

* Mon May 13 2019 L.A. Kostis <lakostis@altlinux.ru> 2019.Q2.3-alt2
- spvgen: fix build.

* Mon May 13 2019 L.A. Kostis <lakostis@altlinux.ru> 2019.Q2.3-alt1
- 2019-05-12 update:
  + xgl: eaecf6b9ad7bc3d310e752528f84fd52fba23747
  + pal: fb9a4dc951c0afd737460b26afb716c96e966b77
  + llpc: fdd5e24be2d9031ab685690cad1c9259d96518f6
  + llvm: f41e1a873108a371ae5574d518c1ee6eb3814cee
- json: bump vulkan version.

* Mon Apr 15 2019 L.A. Kostis <lakostis@altlinux.ru> 2019.Q2.1-alt1
- 2019-4-10 update:
  + xgl: 5b4058dc288a25f6554fcc61f80bf3f27eb35d8d
  + pal: 99901922d67e502ff4233a8bfcbfa0347c0ffa1b
  + llpc: 6c6de1dab3927bfb0f6659ba89c6fe80be8a4a04
  + spvgen: 69311f7c1e220d190909298b9c7bd702ecc237ff
- json: bump vulkan version.

* Sat Apr 13 2019 L.A. Kostis <lakostis@altlinux.ru> 2019.Q1.9-alt2
- Rebuild w/ gcc7.

* Tue Mar 26 2019 L.A. Kostis <lakostis@altlinux.ru> 2019.Q1.9-alt1
- 2019-3-26 update:
  + llvm: 97cc33415120ae3ed472b6dd5cb234b74a80bd80
  + spvgen: 1560d287f779b342e0019499dda85890cb07affc
  + llpc: 32c0c28b1b7fd36b2f9cb17411af2963f6cfc48a
  + pal: e17272e1581ae6e222293880db08e0df7b1f1f75
  + xgl: a082b41ad4a8aed476cb39e6b63cddd25ab9e0b4
- .json: make biarch friendly.

* Wed Mar 06 2019 L.A. Kostis <lakostis@altlinux.ru> 2019.Q1.7-alt1
- 2019-3-1 update:
  + llvm: c7a5a5c3bac75699d45824523b4fcf045913413f
  + llpc: 8eecb4baef898f0a5b9902406626887c3646dbb6
  + pal: e8a5acd90310871053a40015ebcea5b32391a824
  + xgl: f2af4b0c33963842f544107d005f0a6c82ea513f

* Tue Feb 26 2019 L.A. Kostis <lakostis@altlinux.ru> 2019.Q1.6-alt1
- 2019-2-25 update:
  + llvm: 666d463e73a67dd3ccb304a5b13a5b1f09f784f0
  + llpc: b26545220db28772ac07491e17d31bbcf9c249ec
  + pal: 534ab72b967e07934dade777caf15686dc04b940
  + xgl: 1d35effd11e3d47a8e5281f06b75dd334641476e

* Fri Feb 01 2019 L.A. Kostis <lakostis@altlinux.ru> 2019.Q1.4-alt1
- 2019-2-1 update:
  + llvm: d3c2b9d104f0de0be59d914578a28275c8b4784d
  + llpc: a1ee25169453ba909ba940d7d25e2739d2f453ed
  + pal: 3bb2d4082ef9b95a114258a90c7044939a5f0638
  + xgl: dbabc93bc9c3a5a1e7e73672b3d4594b0611fa36
- icd.json: bump vulkan version.

* Tue Jan 22 2019 L.A. Kostis <lakostis@altlinux.ru> 2019.Q1.2-alt1
- 2019-1-15 update:
  + llvm: 3c7dbb214c3680803f7d3e3c3aed02fddb2f7dbb
  + spvgen: d26082d54930ad2ea97da94a2443137e7325b64c
  + llpc: 797be964eb8d65f2ec162a783708b36834a62000
  + pal: 2e94fa1533a606d076061db8d5be514bb69adfc3
  + xgl: 0d7c5a69ba314bfabe2d5dbe3e5e4d1ea3228845
- .spec: added missing conf dir.

* Sat Jan 12 2019 L.A. Kostis <lakostis@altlinux.ru> 2019.Q1.1-alt3
- Rebuild w/ gcc5 (as it does ubuntu).

* Sat Jan 12 2019 L.A. Kostis <lakostis@altlinux.ru> 2019.Q1.1-alt2
- Added wayland knob.
- Fix llvm merge.

* Wed Jan 09 2019 L.A. Kostis <lakostis@altlinux.ru> 2019.Q1.1-alt1
- Initial build for ALTLinux:
  + do not build spvgen for now (only tests rely on it);
  + use gcc7 (gcc8 still unsupported by icd);
- Checkout from github:
  + xgl: master--bca286c1146f9f0662bbb7c10d193e487579e6f0
  + pal: master--f924a4fb84efde321f7754031f8cfa5ab35055d3
  + llpc: master--f36099d4c778327f22b050432f09e17dc815474a
  + spvgen: master--328a0990a958f21eb2c6b1ecb092a43629fe5554
  + llvm: master--0843ddd6f5a03468d42b90715e98e9798f772555
