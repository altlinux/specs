# Unpackaged files in buildroot should terminate build
%define _unpackaged_files_terminate_build 1

Name: simulide
Summary: Simple real time electronic circuit simulator
Summary(ru_RU.UTF-8): Симулятор электронных схем в реальном времени
Version: 1.0.0
Release: alt0.1.rev1178
Group: Engineering
License: GPL-3.0-or-later
URL: https://bazaar.launchpad.net/~arcachofo/simulide
Source0: %name-%version.tar
BuildRequires: desktop-file-utils
BuildRequires: ImageMagick-tools
BuildRequires: libgpsim-devel
#BuildRequires: libelf-devel
BuildRequires: qt5-base-devel
BuildRequires: qt5-tools
BuildRequires: qt5-multimedia-devel
BuildRequires: qt5-svg-devel
BuildRequires: qt5-script-devel
BuildRequires: qt5-serialport-devel

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
touch config.h

%build
cd build_XX
%qmake_qt5
%make_build

%install
mkdir -p %buildroot%_bindir
cp build_XX/executables/SimulIDE_*/%name %buildroot%_bindir/
mkdir -p %buildroot%_datadir/%name
cp -av resources/data %buildroot%_datadir/%name/
cp -av resources/examples %buildroot%_datadir/%name/
for i in 16 32 48 64 96 128 256; do
	mkdir -p %buildroot%_iconsdir/hicolor/${i}x${i}/apps/
	convert resources/icons/hicolor/256x256/%name.png -resize "$i"x"$i" \
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
%doc README.md resources/examples
%_bindir/%name
%_datadir/%name
%_desktopdir/%name.desktop
%_iconsdir/hicolor/*/apps/*.png

%changelog
* Mon Dec 19 2022 Anton Midyukov <antohami@altlinux.org> 1.0.0-alt0.1.rev1178
- Initial build
