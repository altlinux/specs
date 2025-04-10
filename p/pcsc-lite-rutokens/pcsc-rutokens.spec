%define _unpackaged_files_terminate_build 1
%define realname rutokens-driver
%define libpcsclite_usbdropdir %(pkg-config libpcsclite --variable=usbdropdir)

Name: pcsc-lite-rutokens
Version: 1.0.9
Release: alt2
License: LGPL-2.1+
Group: System/Configuration/Hardware
Url: http://www.rutoken.ru/support/download/drivers-for-nix/
Summary: USB IFD Handler for RutokenS

BuildRequires: pkgconfig(libpcsclite) >= 1.3.3
BuildRequires: pkgconfig(libusb)

Provides: %realname ifd-rutokens
Provides: pcsc-ifd-handler
Requires(pre): pcsc-lite

# https://github.com/AktivCo/rutokens-driver
Source: %name-%version.tar

%description
%summary.

%prep
%setup

%build
%autoreconf
%configure \
	--disable-static \
	--enable-usbdropdir=%libpcsclite_usbdropdir \
	--disable-udevrules
%make_build

%install
%makeinstall_std

%post
# Restart pcscd
%post_service pcscd

%files
%doc AUTHORS COPYING NEWS README
%libpcsclite_usbdropdir/ifd-rutokens.bundle

%changelog
* Thu Apr 10 2025 Alexey Shabalin <shaba@altlinux.org> 1.0.9-alt2
- Add Provides: pcsc-ifd-handler.
- Restart pcscd after install ifd-rutokens.

* Mon Feb 20 2023 Andrey Cherepanov <cas@altlinux.org> 1.0.9-alt1
- New version.

* Mon Apr 05 2021 Andrey Cherepanov <cas@altlinux.org> 1.0.7-alt1
- New version.

* Sat Mar 14 2020 Andrey Cherepanov <cas@altlinux.org> 1.0.6-alt1
- New version.

* Mon Oct 07 2019 Andrey Cherepanov <cas@altlinux.org> 1.0.5-alt1
- New version.

* Thu Sep 15 2016 Andrey Cherepanov <cas@altlinux.org> 1.0.4-alt1
- New version

* Wed Apr 02 2014 Gleb F-Malinovskiy <glebfm@altlinux.org> 1.0.3-alt1
- Initial build.
