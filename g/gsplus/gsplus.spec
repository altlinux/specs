Name: gsplus
Version: 0.14
Release: alt1

Summary: Modern cross-platform Apple IIgs emulator and tools based on KEGS
License: GPL-2.0
Group: Emulators
Url: https://github.com/digarok/gsplus

Packager: Artyom Bystrov <arbars@altlinux.org>

Source: %name-%version.tar
BuildRequires(Pre): rpm-macros-cmake
BuildRequires: gcc-c++ cmake re2c libSDL2-devel libSDL2_image-devel libfreetype-devel libpcap-devel libreadline-devel

%description
%summary

%prep
%setup

%build
%cmake
%cmake_build

%install
# There is no automated install; go manually:
# 1. Create needed dirs
mkdir -pm 0755 %buildroot%_bindir
mkdir -pm 0755 %buildroot%_datadir/%name
for i in 16 32 64 128 256 512; do
	mkdir -pm 0755 %buildroot%_iconsdir/hicolor/${i}x${i}/apps/
done
# 2. Install the binary
install -m 0755 %_cmake__builddir/bin/GSplus %buildroot%_bindir/%name
# 3. Provide a menu entry for it
install -d %buildroot%_desktopdir
cat << EOF > %buildroot%_desktopdir/%name.desktop
[Desktop Entry]
Type=Application
Name=%name
Comment=%summary
Exec=%name
Icon=%name
Categories=Game;X-MandrivaLinux-MoreApplications-Emulators;
EOF
# 4. Install the sample config file
install -m 0644 -t %buildroot%_datadir/%name/ src/config.txt
# 5. Install the icons
for i in 16 32 64 128 256 512; do
	install -m 0644 assets/gsp_icon_${i}.png %buildroot%_iconsdir/hicolor/${i}x${i}/apps/%name.png
done

%files
%doc LICENSE.txt README.md
%doc doc/gsplusmanual.pdf
%_bindir/%name
%_datadir/%name/*
%_iconsdir/hicolor/*/apps/%name.png
%_desktopdir/%name.desktop

%changelog
* Wed May 24 2023 Artyom Bystrov <arbars@altlinux.org> 0.14-alt1
- Initial build for Sisyphus
