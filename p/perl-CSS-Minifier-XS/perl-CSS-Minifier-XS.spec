# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl(Benchmark.pm) perl(DynaLoader.pm) perl(Exporter.pm) perl(IO/File.pm) perl-podlators
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:       perl-CSS-Minifier-XS
Version:    0.09
Release:    alt4_12.1
# lib/CSS/Minifier/XS.pm -> GPL+ or Artistic
License:    GPL+ or Artistic
Group:      Development/Other
Summary:    XS based CSS minifier
Source:     http://search.cpan.org/CPAN/authors/id/G/GT/GTERMARS/CSS-Minifier-XS-%{version}.tar.gz
Url:        http://search.cpan.org/dist/CSS-Minifier-XS

BuildRequires: perl-devel
BuildRequires: rpm-build-perl
BuildRequires: perl(CSS/Minifier.pm)
BuildRequires: perl(ExtUtils/MakeMaker.pm)
BuildRequires: perl(Module/Build/Compat.pm)
BuildRequires: perl(Test/More.pm)
BuildRequires: perl(Test/Pod.pm)
BuildRequires: perl(Test/Pod/Coverage.pm)


Source44: import.info

%description
'CSS::Minifier::XS' is a CSS "minifier". It's designed to remove
unnecessary white-space and comments from CSS files, while also
*not* breaking the CSS. 'CSS::Minifier::XS' is similar in function
to 'CSS::Minifier', but is substantially faster as it's written
in XS and not just pure Perl.


%prep
%setup -q -n CSS-Minifier-XS-%{version}

%build
%{__perl} Makefile.PL INSTALLMAN1DIR=%_man1dir INSTALLDIRS=vendor OPTIMIZE="%{optflags}"
%make_build

%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -type f -name '*.bs' -a -size 0 -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'

# %{_fixperms} %{buildroot}/*

%check
make test

%files
%doc Changes README
%{perl_vendor_archlib}/*
%exclude %dir %{perl_vendor_archlib}/auto

%changelog
* Fri Dec 15 2017 Igor Vlasenko <viy@altlinux.ru> 0.09-alt4_12.1
- rebuild with new perl 5.26.1

* Wed Sep 27 2017 Igor Vlasenko <viy@altlinux.ru> 0.09-alt4_12
- update to new release by fcimport

* Thu Aug 03 2017 Igor Vlasenko <viy@altlinux.ru> 0.09-alt4_10
- update to new release by fcimport

* Thu Mar 16 2017 Igor Vlasenko <viy@altlinux.ru> 0.09-alt4_9
- update to new release by fcimport

* Fri Feb 03 2017 Igor Vlasenko <viy@altlinux.ru> 0.09-alt4_8.1
- rebuild with new perl 5.24.1

* Tue Jan 31 2017 Igor Vlasenko <viy@altlinux.ru> 0.09-alt4_8
- to Sisyphus

* Sun May 29 2016 Igor Vlasenko <viy@altlinux.ru> 0.09-alt3_8
- update to new release by fcimport

* Wed Mar 02 2016 Igor Vlasenko <viy@altlinux.ru> 0.09-alt3_7
- update to new release by fcimport

* Fri Nov 27 2015 Cronbuild Service <cronbuild@altlinux.org> 0.09-alt3_6
- rebuild to get rid of unmets

* Mon Sep 21 2015 Igor Vlasenko <viy@altlinux.ru> 0.09-alt2_6
- update to new release by fcimport

* Sat Dec 13 2014 Cronbuild Service <cronbuild@altlinux.org> 0.09-alt2_4
- rebuild to get rid of unmets

* Tue Sep 16 2014 Igor Vlasenko <viy@altlinux.ru> 0.09-alt1_4
- update to new release by fcimport

* Wed Sep 10 2014 Igor Vlasenko <viy@altlinux.ru> 0.09-alt1_3
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 0.09-alt1_2
- update to new release by fcimport

* Tue Nov 12 2013 Igor Vlasenko <viy@altlinux.ru> 0.09-alt1_1
- update to new release by fcimport

* Thu Sep 05 2013 Cronbuild Service <cronbuild@altlinux.org> 0.08-alt3_7
- rebuild to get rid of unmets

* Tue Aug 27 2013 Igor Vlasenko <viy@altlinux.ru> 0.08-alt2_7
- update to new release by fcimport

* Mon Aug 05 2013 Igor Vlasenko <viy@altlinux.ru> 0.08-alt2_6
- update to new release by fcimport

* Wed Feb 27 2013 Igor Vlasenko <viy@altlinux.ru> 0.08-alt2_5
- update to new release by fcimport

* Mon Sep 10 2012 Cronbuild Service <cronbuild@altlinux.org> 0.08-alt2_4
- rebuild with new perl

* Tue Jul 31 2012 Igor Vlasenko <viy@altlinux.ru> 0.08-alt1_4
- update to new release by fcimport

* Thu May 24 2012 Igor Vlasenko <viy@altlinux.ru> 0.08-alt1_2
- fc import

