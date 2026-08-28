%define _unpackaged_files_terminate_build 1

Name: alsa-ucm-conf-asahi
Version: 10
Release: alt1
Summary: ALSA UCM configuration for Apple silicon based devices
License: BSD-3-Clause
Group: System/Configuration/Hardware
Url: https://github.com/AsahiLinux/alsa-ucm-conf-asahi/
VCS: https://github.com/AsahiLinux/alsa-ucm-conf-asahi.git
ExclusiveArch: aarch64

Source: %name-%version.tar

Requires: alsa-ucm-conf

%description
This package contains ALSA Use Case Manager configuration files needed to get
sound on any apple silicon based device, like macbook air m1.

%prep
%setup

%build

%install
mkdir -p %buildroot%_datadir/alsa/
cp -rv ucm2/ %buildroot%_datadir/alsa/

%files
%_datadir/alsa/ucm2

%changelog
* Thu Aug 27 2026 Vasiliy Doylov <neko@altlinux.org> 10-alt1
- Initial build for ALT.
