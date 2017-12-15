%define dist Date-Pcalc
Name: perl-%dist
Version: 6.1
Release: alt6.1

Summary: Gregorian calendar date calculations
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz

# Patch via https://rt.cpan.org/Public/Bug/Display.html?id=76442 
Patch0:  %name-6.1-boolean.patch
# Related: rt#101232
Patch1:         Date-Pcalc-6.1-century.patch
# Fixed error "Unescaped left brace in regex is deprecated"
Patch2:         Date-Pcalc-6.1-Fix-unescaped-left-brace-in-regex.patch

# Automatically added by buildreq on Fri Oct 07 2011
BuildRequires: perl-Bit-Vector perl-ExtUtils-CBuilder

%description
This package consists of a Perl module for all kinds of date
calculations based on the Gregorian calendar (the one used
in all western countries today), thereby complying with all
relevantnorms and standards: ISO/R 2015-1971, DIN 1355 and,
to some extent, ISO 8601 (where applicable).

%prep
%setup -q -n %dist-%version
%patch0 -p2
%patch1 -p1
%patch2 -p1

%build
%perl_vendor_build
#NO_PACKLIST=1 </dev/null

%install
%perl_vendor_install

%files
%doc CHANGES.txt CREDITS.txt EXAMPLES.txt README.txt
%perl_vendor_archlib/Date
%perl_vendor_autolib/Date

%changelog
* Fri Dec 15 2017 Igor Vlasenko <viy@altlinux.ru> 6.1-alt6.1
- rebuild with new perl 5.26.1

* Thu Dec 14 2017 Igor Vlasenko <viy@altlinux.ru> 6.1-alt6
- added patch2: Fix-unescaped-left-brace-in-regex

* Fri Feb 03 2017 Igor Vlasenko <viy@altlinux.ru> 6.1-alt5.1.1
- rebuild with new perl 5.24.1

* Wed Nov 25 2015 Igor Vlasenko <viy@altlinux.ru> 6.1-alt5.1
- rebuild with new perl 5.22.0

* Wed Nov 18 2015 Igor Vlasenko <viy@altlinux.ru> 6.1-alt5
- fixed build

* Tue Dec 09 2014 Igor Vlasenko <viy@altlinux.ru> 6.1-alt4.1
- rebuild with new perl 5.20.1

* Tue Aug 27 2013 Vladimir Lettiev <crux@altlinux.ru> 6.1-alt4
- built for perl 5.18

* Thu Aug 30 2012 Vladimir Lettiev <crux@altlinux.ru> 6.1-alt3
- rebuilt for perl-5.16
- fixed build

* Fri Oct 07 2011 Alexey Tourbin <at@altlinux.ru> 6.1-alt2
- rebuilt for perl-5.14

* Wed Oct 05 2011 Alexey Tourbin <at@altlinux.ru> 6.1-alt1
- 1.2 -> 6.1

* Mon Nov 22 2010 Igor Vlasenko <viy@altlinux.ru> 1.2-alt1.1.1
- repair after perl 5.12 upgrade using girar-nmu

* Sat Feb 19 2005 ALT QA Team Robot <qa-robot@altlinux.org> 1.2-alt1.1
- Rebuilt with rpm-build-perl-0.5.1.

* Mon Aug 30 2004 Alexey Tourbin <at@altlinux.ru> 1.2-alt1
- initial revision (this module is needed for otrs)
