Group: Development/Perl
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl-podlators
# END SourceDeps(oneline)
Name:           perl-Log-Trace
Version:        1.070
Release:        alt2_21
License:        GPLv2+
Summary:        A unified approach to tracing
Source:         http://search.cpan.org/CPAN/authors/id/B/BB/BBC/Log-Trace-%{version}.tar.gz
Url:            http://search.cpan.org/dist/Log-Trace
BuildArch:      noarch
# Build
BuildRequires:  perl
BuildRequires:  perl(ExtUtils/MakeMaker.pm)
# Runtime
BuildRequires:  perl(Carp.pm)
BuildRequires:  perl(Data/Dumper.pm)
BuildRequires:  perl(Data/Serializer.pm)
BuildRequires:  perl(Fcntl.pm)
BuildRequires:  perl(strict.pm)
BuildRequires:  perl(Sys/Syslog.pm)
BuildRequires:  perl(Time/HiRes.pm)
# Tests only
BuildRequires:  perl(File/Basename.pm)
BuildRequires:  perl(File/Spec.pm)
BuildRequires:  perl(File/Spec/Functions.pm)
BuildRequires:  perl(Test/More.pm)
Requires:     perl(Data/Dumper.pm)
Requires:     perl(Data/Serializer.pm)
Requires:     perl(Sys/Syslog.pm)
Requires:     perl(Time/HiRes.pm)


Source44: import.info
%filter_from_provides /^perl\\(DB.pm\\)$/d

%description
This module provides a unified approach to tracing. A script can 'use
Log::Trace qw( < mode > )' to set the behaviour of the TRACE function.By
default, the trace functions are exported to the calling package only.
You can export the trace functions to other packages with the 'Deep'
option. See the "OPTIONS" manpage for more information.

%prep
%setup -q -n Log-Trace-%{version}

%build
perl Makefile.PL INSTALLMAN1DIR=%_man1dir INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
# %{_fixperms} %{buildroot}/*

%check
make test

%files
%doc COPYING
%doc README Changes
%{perl_vendor_privlib}/*

%changelog
* Mon Dec 19 2016 Igor Vlasenko <viy@altlinux.ru> 1.070-alt2_21
- update to new release by fcimport

* Mon Mar 07 2016 Igor Vlasenko <viy@altlinux.ru> 1.070-alt2_20
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 1.070-alt2_18
- update to new release by fcimport

* Mon Oct 27 2014 Igor Vlasenko <viy@altlinux.ru> 1.070-alt2_16
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 1.070-alt2_15
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 1.070-alt2_14
- update to new release by fcimport

* Mon Aug 05 2013 Igor Vlasenko <viy@altlinux.ru> 1.070-alt2_13
- update to new release by fcimport

* Sun Feb 24 2013 Igor Vlasenko <viy@altlinux.ru> 1.070-alt2_12
- converted for ALT Linux by srpmconvert tools

* Tue Dec 11 2012 Igor Vlasenko <viy@altlinux.ru> 1.070-alt2_11
- moved to Sisyphus (Tapper dep)

* Tue Jul 31 2012 Igor Vlasenko <viy@altlinux.ru> 1.070-alt1_11
- update to new release by fcimport

* Wed May 23 2012 Igor Vlasenko <viy@altlinux.ru> 1.070-alt1_9
- fc import

