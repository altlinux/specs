%filter_from_requires /^perl(CPAN.SQLite.pm)/d
%filter_from_requires /^perl(CPANPLUS.Backend.pm)/d
%filter_from_requires /^perl(CPANPLUS.Configure.pm)/d
Group: Development/Perl
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
#BuildRequires: perl(CPAN.pm) perl(CPAN/SQLite.pm) perl(CPAN/SQLite/Index.pm) perl(CPANPLUS/Backend.pm) perl(CPANPLUS/Configure.pm) 
BuildRequires: perl(File/Find/Iterator.pm) perl(GDBM_File.pm) perl(IO/String.pm) perl(IPC/Run3.pm) perl(Pod/Escapes.pm) perl(Pod/Find.pm) perl(Pod/Parser.pm) perl(Smart/Comments.pm) perl(Sort/Key/Natural.pm) perl-podlators
# END SourceDeps(oneline)
%define __spec_autodep_custom_pre export PERL5OPT='-I%buildroot%{_libexecdir}/%{name}/t -MMyTestHelpers'
# fedora bcond_with macro
%define bcond_with() %{expand:%%{?_with_%{1}:%%global with_%{1} 1}}
%define bcond_without() %{expand:%%{!?_without_%{1}:%%global with_%{1} 1}}
# redefine altlinux specific with and without
%define with()         %{expand:%%{?with_%{1}:1}%%{!?with_%{1}:0}}
%define without()      %{expand:%%{?with_%{1}:0}%%{!?with_%{1}:1}}
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
# Perform optinal tests
%bcond_without perl_podlinkcheck_enables_optional_test

Name:           perl-podlinkcheck
Version:        15
Release:        alt3_22
Summary:        Check Perl POD L<> link references
License:        GPLv3+
URL:            https://metacpan.org/release/podlinkcheck
Source0:        https://cpan.metacpan.org/authors/id/K/KR/KRYDE/podlinkcheck-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  rpm-build-perl
BuildRequires:  perl-devel
BuildRequires:  perl
BuildRequires:  perl(ExtUtils/MakeMaker.pm)
BuildRequires:  perl(strict.pm)
BuildRequires:  perl(warnings.pm)
# Run-time:
BuildRequires:  perl(base.pm)
BuildRequires:  perl(Carp.pm)
# Config not used at tests
BuildRequires:  perl(constant/defer.pm)
# File::Find::Iterator not used at tests
BuildRequires:  perl(File/HomeDir.pm)
BuildRequires:  perl(File/Spec.pm)
BuildRequires:  perl(File/Temp.pm)
# FindBin not used at tests
# Getopt::Long not used at tests
BuildRequires:  perl(IPC/Run.pm)
BuildRequires:  perl(List/Util.pm)
BuildRequires:  perl(Locale/TextDomain.pm)
# Pod::Find not used at tests
BuildRequires:  perl(Pod/Simple.pm)
# Search::Dict not used at tests
BuildRequires:  perl(Text/Tabs.pm)
BuildRequires:  perl(vars.pm)
# Recommended run-time:
# Sort::Key::Natural not used at tests
# Tests:
BuildRequires:  perl(Config.pm)
# Data::Dumper not used
BuildRequires:  perl(Exporter.pm)
BuildRequires:  perl(lib.pm)
BuildRequires:  perl(Scalar/Util.pm)
BuildRequires:  perl(Test/More.pm)
%if %{with perl_podlinkcheck_enables_optional_test}
# Optional tests:
BuildRequires:  perl(Data/Dumper.pm)
# Devel::FindRef does not built with Perl 5.22
# Devel::StackTrace not used
%endif
Requires:       perl(Config.pm)
Requires:       perl(File/Find/Iterator.pm)
Requires:       perl(File/HomeDir.pm)
Requires:       perl(File/Spec.pm) >= 0.800
Requires:       perl(File/Temp.pm)
Requires:       perl(FindBin.pm)
Requires:       perl(Getopt/Long.pm)
Requires:       perl(IPC/Run.pm)
Requires:       perl(Pod/Find.pm)
Requires:       perl(Search/Dict.pm)
# Recommended:
Requires:     perl(Sort/Key/Natural.pm)
# We do not (build-)require CPAN, CPANPLUS on purpose
Requires:       perl(CPAN.pm)
#Requires:       perl(CPAN/SQLite.pm)
#Requires:       perl(CPANPLUS/Backend.pm)
#Requires:       perl(CPANPLUS/Configure.pm)

# Remove under-specified dependencies

# Remove private modules


Source44: import.info
%filter_from_requires /^perl(File.Spec.pm)/d
%filter_from_requires /^perl(MyTestHelpers.pm)/d
%filter_from_provides /^perl(MyTestHelpers.pm)/d

%description
PodLinkCheck parses Perl POD from a script, module or documentation
and checks that L<> links within it refer to a known program, module,
or man page.

%package tests
Group: Development/Perl
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl(Config.pm)
Requires:       perl(Scalar/Util.pm)
%if %{with perl_podlinkcheck_enables_optional_test}
Requires:       perl(Data/Dumper.pm)
Requires:       perl(File/HomeDir.pm)
%endif

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
%setup -q -n podlinkcheck-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{makeinstall_std}
# %{_fixperms} %{buildroot}/*
# Install tests
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
#!/bin/sh
cd %{_libexecdir}/%{name} && exec prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test

%check
export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
make test

%files
%doc --no-dereference COPYING
%doc Changes
%{_bindir}/*
%{perl_vendor_privlib}/*
%{_mandir}/man1/*

%files tests
%{_libexecdir}/%{name}

%changelog
* Fri Dec 01 2023 Igor Vlasenko <viy@altlinux.org> 15-alt3_22
- reimport; enabled tests

* Fri Apr 16 2021 Igor Vlasenko <viy@altlinux.org> 15-alt3
- fixed build

* Sun Oct 15 2017 Igor Vlasenko <viy@altlinux.ru> 15-alt2
- cleaned up perl-CPAN-SQLite BR: dependency

* Tue May 09 2017 Igor Vlasenko <viy@altlinux.ru> 15-alt1
- automated CPAN update

* Sat Mar 19 2016 Igor Vlasenko <viy@altlinux.ru> 14-alt1
- automated CPAN update

* Sat Nov 21 2015 Igor Vlasenko <viy@altlinux.ru> 12-alt3_5
- dropped BR: perl(Devel/FindRef.pm) 

* Thu Dec 18 2014 Igor Vlasenko <viy@altlinux.ru> 12-alt2_5
- update to new release by fcimport

* Tue Jul 08 2014 Igor Vlasenko <viy@altlinux.ru> 12-alt2_4
- update to new release by fcimport

* Thu Nov 14 2013 Igor Vlasenko <viy@altlinux.ru> 12-alt2_3
- Sisyphus build

* Mon Sep 02 2013 Igor Vlasenko <viy@altlinux.ru> 12-alt1_3
- update to new release by fcimport

* Mon Aug 05 2013 Igor Vlasenko <viy@altlinux.ru> 12-alt1_2
- update to new release by fcimport

* Wed Feb 20 2013 Igor Vlasenko <viy@altlinux.ru> 12-alt1_1
- update to new release by fcimport

* Mon Feb 04 2013 Igor Vlasenko <viy@altlinux.ru> 11-alt1_1
- initial fc import

