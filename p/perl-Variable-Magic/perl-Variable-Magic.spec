%define _unpackaged_files_terminate_build 1
%define dist Variable-Magic
Name: perl-%dist
Version: 0.62
Release: alt1.1

Summary: Associate user-defined magic to variables from Perl
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source0: http://www.cpan.org/authors/id/V/VP/VPIT/%{dist}-%{version}.tar.gz

# Automatically added by buildreq on Fri Oct 07 2011
BuildRequires: perl-Capture-Tiny perl-Test-Pod perl-threads

%description
Magic is Perl's way of enhancing variables.  This mechanism lets the user
add extra data to any variable and hook syntactical operations (such as
access, assignment or destruction) that can be applied to it.  With this
module, you can add your own magic to any variable without having to write
a single line of XS.

%prep
%setup -q -n %{dist}-%{version}

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_archlib/Variable
%perl_vendor_autolib/Variable

%changelog
* Fri Dec 15 2017 Igor Vlasenko <viy@altlinux.ru> 0.62-alt1.1
- rebuild with new perl 5.26.1

* Wed Nov 08 2017 Igor Vlasenko <viy@altlinux.ru> 0.62-alt1
- automated CPAN update

* Tue Feb 14 2017 Igor Vlasenko <viy@altlinux.ru> 0.61-alt1
- automated CPAN update

* Fri Feb 03 2017 Igor Vlasenko <viy@altlinux.ru> 0.60-alt1.1
- rebuild with new perl 5.24.1

* Tue Sep 20 2016 Igor Vlasenko <viy@altlinux.ru> 0.60-alt1
- automated CPAN update

* Wed Nov 25 2015 Igor Vlasenko <viy@altlinux.ru> 0.59-alt1.1
- rebuild with new perl 5.22.0

* Sun Oct 11 2015 Igor Vlasenko <viy@altlinux.ru> 0.59-alt1
- automated CPAN update

* Fri May 22 2015 Igor Vlasenko <viy@altlinux.ru> 0.57-alt1
- automated CPAN update

* Wed Apr 01 2015 Igor Vlasenko <viy@altlinux.ru> 0.56-alt1
- automated CPAN update

* Tue Dec 09 2014 Igor Vlasenko <viy@altlinux.ru> 0.55-alt1.1
- rebuild with new perl 5.20.1

* Mon Oct 27 2014 Igor Vlasenko <viy@altlinux.ru> 0.55-alt1
- automated CPAN update

* Tue Oct 07 2014 Igor Vlasenko <viy@altlinux.ru> 0.54-alt1
- automated CPAN update

* Thu Sep 12 2013 Igor Vlasenko <viy@altlinux.ru> 0.53-alt1
- automated CPAN update

* Tue Aug 27 2013 Vladimir Lettiev <crux@altlinux.ru> 0.52-alt2
- built for perl 5.18

* Wed Jul 24 2013 Igor Vlasenko <viy@altlinux.ru> 0.52-alt1
- automated CPAN update

* Tue Aug 28 2012 Vladimir Lettiev <crux@altlinux.ru> 0.51-alt1
- 0.46 -> 0.51
- built for perl-5.16

* Fri Oct 07 2011 Alexey Tourbin <at@altlinux.ru> 0.46-alt2
- rebuilt for perl-5.14

* Mon Sep 19 2011 Igor Vlasenko <viy@altlinux.ru> 0.46-alt1
- automated CPAN update

* Fri Nov 05 2010 Vladimir Lettiev <crux@altlinux.ru> 0.43-alt1.1
- rebuilt with perl 5.12

* Tue Jul 13 2010 Igor Vlasenko <viy@altlinux.ru> 0.43-alt1
- automated CPAN update

* Mon Apr 12 2010 Alexey Tourbin <at@altlinux.ru> 0.41-alt1
- initial revision, for B::Hooks::EndOfScope
