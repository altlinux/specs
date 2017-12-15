%define dist Package-Stash-XS
Name: perl-%dist
Version: 0.28
Release: alt2.1.1.1.1

Summary: Faster and more correct implementation of the Package::Stash API
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: http://www.cpan.org/authors/id/D/DO/DOY/Package-Stash-XS-%{version}.tar.gz

# Automatically added by buildreq on Sun Oct 09 2011
BuildRequires: perl-Test-Fatal perl(Test/Requires.pm)

%description
This is a backend for Package::Stash, which provides the functionality in
a way that's less buggy and much faster.  It will be used by default if it's
installed, and should be preferred in all environments with a compiler.

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_archlib/Package*
%perl_vendor_autolib/Package*

%changelog
* Fri Dec 15 2017 Igor Vlasenko <viy@altlinux.ru> 0.28-alt2.1.1.1.1
- rebuild with new perl 5.26.1

* Fri Feb 03 2017 Igor Vlasenko <viy@altlinux.ru> 0.28-alt2.1.1.1
- rebuild with new perl 5.24.1

* Wed Nov 25 2015 Igor Vlasenko <viy@altlinux.ru> 0.28-alt2.1.1
- rebuild with new perl 5.22.0

* Tue Dec 09 2014 Igor Vlasenko <viy@altlinux.ru> 0.28-alt2.1
- rebuild with new perl 5.20.1

* Sun Aug 25 2013 Vladimir Lettiev <crux@altlinux.ru> 0.28-alt2
- built for perl 5.18

* Sat Jul 27 2013 Igor Vlasenko <viy@altlinux.ru> 0.28-alt1
- automated CPAN update

* Tue Aug 28 2012 Vladimir Lettiev <crux@altlinux.ru> 0.25-alt2
- rebuilt for perl-5.16

* Sun Oct 09 2011 Alexey Tourbin <at@altlinux.ru> 0.25-alt1
- initial revision
