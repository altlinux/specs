Name:     spi-tools
Version:  1.0.0
Release:  alt1

Summary:  Simple command line tools to help using Linux spidev devices
License:  GPL-2.0
Group:    System/Kernel and hardware
Url:      https://github.com/cpb-/spi-tools

Packager: Anton Midyukov <antohami@altlinux.org>

Source:   %name-%version.tar

Buildrequires: help2man

%description
%summary

%prep
%setup

%build
%autoreconf 
%configure
%make_build

%install
%makeinstall_std

%files
%_bindir/*
%_man1dir/*
%doc *.md

%changelog
* Sat Oct 02 2021 Anton Midyukov <antohami@altlinux.org> 1.0.0-alt1
- new version 1.0.0
- fix Group tag

* Sun Jun 27 2021 Anton Midyukov <antohami@altlinux.org> 0.8.7-alt1
- new version 0.8.7

* Sun Mar 22 2020 Anton Midyukov <antohami@altlinux.org> 0.8.4-alt1
- new version 0.8.4

* Thu Apr 25 2019 Anton Midyukov <antohami@altlinux.org> 0.8.3-alt1
- Initial build for Sisyphus
