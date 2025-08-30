# Unpackaged files in buildroot should terminate build
%define _unpackaged_files_terminate_build 1

%define shortcommit 9c568baa

# examples for oter arches
%add_verify_elf_skiplist %_datadir/simulide/examples/*

Name: simulide
Summary: Simple real time electronic circuit simulator
Summary(ru_RU.UTF-8): Симулятор электронных схем в реальном времени
Version: 1.2.0
Release: alt0.00.%shortcommit.1
Group: Engineering
License: GPL-3.0-or-later
URL: https://launchpad.net/simulide
VCS: https://github.com/eeTools/SimulIDE-dev.git

Source0: %name-%version.tar
Patch: %name-%version-%release.patch

# https://github.com/eeTools/SimulIDE-dev/issues/19
ExcludeArch: aarch64

BuildRequires: desktop-file-utils
BuildRequires: ImageMagick-tools
BuildRequires: libgpsim-devel
BuildRequires: qt5-base-devel
BuildRequires: qt5-tools
BuildRequires: qt5-multimedia-devel
BuildRequires: qt5-svg-devel
#BuildRequires: qt5-script-devel
BuildRequires: qt5-serialport-devel
BuildRequires: zlib-devel

%description
Simulide is a real time electronic circuit simulator intended for hobbist and
student experimentation with simple general purpose electronic circuits and
PIC, AVR and Arduino microcontroller simulations.

PIC and AVR simulation are provided by gpsim and simavr.

%description -l ru_RU.UTF-8
Simulide является симулятором электронных схем в реальном времени, предназначенный
для любительских и студенческие экспериментов с простыми электронными схемами общего
назначения и моделирования микроконтроллеров PIC, AVR и Arduino.

Эмуляция PIC и AVR микроконтроллеров предоставляется gpsim и simavr.

%prep
%setup
%autopatch -p1
touch config.h

# Fix revision information
sed -i 's/REV_NO =.*/REV_NO = %shortcommit/' SimulIDE.pri

%build
cd build_XX
%qmake_qt5
%make_build

%install
mkdir -p %buildroot%_bindir
cp build_XX/executables/SimulIDE_*/%name %buildroot%_bindir/
mkdir -p %buildroot%_datadir/%name
cp -av resources/data %buildroot%_datadir/%name/
for i in 16 32 48 64 96 128 256; do
	mkdir -p %buildroot%_iconsdir/hicolor/${i}x${i}/apps/
	convert resources/icons/%name.png -resize "$i"x"$i" \
		%buildroot%_iconsdir/hicolor/"$i"x"$i"/apps/%name.png
done

### == desktop file
mkdir -p %buildroot%_desktopdir
cat>%buildroot%_desktopdir/%name.desktop<<END
[Desktop Entry]
Name=SimulIDE
GenericName=SimulIDE
Comment=Electronic Circuit Simulator Software
Comment[ru]=Симулятор электронных схем
Exec=%name
Icon=%name.png
Terminal=false
Type=Application
Categories=Education;Electronics;
END

%files
%doc README.md
%_bindir/%name
%_datadir/%name
%_desktopdir/%name.desktop
%_iconsdir/hicolor/*/apps/*.png

%changelog
* Sat Aug 30 2025 Anton Midyukov <antohami@altlinux.org> 1.2.0-alt0.00.9c568baa.1
- new snapshot
- spec: add VCS tag
- build from git
- ExcludeArch: aarch64

* Fri Nov 15 2024 Anton Midyukov <antohami@altlinux.org> 1.1.0-alt1.rev1917
- Release 1.1.0 (Closes: 52052)

* Sat Mar 18 2023 Anton Midyukov <antohami@altlinux.org> 1.0.0-alt1.rev1320
- Release 1.0.0
- Fix revision information (thanks w00zy)
- Fix russian translation (thanks w00zy)
- Fix path for compile (thanks w00zy)
- Fix Url

* Mon Dec 19 2022 Anton Midyukov <antohami@altlinux.org> 1.0.0-alt0.1.rev1178
- Initial build
