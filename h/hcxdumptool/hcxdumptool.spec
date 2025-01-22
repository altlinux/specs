%define _unpackaged_files_terminate_build 1

Name: hcxdumptool
Version: 6.3.5
Release: alt1

Summary: Small tool to capture packets from wlan devices
License: MIT
Group: Security/Networking
Url: https://github.com/ZerBea/hcxdumptool 
Vcs: https://github.com/ZerBea/hcxdumptool

Source: %name-%version.tar
Patch: %name-%version-alt.patch

BuildRequires: libpcap-devel

%description
A tool to capture packets from WLAN devices and to discover potential
weak points within own WiFi networks by running layer 2 attacks against
the WPA protocol.

%prep
%setup
%autopatch -p1

%build
%make_build

%install
%makeinstall_std PREFIX=%prefix

%files
%_bindir/*
%doc README.md license.txt changelog 

%changelog
* Fri Jan 17 2025 Artem Krasovskiy <aibure@altlinux.org> 6.3.5-alt1
- Initial Build

