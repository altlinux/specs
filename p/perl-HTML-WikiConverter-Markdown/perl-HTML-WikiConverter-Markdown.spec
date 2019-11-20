Group: Development/Other
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl-podlators
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           perl-HTML-WikiConverter-Markdown
Version:        0.06
Release:        alt1_14
Summary:        Convert HTML to Markdown markup
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/HTML-WikiConverter-Markdown
Source0:        https://cpan.metacpan.org/authors/id/J/JF/JFEARN/HTML-WikiConverter-Markdown-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  rpm-build-perl
BuildRequires:  perl(base.pm)
BuildRequires:  perl(ExtUtils/MakeMaker.pm)
BuildRequires:  perl(File/Spec.pm)
BuildRequires:  perl(HTML/Entities.pm)
BuildRequires:  perl(HTML/Tagset.pm)
BuildRequires:  perl(HTML/WikiConverter.pm)
BuildRequires:  perl(Params/Validate.pm)
BuildRequires:  perl(strict.pm)
BuildRequires:  perl(Test/More.pm)
BuildRequires:  perl(URI.pm)
BuildRequires:  perl(warnings.pm)
# not automatically detected
Requires:       perl(HTML/WikiConverter.pm) >= 0.670
Source44: import.info

%description
This module contains rules for converting HTML into Markdown markup. You
should not use this module directly; HTML::WikiConverter is the entry point
for html->wiki conversion (eg, see synopsis above). See HTML::WikiConverter
for additional usage details.

%prep
%setup -q -n HTML-WikiConverter-Markdown-%{version}

%build
/usr/bin/perl Makefile.PL INSTALLDIRS=vendor
%make_build

%install
make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;

# %{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc Changes README
%{perl_vendor_privlib}/*

%changelog
* Wed Nov 20 2019 Igor Vlasenko <viy@altlinux.ru> 0.06-alt1_14
- update to new release by fcimport

* Sat Jul 14 2018 Igor Vlasenko <viy@altlinux.ru> 0.06-alt1_10
- update to new release by fcimport

* Wed Sep 27 2017 Igor Vlasenko <viy@altlinux.ru> 0.06-alt1_8
- update to new release by fcimport

* Thu Aug 03 2017 Igor Vlasenko <viy@altlinux.ru> 0.06-alt1_7
- update to new release by fcimport

* Thu Mar 16 2017 Igor Vlasenko <viy@altlinux.ru> 0.06-alt1_6
- update to new release by fcimport

* Tue Jul 26 2016 Igor Vlasenko <viy@altlinux.ru> 0.06-alt1_5
- update to new release by fcimport

* Thu Feb 25 2016 Igor Vlasenko <viy@altlinux.ru> 0.06-alt1_4
- to Sisyphus for publican

* Mon Sep 21 2015 Igor Vlasenko <viy@altlinux.ru> 0.06-alt1_3
- update to new release by fcimport

* Mon Oct 20 2014 Igor Vlasenko <viy@altlinux.ru> 0.06-alt1_1
- update to new release by fcimport

* Tue Sep 16 2014 Igor Vlasenko <viy@altlinux.ru> 0.05-alt2_15
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 0.05-alt2_14
- update to new release by fcimport

* Tue Aug 27 2013 Igor Vlasenko <viy@altlinux.ru> 0.05-alt2_13
- update to new release by fcimport

* Mon Aug 05 2013 Igor Vlasenko <viy@altlinux.ru> 0.05-alt2_12
- update to new release by fcimport

* Mon Mar 04 2013 Igor Vlasenko <viy@altlinux.ru> 0.05-alt2_11
- update to new release by fcimport

* Tue Jul 31 2012 Igor Vlasenko <viy@altlinux.ru> 0.05-alt2_10
- update to new release by fcimport

* Fri May 25 2012 Igor Vlasenko <viy@altlinux.ru> 0.05-alt2_8
- fc import

* Thu May 24 2012 Igor Vlasenko <viy@altlinux.ru> 0.05-alt1_8
- fc import

