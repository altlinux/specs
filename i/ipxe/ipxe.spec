%define formats rom
%define qemuroms rtl8139 e1000_82540 virtio-net pcnet32 ne2k_isa ns8390 eepro100

Name: ipxe
Version: 1.0.0
Release: alt2.git174df77

Summary: PXE boot firmware
License: GPLv2+
Group: Networking/Other
Url: http://ipxe.org/
#Vcs-Git: git://git.ipxe.org/ipxe.git
BuildArch: noarch
Provides: gpxe
Obsoletes: gpxe

Source: %name-%version.tar
Patch: %name-%version-%release.patch

Requires: ipxe-bootimgs
BuildRequires: mkisofs mtools syslinux

%description
iPXE is the leading open source network boot firmware.
It provides a full PXE implementation enhanced with additional features such as:
- boot from a web server via HTTP
- boot from an iSCSI SAN
- boot from a Fibre Channel SAN via FCoE
- boot from an AoE SAN
- boot from a wireless network
- boot from a wide-area network
- boot from an Infiniband network
- control the boot process with a script

You can use iPXE to replace the existing PXE ROM on your network card,
or you can chainload into iPXE to obtain the features of iPXE without the hassle of reflashing.

%package bootimgs
Summary: Network boot loader images in bootable USB, CD, floppy and GRUB formats
Group: Development/Tools
Provides: gpxe-bootimgs
Obsoletes: gpxe-bootimgs

%description bootimgs
iPXE is an implementation of the PXE specification for network
booting, with extensions to allow additional features such as booting
via HTTP, iSCSI, and AoE.

This package contains the iPXE boot images in USB, CD, floppy, and PXE
UNDI formats.

%package roms
Summary: Network boot loader roms in .rom format
Group: Development/Tools
Requires: %name-roms-qemu = %version-%release
Provides: gpxe-roms
Obsoletes: gpxe-roms

%description roms
iPXE is an implementation of the PXE specification for network
booting, with extensions to allow additional features such as booting
via HTTP, iSCSI, and AoE.

This package contains the iPXE roms in .rom format.

%package roms-qemu
Summary: Network boot loader roms supported by QEMU, .rom format
Group: Development/Tools
Provides: gpxe-roms-qemu
Obsoletes: gpxe-roms-qemu

%description roms-qemu
iPXE is an implementation of the PXE specification for network
booting, with extensions to allow additional features such as booting
via HTTP, iSCSI, and AoE.

This package contains the iPXE ROMs for devices emulated by QEMU, in
.rom format.

%prep
%setup
%patch -p1

%build
make -C src V=1 NO_WERROR=1 all allbaseroms bin/ipxe.pxe

%install
mkdir -p %buildroot%_libexecdir/%name

pushd src/bin/

install -pm0644 ipxe.{dsk,iso,usb,lkrn,pxe} undionly.kpxe %buildroot%_libexecdir/%name

for fmt in %formats; do
 for img in *.${fmt}; do
      if [ -e $img ]; then
   cp -a $img %buildroot%_libexecdir/%name/
   echo %_libexecdir/%name/$img >> ../../${fmt}.list
  fi
 done
done
popd

# the roms supported by qemu will be packaged separatedly
# remove from the main rom list and add them to qemu.list
for fmt in rom ; do
 for rom in %qemuroms ; do
  sed -i -e "/\/${rom}.${fmt}/d" ${fmt}.list
  echo %_libexecdir/%name/${rom}.${fmt} >> qemu.${fmt}.list
 done
done

%files
%doc README

%files bootimgs
%dir %_libexecdir/%name
%_libexecdir/%name/ipxe.iso
%_libexecdir/%name/ipxe.usb
%_libexecdir/%name/ipxe.dsk
%_libexecdir/%name/ipxe.lkrn
%_libexecdir/%name/ipxe.pxe
%_libexecdir/%name/undionly.kpxe
%doc COPYING COPYRIGHTS

%files roms -f rom.list
%doc COPYING COPYRIGHTS

%files roms-qemu -f qemu.rom.list
%doc COPYING COPYRIGHTS

%changelog
* Fri Aug 12 2011 Alexey Shabalin <shaba@altlinux.ru> 1.0.0-alt2.git174df77
- add Provides Obsoletes for gpxe

* Thu Aug 11 2011 Alexey Shabalin <shaba@altlinux.ru> 1.0.0-alt1.git174df77
- Initial build.
