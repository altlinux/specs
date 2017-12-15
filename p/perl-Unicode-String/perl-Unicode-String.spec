%define _unpackaged_files_terminate_build 1
%define dist Unicode-String
Name: perl-%dist
Version: 2.10
Release: alt1.1.1

Summary: Perl module to represent strings of Unicode chars 
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: http://www.cpan.org/authors/id/G/GA/GAAS/GAAS/Unicode-String-%{version}.tar.gz

Provides: perl-Unicode-CharName = %version
Obsoletes: perl-Unicode-CharName <= %version

# Automatically added by buildreq on Sat Oct 08 2011
BuildRequires: perl-devel

%description
Perl module to represent strings of Unicode chars. They were made before
perl included native UTF8 support.

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_archlib/Unicode
%perl_vendor_autolib/Unicode

%changelog
* Fri Dec 15 2017 Igor Vlasenko <viy@altlinux.ru> 2.10-alt1.1.1
- rebuild with new perl 5.26.1

* Fri Feb 03 2017 Igor Vlasenko <viy@altlinux.ru> 2.10-alt1.1
- rebuild with new perl 5.24.1

* Tue Sep 20 2016 Igor Vlasenko <viy@altlinux.ru> 2.10-alt1
- automated CPAN update

* Wed Nov 25 2015 Igor Vlasenko <viy@altlinux.ru> 2.09-alt4.1
- rebuild with new perl 5.22.0

* Thu Nov 19 2015 Igor Vlasenko <viy@altlinux.ru> 2.09-alt4
- fixed build with perl 5.22

* Tue Dec 09 2014 Igor Vlasenko <viy@altlinux.ru> 2.09-alt3.1
- rebuild with new perl 5.20.1

* Wed Aug 28 2013 Vladimir Lettiev <crux@altlinux.ru> 2.09-alt3
- built for perl 5.18

* Fri Aug 31 2012 Vladimir Lettiev <crux@altlinux.ru> 2.09-alt2
- rebuilt for perl-5.16

* Sat Oct 08 2011 Alexey Tourbin <at@altlinux.ru> 2.09-alt1.2
- rebuilt for perl-5.14
- merged perl-Unicode-CharName subpackage into perl-Unicode-String

* Sun Nov 07 2010 Vladimir Lettiev <crux@altlinux.ru> 2.09-alt1.1
- rebuilt with perl 5.12

* Sat Sep 06 2008 Vitaly Lipatov <lav@altlinux.ru> 2.09-alt1
- disable man packaging

* Tue Feb 21 2006 Vitaly Lipatov <lav@altlinux.ru> 2.09-alt0.1
- new version (2.09)
- change packager
- add Url, fix Source URL

* Sat Feb 19 2005 ALT QA Team Robot <qa-robot@altlinux.org> 2.07-alt1.1
- Rebuilt with rpm-build-perl-0.5.1.

* Thu Mar 20 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.07-alt1
- 2.07

* Mon Nov 04 2002 Stanislav Ievlev <inger@altlinux.ru> 2.06-alt2
- rebuild with new perl

* Thu Jan 10 2002 Yuri N. Sedunov <aris@altlinux.ru> 2.06-alt1
- First build for Sisyphus.
