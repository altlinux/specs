%define _unpackaged_files_terminate_build 1
%define dist String-CRC32
Name: perl-%dist
Version: 1.6
Release: alt1.1

Summary: Cyclic redundency check generation
License: Public Domain
Group: Development/Perl

URL: %CPAN %dist
Source0: http://www.cpan.org/authors/id/L/LE/LEEJO/%{dist}-%{version}.tar.gz

# Automatically added by buildreq on Fri Oct 07 2011
BuildRequires: perl-devel

%description
This packages provides a perl module to generate checksums from strings
and from files.

%prep
%setup -q -n %{dist}-%{version}

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README.md Changes LICENSE
%dir	%perl_vendor_archlib/String
	%perl_vendor_archlib/String/CRC32.pm
%doc	%perl_vendor_archlib/String/CRC32.pod
	%perl_vendor_autolib/String

%changelog
* Fri Dec 15 2017 Igor Vlasenko <viy@altlinux.ru> 1.6-alt1.1
- rebuild with new perl 5.26.1

* Wed Aug 02 2017 Igor Vlasenko <viy@altlinux.ru> 1.6-alt1
- automated CPAN update

* Fri Feb 03 2017 Igor Vlasenko <viy@altlinux.ru> 1.5-alt1.1.1.1
- rebuild with new perl 5.24.1

* Wed Nov 25 2015 Igor Vlasenko <viy@altlinux.ru> 1.5-alt1.1.1
- rebuild with new perl 5.22.0

* Tue Dec 09 2014 Igor Vlasenko <viy@altlinux.ru> 1.5-alt1.1
- rebuild with new perl 5.20.1

* Fri Jan 03 2014 Igor Vlasenko <viy@altlinux.ru> 1.5-alt1
- automated CPAN update

* Wed Aug 28 2013 Vladimir Lettiev <crux@altlinux.ru> 1.4-alt3
- built for perl 5.18

* Thu Aug 30 2012 Vladimir Lettiev <crux@altlinux.ru> 1.4-alt2
- rebuilt for perl-5.16

* Fri Oct 07 2011 Alexey Tourbin <at@altlinux.ru> 1.4-alt1.2
- rebuilt for perl-5.14

* Sun Nov 07 2010 Vladimir Lettiev <crux@altlinux.ru> 1.4-alt1.1
- rebuilt with perl 5.12

* Tue Dec 16 2008 Alexey Tourbin <at@altlinux.ru> 1.4-alt1
- 1.2 -> 1.4

* Sat Feb 19 2005 ALT QA Team Robot <qa-robot@altlinux.org> 1.2-alt2.1
- Rebuilt with rpm-build-perl-0.5.1.

* Tue Nov 05 2002 Stanislav Ievlev <inger@altlinux.ru> 1.2-alt2
- rebuild with new perl

* Tue Oct  9 2001 Grigory Milev <week@altlinux.ru> 1.2-alt1
- Initial build for ALT Linux distribution.
