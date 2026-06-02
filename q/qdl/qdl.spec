%define _unpackaged_files_terminate_build 1

Name: qdl
Version: 2.6
Release: alt1

Summary: Tool to communicate with Qualcomm System On a Chip bootroms to install or execute code
License: BSD-3-Clause
Group: Development/Tools

Url: https://github.com/linux-msm/qdl

Source: %name-%version.tar

BuildRequires: gcc-c++ make
BuildRequires: libxml2-devel libusb-devel help2man


%description
This tool communicates with Qualcomm EDL USB devices (Vendor ID 05c6, Product IDs 9008, 900e, 901d)
to upload a flash loader and use it to flash images.

%prep
%setup

%build
%make_build VERSION="%version"
%make manpages

%install
%makeinstall
install -vDm644 ./*.1 -t %{buildroot}%{_man1dir}

%check
%make tests


%files
%doc README.md
%_bindir/*
%_man1dir/*


%changelog
* Tue Jun 2 2026 Andrey Alekseev <parovoz@altlinux.org> 2.6-alt1
- Initial build for Sisyphus
