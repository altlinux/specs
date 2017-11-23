%define _unpackaged_files_terminate_build 1
%define dist Filter
Name: perl-%dist
Version: 1.58
Release: alt1

Summary: Source Filters
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source0: http://www.cpan.org/authors/id/R/RU/RURBAN/%{dist}-%{version}.tar.gz

# Automatically added by buildreq on Fri Oct 07 2011
BuildRequires: perl-devel

%description
Source filters alter the program text of a module before Perl sees it,
much as a C preprocessor alters the source text of a C program before
the compiler sees it.

%prep
%setup -q -n %{dist}-%{version}

%ifdef __buildreqs
mv t/pod.t t/pod.t.orig
%endif

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc	Changes README examples
%perl_vendor_archlib/Filter
%perl_vendor_autolib/Filter

%changelog
* Thu Nov 23 2017 Igor Vlasenko <viy@altlinux.ru> 1.58-alt1
- automated CPAN update

* Tue Feb 14 2017 Igor Vlasenko <viy@altlinux.ru> 1.57-alt1
- automated CPAN update

* Fri Feb 03 2017 Igor Vlasenko <viy@altlinux.ru> 1.55-alt1.1.1
- rebuild with new perl 5.24.1

* Wed Nov 25 2015 Igor Vlasenko <viy@altlinux.ru> 1.55-alt1.1
- rebuild with new perl 5.22.0

* Sun Oct 11 2015 Igor Vlasenko <viy@altlinux.ru> 1.55-alt1
- automated CPAN update

* Mon Jan 19 2015 Igor Vlasenko <viy@altlinux.ru> 1.54-alt1
- automated CPAN update

* Mon Dec 22 2014 Igor Vlasenko <viy@altlinux.ru> 1.53-alt1
- automated CPAN update

* Tue Dec 16 2014 Igor Vlasenko <viy@altlinux.ru> 1.51-alt1
- automated CPAN update

* Tue Dec 09 2014 Igor Vlasenko <viy@altlinux.ru> 1.49-alt2.1
- rebuild with new perl 5.20.1

* Wed Aug 21 2013 Vladimir Lettiev <crux@altlinux.ru> 1.49-alt2
- built for perl 5.18

* Wed Jul 24 2013 Igor Vlasenko <viy@altlinux.ru> 1.49-alt1
- automated CPAN update

* Thu Aug 23 2012 Vladimir Lettiev <crux@altlinux.ru> 1.45-alt1
- 1.43 -> 1.45

* Thu May 03 2012 Vladimir Lettiev <crux@altlinux.ru> 1.43-alt1
- 1.39 -> 1.43
- build for perl-5.16

* Thu Oct 06 2011 Alexey Tourbin <at@altlinux.ru> 1.39-alt1
- 1.37 -> 1.39
- build for perl-5.14
- rebuilt as palin src.rpm

* Mon Sep 20 2010 Alexey Tourbin <at@altlinux.ru> 1.37-alt1
- 1.36 -> 1.37
- built for perl-5.12
- disabled build dependency on perl-Test-Pod

* Tue Mar 03 2009 Alexey Tourbin <at@altlinux.ru> 1.36-alt1
- 1.34 -> 1.36

* Tue Aug 21 2007 Alexey Tourbin <at@altlinux.ru> 1.34-alt1
- 1.32 -> 1.34
- perlfilter.pod not packaged (a copy in perl-pod is better)

* Wed Feb 28 2007 Alexey Tourbin <at@altlinux.ru> 1.32-alt2
- imported into git and adapted for gear
- replaced DynaLoader with XSLoader
- replaced Perl_ninstr() with memchr(3)

* Mon Aug 07 2006 Alexey Tourbin <at@altlinux.ru> 1.32-alt1
- 1.30 -> 1.32

* Tue Dec 14 2004 Alexey Tourbin <at@altlinux.ru> 1.30-alt1
- initial revision (split off from perl-base)
