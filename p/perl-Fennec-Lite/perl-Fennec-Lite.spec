# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl-Module-Build perl-podlators
# END SourceDeps(oneline)
Name:           perl-Fennec-Lite
Version:        0.004
Release:        alt2_10
Summary:        Minimalist Fennec, the commonly used bits
License:        GPL+ or Artistic
Group:          Development/Perl
URL:            http://search.cpan.org/dist/Fennec-Lite/
Source0:        http://www.cpan.org/authors/id/E/EX/EXODIST/Fennec-Lite-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl(Carp.pm)
BuildRequires:  perl(List/Util.pm)
BuildRequires:  perl(Module/Build.pm)
BuildRequires:  perl(Test/Builder.pm)
BuildRequires:  perl(Test/More.pm)
Requires:       perl(Test/Builder.pm)
Requires:       perl(Test/More.pm)
Source44: import.info

%description
Fennec does a ton, but it may be hard to adopt it all at once. It also is a
large project, and has not yet been fully split into component projects.
Fennec::Lite takes a minimalist approach to do for Fennec what Mouse does
for Moose.

%prep
%setup -q -n Fennec-Lite-%{version}

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
%doc README
%{perl_vendor_privlib}/*

%changelog
* Mon Sep 26 2016 Igor Vlasenko <viy@altlinux.ru> 0.004-alt2_10
- to Sisyphus

* Sun May 29 2016 Igor Vlasenko <viy@altlinux.ru> 0.004-alt1_10
- update to new release by fcimport

* Wed Mar 02 2016 Igor Vlasenko <viy@altlinux.ru> 0.004-alt1_9
- update to new release by fcimport

* Mon Sep 21 2015 Igor Vlasenko <viy@altlinux.ru> 0.004-alt1_8
- update to new release by fcimport

* Tue Sep 16 2014 Igor Vlasenko <viy@altlinux.ru> 0.004-alt1_6
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 0.004-alt1_5
- update to new release by fcimport

* Tue Aug 27 2013 Igor Vlasenko <viy@altlinux.ru> 0.004-alt1_4
- update to new release by fcimport

* Mon Aug 05 2013 Igor Vlasenko <viy@altlinux.ru> 0.004-alt1_3
- update to new release by fcimport

* Fri Apr 26 2013 Igor Vlasenko <viy@altlinux.ru> 0.004-alt1_2
- initial fc import

