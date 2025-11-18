Name: vkQuake
Version: 1.30.1
Release: alt2

Summary: Quake I engine
License: GPL
Group: Games/Arcade
Url: https://github.com/Novum/vkQuake

BuildRequires: glslang libSDL2-devel libmad-devel libvorbis-devel libvulkan-devel meson spirv-tools


Packager: %packager
Source: %name-%version-%release.tar

# https://github.com/Novum/vkQuake/pull/809
Patch0: fix-build-with-glslang-16.patch

%description
Vulkan port of id software's Quake engine.

%description -l ru_RU.UTF-8
vkQuake - современный движок для игры Quake, базирующийся на Vulkan.
Основой движка послужили Quakespasm и его форк Quakespasm-spiked.
Обещается, что vkQuake быстрее, чем Quakespasm засчёт многопоточности.

В качестве Readme.maintainer см. аналогичный файл из пакета Quakespasm

%prep
%setup -n %name-%version-%release
%patch0 -p1
%ifarch %e2k
# error: unknown attribute "alloc_align"
sed -i 's/__INTEL_COMPILER/__EDG__/' Quake/mimalloc/mimalloc.h
%endif

%build
meson setup build && ninja -C build

%install
mkdir -p %buildroot/%_bindir/
install -pm755 build/vkquake %buildroot/%_bindir/

%define docdir %_docdir/%name-%version
mkdir -p %buildroot%docdir

install -pm644 LICENSE.txt %buildroot%docdir/
install -pm644 readme.md %buildroot%docdir/

%files
%_bindir/vkquake
%dir %docdir
%docdir/LICENSE.txt
%docdir/readme.md

%changelog
* Tue Nov 18 2025 Ilya Kurdyukov <ilyakurdyukov@altlinux.org> 1.30.1-alt2
- e2k build fix

* Tue Nov 18 2025 Nazarov Denis <nenderus@altlinux.org> 1.30.1-alt1.1
- Fix build with glslang >= 16.0

* Mon Jul  3 2023 Artyom Bystrov <arbars@altlinux.org> 1.30.1-alt1
- Update to new version

* Sat Jan 21 2023 Andrey Bergman <vkni@altlinux.org> 1.22.3-alt1
- Initial release for Sisyphus
