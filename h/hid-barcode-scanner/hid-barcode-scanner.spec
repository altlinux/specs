Name: hid-barcode-scanner
Version: 0.1
Release: alt1

Summary: HID barcode scanner interface
Group: System/Kernel and hardware
License: GPL
Url: http://git.altlinux.org/people/prividen/packages/hid-barcode-scanner.git
Packager: Michael A. Kangin <prividen@altlinux.org>

Requires: libhid
BuildRequires: libhid-devel

Source0: %name-%version.tar.gz


%description
%name allow to detach HID device (e.g. barcode scanner) from console
and send all data from this device to the standart output.

%prep
%setup -q

%build
%make_build

%install
%make DESTDIR=%buildroot install

%files
%_bindir/*
%doc README

%changelog
* Fri May 08 2009 Michael A. Kangin <prividen@altlinux.org> 0.1-alt1
- Release for Sisyphus

* Sun Mar 22 2009 Michael A. Kangin <prividen@altlinux.org> 0.1-alt0.1
- Initial build

