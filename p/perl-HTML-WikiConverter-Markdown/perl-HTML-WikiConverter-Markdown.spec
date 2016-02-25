# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl-devel perl-podlators
# END SourceDeps(oneline)
Name:           perl-HTML-WikiConverter-Markdown
Version:        0.06
Release:        alt1_4
Summary:        Convert HTML to Markdown markup
License:        GPL+ or Artistic
Group:          Development/Perl
URL:            http://search.cpan.org/dist/HTML-WikiConverter-Markdown/
Source0:        http://www.cpan.org/authors/id/J/JF/JFEARN/HTML-WikiConverter-Markdown-%{version}.tar.gz
BuildArch:      noarch
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
Requires:       perl(HTML/WikiConverter.pm) >= 0.67
Source44: import.info

%description
This module contains rules for converting HTML into Markdown markup. You
should not use this module directly; HTML::WikiConverter is the entry point
for html->wiki conversion (eg, see synopsis above). See HTML::WikiConverter
for additional usage details.

%prep
%setup -q -n HTML-WikiConverter-Markdown-%{version}

%build
%{__perl} Makefile.PL INSTALLMAN1DIR=%_man1dir INSTALLDIRS=vendor
make %{?_smp_mflags}

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

