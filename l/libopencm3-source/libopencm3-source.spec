Name: libopencm3-source
Version: 2.8
Release: alt1.20161001

Summary: Open Source ARM cortex m microcontroller library
License: GPLv3+ and LGPLv3+
Group: Development/Other
Url: https://github.com/nucleron/libopencm3

Packager: Anton Midyukov <antohami@altlinux.org>

Source: libopencm3-source-%version.tar

Buildarch: noarch

%description
Open Source ARM cortex m microcontroller library

%prep
%setup
rm -fr .gear

%build

%install
mkdir -p %buildroot%_prefix/src/libopencm3
cp -r * %buildroot%_prefix/src/libopencm3

%files
%_prefix/src/libopencm3

%changelog
* Sat Mar 10 2017 Anton Midyukov <antohami@altlinux.org> 2.8-alt1.20161001
- Initial build for ALT Sisyphus
