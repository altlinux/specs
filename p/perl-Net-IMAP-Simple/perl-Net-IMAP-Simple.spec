%define _without_test 1
## SPEC file for Perl module Net::IMAP::Simple

%define version    1.2025
%define release    alt1

Name: perl-Net-IMAP-Simple
Version: 1.2025
Release: alt1

Summary: Perl extension for simple IMAP account handling

License: Perl license
Group: Development/Perl
URL: http://search.cpan.org/~cfaber/Net-IMAP-Simple/

Packager: Nikolay A. Fetisov <naf@altlinux.ru>
BuildArch: noarch

%define real_name Net-IMAP-Simple
Source: http://www.cpan.org/authors/id/J/JE/JETTERO/Net-IMAP-Simple-%{version}.tar.gz
Patch0: %name-1.17-alt-fix_require.patch

AutoReqProv: perl, yes
BuildRequires: perl-devel perl(Parse/RecDescent.pm) perl-Class-Accessor perl(Regexp/Common.pm) perl(Email/Address.pm) perl(Email/MIME.pm) perl-DateTime perl(DateTime/Format/Strptime.pm) perl(DateTime/Format/Mail.pm)


%description
Perl module Net::IMAP::Simple provides a simple way for accessing
IMAP accounts.

%prep
%setup  -n %real_name-%version
%patch0

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README Changes
%perl_vendor_privlib/Net/IMAP/Simple*

%changelog
* Thu Sep 29 2011 Igor Vlasenko <viy@altlinux.ru> 1.2025-alt1
- automated CPAN update

* Mon Nov 22 2010 Igor Vlasenko <viy@altlinux.ru> 1.17-alt1.1
- repair after perl 5.12 upgrade using girar-nmu

* Sun Mar 25 2007 Nikolay A. Fetisov <naf@altlinux.ru> 1.17-alt1
- New version 1.17
  - Added debugging
  - Upgraded imap.pl example script
  - Updated documentation
  - Several small patches

* Thu Sep 28 2006 Nikolay A. Fetisov <naf@altlinux.ru> 1.16-alt1
- Initial build for ALT Linux Sisyphus

* Thu Sep 28 2006 Nikolay A. Fetisov <naf@altlinux.ru> 1.16-alt0
- Initial build

