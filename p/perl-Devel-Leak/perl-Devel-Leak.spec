%define dist Devel-Leak
Name: perl-%dist
Version: 0.03
Release: alt4.1.1.1.1

Summary: Utility for looking for perl objects that are not reclaimed
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar
Patch: %name-%version-%release.patch

# Automatically added by buildreq on Thu Oct 06 2011
BuildRequires: perl-devel

%description
Devel::Leak is a utility for looking for Perl objects that are not
reclaimed.

%prep
%setup -q -n %dist-%version
%patch -p1

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README
%perl_vendor_archlib/Devel*
%perl_vendor_autolib/Devel*

%changelog
* Fri Dec 15 2017 Igor Vlasenko <viy@altlinux.ru> 0.03-alt4.1.1.1.1
- rebuild with new perl 5.26.1

* Fri Feb 03 2017 Igor Vlasenko <viy@altlinux.ru> 0.03-alt4.1.1.1
- rebuild with new perl 5.24.1

* Wed Nov 25 2015 Igor Vlasenko <viy@altlinux.ru> 0.03-alt4.1.1
- rebuild with new perl 5.22.0

* Tue Dec 09 2014 Igor Vlasenko <viy@altlinux.ru> 0.03-alt4.1
- rebuild with new perl 5.20.1

* Tue Aug 27 2013 Vladimir Lettiev <crux@altlinux.ru> 0.03-alt4
- built for perl 5.18

* Tue Aug 28 2012 Vladimir Lettiev <crux@altlinux.ru> 0.03-alt3
- rebuilt for perl-5.16

* Thu Oct 06 2011 Alexey Tourbin <at@altlinux.ru> 0.03-alt2.3
- rebuilt for perl-5.14

* Tue Sep 21 2010 Alexey Tourbin <at@altlinux.ru> 0.03-alt2.2
- rebuilt for perl-5.12

* Mon Sep 20 2010 Alexey Tourbin <at@altlinux.ru> 0.03-alt2.1
- rebuilt for perl-5.12

* Thu Oct 26 2006 Alexey Tourbin <at@altlinux.ru> 0.03-alt2
- imported sources into git and built with gear
- fixed SEGV when re-using $handle several times (cpan #19067);
  explicitly reset the handle so it is not reused by mistake

* Sat Apr 02 2005 Alexey Tourbin <at@altlinux.ru> 0.03-alt1
- initial revision (for finding leaks in perl-RPM)
