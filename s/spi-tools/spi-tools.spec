Name:     spi-tools
Version:  0.8.3
Release:  alt1

Summary:  Simple command line tools to help using Linux spidev devices
License:  GPL-2.0
Group:    Other
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
* Thu Apr 25 2019 Anton Midyukov <antohami@altlinux.org> 0.8.3-alt1
- Initial build for Sisyphus
