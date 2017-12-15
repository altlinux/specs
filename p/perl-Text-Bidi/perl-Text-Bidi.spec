%define dist Text-Bidi
Name: perl-%dist
Version: 2.12
Release: alt1.1.1

Summary: Unicode bidi algorithm for Perl using libfribidi
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar
Source1: %name.watch

# Automatically added by buildreq on Wed Oct 19 2011
BuildRequires: libfribidi-devel perl-Test-Pod perl-unicore

%description
This is a perl interface to the libfribidi library that implements the
Unicode bidi algorithm.  The bidi algorithm is a specification for
displaying text that consists of both left-to-right and right-to-left
written languages.

%prep
%setup -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes
%perl_vendor_archlib/Text
%perl_vendor_autolib/Text

%changelog
* Fri Dec 15 2017 Igor Vlasenko <viy@altlinux.ru> 2.12-alt1.1.1
- rebuild with new perl 5.26.1

* Fri Feb 03 2017 Igor Vlasenko <viy@altlinux.ru> 2.12-alt1.1
- rebuild with new perl 5.24.1

* Fri Nov 18 2016 Igor Vlasenko <viy@altlinux.ru> 2.12-alt1
- automated CPAN update

* Wed Nov 25 2015 Igor Vlasenko <viy@altlinux.ru> 2.11-alt1.1
- rebuild with new perl 5.22.0

* Wed Nov 11 2015 Igor Vlasenko <viy@altlinux.ru> 2.11-alt1
- automated CPAN update

* Tue Dec 09 2014 Igor Vlasenko <viy@altlinux.ru> 2.09-alt1.1
- rebuild with new perl 5.20.1

* Thu Jun 19 2014 Anton Farygin <rider@altlinux.ru> 2.09-alt1
- new version 2.09

* Fri Oct 11 2013 Anton Farygin <rider@altlinux.ru> 2.02-alt1
- new version

* Thu Aug 29 2013 Vladimir Lettiev <crux@altlinux.ru> 0.03-alt6
- built for perl 5.18

* Sun Sep 02 2012 Vladimir Lettiev <crux@altlinux.ru> 0.03-alt5
- rebuilt for perl-5.16

* Wed Oct 19 2011 Alexey Tourbin <at@altlinux.ru> 0.03-alt4
- rebuilt for perl-5.14

* Fri Jun 03 2011 Dmitry V. Levin <ldv@altlinux.org> 0.03-alt3
- Synced with libtext-bidi-perl-0.03-5 from Debian (fixes CPAN#42774).

* Sun Nov 07 2010 Vladimir Lettiev <crux@altlinux.ru> 0.03-alt2.1
- rebuilt with perl 5.12

* Mon Sep 08 2008 Anton Farygin <rider@altlinux.ru> 0.03-alt2
- fixed build

* Mon Apr 07 2008 Anton Farygin <rider@altlinux.ru> 0.03-alt1
- first build for Sisyphus
