%define dist Proc-ProcessTable
Name: perl-%dist
Version: 0.49
Release: alt1

Summary: Perl extension to access the unix process table
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: http://www.cpan.org/authors/id/J/JW/JWB/Proc-ProcessTable-%{version}.tar.gz

# mount /proc in hasher
BuildRequires: /proc

# Automatically added by buildreq on Sat Oct 08 2011
BuildRequires: perl-devel

%description
Perl interface to the unix process table.

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_archlib/Proc
%perl_vendor_autolib/Proc

%changelog
* Fri Dec 06 2013 Igor Vlasenko <viy@altlinux.ru> 0.49-alt1
- automated CPAN update

* Wed Aug 28 2013 Vladimir Lettiev <crux@altlinux.ru> 0.48-alt2
- built for perl 5.18

* Wed Jul 24 2013 Igor Vlasenko <viy@altlinux.ru> 0.48-alt1
- automated CPAN update

* Tue Oct 23 2012 Igor Vlasenko <viy@altlinux.ru> 0.46-alt1
- automated CPAN update

* Fri Aug 31 2012 Vladimir Lettiev <crux@altlinux.ru> 0.45-alt2
- rebuilt for perl-5.16

* Sat Oct 08 2011 Alexey Tourbin <at@altlinux.ru> 0.45-alt1.2
- rebuilt for perl-5.14

* Sun Nov 07 2010 Vladimir Lettiev <crux@altlinux.ru> 0.45-alt1.1
- rebuilt with perl 5.12

* Wed Apr 08 2009 Igor Vlasenko <viy@altlinux.ru> 0.45-alt1
- first build for ALT Linux Sisyphus
