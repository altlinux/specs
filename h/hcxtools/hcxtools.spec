%define _unpackaged_files_terminate_build 1

Name: hcxtools
Version: 6.3.5
Release: alt1

Summary: Tools to convert packets from capture files to hash files
License: MIT
Group: Security/Networking
Url: https://github.com/ZerBea/hcxtools 
Vcs: https://github.com/ZerBea/hcxtools

Source: %name-%version.tar
Patch: %name-%version-alt.patch

BuildRequires: libcurl-devel
BuildRequires: openssl-devel
BuildRequires: zlib-devel

%description
A small set of tools to convert packets from capture files to hash files
for use with Hashcat or John the Ripper.

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

