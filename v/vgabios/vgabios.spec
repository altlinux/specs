
Name: vgabios
Version: 0.7a
Release: alt1
Summary: LGPL implementation of a vga video bios

Group: Emulators
License: LGPLv2
Url: http://www.nongnu.org/vgabios/
Packager: Alexey Shabalin <shaba@altlinux.ru>

Source: http://savannah.gnu.org/download/%name/%name-%version.tgz

Patch03: 0003-Add-qemu-stdvga-pci-bios.patch
Patch05: 0005-Add-qemu-vmware-vga-pci-bios.patch
Patch06: 0006-Add-qemu-qxl-vga-pci-bios.patch

BuildRequires: dev86
BuildArch: noarch

%description
vgabios is an LPGL implementation of a bios for a video card.
It is tied to plex86/bochs, althoug it will likely work on other
emulators. It is not intended for use in real cards.

%prep
%setup -n %name-%version

%patch03 -p1
%patch05 -p1
%patch06 -p1

%build
make clean
%make_build biossums
%make_build

%install
mkdir -p %buildroot%_datadir/%name
install -m 0644 VGABIOS-lgpl-*.bin %buildroot%_datadir/%name

%files
%dir %_datadir/%name
%doc README COPYING
%_datadir/%name/VGABIOS-lgpl-*.bin

%changelog
* Fri Dec 02 2011 Alexey Shabalin <shaba@altlinux.ru> 0.7a-alt1
- 0.7a

* Fri Dec 24 2010 Alexey Shabalin <shaba@altlinux.ru> 0.6c-alt1
- initial build for ALT Linux Sisyphus (based on fedora spec)
