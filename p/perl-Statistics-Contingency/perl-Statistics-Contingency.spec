BuildRequires: perl(Module/Build.pm)
%define dist Statistics-Contingency
Name: perl-%dist
Version: 0.08
Release: alt1

Summary: Calculate precision, recall, F1, accuracy, etc.
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: http://www.cpan.org/authors/id/K/KW/KWILLIAMS/Statistics-Contingency-%{version}.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Thu Jul 01 2004
BuildRequires: perl-Params-Validate perl-devel

%description
The Statistics::Contingency class helps you calculate several
useful statistical measures based on 2x2 "contingency tables". 
These measures are used to help judge the results of automatic text
categorization experiments, but they are useful in other situations
as well.

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README Changes
%perl_vendor_privlib/Statistics*

%changelog
* Sun Sep 25 2011 Igor Vlasenko <viy@altlinux.ru> 0.08-alt1
- automated CPAN update

* Mon Nov 22 2010 Igor Vlasenko <viy@altlinux.ru> 0.06-alt1.1.1
- repair after perl 5.12 upgrade using girar-nmu

* Sat Feb 19 2005 ALT QA Team Robot <qa-robot@altlinux.org> 0.06-alt1.1
- Rebuilt with rpm-build-perl-0.5.1.

* Thu Jul 01 2004 Alexey Tourbin <at@altlinux.ru> 0.06-alt1
- initial revision
