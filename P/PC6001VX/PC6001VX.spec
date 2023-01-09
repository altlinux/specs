Name:     PC6001VX
Version:  4.1.2
Release:  alt1

Summary:  Cross platform version of NEC PC-6001 emulator based on PC6001V
License:  LGPL-2.1
Group:    Emulators
Url:      https://github.com/eighttails/PC6001VX

Packager: Artyom Bystrov <arbars@altlinux.org>

Source:   %name-%version.tar
Source1: PC6001VX.eng.6
Source2: PC6001VX.rus.6

BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake gcc-c++ libSDL2_mixer-devel libSDL2-devel libpng-devel zlib-devel ninja-build qt6-base-devel qt6-websockets-devel qt6-shadertools-devel qt6-5compat-devel qt6-multimedia-devel

%description
Cross platform version of NEC PC-6001 emulator based on PC6001V. 

IMPORTANT INFORMATION!

Open source BASIC images was placed in %_datadir/%name/compatible_rom folder. In first run
program saying "No ROM files found. Please copy ROM files to the ROM folder
(/home/USERNAME/.pc6001vx4/rom/) or specify another folder. Do you want to specify another folder?"
Press "No" button and after this program answer "Do you want to use the built-in compatible ROM?".
Press "Yes" and start to using Emulator.

Choose number of pages of memory for soft usage (look on name of soft image for this computer)

Functional menu pinned on the right mouse button. Press them and ro to "Tape > Insert..." and choose
image file with program what you need.

Next, type "cload" in emulator and press Enter, the program will start to load. After that, type "run",
and program will start.

%prep
%setup

%build

qmake6 PC6001VX.pro
%make_build

%install
install -d %buildroot%_bindir
install -d %buildroot%_datadir/%name/compatible_rom/basic60-v075
install -d %buildroot%_datadir/%name/compatible_rom/basic66-v042
install -d %buildroot%_man6dir/ru/man6

install -pDm755 %name %buildroot%_bindir

mkdir -p %buildroot%_desktopdir
cat << EOF > %buildroot%_desktopdir/%name.desktop
[Desktop Entry]
Type=Application
Name= PC6001VX
GenericName=PC6001VX
Comment=%{summary}
Exec=%name
Icon=%{name}.png
Categories=Game;X-MandrivaLinux-MoreApplications-Emulators;
EOF

for N in 16 32 48 64 128;
do
install -D -m 0644 data/PC-6001_${N}.png %buildroot%_iconsdir/hicolor/${N}x${N}/apps/%name.png
done

cp -r compatible_rom/basic66-v042/BASIC* %buildroot%_datadir/%name/compatible_rom/basic66-v042
cp -r compatible_rom/basic66-v042/VOICEROM* %buildroot%_datadir/%name/compatible_rom/basic66-v042
cp -r compatible_rom/basic60-v075/BASIC* %buildroot%_datadir/%name/compatible_rom/basic60-v075
cp -r fonts %buildroot%_datadir/%name/

install -D -m 0644 %SOURCE1 %buildroot%_man6dir/%name.6
install -D -m 0644 %SOURCE2 %buildroot%_man6dir/ru/man6/%name.6

%files
%_bindir/%name
%_datadir/%name/*
%_desktopdir/%name.desktop
%_iconsdir/hicolor/*/apps/%name.png
%_man6dir/*
%doc LICENSE README.adoc

%changelog
* Mon Jan 09 2023 Artyom Bystrov <arbars@altlinux.org> 4.1.2-alt1
- new version 4.1.2

* Sun Jan 08 2023 Artyom Bystrov <arbars@altlinux.org> 4.1.1-alt1
- Initial build for Sisyphus
