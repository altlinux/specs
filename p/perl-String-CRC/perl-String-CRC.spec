%define dist String-CRC
Name: perl-%dist
Version: 1.0
Release: alt3.1.1.1.1

Summary: Cyclic redundency check generation
License: Public Domain
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz

# Automatically added by buildreq on Sat Oct 08 2011
BuildRequires: perl-devel

%description
This packages provides a perl module to generate checksums from strings
and from files.

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc	README
%dir	%perl_vendor_archlib/String
	%perl_vendor_archlib/String/CRC.pm
%doc	%perl_vendor_archlib/String/CRC.pod
	%perl_vendor_autolib/String

%changelog
* Fri Dec 15 2017 Igor Vlasenko <viy@altlinux.ru> 1.0-alt3.1.1.1.1
- rebuild with new perl 5.26.1

* Fri Feb 03 2017 Igor Vlasenko <viy@altlinux.ru> 1.0-alt3.1.1.1
- rebuild with new perl 5.24.1

* Wed Nov 25 2015 Igor Vlasenko <viy@altlinux.ru> 1.0-alt3.1.1
- rebuild with new perl 5.22.0

* Tue Dec 09 2014 Igor Vlasenko <viy@altlinux.ru> 1.0-alt3.1
- rebuild with new perl 5.20.1

* Wed Aug 28 2013 Vladimir Lettiev <crux@altlinux.ru> 1.0-alt3
- built for perl 5.18

* Fri Aug 31 2012 Vladimir Lettiev <crux@altlinux.ru> 1.0-alt2
- rebuilt for perl-5.16

* Sat Oct 08 2011 Alexey Tourbin <at@altlinux.ru> 1.0-alt1.2
- rebuilt for perl-5.14

* Sun Nov 07 2010 Vladimir Lettiev <crux@altlinux.ru> 1.0-alt1.1
- rebuilt with perl 5.12

* Wed Jul 01 2009 Grigory Milev <week@altlinux.ru> 1.0-alt1
- Initial build for ALT Linux distribution.
