%define _unpackaged_files_terminate_build 1

Name: qdl
Version: 2.8
Release: alt1

Summary: Tool to communicate with Qualcomm System On a Chip bootroms to install or execute code
License: BSD-3-Clause
Group: Development/Tools

Url: https://github.com/linux-msm/qdl

Source: %name-%version.tar

BuildRequires: gcc-c++ meson
BuildRequires: libxml2-devel libusb-devel libzip-devel help2man
%{?!_without_check:%{?!_disable_check:BuildRequires: libcmocka-devel zip}}

%description
This tool communicates with Qualcomm EDL USB devices (Vendor ID 05c6, Product IDs 9008, 900e, 901d)
to upload a flash loader and use it to flash images.

%prep
%setup

%build
%meson -DVERSION="%version"
%meson_build

%install
%meson_install

%check
%meson_test


%files
%doc README.md
%_bindir/*
%_man1dir/*


%changelog
* Mon Aug 3 2026 Andrey Alekseev <parovoz@altlinux.org> 2.8-alt1
- New version

* Tue Jun 2 2026 Andrey Alekseev <parovoz@altlinux.org> 2.6-alt1
- Initial build for Sisyphus
