Name: vkQuake
Version: 1.22.3
Release: alt1

Summary: Quake I engine
License: GPL
Group: Games/Arcade
Url: https://github.com/Novum/vkQuake

BuildRequires: glslang libSDL2-devel libmad-devel libvorbis-devel libvulkan-devel meson spirv-tools


Packager: %packager
Source: %name-%version-%release.tar

%description
Vulkan port of id software's Quake engine.

%description -l ru_RU.UTF-8
vkQuake - современный движок для игры Quake, базирующийся на Vulkan.
Основой движка послужили Quakespasm и его форк Quakespasm-spiked.
Обещается, что vkQuake быстрее, чем Quakespasm засчёт многопоточности.

В качестве Readme.maintainer см. аналогичный файл из пакета Quakespasm

%prep
%setup -n %name-%version-%release

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
* Sat Jan 21 2023 Andrey Bergman <vkni@altlinux.org> 1.22.3-alt1
- Initial release for Sisyphus


