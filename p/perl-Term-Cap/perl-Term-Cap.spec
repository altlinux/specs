%define dist Term-Cap
Name: perl-%dist
Version: 1.16
Release: alt1

Summary: Perl termcap interface
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: http://www.cpan.org/authors/id/J/JS/JSTOWE/Term-Cap-%{version}.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Tue Sep 21 2010
BuildRequires: perl-devel

%description
These are low-level functions to extract and use capabilities from
a terminal capability (termcap) database.

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_privlib/Term

%changelog
* Tue Jun 10 2014 Igor Vlasenko <viy@altlinux.ru> 1.16-alt1
- automated CPAN update

* Sun Oct 27 2013 Igor Vlasenko <viy@altlinux.ru> 1.15-alt1
- automated CPAN update

* Tue Sep 21 2010 Alexey Tourbin <at@altlinux.ru> 1.12-alt1
- initial revision, for perl-5.12
