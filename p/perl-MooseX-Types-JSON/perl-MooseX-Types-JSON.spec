%define _unpackaged_files_terminate_build 1
%define dist MooseX-Types-JSON
Name: perl-%dist
Version: 1.00
Release: alt1.1

Summary: JSON datatype for Moose
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: http://www.cpan.org/authors/id/M/MI/MILA/MooseX-Types-JSON-%{version}.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Tue Apr 13 2010
BuildRequires: perl-Class-C3-XS perl-JSON-XS perl-MooseX-Types perl-Test-Pod perl-JSON

%description
%summary.

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_privlib/MooseX*

%changelog
* Sat Apr 09 2016 Igor Vlasenko <viy@altlinux.ru> 1.00-alt1.1
- rebuild to restore role requires

* Tue Dec 16 2014 Igor Vlasenko <viy@altlinux.ru> 1.00-alt1
- automated CPAN update

* Mon Jan 06 2014 Igor Vlasenko <viy@altlinux.ru> 0.03-alt1
- automated CPAN update

* Tue Apr 13 2010 Alexey Tourbin <at@altlinux.ru> 0.02-alt1
- initial revision
