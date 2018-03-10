Name: libremodbus-source
Version: 2017.12.27
Release: alt1

Summary: YAPLC runtime environment project
License: GPLv3+
Group: Development/Other
Url: https://github.com/nucleron/libremodbus

Packager: Anton Midyukov <antohami@altlinux.org>

Source: libremodbus-source-%version.tar

Buildarch: noarch

%description
Open Source ARM cortex m microcontroller library

%prep
%setup
rm -fr .gear

%build

%install
mkdir -p %buildroot%_prefix/src/libremodbus
cp -r * %buildroot%_prefix/src/libremodbus

%files
%_prefix/src/libremodbus

%changelog
* Sat Mar 10 2017 Anton Midyukov <antohami@altlinux.org> 2017.12.27-alt1
- Initial build for ALT Sisyphus
