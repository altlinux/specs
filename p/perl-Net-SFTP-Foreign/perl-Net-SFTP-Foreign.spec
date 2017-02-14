## SPEC file for Perl module Net::SFTP::Foreign

Name: perl-Net-SFTP-Foreign
Version: 1.87
Release: alt1

Summary: SSH File Transfer Protocol client

License: %perl_license
Group: Development/Perl
URL: http://search.cpan.org/dist/Net-SFTP-Foreign/

Packager: Nikolay A. Fetisov <naf@altlinux.org>
BuildArch: noarch

%define real_name Net-SFTP-Foreign
Source: %name-%version.tar

AutoReqProv: perl, yes
BuildRequires(pre): rpm-build-licenses perl-devel

# Automatically added by buildreq on Tue Jun 21 2016
# optimized out: perl perl-Encode perl-Pod-Escapes perl-Pod-Simple perl-devel python-base python-modules python3
BuildRequires: openssh-clients openssh-server perl-File-Which perl-Test-Pod

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
* Tue Feb 14 2017 Nikolay A. Fetisov <naf@altlinux.org> 1.87-alt1
- New version

* Tue Jun 21 2016 Nikolay A. Fetisov <naf@altlinux.ru> 1.86-alt1
- New version

* Mon Jan 04 2016 Nikolay A. Fetisov <naf@altlinux.ru> 1.81-alt1
- New version

* Sun Oct 25 2015 Nikolay A. Fetisov <naf@altlinux.ru> 1.79-alt1
- New version

* Sun Dec 01 2013 Nikolay A. Fetisov <naf@altlinux.ru> 1.77-alt1
- Initial build for ALT Linux Sisyphus

