# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl(Fcntl.pm) perl(File/Spec/Functions.pm) perl-devel perl-podlators
# END SourceDeps(oneline)
Name:       perl-Log-Trace 
Version:    1.070 
Release:    alt2_11
# lib/Log/Trace.pm -> GPLv2+ 
License:    GPLv2+
Group:      Development/Perl
Summary:    A unified approach to tracing 
Source:     http://search.cpan.org/CPAN/authors/id/B/BB/BBC/Log-Trace-%{version}.tar.gz
Url:        http://search.cpan.org/dist/Log-Trace
BuildArch:  noarch

BuildRequires: perl(ExtUtils/MakeMaker.pm)
BuildRequires: perl(Test/More.pm)

# autoprov detects perl(DB), which is just wrong.  In this specific case,
# it's easier just to turn autoprov off.
AutoProv:   no
Provides:   perl(Log/Trace.pm) = %{version}
Source44: import.info

%description
This module provides a unified approach to tracing. A script can 'use
Log::Trace qw( < mode > )' to set the behaviour of the TRACE function.By
default, the trace functions are exported to the calling package only.
You can export the trace functions to other packages with the 'Deep'
option. See the "OPTIONS" manpage for more information. 


%prep
%setup -q -n Log-Trace-%{version}

%build
%{__perl} Makefile.PL INSTALLMAN1DIR=%_man1dir INSTALLDIRS=vendor
make %{?_smp_mflags}

%install

make pure_install PERL_INSTALL_ROOT=%{buildroot}
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'


%check
make test

%files
%doc README Changes COPYING 
%{perl_vendor_privlib}/*

%changelog
* Tue Dec 11 2012 Igor Vlasenko <viy@altlinux.ru> 1.070-alt2_11
- moved to Sisyphus (Tapper dep)

* Tue Jul 31 2012 Igor Vlasenko <viy@altlinux.ru> 1.070-alt1_11
- update to new release by fcimport

* Wed May 23 2012 Igor Vlasenko <viy@altlinux.ru> 1.070-alt1_9
- fc import

