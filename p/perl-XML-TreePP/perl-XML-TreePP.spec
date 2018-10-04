Name: perl-XML-TreePP
Version: 0.43
Release: alt2
Summary: Pure Perl implementation for parsing/writing XML documents
Group: Development/Other
License: GPL+ or Artistic
URL: https://metacpan.org/release/XML-TreePP
Source0: https://cpan.metacpan.org/authors/id/K/KA/KAWASAKI/XML-TreePP-%{version}.tar.gz

BuildArch: noarch
BuildRequires: rpm-build-perl
BuildRequires: perl-devel
BuildRequires: perl(Encode.pm)
BuildRequires: perl(HTTP/Lite.pm)
BuildRequires: perl(Jcode.pm)
BuildRequires: perl(LWP/UserAgent.pm)
#BuildRequires: perl(LWP/UserAgent/WithCache.pm)
BuildRequires: perl(Tie/IxHash.pm)
# Extra build requirements for tests (with $MORE_TESTS)
#BuildRequires: perl(HTTP::Lite)
#BuildRequires: perl(LWP::UserAgent::WithCache)

%description
Pure Perl implementation for parsing/writing XML documents

%prep
%setup -q -n XML-TreePP-%{version}

%build
/usr/bin/perl Makefile.PL INSTALLDIRS=vendor
%make_build

%install
make %{?_smp_mflags} pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} ';'
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null ';'
chmod -R u+w $RPM_BUILD_ROOT

chmod a-x Changes
chmod a-x $RPM_BUILD_ROOT/%{perl_vendor_privlib}/XML/TreePP.pm

%check
make %{?_smp_mflags} test || :

%files
%doc README Changes
%dir %{perl_vendor_privlib}/XML/
%{perl_vendor_privlib}/XML/TreePP.pm

%changelog
* Thu Oct 04 2018 Andrey Cherepanov <cas@altlinux.org> 0.43-alt2
- Initial build for Sisyphus.

* Wed Aug 01 2018 Igor Vlasenko <viy@altlinux.ru> 0.43-alt1_10
- update to new release by fcimport

* Sun Jul 15 2018 Igor Vlasenko <viy@altlinux.ru> 0.43-alt1_9
- update to new release by fcimport

* Wed Apr 04 2018 Igor Vlasenko <viy@altlinux.ru> 0.43-alt1_8
- update to new release by fcimport

* Wed Sep 27 2017 Igor Vlasenko <viy@altlinux.ru> 0.43-alt1_7
- update to new release by fcimport

* Thu Aug 03 2017 Igor Vlasenko <viy@altlinux.ru> 0.43-alt1_6
- update to new release by fcimport

* Wed Mar 15 2017 Igor Vlasenko <viy@altlinux.ru> 0.43-alt1_5
- update to new release by fcimport

* Sun May 29 2016 Igor Vlasenko <viy@altlinux.ru> 0.43-alt1_4
- update to new release by fcimport

* Wed Mar 02 2016 Igor Vlasenko <viy@altlinux.ru> 0.43-alt1_3
- update to new release by fcimport

* Mon Sep 21 2015 Igor Vlasenko <viy@altlinux.ru> 0.43-alt1_2
- update to new release by fcimport

* Tue Sep 16 2014 Igor Vlasenko <viy@altlinux.ru> 0.39-alt1_14
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 0.39-alt1_13
- update to new release by fcimport

* Mon Sep 02 2013 Igor Vlasenko <viy@altlinux.ru> 0.39-alt1_12
- update to new release by fcimport

* Mon Aug 05 2013 Igor Vlasenko <viy@altlinux.ru> 0.39-alt1_11
- update to new release by fcimport

* Mon Mar 04 2013 Igor Vlasenko <viy@altlinux.ru> 0.39-alt1_10
- update to new release by fcimport

* Tue Jul 31 2012 Igor Vlasenko <viy@altlinux.ru> 0.39-alt1_9
- update to new release by fcimport

* Wed May 23 2012 Igor Vlasenko <viy@altlinux.ru> 0.39-alt1_7
- fc import

