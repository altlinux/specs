Name: opensd
Version: 0.48.0
Release: alt1.1

Summary: An open-source Linux userspace driver for Valve's Steam Deck hardware
License: GPLv3
Group: System/Libraries

Url: https://gitlab.com/open-sd/opensd

ExclusiveArch: x86_64

Packager: Artyom Bystrov <arbars@altlinux.org>

Source: %name-%version.tar

BuildRequires: cmake gcc-c++ rpm-macros-cmake 

%description
OpenSD is a highly-configurable userspace driver for the Steam Deck written in modern C++.
It aims to be lighweight, very fast and provide a way to fully utilize the hardware without
running any closed-source, proprietary or anti-privacy software like Steam.

%prep
%setup -n %name-%version

%build
%cmake_insource \
	-DOPT_POSTINSTALL=FALSE \
	-DCMAKE_BUILD_TYPE=Release

%cmake_build

%install
%cmakeinstall_std

%files
%_bindir/opensdd
%_datadir/%name
%_libexecdir/systemd/*/%name.service
%_docdir/%name/*
%_udevrulesdir/60-opensd.rules
%_man5dir/*
%_man1dir/*

%changelog
* Sat Jul 13 2024 Artyom Bystrov <arbars@altlinux.org> 0.48.0-alt1.1
- fix path to udev rule

* Sat Jul 01 2023 Artyom Bystrov <arbars@altlinux.org> 0.48.0-alt1
- Initial commit in Sisyphus
