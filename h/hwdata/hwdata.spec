Name: hwdata
Version: 0.374
Release: alt1

Summary: Hardware identification and configuration data
License: GPLv2+
Group: System/Libraries

Url: https://github.com/vcrhonek/hwdata
BuildArch: noarch
Source: %name-%version.tar

Requires: pciids usbids

BuildRequires: pciids usbids

%description
hwdata contains various hardware identification and configuration data,
such as the pci.ids and usb.ids databases.

%package devel
Group: Development/Other
Summary: Development files for %name
Requires: %name = %version-%release

%description devel
The %name-devel package contains files for developing applications that use
%name.

%prep
%setup

%build
%configure

%install
%makeinstall_std libdir=/etc

rm %buildroot%_datadir/%name/pci.ids
rm %buildroot%_datadir/%name/usb.ids
ln -s ../misc/pci.ids %buildroot%_datadir/%name/pci.ids
ln -s ../misc/usb.ids %buildroot%_datadir/%name/usb.ids
rm -v %buildroot/etc/modprobe.d/dist-blacklist.conf

%files
%doc COPYING
%dir %_datadir/%name
%_datadir/%name/*

%files devel
%_datadir/pkgconfig/%name.pc

%changelog
* Mon Sep 11 2023 Roman Alifanov <ximper@altlinux.org> 0.374-alt1
- new version 0.374 (with rpmrb script)

* Thu May 04 2023 Roman Alifanov <ximper@altlinux.org> 0.370-alt1
- Initial build for Sisyphus (ALT bug 46002)
