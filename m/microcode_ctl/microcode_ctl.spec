Name: microcode_ctl
Version: 2.0
Release: alt0.2
Epoch: 1

Packager: L.A. Kostis <lakostis@altlinux.org>

Summary: Tool to update x86/x86-64 CPU microcode
License: GPLv2+
Group: System/Kernel and hardware

URL: http://fedorahosted.org/microcode_ctl
Source0: http://fedorahosted.org/released/microcode_ctl/%{name}-%{version}.tar.xz

%description
The microcode_ctl utility is a companion to the microcode driver written
by Tigran Aivazian <tigran@aivazian.fsnet.co.uk>.

The microcode update is volatile and needs to be uploaded on each system
boot i.e. it doesn't reflash your cpu permanently, reboot and it reverts
back to the old microcode.

%package -n firmware-intel-ucode
Summary: Microcode definitions for Intel processors
License: INTEL SOFTWARE LICENSE AGREEMENT
Group: System/Kernel and hardware
Provides: microcode-data-intel = %version-%release
Obsoletes: microcode-data-intel <= 20130222-alt2
BuildArch: noarch

%description -n firmware-intel-ucode
The microcode data file for Linux contains the latest microcode
definitions for all Intel processors.

%package -n firmware-amd-ucode
Summary: Microcode patches for AMD processors
License: ADVANCED MICRO DEVICES INC SOFTWARE LICENSE AGREEMENT
Group: System/Kernel and hardware
Obsoletes: firmware-amd-ucode <= 20120910-alt1
BuildArch: noarch

%description -n firmware-amd-ucode
This package provides latest microcode patches for AMD processor
families >= 0x10.

%prep
%setup -q

%build
%make_build CFLAGS="%optflags"

%install
make DESTDIR=%{buildroot} PREFIX=%{_prefix} INSDIR=/usr/sbin install clean
rm -f *amd*.tar
cp -a %buildroot/usr/share/doc/microcode_ctl/*amd* .

%files
%_sbindir/intel-microcode2ucode
%doc README Change*

%files -n firmware-intel-ucode
%dir /lib/firmware/intel-ucode
/lib/firmware/intel-ucode/*

%files -n firmware-amd-ucode
%dir /lib/firmware/amd-ucode
/lib/firmware/amd-ucode/*
%doc *amd*

%changelog
* Mon Apr 08 2013 L.A. Kostis <lakostis@altlinux.ru> 1:2.0-alt0.2
- Get rid of versioning mess.

* Mon Apr 08 2013 L.A. Kostis <lakostis@altlinux.ru> 2.0-alt0.1
- 2.0 release from fedora.
- it's just a helper for seamless in-kernel firmware management.
- combine separate firmware files.

* Tue Nov 09 2010 Victor Forsiuk <force@altlinux.org> 1.17-alt2
- Package only utility. Microcode data will be in separate packages.
- Move utility from %_sbindir to /sbin.
- Use /lib/microcode for microcode data instead of /etc.

* Wed May 02 2007 Victor Forsyuk <force@altlinux.org> 1.17-alt1
- 1.17

* Mon Apr 02 2007 Victor Forsyuk <force@altlinux.org> 1.16-alt2
- Comment ExclusiveArch for now.

* Tue Mar 27 2007 Victor Forsyuk <force@altlinux.org> 1.16-alt1
- 1.16

* Mon Nov 13 2006 Denis Smirnov <mithraen@altlinux.ru> 1.14-alt1
- Update to 1.14

* Mon Dec 12 2005 Victor Forsyuk <force@altlinux.ru> 1.12-alt2
- Shift service start priority to run after udev is up.
- Remove microcode kernel module after microcode uploading.

* Wed Oct 19 2005 Victor Forsyuk <force@altlinux.ru> 1.12-alt1
- Initial build.
