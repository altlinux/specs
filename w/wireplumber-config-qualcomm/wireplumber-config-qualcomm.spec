%define _unpackaged_files_terminate_build 1
%define _wireplumberdir %_datadir/wireplumber/wireplumber.conf.d

Name: wireplumber-config-qualcomm
Version: 1
Release: alt1
Summary: Qualcomm config for wireplumber
License: MIT
Group: System/Kernel and hardware

BuildArch: noarch

Source: %name-%version.tar

%description
%summary.

%prep
%setup

%install
mkdir -p %buildroot%_wireplumberdir
install -Dm 0644 qualcomm-sound.conf %buildroot%_wireplumberdir

%files
%_wireplumberdir/*.conf

%changelog
* Sat May 09 2026 Vasiliy Doylov <neko@altlinux.org> 1-alt1
- Initial build for ALT
