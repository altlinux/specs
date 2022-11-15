%define _unpackaged_files_terminate_build 1

Name: pve-http-server
Summary: Proxmox Asynchrounous HTTP Server Implementation
Version: 4.1.5
Release: alt1
License: AGPL-3.0+
Group: Development/Perl
Url: https://www.proxmox.com
Vcs: git://git.proxmox.com/git/pve-http-server.git
Source: %name-%version.tar

ExclusiveArch: x86_64 aarch64

Provides: perl-%name = %EVR
# from debian/control
Provides: libpve-http-server-perl = %EVR
Conflicts: pve-storage < 7.0.11
Conflicts: pmg-api < 6.1.6
Conflicts: pve-manager < 6.1.6

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
%perl_vendor_privlib/PVE/*

%changelog
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

