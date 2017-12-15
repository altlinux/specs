%define _unpackaged_files_terminate_build 1
%define dist Devel-Declare
Name: perl-%dist
Version: 0.006019
Release: alt1.1

Summary: Adding keywords to perl, in perl
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source0: http://www.cpan.org/authors/id/E/ET/ETHER/%{dist}-%{version}.tar.gz

# Automatically added by buildreq on Sun Nov 20 2011
BuildRequires: perl-B-Hooks-EndOfScope perl-B-Hooks-OP-Check perl-ExtUtils-Depends perl-Pod-Escapes perl-Sub-Name perl-Test-Warn perl(Test/Requires.pm)

%description
Devel::Declare can install subroutines called declarators which locally
take over Perl's parser, allowing the creation of new syntax.

%prep
%setup -q -n %{dist}-%{version}

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_archlib/Devel
%perl_vendor_autolib/Devel

%changelog
* Fri Dec 15 2017 Igor Vlasenko <viy@altlinux.ru> 0.006019-alt1.1
- rebuild with new perl 5.26.1

* Mon Apr 03 2017 Igor Vlasenko <viy@altlinux.ru> 0.006019-alt1
- automated CPAN update

* Fri Feb 03 2017 Igor Vlasenko <viy@altlinux.ru> 0.006018-alt1.1.1
- rebuild with new perl 5.24.1

* Wed Nov 25 2015 Igor Vlasenko <viy@altlinux.ru> 0.006018-alt1.1
- rebuild with new perl 5.22.0

* Wed Apr 01 2015 Igor Vlasenko <viy@altlinux.ru> 0.006018-alt1
- automated CPAN update

* Tue Dec 09 2014 Igor Vlasenko <viy@altlinux.ru> 0.006017-alt1.1
- rebuild with new perl 5.20.1

* Tue Oct 07 2014 Igor Vlasenko <viy@altlinux.ru> 0.006017-alt1
- automated CPAN update

* Wed Apr 02 2014 Igor Vlasenko <viy@altlinux.ru> 0.006016-alt1
- automated CPAN update

* Wed Feb 05 2014 Igor Vlasenko <viy@altlinux.ru> 0.006015-alt1
- automated CPAN update

* Fri Aug 30 2013 Vladimir Lettiev <crux@altlinux.ru> 0.006014-alt2
- built for perl 5.18

* Fri Jul 26 2013 Igor Vlasenko <viy@altlinux.ru> 0.006014-alt1
- automated CPAN update

* Tue Sep 04 2012 Vladimir Lettiev <crux@altlinux.ru> 0.006011-alt1
- 0.006008 -> 0.006011
- built for perl-5.16

* Sun Nov 20 2011 Alexey Tourbin <at@altlinux.ru> 0.006008-alt1
- initial revision
