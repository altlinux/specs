%define _unpackaged_files_terminate_build 1

Name: pve-apiclient
Summary: PVE API client library
Version: 3.2.1
Release: alt1
License: AGPL-3.0+
Group: Development/Perl
Url: https://www.proxmox.com
Vcs: git://git.proxmox.com/git/pve-apiclient.git
Source: %name-%version.tar

BuildArch: noarch

Provides: perl-%name = %EVR
# from debian/control
Provides: libpve-apiclient-perl = %EVR

BuildRequires: perl(HTTP/Status.pm) perl(HTTP/Request/Common.pm)
BuildRequires: perl(IO/Socket/SSL.pm) perl(Net/SSLeay.pm)
BuildRequires: perl(JSON.pm)
BuildRequires: perl(LWP/UserAgent.pm)
BuildRequires: perl(URI.pm)

%description
This implements an API client for Proxmox VE in perl.

%prep
%setup

%install
install -D -m 0644 PVE/APIClient/LWP.pm %buildroot%perl_vendor_privlib/PVE/APIClient/LWP.pm
install -D -m 0644 PVE/APIClient/Exception.pm %buildroot%perl_vendor_privlib/PVE/APIClient/Exception.pm

%files
%doc examples
%perl_vendor_privlib/PVE/*

%changelog
* Sun Mar 06 2022 Alexey Shabalin <shaba@altlinux.org> 3.2.1-alt1
- 3.2-1
- build as separate package

