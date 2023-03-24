%define _unpackaged_files_terminate_build 1
%add_findreq_skiplist %perl_vendor_privlib/PVE/API2/TFA.pm
%filter_from_requires /^perl.PVE.Cluster.pm./d
%filter_from_requires /^perl.PVE.DataCenterConfig.pm./d

Name: pve-access-control
Summary: PVE access control library
Version: 7.4.2
Release: alt1
License: AGPL-3.0+
Group: Development/Perl
Url: https://www.proxmox.com
Vcs: git://git.proxmox.com/git/pve-apiclient.git
Source: %name-%version.tar

ExclusiveArch: x86_64 aarch64

Provides: perl-%name = %EVR
# from debian/control
Provides: libpve-access-control = %EVR

Requires: perl(HTTP/Status.pm)

BuildRequires: pve-doc-generator
BuildRequires: perl(MIME/Base32.pm) perl(MIME/Base64.pm) perl(Digest/SHA.pm)
BuildRequires: perl(Encode.pm)
BuildRequires: perl(Crypt/OpenSSL/Random.pm) perl(Crypt/OpenSSL/RSA.pm)
BuildRequires: perl(Net/SSLeay.pm) perl(Net/IP.pm)
BuildRequires: perl(HTTP/Status.pm)
BuildRequires: perl(JSON.pm)
BuildRequires: perl(URI.pm)
BuildRequires: perl(UUID.pm)
BuildRequires: perl(Authen/PAM.pm)

BuildRequires: perl(PVE/Cluster.pm)
BuildRequires: perl(PVE/DataCenterConfig.pm)
BuildRequires: perl(PVE/CLIFormatter.pm)
BuildRequires: perl(PVE/CLIHandler.pm)
BuildRequires: perl(PVE/JSONSchema.pm)
BuildRequires: perl(PVE/PTY.pm)
BuildRequires: perl(PVE/RESTHandler.pm)
BuildRequires: perl(PVE/Tools.pm)
BuildRequires: perl(PVE/OTP.pm)
BuildRequires: perl(PVE/Ticket.pm)
BuildRequires: perl(PVE/Cluster.pm)
BuildRequires: perl(PVE/INotify.pm)
BuildRequires: perl(PVE/ProcFSTools.pm)
BuildRequires: perl(PVE/RESTEnvironment.pm)
BuildRequires: perl(PVE/SafeSyslog.pm)

BuildRequires: perl(PVE/RS/TFA.pm)
BuildRequires: perl(PVE/RS/OpenId.pm)

%description
This package contains the role based user management and access
control function used by Proxmox VE.

%prep
%setup

%install
%makeinstall_std -C src

%files
%_bindir/oathkeygen
%_sbindir/pveum
%_man1dir/pveum.1*
%perl_vendor_privlib/PVE/*
%_datadir/bash-completion/completions/pveum
%_datadir/zsh/vendor-completions/_pveum

%changelog
* Fri Mar 24 2023 Andrew A. Vasilyev <andy@altlinux.org> 7.4.2-alt1
- 7.4-2

* Sat Mar 11 2023 Andrew A. Vasilyev <andy@altlinux.org> 7.3.2-alt1
- 7.3-2

* Tue Nov 29 2022 Andrew A. Vasilyev <andy@altlinux.org> 7.2.5-alt1
- 7.2-5

* Mon Oct 03 2022 Alexey Shabalin <shaba@altlinux.org> 7.2.4-alt1
- 7.2-4

* Thu May 05 2022 Andrew A. Vasilyev <andy@altlinux.org> 7.1.8-alt1
- 7.1-8

* Sun Mar 06 2022 Alexey Shabalin <shaba@altlinux.org> 7.1.6-alt1
- 7.1-6
- build as separate package

