Name:    fileman
Version: 1.0
Release: alt2.git2507b35

Summary: A single panel file Manager forked from 351Files.

License: GPLv2
Group:   File tools
Url:     https://github.com/ROCKNIX/fileman

Source: %name-%version.tar
Patch0: 000-sdl-vulkan.patch

ExcludeArch: ppc64le
Source1: fileman.sh

BuildRequires: gcc gcc-c++ make libSDL2-devel libSDL2_ttf-devel libSDL2_image-devel libevdev-devel

%description
A single panel file Manager tailored for Anbernic 351 devices: RG351V and RG351P.
Can be easily adapted to any Linux-based device.

Based on DinguxCommander.

%prep
%setup
%patch0 -p1

%build
%ifarch aarch64
for device in PC RK3326 RK3399 RK3566 RK3566_X55 RK3588 SD865 S922X; do
%make DEVICE=$device RES_PATH=/usr/share/fileman/res START_PATH=/home SDL2_CONFIG=%prefix/bin/sdl2-config CC=%prefix/bin/g++
mv fileman fileman_$device
done
%else
%make DEVICE=PC RES_PATH=/usr/share/fileman/res START_PATH=/home SDL2_CONFIG=%prefix/bin/sdl2-config CC=%prefix/bin/g++
%endif

%install
mkdir -p %buildroot%_datadir/%name
%ifarch aarch64
for device in RK3326 RK3399 RK3566 RK3566_X55 RK3588 SD865 S922X; do
install -Dm0755 ./fileman_$device %buildroot%_bindir/fileman_$device
done
%else
for device in PC; do
install -Dm0755 ./fileman %buildroot%_bindir/fileman_$device
done
%endif

install -Dm0755 %SOURCE1 %buildroot%_bindir/fileman

cp -r res %buildroot%_datadir/%name

%files
%doc *.md
%_bindir/fileman
%_bindir/fileman_*
%_datadir/%name/res/*

%changelog
* Mon Feb 17 2025 Artyom Bystrov <arbars@altlinux.org> 1.0-alt2.git2507b35
- Update targets

* Tue Oct 15 2024 Artyom Bystrov <arbars@altlinux.org> 1.0-alt1.git2507b35
- Initial build