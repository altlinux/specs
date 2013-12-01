## SPEC file for Perl module Net::SFTP::Foreign

Name: perl-Net-SFTP-Foreign
Version: 1.77
Release: alt1

Summary: SSH File Transfer Protocol client

License: %perl_license
Group: Development/Perl
URL: http://search.cpan.org/dist/Net-SFTP-Foreign/

Packager: Nikolay A. Fetisov <naf@altlinux.ru>
BuildArch: noarch

%define real_name Net-SFTP-Foreign
Source: %name-%version.tar

AutoReqProv: perl, yes
BuildRequires(pre): rpm-build-licenses perl-devel

# Automatically added by buildreq on Sun Dec 01 2013
BuildRequires: openssh-clients openssh-server perl-Encode perl-File-Which

%description
Perl module Net::SFTP::Foreign implements an SFTP client in Perl
using the native SSH client application to establish the
connection to the remote host.

It rely on an external SSH2 client reachable from your PATH.

%prep
%setup
chmod 644 samples/*

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README TODO Changes samples
%perl_vendor_privlib/Net/SFTP/Foreign*

%changelog
* Sun Dec 01 2013 Nikolay A. Fetisov <naf@altlinux.ru> 1.77-alt1
- Initial build for ALT Linux Sisyphus

