Group: Development/Other
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl(Term/ReadLine.pm) perl(Test/Pod.pm) perl-podlators
# END SourceDeps(oneline)
# fedora bcond_with macro
%define bcond_with() %{expand:%%{?_with_%{1}:%%global with_%{1} 1}}
%define bcond_without() %{expand:%%{!?_without_%{1}:%%global with_%{1} 1}}
# redefine altlinux specific with and without
%define with()         %{expand:%%{?with_%{1}:1}%%{!?with_%{1}:0}}
%define without()      %{expand:%%{?with_%{1}:0}%%{!?with_%{1}:1}}
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
# Supported rpmbuild options:
#
# --with live-test/--without live-test
#   include/exclude LIVE_TEST testsuite
#   Default: --without (Requires networking, doesn't work in mock)
%bcond_with     live_test

Name:           perl-Web-Scraper
Version:        0.38
Release:        alt3_20
Summary:        Web Scraping Toolkit using HTML and CSS Selectors or XPath expressions
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/Web-Scraper
Source0:        https://cpan.metacpan.org/authors/id/M/MI/MIYAGAWA/Web-Scraper-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  rpm-build-perl
BuildRequires:  perl(base.pm)
BuildRequires:  perl(Module/Build/Tiny.pm)
BuildRequires:  perl(Carp.pm)
BuildRequires:  perl(HTML/Entities.pm)
BuildRequires:  perl(HTML/Selector/XPath.pm)
BuildRequires:  perl(HTML/Tagset.pm)
BuildRequires:  perl(HTML/TreeBuilder.pm)
BuildRequires:  perl(HTML/TreeBuilder/XPath.pm)
BuildRequires:  perl(HTML/TreeBuilder/LibXML.pm)
BuildRequires:  perl(List/Util.pm)
BuildRequires:  perl(LWP.pm)
BuildRequires:  perl(LWP/UserAgent.pm)
BuildRequires:  perl(Scalar/Util.pm)
BuildRequires:  perl(Test/Base.pm)
BuildRequires:  perl(Test/More.pm)
BuildRequires:  perl(Test/Requires.pm)
BuildRequires:  perl(UNIVERSAL/require.pm)
BuildRequires:  perl(URI.pm)
BuildRequires:  perl(warnings.pm)
BuildRequires:  perl(XML/XPathEngine.pm)
BuildRequires:  perl(YAML.pm)
BuildRequires:  perl(strict.pm)

# Required by the testsuite
BuildRequires:  /bin/ps


# rpm's deptracker misses these:
Requires:  perl(LWP/UserAgent.pm)


Source44: import.info

%description
Web::Scraper is a web scraper toolkit, inspired by Ruby's equivalent
Scrapi. It provides a DSL-ish interface for traversing HTML documents and
returning a neatly arranged Perl data structure.

%prep
%setup -q -n Web-Scraper-%{version}

# Package does not depend on ExtUtils::MakeMaker
sed -i '/ExtUtils::MakeMaker/d' META.*

%build
/usr/bin/perl Build.PL --installdirs=vendor
./Build

%install
./Build install --destdir=$RPM_BUILD_ROOT --create_packlist=0

# Web-Scraper >= 0.38 misses to install bin/scaper
# Install it manually
install -m 755 -d ${RPM_BUILD_ROOT}%{_bindir}
install -m 755 bin/scraper ${RPM_BUILD_ROOT}%{_bindir}

find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;

# %{_fixperms} $RPM_BUILD_ROOT/*

%check
LEAK_TEST=1 %{?with_live_test:LIVE_TEST=1} ./Build test

%files
%doc Changes README
%{_bindir}/scraper
%{perl_vendor_privlib}/*

%changelog
* Mon Jul 12 2021 Igor Vlasenko <viy@altlinux.org> 0.38-alt3_20
- to Sisyphus as perl-Finance-Quote dep

* Thu Jul 08 2021 Igor Vlasenko <viy@altlinux.org> 0.38-alt2_20
- update to new release by fcimport

* Wed Mar 17 2021 Igor Vlasenko <viy@altlinux.org> 0.38-alt2_19
- update to new release by fcimport

* Wed Jan 27 2021 Igor Vlasenko <viy@altlinux.ru> 0.38-alt2_18
- update to new release by fcimport

* Wed Sep 02 2020 Igor Vlasenko <viy@altlinux.ru> 0.38-alt1_18
- update to new release by fcimport

* Mon Jul 06 2020 Igor Vlasenko <viy@altlinux.ru> 0.38-alt1_17
- update to new release by fcimport

* Thu Mar 05 2020 Igor Vlasenko <viy@altlinux.ru> 0.38-alt1_16
- update to new release by fcimport

* Tue Aug 06 2019 Igor Vlasenko <viy@altlinux.ru> 0.38-alt1_15
- update to new release by fcimport

* Mon Jun 17 2019 Igor Vlasenko <viy@altlinux.ru> 0.38-alt1_14
- update to new release by fcimport

* Fri Mar 01 2019 Igor Vlasenko <viy@altlinux.ru> 0.38-alt1_13
- update to new release by fcimport

* Wed Aug 01 2018 Igor Vlasenko <viy@altlinux.ru> 0.38-alt1_12
- update to new release by fcimport

* Sun Jul 15 2018 Igor Vlasenko <viy@altlinux.ru> 0.38-alt1_11
- update to new release by fcimport

* Wed Apr 04 2018 Igor Vlasenko <viy@altlinux.ru> 0.38-alt1_10
- update to new release by fcimport

* Wed Sep 27 2017 Igor Vlasenko <viy@altlinux.ru> 0.38-alt1_9
- update to new release by fcimport

* Thu Aug 03 2017 Igor Vlasenko <viy@altlinux.ru> 0.38-alt1_8
- update to new release by fcimport

* Wed Mar 15 2017 Igor Vlasenko <viy@altlinux.ru> 0.38-alt1_7
- update to new release by fcimport

* Sun May 29 2016 Igor Vlasenko <viy@altlinux.ru> 0.38-alt1_6
- update to new release by fcimport

* Wed Mar 02 2016 Igor Vlasenko <viy@altlinux.ru> 0.38-alt1_5
- update to new release by fcimport

* Mon Sep 21 2015 Igor Vlasenko <viy@altlinux.ru> 0.38-alt1_3
- update to new release by fcimport

* Tue Dec 23 2014 Igor Vlasenko <viy@altlinux.ru> 0.38-alt1_1
- update to new release by fcimport

* Tue Sep 16 2014 Igor Vlasenko <viy@altlinux.ru> 0.37-alt1_6
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 0.37-alt1_5
- update to new release by fcimport

* Mon Sep 02 2013 Igor Vlasenko <viy@altlinux.ru> 0.37-alt1_4
- update to new release by fcimport

* Mon Aug 05 2013 Igor Vlasenko <viy@altlinux.ru> 0.37-alt1_3
- update to new release by fcimport

* Fri Apr 26 2013 Igor Vlasenko <viy@altlinux.ru> 0.37-alt1_2
- initial fc import

