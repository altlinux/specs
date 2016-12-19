# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl(Alien/SeleniumRC.pm) perl(CPAN.pm) perl-Module-Build perl-podlators
# END SourceDeps(oneline)
Name:           perl-TAP-Formatter-HTML
Version:        0.11
Release:        alt1_10
Summary:        TAP Test Harness output delegate for html output
License:        GPL+ or Artistic
Group:          Development/Other
URL:            http://search.cpan.org/dist/TAP-Formatter-HTML/
Source0:        http://www.cpan.org/authors/id/S/SP/SPURKIS/TAP-Formatter-HTML-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl(accessors.pm)
BuildRequires:  perl(Module/Build.pm)
BuildRequires:  perl(TAP/Parser.pm)
BuildRequires:  perl(Template.pm)
BuildRequires:  perl(Test/More.pm)
BuildRequires:  perl(URI.pm)
Requires:       perl(accessors.pm) >= 0.02
Requires:       perl(TAP/Parser.pm) >= 3.10
Requires:       perl(Template.pm) >= 2.14
Requires:       perl(URI.pm) >= 1.35
Source44: import.info

%description
This module provides HTML output formatting for TAP::Harness (a replacement
for Test::Harness. It is largely based on ideas from TAP::Test::HTMLMatrix
(which was built on Test::Harness and thus had a few limitations - hence
this module). For sample output, see:

%prep
%setup -q -n TAP-Formatter-HTML-%{version}

%build
%{__perl} Build.PL --install_path bindoc=%_man1dir installdirs=vendor
./Build

%install

./Build install destdir=$RPM_BUILD_ROOT create_packlist=0
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;

# %{_fixperms} $RPM_BUILD_ROOT/*

%check
./Build test

%files
%doc Changes README Todo
%{perl_vendor_privlib}/*

%changelog
* Mon Dec 19 2016 Igor Vlasenko <viy@altlinux.ru> 0.11-alt1_10
- update to new release by fcimport

* Mon Mar 07 2016 Igor Vlasenko <viy@altlinux.ru> 0.11-alt1_9
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 0.11-alt1_8
- update to new release by fcimport

* Mon Oct 27 2014 Igor Vlasenko <viy@altlinux.ru> 0.11-alt1_6
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 0.11-alt1_5
- update to new release by fcimport

* Wed Aug 07 2013 Igor Vlasenko <viy@altlinux.ru> 0.11-alt1_4
- Sisyphus build

* Mon Mar 04 2013 Igor Vlasenko <viy@altlinux.ru> 0.11-alt1_2
- update to new release by fcimport

* Tue Jan 29 2013 Igor Vlasenko <viy@altlinux.ru> 0.11-alt1_1
- update to new release by fcimport

* Tue Jul 31 2012 Igor Vlasenko <viy@altlinux.ru> 0.09-alt2_8
- update to new release by fcimport

* Fri May 25 2012 Igor Vlasenko <viy@altlinux.ru> 0.09-alt2_6
- fc import

* Thu May 24 2012 Igor Vlasenko <viy@altlinux.ru> 0.09-alt1_6
- fc import

