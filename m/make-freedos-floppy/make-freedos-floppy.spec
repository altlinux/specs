Name: make-freedos-floppy
Version: 1.1
Release: alt1

Summary: Create bootable FreeDOS floppy image from scratch
License: GPL
Group: System/Kernel and hardware

# thanks raorn@ for the hint, ms-sys <= 2.2.1 won't do
Url: http://www.freedos.org/freedos/files/
Source0: http://www.ibiblio.org/pub/micro/pc-stuff/freedos/files/dos/sys/sys-freedos-linux/sys-freedos-linux.zip
Source1: make-freedos-floppy

BuildArch: noarch

BuildRequires: nasm unzip
Requires: dosemu-freedos glibc-gconv-modules mtools
# Suggests: qemu-system

%description
The tool creating a bootable FreeDOS floppy image.

%prep
%setup -c -n sys-freedos-linux
sed -i "s,dirname(\$0),\"%_datadir/%name\"," sys-freedos.pl

%build
pushd bootsecs
nasm -o boot32lb.mbr boot32lb.asm
nasm -o boot32.mbr boot32.asm
nasm -o boot16.mbr -dISFAT16 boot.asm
nasm -o boot12.mbr -dISFAT12 boot.asm
popd

%install
mkdir -p %buildroot{%_bindir,%_datadir/%name}
cp -a bootsecs %buildroot%_datadir/%name
install -pm755 %SOURCE1 sys-freedos.pl %buildroot%_bindir/

%files
%_bindir/*
%_datadir/%name

%changelog
* Tue Sep 06 2011 Michael Shigorin <mike@altlinux.org> 1.1-alt1
- compile all bootsectors at package build time
- partially rewrote sys-freedos.pl to use precompiled bootsector
- added missing Requires: (regarding "codepage 850")

* Tue Sep 06 2011 Michael Shigorin <mike@altlinux.org> 1.0-alt2
- wrapped qemu to avoid autodependency
- minor spec cleanup

* Tue Sep 06 2011 Mykola Grechukh <gns@altlinux.ru> 1.0-alt1
- initial build for Sisyphus
