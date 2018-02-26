BuildRequires: perl(Module/Build.pm)
%define dist Statistics-Descriptive
Name: perl-%dist
Version: 3.0202
Release: alt1

Summary: Basic descriptive statistical functions
License: GPL or Artistic
Group: Development/Perl

Url: %CPAN %dist
Source: http://www.cpan.org/authors/id/S/SH/SHLOMIF/Statistics-Descriptive-%{version}.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Fri Apr 16 2004
BuildRequires: perl-devel

%description
This Perl module provides basic functions used in descriptive statistics.

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_privlib/Statistics

%changelog
* Sun Sep 25 2011 Igor Vlasenko <viy@altlinux.ru> 3.0202-alt1
- automated CPAN update

* Mon Nov 22 2010 Igor Vlasenko <viy@altlinux.ru> 2.6-alt2.1.1
- repair after perl 5.12 upgrade using girar-nmu

* Sat Feb 19 2005 ALT QA Team Robot <qa-robot@altlinux.org> 2.6-alt2.1
- Rebuilt with rpm-build-perl-0.5.1.

* Fri Apr 16 2004 Alexey Tourbin <at@altlinux.ru> 2.6-alt2
- fixed URL

* Fri Oct 24 2003 Alexey Tourbin <at@altlinux.ru> 2.6-alt1
- initial revision (this package is required by mon)
