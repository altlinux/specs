Name:     ares
Version:  131
Release:  alt1

Summary:  ares is a cross-platform, open source, multi-system emulator, focusing on accuracy and preservation.
License:  ISC
Group:    Emulators
Url:      https://github.com/ares-emulator/ares

Packager: Artyom Bystrov <arbars@altlinux.org>

Source:   %name-%version.tar

BuildRequires: gcc-c++ libgtk+3-devel libSDL-devel libudev-devel libopenal-devel libXv-devel libpulseaudio-devel libGL-devel libXrandr-devel libalsa-devel libvulkan-devel ImageMagick-tools

ExclusiveArch: x86_64 aarch64

%description
ares is a multi-system emulator that began development
on October 14th, 2004. It is a descendent of higan and bsnes,
and focuses on accuracy and preservation.

%prep
%setup

%build

%make -C ./desktop-ui hiro=gtk3 build=release VERBOSE=1

%install
mkdir -p %buildroot%_datadir/%name
mkdir -p %buildroot%_desktopdir

install -Dm0755 desktop-ui/out/%name %buildroot%_bindir/%name

install -Dm 644 ./desktop-ui/resource/ares.desktop %buildroot%_desktopdir/%name.desktop
# install menu icons
for N in 16 32 48 64 128;
do
convert ./desktop-ui/resource/ares.png -scale ${N}x${N} $N.png;
install -D -m 0644 $N.png %buildroot%_iconsdir/hicolor/${N}x${N}/apps/%name.png
done

cp -dr --no-preserve=ownership ./ares/Shaders/ %buildroot%_datadir/%name/
cp -dr --no-preserve=ownership ./mia/Database/ %buildroot%_datadir/%name/

%files
%_bindir/%name
%dir %_datadir/%name/Shaders/
%dir %_datadir/%name/Database/
%_datadir/%name/Shaders/*
%_datadir/%name/Database/*
%_desktopdir/%name.desktop
%_iconsdir/hicolor/*/apps/%name.png
%doc LICENSE

%changelog
* Wed Feb 22 2023 Artyom Bystrov <arbars@altlinux.org> 131-alt1
- new version 131

* Tue Dec 20 2022 Artyom Bystrov <arbars@altlinux.org> 130.1-alt1
- Initial build for Sisyphus
