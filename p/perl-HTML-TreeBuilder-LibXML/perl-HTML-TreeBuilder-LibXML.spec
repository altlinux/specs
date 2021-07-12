%define perl_bootstrap 1
Group: Development/Other
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl(LWP/UserAgent.pm) perl(URI.pm) perl-podlators
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           perl-HTML-TreeBuilder-LibXML
Version:        0.26
Release:        alt3_22
Summary:        HTML::TreeBuilder and XPath compatible interface with libxml
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/HTML-TreeBuilder-LibXML
Source0:        https://cpan.metacpan.org/authors/id/T/TO/TOKUHIROM/HTML-TreeBuilder-LibXML-%{version}.tar.gz
Patch0:         HTML-TreeBuilder-LibXML-0.26-empty-string-test.patch

BuildArch:      noarch
BuildRequires:  rpm-build-perl
BuildRequires:  perl(base.pm)
BuildRequires:  perl(Carp.pm)
BuildRequires:  perl(Data/Dumper.pm)
BuildRequires:  perl(inc/Module/Install.pm)
BuildRequires:  perl(HTML/TreeBuilder/XPath.pm)
BuildRequires:  perl(Module/Build/Tiny.pm)
BuildRequires:  perl(Test/Exception.pm)
BuildRequires:  perl(Test/More.pm)
BuildRequires:  perl(XML/LibXML.pm)

# perl-Web-Scraper requires HTML::TreeBuilder::LibXML so don't pull
# in this optional test requirement when bootstrapping (#982293)
%if 0%{!?perl_bootstrap:1}
BuildRequires:  perl(Web/Scraper.pm)
%endif

# not picked up by rpm deptracker
Requires:       perl(HTML/TreeBuilder/XPath.pm) >= 0.140
Requires:       perl(XML/LibXML.pm) >= 1.700



Source44: import.info
%filter_from_requires /^perl(XML.LibXML.pm)/d

%description
HTML::TreeBuilder::XPath is a libxml based compatible interface to
HTML::TreeBuilder, which could be slow for a large document.
HTML::TreeBuilder::LibXML is drop-in-replacement for HTML::TreeBuilder::XPath.

%prep
%setup -q -n HTML-TreeBuilder-LibXML-%{version}
%patch0

%build
/usr/bin/perl Build.PL --installdirs=vendor
./Build

%install
./Build install --destdir=%{buildroot} --create_packlist=0

# %{_fixperms} $RPM_BUILD_ROOT/*

%check
./Build test

%files
%doc Changes README.md
%doc --no-dereference LICENSE
%{perl_vendor_privlib}/HTML*

%changelog
* Mon Jul 12 2021 Igor Vlasenko <viy@altlinux.org> 0.26-alt3_22
- to Sisyphus as perl-Finance-Quote dep
- bootstrap build

* Thu Jul 08 2021 Igor Vlasenko <viy@altlinux.org> 0.26-alt2_22
- update to new release by fcimport

* Wed Mar 17 2021 Igor Vlasenko <viy@altlinux.org> 0.26-alt2_18
- update to new release by fcimport

* Wed Jan 27 2021 Igor Vlasenko <viy@altlinux.ru> 0.26-alt2_17
- update to new release by fcimport

* Wed Sep 02 2020 Igor Vlasenko <viy@altlinux.ru> 0.26-alt1_17
- update to new release by fcimport

* Mon Jul 06 2020 Igor Vlasenko <viy@altlinux.ru> 0.26-alt1_16
- update to new release by fcimport

* Thu Mar 05 2020 Igor Vlasenko <viy@altlinux.ru> 0.26-alt1_14
- update to new release by fcimport

* Tue Aug 06 2019 Igor Vlasenko <viy@altlinux.ru> 0.26-alt1_13
- update to new release by fcimport

* Mon Jun 17 2019 Igor Vlasenko <viy@altlinux.ru> 0.26-alt1_12
- update to new release by fcimport

* Fri Mar 01 2019 Igor Vlasenko <viy@altlinux.ru> 0.26-alt1_10
- update to new release by fcimport

* Wed Aug 01 2018 Igor Vlasenko <viy@altlinux.ru> 0.26-alt1_9
- update to new release by fcimport

* Sun Jul 15 2018 Igor Vlasenko <viy@altlinux.ru> 0.26-alt1_8
- update to new release by fcimport

* Wed Apr 04 2018 Igor Vlasenko <viy@altlinux.ru> 0.26-alt1_6
- update to new release by fcimport

* Wed Sep 27 2017 Igor Vlasenko <viy@altlinux.ru> 0.26-alt1_5
- update to new release by fcimport

* Thu Aug 03 2017 Igor Vlasenko <viy@altlinux.ru> 0.26-alt1_4
- update to new release by fcimport

* Wed Mar 15 2017 Igor Vlasenko <viy@altlinux.ru> 0.26-alt1_2
- update to new release by fcimport

* Thu Nov 17 2016 Igor Vlasenko <viy@altlinux.ru> 0.26-alt1_1
- update to new release by fcimport

* Sun May 29 2016 Igor Vlasenko <viy@altlinux.ru> 0.25-alt1_7
- update to new release by fcimport

* Wed Mar 02 2016 Igor Vlasenko <viy@altlinux.ru> 0.25-alt1_5
- update to new release by fcimport

* Mon Sep 21 2015 Igor Vlasenko <viy@altlinux.ru> 0.25-alt1_4
- update to new release by fcimport

* Mon Oct 20 2014 Igor Vlasenko <viy@altlinux.ru> 0.24-alt1_1
- update to new release by fcimport

* Tue Sep 16 2014 Igor Vlasenko <viy@altlinux.ru> 0.23-alt1_8
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 0.23-alt1_6
- update to new release by fcimport

* Tue Aug 27 2013 Igor Vlasenko <viy@altlinux.ru> 0.23-alt1_5
- update to new release by fcimport

* Mon Aug 05 2013 Igor Vlasenko <viy@altlinux.ru> 0.23-alt1_3
- update to new release by fcimport

* Fri Jul 12 2013 Igor Vlasenko <viy@altlinux.ru> 0.23-alt1_2
- update to new release by fcimport

* Tue May 21 2013 Igor Vlasenko <viy@altlinux.ru> 0.23-alt1_1
- update to new release by fcimport

* Mon Mar 04 2013 Igor Vlasenko <viy@altlinux.ru> 0.17-alt1_4
- update to new release by fcimport

* Tue Jul 31 2012 Igor Vlasenko <viy@altlinux.ru> 0.17-alt1_3
- update to new release by fcimport

* Tue Jun 05 2012 Igor Vlasenko <viy@altlinux.ru> 0.16-alt1_2
- fc import

