%define _unpackaged_files_terminate_build 1
%define dist PadWalker
Name: perl-%dist
Version: 2.3
Release: alt1

Summary: Inspect lexical variables in any subroutine which called you
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source0: http://www.cpan.org/authors/id/R/RO/ROBIN/%{dist}-%{version}.tar.gz

# Automatically added by buildreq on Fri Oct 07 2011
BuildRequires: perl-devel

%description
PadWalker is a module which allows you to inspect (and even change!)
lexical variables in any subroutine which called you. It will only
show those variables which are in scope at the point of the call.

PadWalker is particularly useful for debugging. It's even
used by Perl's built-in debugger. (It can also be used
for evil, of course.)

I wouldn't recommend using PadWalker directly in production
code, but it's your call. Some of the modules that use
PadWalker internally are certainly safe for and useful
in production.

%prep
%setup -q -n %{dist}-%{version}

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_archlib/PadWalker*
%perl_vendor_autolib/PadWalker*

%changelog
* Thu Nov 23 2017 Igor Vlasenko <viy@altlinux.ru> 2.3-alt1
- automated CPAN update

* Fri Feb 03 2017 Igor Vlasenko <viy@altlinux.ru> 2.2-alt1.1.1
- rebuild with new perl 5.24.1

* Wed Nov 25 2015 Igor Vlasenko <viy@altlinux.ru> 2.2-alt1.1
- rebuild with new perl 5.22.0

* Mon Oct 26 2015 Igor Vlasenko <viy@altlinux.ru> 2.2-alt1
- automated CPAN update

* Fri May 22 2015 Igor Vlasenko <viy@altlinux.ru> 2.1-alt1
- automated CPAN update

* Tue Dec 16 2014 Igor Vlasenko <viy@altlinux.ru> 2.0-alt1
- automated CPAN update

* Tue Dec 09 2014 Igor Vlasenko <viy@altlinux.ru> 1.99-alt1.1
- rebuild with new perl 5.20.1

* Thu Nov 13 2014 Igor Vlasenko <viy@altlinux.ru> 1.99-alt1
- automated CPAN update

* Mon Oct 28 2013 Igor Vlasenko <viy@altlinux.ru> 1.98-alt1
- automated CPAN update

* Wed Aug 28 2013 Vladimir Lettiev <crux@altlinux.ru> 1.96-alt2
- built for perl 5.18

* Thu Aug 30 2012 Vladimir Lettiev <crux@altlinux.ru> 1.96-alt1
- 1.92 -> 1.96
- rebuilt for perl-5.16

* Fri Oct 07 2011 Alexey Tourbin <at@altlinux.ru> 1.92-alt1.2
- rebuilt for perl-5.14

* Sun Nov 07 2010 Vladimir Lettiev <crux@altlinux.ru> 1.92-alt1.1
- rebuilt with perl 5.12

* Fri Jul 16 2010 Igor Vlasenko <viy@altlinux.ru> 1.92-alt1
- automated CPAN update

* Tue Jul 13 2010 Igor Vlasenko <viy@altlinux.ru> 1.9-alt1
- automated CPAN update

* Mon Oct 06 2008 Igor Vlasenko <viy@altlinux.ru> 1.7-alt1.1
- NMU for unknown reason

* Sun Apr 20 2008 Michael Bochkaryov <misha@altlinux.ru> 1.7-alt1
- first build for ALT Linux Sisyphus
