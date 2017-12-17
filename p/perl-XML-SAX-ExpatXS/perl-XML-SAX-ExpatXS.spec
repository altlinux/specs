# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl-podlators
# END SourceDeps(oneline)
%filter_from_requires /^perl.XML.SAX.ExpatXS.Preload.pm./d
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           perl-XML-SAX-ExpatXS
Version:        1.33
Release:        alt3_18.1
Summary:        Perl SAX 2 XS extension to Expat parser
License:        GPL+ or Artistic
Group:          Development/Other
URL:            http://search.cpan.org/dist/XML-SAX-ExpatXS/
Source0:        http://www.cpan.org/authors/id/P/PC/PCIMPRICH/XML-SAX-ExpatXS-%{version}.tar.gz
BuildRequires:  perl-devel
BuildRequires:  rpm-build-perl
BuildRequires:  perl(Carp.pm)
BuildRequires:  perl(Config.pm)
BuildRequires:  perl(DynaLoader.pm)
BuildRequires:  perl(ExtUtils/MakeMaker.pm)
BuildRequires:  perl(IO/File.pm)
BuildRequires:  perl(Test.pm)
BuildRequires:  perl(vars.pm)
BuildRequires:  perl(XML/SAX/Base.pm)
BuildRequires:  perl(XML/SAX.pm)
BuildRequires:  libexpat-devel
Requires:       perl(XML/SAX.pm) >= 0.960

 # Filters (not)shared c libs
Source44: import.info

%description
XML::SAX::ExpatXS is a direct XS extension to Expat XML parser. It
implements Perl SAX 2.1 interface. See http://perl-xml.sourceforge.net/perl-
sax/ for Perl SAX API description. Any deviations from the Perl SAX 2.1
specification are considered as bugs.

%prep
%setup -q -n XML-SAX-ExpatXS-%{version}
chmod -x ExpatXS.xs

%build
echo n | %{__perl} Makefile.PL INSTALLMAN1DIR=%_man1dir INSTALLDIRS=vendor OPTIMIZE="$RPM_OPT_FLAGS"
%make_build

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -type f -name '*.bs' -size 0 -exec rm -f {} \;

# %{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%triggerin -- perl-XML-SAX
%{__perl} -MXML::SAX -e \
  'XML::SAX->add_parser(q(XML::SAX::ExpatXS))->save_parsers()' 2>/dev/null || :

%preun
if [ $1 -eq 0 ]; then
 %{__perl} -MXML::SAX -e \
    'XML::SAX->remove_parser(q(XML::SAX::ExpatXS))->save_parsers()' \
    2>/dev/null || :
fi

%files
%doc Changes README
%{perl_vendor_archlib}/auto/*
%{perl_vendor_archlib}/XML*

%changelog
* Fri Dec 15 2017 Igor Vlasenko <viy@altlinux.ru> 1.33-alt3_18.1
- rebuild with new perl 5.26.1

* Wed Sep 27 2017 Igor Vlasenko <viy@altlinux.ru> 1.33-alt3_18
- update to new release by fcimport

* Thu Aug 03 2017 Igor Vlasenko <viy@altlinux.ru> 1.33-alt3_16
- update to new release by fcimport

* Thu Mar 16 2017 Igor Vlasenko <viy@altlinux.ru> 1.33-alt3_15
- update to new release by fcimport

* Fri Feb 03 2017 Igor Vlasenko <viy@altlinux.ru> 1.33-alt3_14.1
- rebuild with new perl 5.24.1

* Tue Jul 26 2016 Igor Vlasenko <viy@altlinux.ru> 1.33-alt3_14
- update to new release by fcimport

* Mon Mar 07 2016 Igor Vlasenko <viy@altlinux.ru> 1.33-alt3_13
- update to new release by fcimport

* Wed Nov 25 2015 Igor Vlasenko <viy@altlinux.ru> 1.33-alt3_12.1
- rebuild with new perl 5.22.0

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 1.33-alt3_12
- update to new release by fcimport

* Tue Dec 09 2014 Igor Vlasenko <viy@altlinux.ru> 1.33-alt3_10.1
- rebuild with new perl 5.20.1

* Mon Oct 27 2014 Igor Vlasenko <viy@altlinux.ru> 1.33-alt3_10
- update to new release by fcimport

* Wed Aug 27 2014 Igor Vlasenko <viy@altlinux.ru> 1.33-alt3_9
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 1.33-alt3_8
- update to new release by fcimport

* Tue Feb 18 2014 Igor Vlasenko <viy@altlinux.ru> 1.33-alt3_7
- moved to Sisyphus for Slic3r (by dd@ request)

* Wed Sep 11 2013 Igor Vlasenko <viy@altlinux.ru> 1.33-alt2_7
- rebuild

* Mon Sep 02 2013 Igor Vlasenko <viy@altlinux.ru> 1.33-alt1_7
- update to new release by fcimport

* Mon Aug 05 2013 Igor Vlasenko <viy@altlinux.ru> 1.33-alt1_6
- update to new release by fcimport

* Fri Apr 26 2013 Igor Vlasenko <viy@altlinux.ru> 1.33-alt1_5
- initial fc import

