%define _unpackaged_files_terminate_build 1

Name: pve-http-server
Summary: Proxmox Asynchrounous HTTP Server Implementation
Version: 5.1.2
Release: alt0.1
License: AGPL-3.0+
Group: Development/Perl
Url: https://www.proxmox.com
Vcs: git://git.proxmox.com/git/pve-http-server.git
Source: %name-%version.tar

ExclusiveArch: x86_64 aarch64

Provides: perl-%name = %EVR
# from debian/control
Provides: libpve-http-server-perl = %EVR
#Conflicts: pve-storage < 8.2.5
#Conflicts: pmg-api < 8.1.4
#Conflicts: pve-manager < 8.2.7

Requires: fonts-font-awesome javascript-jquery javascript-bootstrap

BuildRequires: perl(AnyEvent/HTTP.pm) perl(AnyEvent/Handle.pm) perl(AnyEvent/IO.pm) perl(AnyEvent/Socket.pm) perl(AnyEvent/TLS.pm) perl(AnyEvent/Util.pm)
BuildRequires: perl(Compress/Zlib.pm)
BuildRequires: perl(Digest/MD5.pm) perl(Digest/SHA.pm) perl(Encode.pm)
BuildRequires: perl(Net/SSLeay.pm)
BuildRequires: perl(Time/HiRes.pm)
BuildRequires: perl(HTTP/Date.pm) perl(HTTP/Headers.pm) perl(HTTP/Request.pm) perl(HTTP/Response.pm) perl(HTTP/Status.pm) perl(HTML/Entities.pm)
BuildRequires: perl(JSON.pm)
BuildRequires: perl(Net/IP.pm)
BuildRequires: perl(URI/Escape.pm) perl(URI.pm)
BuildRequires: perl(PVE/INotify.pm) perl(PVE/SafeSyslog.pm) perl(PVE/Tools.pm) perl(PVE/JSONSchema.pm)

%description
%summary.
This package is used as base to implement the REST API in all perl based

%prep
%setup

%install
%makeinstall_std -C src

%files
%doc debian/copyright
%perl_vendor_privlib/PVE/*

%changelog
* Sun Oct 20 2024 Alexey Shabalin <shaba@altlinux.org> 5.1.2-alt0.1
- 5.1.2
- bootstrap, build without conflicts

* Thu Aug 29 2024 Andrew A. Vasilyev <andy@altlinux.org> 5.1.0-alt1
- 5.1.0

* Fri Mar 29 2024 Andrew A. Vasilyev <andy@altlinux.org> 5.0.6-alt1
- 5.0.6

* Wed Feb 28 2024 Andrew A. Vasilyev <andy@altlinux.org> 5.0.5-alt1
- 5.0.5

* Thu May 25 2023 Andrew A. Vasilyev <andy@altlinux.org> 4.2.3-alt1
- 4.2-3
- add copyright file

* Mon Mar 20 2023 Andrew A. Vasilyev <andy@altlinux.org> 4.2.1-alt1
- 4.2-1

* Sat Mar 11 2023 Andrew A. Vasilyev <andy@altlinux.org> 4.1.6-alt1
- 4.1-6

* Mon Nov 14 2022 Alexey Shabalin <shaba@altlinux.org> 4.1.5-alt1
- 4.1-5

* Fri Oct 07 2022 Andrew A. Vasilyev <andy@altlinux.org> 4.1.4-alt2
- fix CPU eating loop

* Mon Oct 03 2022 Alexey Shabalin <shaba@altlinux.org> 4.1.4-alt1
- 4.1-4

* Thu Jul 07 2022 Andrew A. Vasilyev <andy@altlinux.org> 4.1.3-alt1
- 4.1-3

* Thu Feb 17 2022 Alexey Shabalin <shaba@altlinux.org> 4.1.1-alt1
- 4.1-1
- build as separate package

