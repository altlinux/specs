%define dist MongoDB
Name: perl-%dist
Version: 0.501.1
Release: alt1

Summary: Mongo Driver for Perl
License: GPL or Artistic
Group: Development/Perl

URL: http://www.cpan.org
Source: http://www.cpan.org/authors/id/F/FR/FRIEDO/MongoDB-%{version}.tar.gz

# Automatically added by buildreq on Sun Oct 09 2011 (-bb)
BuildRequires: perl-Any-Moose perl-Class-Method-Modifiers perl-Data-Types perl-DateTime perl-File-Slurp perl-JSON perl-Module-Install perl-Moose perl-Package-Stash-XS perl-Readonly perl-Readonly-XS perl-Test-Exception perl-Tie-IxHash perl-boolean

%description
This is the Perl driver for MongoDB, a document-oriented database.

%prep
%setup -q -n %dist-%version

# need database connection
%def_without test

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_archlib/MongoDB*
%perl_vendor_autolib/MongoDB

%changelog
* Tue Oct 23 2012 Igor Vlasenko <viy@altlinux.ru> 0.501.1-alt1
- automated CPAN update

* Sat Sep 01 2012 Vladimir Lettiev <crux@altlinux.ru> 0.45-alt3
- rebuilt for perl-5.16

* Sun Oct 09 2011 Alexey Tourbin <at@altlinux.ru> 0.45-alt2
- rebuilt for perl-5.14

* Thu Sep 22 2011 Igor Vlasenko <viy@altlinux.ru> 0.45-alt1
- automated CPAN update

* Sat Jan 01 2011 Denis Smirnov <mithraen@altlinux.ru> 0.40-alt1
- initial build for ALT Linux Sisyphus
