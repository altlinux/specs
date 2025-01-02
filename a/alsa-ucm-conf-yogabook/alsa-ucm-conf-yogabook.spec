Name: alsa-ucm-conf-yogabook
Version: 1.4
Release: alt1

Summary: ALSA UCM configuration for Lenovo Yoga Book
Group: System/Configuration/Hardware
License: BSD-3-Clause

Url: https://github.com/jekhor/alsa-ucm-conf-yogabook

ExclusiveArch: x86_64

Requires: alsa-ucm-conf

Source: %name-%version.tar

%description
ALSA Use Case Manager configuration files for Lenovo Yoga Book

This package contains ALSA Use Case Manager configuration files needed to get
sound at Lenovo Yoga Book tablet working.

%prep
%setup

%build

%install
mkdir -p %buildroot%_datadir/alsa
cp -ar ucm2 %buildroot%_datadir/alsa/

%files
%_datadir/alsa/ucm2/cht-yogabook
%_datadir/alsa/ucm2/conf.d/cht-yogabook

%changelog
* Thu Jan 02 2025 L.A. Kostis <lakostis@altlinux.ru> 1.4-alt1
- Initial build for ALTLinux.

