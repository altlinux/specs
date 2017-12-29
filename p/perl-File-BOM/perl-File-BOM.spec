Group: Development/Perl
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl(CPAN.pm) perl-podlators
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           perl-File-BOM
Version:        0.15
Release:        alt2_6
Summary:        Utilities for handling Byte Order Marks
License:        GPL+ or Artistic
URL:            http://search.cpan.org/dist/File-BOM/
Source0:        http://www.cpan.org/authors/id/M/MA/MATTLAW/File-BOM-%{version}.tar.gz
BuildArch:      noarch
# Build
BuildRequires:  perl-devel
BuildRequires:  rpm-build-perl
BuildRequires:  perl(lib.pm)
BuildRequires:  perl(Module/Build.pm)
BuildRequires:  perl(strict.pm)
BuildRequires:  perl(warnings.pm)
# Runtime
BuildRequires:  perl(base.pm)
BuildRequires:  perl(bytes.pm)
BuildRequires:  perl(Carp.pm)
BuildRequires:  perl(Encode.pm)
BuildRequires:  perl(Exporter.pm)
BuildRequires:  perl(Fcntl.pm)
BuildRequires:  perl(Readonly.pm)
BuildRequires:  perl(Symbol.pm)
# Tests only
BuildRequires:  perl(File/Spec/Functions.pm)
BuildRequires:  perl(File/Temp.pm)
BuildRequires:  perl(POSIX.pm)
BuildRequires:  perl(Test/Exception.pm)
BuildRequires:  perl(Test/More.pm)
BuildRequires:  perl(Test/Simple.pm)
BuildRequires:  perl(utf8.pm)
Requires:       perl(Encode.pm) >= 1.990
Requires:       perl(Readonly.pm) >= 0.060



Source44: import.info
%filter_from_requires /^perl\\(Encode.pm\\)$/d
%filter_from_requires /^perl\\(Readonly.pm\\)$/d

%description
This module provides functions for handling Unicode byte order marks, which
are to be found at the beginning of some files and streams.

%prep
%setup -q -n File-BOM-%{version}

%build
perl Build.PL installdirs=vendor
./Build

%install
./Build install --destdir=%{buildroot} --create_packlist=0
# %{_fixperms} %{buildroot}/*

%check
./Build test

%files
%doc Changes README TODO
%{perl_vendor_privlib}/*

%changelog
* Fri Dec 29 2017 Igor Vlasenko <viy@altlinux.ru> 0.15-alt2_6
- to Sisyphus

* Wed Sep 27 2017 Igor Vlasenko <viy@altlinux.ru> 0.15-alt1_6
- update to new release by fcimport

* Thu Aug 03 2017 Igor Vlasenko <viy@altlinux.ru> 0.15-alt1_5
- update to new release by fcimport

* Wed Mar 15 2017 Igor Vlasenko <viy@altlinux.ru> 0.15-alt1_4
- update to new release by fcimport

* Sun May 29 2016 Igor Vlasenko <viy@altlinux.ru> 0.15-alt1_3
- update to new release by fcimport

* Wed Mar 02 2016 Igor Vlasenko <viy@altlinux.ru> 0.15-alt1_2
- update to new release by fcimport

* Mon Sep 21 2015 Igor Vlasenko <viy@altlinux.ru> 0.14-alt2_21
- update to new release by fcimport

* Tue Sep 16 2014 Igor Vlasenko <viy@altlinux.ru> 0.14-alt2_19
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 0.14-alt2_18
- update to new release by fcimport

* Tue Aug 27 2013 Igor Vlasenko <viy@altlinux.ru> 0.14-alt2_17
- update to new release by fcimport

* Mon Aug 05 2013 Igor Vlasenko <viy@altlinux.ru> 0.14-alt2_16
- update to new release by fcimport

* Wed Feb 27 2013 Igor Vlasenko <viy@altlinux.ru> 0.14-alt2_15
- update to new release by fcimport

* Tue Jul 31 2012 Igor Vlasenko <viy@altlinux.ru> 0.14-alt2_14
- update to new release by fcimport

* Fri May 25 2012 Igor Vlasenko <viy@altlinux.ru> 0.14-alt2_12
- fc import

* Thu May 24 2012 Igor Vlasenko <viy@altlinux.ru> 0.14-alt1_12
- fc import

