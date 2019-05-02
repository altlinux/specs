## SPEC file for Perl module Net::SFTP::Foreign

Name: perl-Net-SFTP-Foreign
Version: 1.90
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

# Automatically added by buildreq on Thu May 02 2019
# optimized out: gem-power-assert perl perl-CPAN-Meta-Requirements perl-Encode perl-JSON-PP perl-Parse-CPAN-Meta perl-Pod-Escapes perl-Pod-Simple perl-devel perl-parent python-base python-modules python3 python3-base python3-dev ruby ruby-coderay ruby-method_source ruby-pry ruby-rake ruby-rdoc ruby-stdlibs sh4
BuildRequires: openssh-clients openssh-server perl-CPAN-Meta perl-File-Which perl-Test-Pod

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
* Thu May 02 2019 Nikolay A. Fetisov <naf@altlinux.org> 1.90-alt1
- New version

* Fri Mar 02 2018 Nikolay A. Fetisov <naf@altlinux.org> 1.89-alt1
- New version

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

