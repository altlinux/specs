%define _unpackaged_files_terminate_build 1
%define dist Text-CSV_XS
Name: perl-%dist
Version: 1.34
Release: alt1.1.1

Summary: Comma-separated values manipulation routines
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source0: http://www.cpan.org/authors/id/H/HM/HMBRAND/%{dist}-%{version}.tgz

# Automatically added by buildreq on Fri Oct 07 2011
BuildRequires: perl-Test-Pod perl-Test-Pod-Coverage perl(charnames.pm)

%description
Text::CSV_XS provides facilities for the composition and decomposition of
comma-separated values.  An instance of the Text::CSV_XS class can combine
fields into a CSV string and parse a CSV string into fields.

%prep
%setup -q -n %{dist}-%{version}

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc ChangeLog README CONTRIBUTING.md examples
%perl_vendor_archlib/Text
%perl_vendor_autolib/Text

%changelog
* Fri Dec 15 2017 Igor Vlasenko <viy@altlinux.ru> 1.34-alt1.1.1
- rebuild with new perl 5.26.1

* Fri Nov 17 2017 Igor Vlasenko <viy@altlinux.ru> 1.34-alt1.1
- automated CPAN update

* Wed Nov 08 2017 Igor Vlasenko <viy@altlinux.ru> 1.34-alt1
- automated CPAN update

* Wed Nov 01 2017 Igor Vlasenko <viy@altlinux.ru> 1.33-alt1
- automated CPAN update

* Tue Sep 26 2017 Igor Vlasenko <viy@altlinux.ru> 1.32-alt1
- automated CPAN update

* Wed Aug 02 2017 Igor Vlasenko <viy@altlinux.ru> 1.31-alt1
- automated CPAN update

* Tue May 09 2017 Igor Vlasenko <viy@altlinux.ru> 1.29-alt1
- automated CPAN update

* Sat Mar 25 2017 Igor Vlasenko <viy@altlinux.ru> 1.28-alt1
- automated CPAN update

* Wed Mar 15 2017 Igor Vlasenko <viy@altlinux.ru> 1.27-alt1
- automated CPAN update

* Fri Feb 03 2017 Igor Vlasenko <viy@altlinux.ru> 1.26-alt1.1
- rebuild with new perl 5.24.1

* Sun Dec 18 2016 Igor Vlasenko <viy@altlinux.ru> 1.26-alt1
- automated CPAN update

* Tue Sep 20 2016 Igor Vlasenko <viy@altlinux.ru> 1.25-alt1
- automated CPAN update

* Mon Jul 25 2016 Igor Vlasenko <viy@altlinux.ru> 1.24-alt1
- automated CPAN update

* Mon Mar 28 2016 Igor Vlasenko <viy@altlinux.ru> 1.23-alt1
- automated CPAN update

* Thu Mar 03 2016 Igor Vlasenko <viy@altlinux.ru> 1.22-alt1
- automated CPAN update

* Wed Feb 10 2016 Igor Vlasenko <viy@altlinux.ru> 1.21-alt1
- automated CPAN update

* Wed Nov 25 2015 Igor Vlasenko <viy@altlinux.ru> 1.20-alt1.1
- rebuild with new perl 5.22.0

* Sun Oct 11 2015 Igor Vlasenko <viy@altlinux.ru> 1.20-alt1
- automated CPAN update

* Fri May 22 2015 Igor Vlasenko <viy@altlinux.ru> 1.17-alt1
- automated CPAN update

* Wed Apr 01 2015 Igor Vlasenko <viy@altlinux.ru> 1.16-alt1
- automated CPAN update

* Wed Feb 11 2015 Igor Vlasenko <viy@altlinux.ru> 1.14-alt1
- automated CPAN update

* Mon Jan 12 2015 Igor Vlasenko <viy@altlinux.ru> 1.13-alt1
- automated CPAN update

* Tue Dec 09 2014 Igor Vlasenko <viy@altlinux.ru> 1.12-alt1.1
- rebuild with new perl 5.20.1

* Tue Nov 25 2014 Igor Vlasenko <viy@altlinux.ru> 1.12-alt1
- automated CPAN update

* Tue Aug 19 2014 Igor Vlasenko <viy@altlinux.ru> 1.11-alt1
- automated CPAN update

* Tue Jun 10 2014 Igor Vlasenko <viy@altlinux.ru> 1.09-alt1
- automated CPAN update

* Mon May 26 2014 Igor Vlasenko <viy@altlinux.ru> 1.08-alt1
- automated CPAN update

* Fri May 02 2014 Igor Vlasenko <viy@altlinux.ru> 1.07-alt1
- automated CPAN update

* Sat Mar 15 2014 Igor Vlasenko <viy@altlinux.ru> 1.05-alt1
- automated CPAN update

* Sat Feb 08 2014 Igor Vlasenko <viy@altlinux.ru> 1.04-alt1
- automated CPAN update

* Sat Jan 25 2014 Igor Vlasenko <viy@altlinux.ru> 1.03-alt1
- automated CPAN update

* Wed Nov 13 2013 Igor Vlasenko <viy@altlinux.ru> 1.02-alt1
- automated CPAN update

* Tue Aug 27 2013 Vladimir Lettiev <crux@altlinux.ru> 1.01-alt2
- built for perl 5.18

* Wed Jul 24 2013 Igor Vlasenko <viy@altlinux.ru> 1.01-alt1
- automated CPAN update

* Wed Aug 29 2012 Vladimir Lettiev <crux@altlinux.ru> 0.91-alt1
- 0.85 -> 0.91
- built for perl-5.16

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

