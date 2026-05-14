Name: vkQuake
Version: 1.34.1
Release: alt1

Summary: Quake I engine
License: GPL-2.0
Group: Games/Arcade
Url: https://github.com/Novum/vkQuake

BuildRequires: glslang libSDL2-devel libvulkan-devel meson spirv-tools
BuildRequires: libflac-devel libvorbis-devel libopusfile-devel libmpg123-devel libstb-devel

Source: %name-%version.tar

%description
Vulkan port of id software's Quake engine.

%description -l ru_RU.UTF-8
vkQuake - современный движок для игры Quake, базирующийся на Vulkan.
Основой движка послужили Quakespasm и его форк Quakespasm-spiked.
Обещается, что vkQuake быстрее, чем Quakespasm засчёт многопоточности.

В качестве Readme.maintainer см. аналогичный файл из пакета Quakespasm

%prep
%setup -q
%ifarch %e2k
# error: unknown attribute "alloc_align"
sed -i 's/__INTEL_COMPILER/__EDG__/' Quake/mimalloc/mimalloc.h
sed -i 's/-Werror/-Wno-error/g' meson.build
%endif
# unbundle stb libraries
pushd Quake
ln -svf %_includedir/stb/stb_image.h \
	%_includedir/stb/stb_image_resize.h \
	%_includedir/stb/stb_image_write.h ./
popd

%build
%add_optflags -Wno-error=unused-function
%meson -Dmp3_lib=mpg123 -Ddo_userdirs=enabled
%meson_build -v

%install
install -pDm755 %__builddir/vkquake %buildroot%_bindir/vkquake

%files
%doc LICENSE.txt readme.md
%_bindir/vkquake

%changelog
* Thu May 14 2026 L.A. Kostis <lakostis@altlinux.ru> 1.34.1-alt1
- 1.34.1.

* Fri Jan 16 2026 L.A. Kostis <lakostis@altlinux.ru> 1.33.1-alt1
- 1.33.1.
- build: enable user directories support.

* Wed Nov 19 2025 Ilya Kurdyukov <ilyakurdyukov@altlinux.org> 1.32.3.1-alt2
- e2k build fix

* Tue Nov 18 2025 L.A. Kostis <lakostis@altlinux.ru> 1.32.3.1-alt1
- 1.32.3.1.
- spec updates:
  + BR: update.
  + unbundle stb libs.
  + use mpg123 as mp3 decoder (upstream change).
  + use meson macros.
  + fix SPDX name of license.
  + fix docs.

* Tue Nov 18 2025 Ilya Kurdyukov <ilyakurdyukov@altlinux.org> 1.30.1-alt2
- e2k build fix

* Tue Nov 18 2025 Nazarov Denis <nenderus@altlinux.org> 1.30.1-alt1.1
- Fix build with glslang >= 16.0

* Mon Jul  3 2023 Artyom Bystrov <arbars@altlinux.org> 1.30.1-alt1
- Update to new version

* Sat Jan 21 2023 Andrey Bergman <vkni@altlinux.org> 1.22.3-alt1
- Initial release for Sisyphus
