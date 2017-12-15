# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl-podlators
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
# License information:
#
# This code is largely a Perl wrapper around data tables provided by the
# Unicode Consortium under their Unicode Character Database Terms Of Use
#
# Upstream is happy for us to distribute the Perl parts under any terms
# we like, so I have selected the standard "same as Perl" terms of
# "GPL+ or Artistic"
#
# Ref: https://rt.cpan.org/Public/Bug/Display.html?id=70210

Summary:	Checks if scalar is valid UTF-8
Name:		perl-Unicode-CheckUTF8
Version:	1.03
Release:	alt4_20.1
License:	UCD and (GPL+ or Artistic)
Group:		Development/Other
Url:		http://search.cpan.org/dist/Unicode-String/
Source0:	http://search.cpan.org/CPAN/authors/id/B/BR/BRADFITZ/Unicode-CheckUTF8-%{version}.tar.gz
# Module Build
BuildRequires:	coreutils
BuildRequires:	findutils
BuildRequires:	gcc-common
BuildRequires:	perl-devel
BuildRequires:	perl-devel
BuildRequires:	rpm-build-perl
BuildRequires:	perl(ExtUtils/MakeMaker.pm)
# Module Runtime
BuildRequires:	perl(base.pm)
BuildRequires:	perl(Exporter.pm)
BuildRequires:	perl(XSLoader.pm)
# Test Suite
BuildRequires:	perl(Test/More.pm)
# Dependencies

# Don't "provide" private Perl libs

Source44: import.info

%description
This is an XS wrapper around some Unicode Consortium code to check if a string
is valid UTF-8, revised to conform to what expat/Mozilla think is valid UTF-8,
especially with regard to low-ASCII characters.

Note that this module has NOTHING to do with Perl's internal UTF8 flag on
scalars.

This module is for use when you're getting input from users and want to make
sure it's valid UTF-8 before continuing.

%prep
%setup -q -n Unicode-CheckUTF8-%{version} 

%build
perl Makefile.PL INSTALLMAN1DIR=%_man1dir INSTALLDIRS=vendor OPTIMIZE="%{optflags}"
%make_build

%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -delete
find %{buildroot} -type f -name '*.bs' -a -empty -delete
# %{_fixperms} %{buildroot}

%check
make test

%files
%doc CHANGES
%{perl_vendor_archlib}/Unicode/
%{perl_vendor_archlib}/auto/Unicode/

%changelog
* Fri Dec 15 2017 Igor Vlasenko <viy@altlinux.ru> 1.03-alt4_20.1
- rebuild with new perl 5.26.1

* Mon Oct 02 2017 Igor Vlasenko <viy@altlinux.ru> 1.03-alt4_20
- update to new release by fcimport

* Thu Aug 03 2017 Igor Vlasenko <viy@altlinux.ru> 1.03-alt4_18
- update to new release by fcimport

* Thu Mar 16 2017 Igor Vlasenko <viy@altlinux.ru> 1.03-alt4_17
- update to new release by fcimport

* Fri Feb 03 2017 Igor Vlasenko <viy@altlinux.ru> 1.03-alt4_16.1
- rebuild with new perl 5.24.1

* Mon Dec 19 2016 Igor Vlasenko <viy@altlinux.ru> 1.03-alt4_16
- update to new release by fcimport

* Sun May 08 2016 Igor Vlasenko <viy@altlinux.ru> 1.03-alt4_15
- update to new release by fcimport

* Mon Mar 07 2016 Igor Vlasenko <viy@altlinux.ru> 1.03-alt4_14
- update to new release by fcimport

* Wed Nov 25 2015 Igor Vlasenko <viy@altlinux.ru> 1.03-alt4_13.1
- rebuild with new perl 5.22.0

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 1.03-alt4_13
- update to new release by fcimport

* Tue Dec 09 2014 Igor Vlasenko <viy@altlinux.ru> 1.03-alt4_11.1
- rebuild with new perl 5.20.1

* Mon Oct 27 2014 Igor Vlasenko <viy@altlinux.ru> 1.03-alt4_11
- update to new release by fcimport

* Wed Aug 27 2014 Igor Vlasenko <viy@altlinux.ru> 1.03-alt4_10
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 1.03-alt4_9
- update to new release by fcimport

* Thu Nov 14 2013 Igor Vlasenko <viy@altlinux.ru> 1.03-alt4_8
- Sisyphus build

* Thu Sep 05 2013 Cronbuild Service <cronbuild@altlinux.org> 1.03-alt3_8
- rebuild to get rid of unmets

* Mon Sep 02 2013 Igor Vlasenko <viy@altlinux.ru> 1.03-alt2_8
- update to new release by fcimport

* Mon Aug 05 2013 Igor Vlasenko <viy@altlinux.ru> 1.03-alt2_7
- update to new release by fcimport

* Mon Mar 04 2013 Igor Vlasenko <viy@altlinux.ru> 1.03-alt2_6
- update to new release by fcimport

* Mon Sep 10 2012 Cronbuild Service <cronbuild@altlinux.org> 1.03-alt2_5
- rebuild with new perl

* Tue Jul 31 2012 Igor Vlasenko <viy@altlinux.ru> 1.03-alt1_5
- update to new release by fcimport

* Wed May 23 2012 Igor Vlasenko <viy@altlinux.ru> 1.03-alt1_3
- fc import

