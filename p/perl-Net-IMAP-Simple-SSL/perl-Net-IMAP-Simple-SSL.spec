## SPEC file for Perl module Net::IMAP::Simple

%define version    1.3
%define release    alt1

Name: perl-Net-IMAP-Simple-SSL
Version: %version
Release: alt1.1

Summary: Perl extension for adding SSL support for NEt::IMAP::Simple

License: Perl license
Group: Development/Perl
URL: http://search.cpan.org/~cwest/Net-IMAP-Simple-SSL/

Packager: Nikolay A. Fetisov <naf@altlinux.ru>
BuildArch: noarch

%define real_name Net-IMAP-Simple-SSL
Source: http://search.cpan.org/CPAN/authors/id/C/CW/CWEST/%real_name-%version.tar.gz

AutoReqProv: perl, yes
BuildPreReq: perl-devel perl-IO-Socket-SSL


%description
Perl module Net::IMAP::Simple::SSL provides a SSL support for 
Net::IMAP::Simple.

%prep
%setup  -n %real_name-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README Changes
%perl_vendor_privlib/Net/IMAP/Simple/SSL*
%exclude /.perl.req

%changelog
* Mon Nov 22 2010 Igor Vlasenko <viy@altlinux.ru> 1.3-alt1.1
- repair after perl 5.12 upgrade using girar-nmu

* Thu Sep 28 2006 Nikolay A. Fetisov <naf@altlinux.ru> 1.3-alt1
- Initial build for ALT Linux Sisyphus

* Thu Sep 28 2006 Nikolay A. Fetisov <naf@altlinux.ru> 1.3-alt0
- Initial build

