%define dist Text-CSV_XS
Name: perl-%dist
Version: 0.85
Release: alt1

Summary: Comma-separated values manipulation routines
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tgz

# Automatically added by buildreq on Fri Oct 07 2011
BuildRequires: perl-Test-Pod perl-Test-Pod-Coverage

%description
Text::CSV_XS provides facilities for the composition and decomposition of
comma-separated values.  An instance of the Text::CSV_XS class can combine
fields into a CSV string and parse a CSV string into fields.

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc ChangeLog README
%perl_vendor_archlib/Text
%perl_vendor_autolib/Text

%changelog
* Fri Oct 07 2011 Alexey Tourbin <at@altlinux.ru> 0.85-alt1
- 0.80 -> 0.85
- built for perl-5.14
- rebuilt as plain src.rpm

* Sun Dec 26 2010 Alexey Tourbin <at@altlinux.ru> 0.80-alt1
- 0.73 -> 0.80

* Fri Nov 05 2010 Vladimir Lettiev <crux@altlinux.ru> 0.73-alt1.1
- rebuilt with perl 5.12

* Thu Jun 10 2010 Alexey Tourbin <at@altlinux.ru> 0.73-alt1
- 0.70 -> 0.73

* Tue Feb 16 2010 Alexey Tourbin <at@altlinux.ru> 0.70-alt1
- 0.68 -> 0.70

* Thu Oct 08 2009 Alexey Tourbin <at@altlinux.ru> 0.68-alt1
- 0.64 -> 0.68

* Tue Apr 07 2009 Alexey Tourbin <at@altlinux.ru> 0.64-alt1
- 0.60 -> 0.64

* Sat Mar 07 2009 Alexey Tourbin <at@altlinux.ru> 0.60-alt1
- 0.57 -> 0.60

* Mon Oct 27 2008 Alexey Tourbin <at@altlinux.ru> 0.57-alt1
- 0.54 -> 0.57

* Sun Sep 07 2008 Alexey Tourbin <at@altlinux.ru> 0.54-alt1
- 0.52 -> 0.54

* Tue Jul 15 2008 Alexey Tourbin <at@altlinux.ru> 0.52-alt1
- 0.50 -> 0.52

* Thu Jun 12 2008 Alexey Tourbin <at@altlinux.ru> 0.50-alt1
- 0.45 -> 0.50

* Thu Apr 24 2008 Alexey Tourbin <at@altlinux.ru> 0.45-alt1
- 0.41 -> 0.45

* Sat Apr 12 2008 Alexey Tourbin <at@altlinux.ru> 0.41-alt1
- 0.36 -> 0.41

* Fri Mar 07 2008 Alexey Tourbin <at@altlinux.ru> 0.36-alt1
- 0.31 -> 0.36

* Thu Jul 26 2007 Alexey Tourbin <at@altlinux.ru> 0.31-alt1
- 0.29 -> 0.31

* Fri Jun 08 2007 Alexey Tourbin <at@altlinux.ru> 0.29-alt1
- 0.23 -> 0.29

* Thu Apr 19 2007 Alexey Tourbin <at@altlinux.ru> 0.23-alt2
- cleanup

* Sat Feb 19 2005 ALT QA Team Robot <qa-robot@altlinux.org> 0.23-alt1.1
- Rebuilt with rpm-build-perl-0.5.1.

* Tue Jul 08 2003 Michael Shigorin <mike@altlinux.ru> 0.23-alt1
- alt1
- spec file provided by Valentin Solomko

* Thu May 15 2003 Valentyn Solomko <vesna@slovnyk.org> 0.23-val1
- built for ALT Linux

