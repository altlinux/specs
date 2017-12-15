Name: perl-Parse-ExuberantCTags
Version: 1.02
Release: alt3.1.1.1.1

Summary: Efficiently parse exuberant ctags files
License: GPL or Artistic
Group: Development/Perl

URL: http://search.cpan.org/dist/Parse-ExuberantCTags/
Source: Parse-ExuberantCTags-%version.tar.gz

# Automatically added by buildreq on Wed Oct 19 2011
BuildRequires: perl-devel

%description
%summary

%prep
%setup -q -n Parse-ExuberantCTags-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README 
%perl_vendor_archlib/Parse
%perl_vendor_autolib/Parse

%changelog
* Fri Dec 15 2017 Igor Vlasenko <viy@altlinux.ru> 1.02-alt3.1.1.1.1
- rebuild with new perl 5.26.1

* Fri Feb 03 2017 Igor Vlasenko <viy@altlinux.ru> 1.02-alt3.1.1.1
- rebuild with new perl 5.24.1

* Wed Nov 25 2015 Igor Vlasenko <viy@altlinux.ru> 1.02-alt3.1.1
- rebuild with new perl 5.22.0

* Tue Dec 09 2014 Igor Vlasenko <viy@altlinux.ru> 1.02-alt3.1
- rebuild with new perl 5.20.1

* Thu Aug 29 2013 Vladimir Lettiev <crux@altlinux.ru> 1.02-alt3
- built for perl 5.18

* Sun Sep 02 2012 Vladimir Lettiev <crux@altlinux.ru> 1.02-alt2
- rebuilt for perl-5.16

* Wed Oct 19 2011 Alexey Tourbin <at@altlinux.ru> 1.02-alt1.2
- rebuilt for perl-5.14

* Sun Nov 07 2010 Vladimir Lettiev <crux@altlinux.ru> 1.02-alt1.1
- rebuilt with perl 5.12

* Sun Sep 26 2010 Vladimir Lettiev <crux@altlinux.ru> 1.02-alt1
- New version 1.02

* Mon Jan 25 2010 Vladimir Lettiev <crux@altlinux.ru> 1.01-alt1
- initial build
