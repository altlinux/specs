Name:     blastem
Version:  0.6.2
Release:  alt1

Summary:  open-source Sega Genesis/Mega Drive emulator developed primarily for Linux
License:  GPL-3.0
Group:    Emulators
Url:      https://www.retrodev.com/blastem/

Packager: Artyom Bystrov <arbars@altlinux.org>

Source:   %name-%version.tar
Source1: run_blastem.sh
Patch0: 0001-fix-wrong-header.patch

BuildRequires: libSDL2-devel libpng-devel zlib-devel libGLEW-devel ImageMagick-tools

ExclusiveArch: x86_64 %ix86

%description
BlastEm aims for cycle accuracy while also hitting lower system requirements than Exodus;
it is one of the only emulators to properly run Overdrive 2, a demoscene production by
the group Titan meant to showcase the capabilities of the Genesis through digital art.
The first Overdrive demo runs perfectly which only Genesis Plus GX can also claim.
Commercial game compatibility is close to, but not quite at, 100 percents. It is the only emulator
other than Exodus that can properly display direct color DMA demos and to pass all of
the tests in Nemesis' VDP FIFO Testing ROM.

%prep
%setup
%patch0 -p1

#GCC10 workaround
perl -pi -e 's|(CFLAGS:=)(-std=gnu99.*)|\1-fcommon \2|g' Makefile

%build
make blastem

%install
install -d %buildroot%_bindir
install -d %buildroot%_datadir/%name

cp -r shaders %buildroot%_datadir/%name
cp -r images %buildroot%_datadir/%name

for BIN in blastem rom.db
do
install -D -m755 $BIN %buildroot%_bindir
done

install -D -m755 %SOURCE1 %buildroot%_bindir/run_blastem

install -D -m 0644 default.cfg %buildroot%_datadir/%name
install -D -m 0644 gamecontrollerdb.txt %buildroot%_datadir/%name

mkdir -p %buildroot%_desktopdir
cat << EOF > %buildroot%_desktopdir/%name.desktop
[Desktop Entry]
Type=Application
Name=BlastEm
GenericName=picodrive
Comment=%{summary}
Exec=run_blastem
Icon=%{name}.png
Categories=Game;X-MandrivaLinux-MoreApplications-Emulators;
EOF

install -D -m 0644 icons/windows.ico %buildroot%_datadir/pixmaps/%name.png

%files

%doc README CHANGELOG COPYING
%_bindir/*
%_datadir/%name/*
%_desktopdir/%name.desktop
%_datadir/pixmaps/*

%changelog
* Thu Dec 08 2022 Artyom Bystrov <arbars@altlinux.org> 0.6.2-alt1
- Initial build for Sisyphus
