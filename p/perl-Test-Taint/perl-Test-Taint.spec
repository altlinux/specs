%def_with test
%define dist Test-Taint
Name: perl-%dist
Version: 1.06
Release: alt4

Summary: Checks for taintedness of variables
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: http://www.cpan.org/authors/id/P/PE/PETDANCE/Test-Taint-%{version}.tar.gz

# Automatically added by buildreq on Sun Oct 09 2011
BuildRequires: perl-Test-Pod perl-Test-Pod-Coverage

%description
Tainted data is data that comes from an unsafe source, such as the
command line, or, in the case of web apps, any GET or POST transactions.
Read the the perlsec manpage man page for details on why tainted data is bad,
and how to untaint the data.

When you're writing unit tests for code that deals with tainted data,
you'll want to have a way to provide tainted data for your routines to
handle, and easy ways to check and report on the taintedness of your data,
in standard the Test::More manpage style.

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes
%perl_vendor_archlib/Test
%perl_vendor_autolib/Test

%changelog
* Tue Dec 19 2017 Igor Vlasenko <viy@altlinux.ru> 1.06-alt4
- enabled tests again

* Sat Dec 16 2017 Igor Vlasenko <viy@altlinux.ru> 1.06-alt3
- disabled tests until perl 5.26 migration

* Fri Dec 15 2017 Igor Vlasenko <viy@altlinux.ru> 1.06-alt2.1.1.1.1
- rebuild with new perl 5.26.1

* Fri Feb 03 2017 Igor Vlasenko <viy@altlinux.ru> 1.06-alt2.1.1.1
- rebuild with new perl 5.24.1

* Wed Nov 25 2015 Igor Vlasenko <viy@altlinux.ru> 1.06-alt2.1.1
- rebuild with new perl 5.22.0

* Tue Dec 09 2014 Igor Vlasenko <viy@altlinux.ru> 1.06-alt2.1
- rebuild with new perl 5.20.1

* Wed Aug 28 2013 Vladimir Lettiev <crux@altlinux.ru> 1.06-alt2
- built for perl 5.18

* Wed Jul 24 2013 Igor Vlasenko <viy@altlinux.ru> 1.06-alt1
- automated CPAN update

* Sat Sep 01 2012 Vladimir Lettiev <crux@altlinux.ru> 1.04-alt3
- rebuilt for perl-5.16

* Sun Oct 09 2011 Alexey Tourbin <at@altlinux.ru> 1.04-alt2
- rebuilt for perl-5.14

* Sat Dec 04 2010 Denis Baranov <baraka@altlinux.org> 1.04-alt1
- initial build for ALT Linux Sisyphus
