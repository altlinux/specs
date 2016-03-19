%define _unpackaged_files_terminate_build 1
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl(CPAN.pm) perl(CPAN/SQLite.pm) perl(CPAN/SQLite/Index.pm) perl(Config.pm) perl(Fcntl.pm) perl(File/Find.pm) perl(FindBin.pm) perl(GDBM_File.pm) perl(IO/String.pm) perl(IPC/Open3.pm) perl(IPC/Run3.pm) perl(Pod/Escapes.pm) perl(Pod/ParseLink.pm) perl(Pod/Parser.pm) perl(Pod/Simple/HTML.pm) perl(Pod/Simple/HTMLBatch.pm) perl(Smart/Comments.pm) perl-devel perl-podlators
# END SourceDeps(oneline)
Name:           perl-podlinkcheck
Version:        14
Release:        alt1
Summary:        Check Perl POD L<> link references
License:        GPLv3+
Group:          Development/Perl
URL:            http://search.cpan.org/dist/podlinkcheck/
Source:        http://www.cpan.org/authors/id/K/KR/KRYDE/podlinkcheck-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl
# The inc/my_pod2html is not executed
BuildRequires:  perl(lib.pm)
BuildRequires:  perl(ExtUtils/MakeMaker.pm)
# Run-time:
BuildRequires:  perl(base.pm)
BuildRequires:  perl(Carp.pm)
BuildRequires:  perl(constant/defer.pm)
BuildRequires:  perl(File/Find/Iterator.pm)
BuildRequires:  perl(File/Spec.pm)
BuildRequires:  perl(File/Temp.pm)
BuildRequires:  perl(Getopt/Long.pm)
BuildRequires:  perl(IPC/Run.pm)
BuildRequires:  perl(List/Util.pm)
BuildRequires:  perl(Locale/TextDomain.pm)
BuildRequires:  perl(Pod/Find.pm)
BuildRequires:  perl(Pod/Simple.pm)
BuildRequires:  perl(Text/Tabs.pm)
# Recommended run-time:
BuildRequires:  perl(Sort/Key/Natural.pm)
# Tests:
BuildRequires:  perl(Exporter.pm)
BuildRequires:  perl(Scalar/Util.pm)
BuildRequires:  perl(Test/More.pm)
# Optional tests:
BuildRequires:  perl(Data/Dumper.pm)
BuildRequires:  perl(Devel/FindRef.pm)
BuildRequires:  perl(Devel/StackTrace.pm)
BuildRequires:  perl(File/HomeDir.pm)
Requires:       perl(File/Find/Iterator.pm)
Requires:       perl(File/Spec.pm) >= 0.8
Requires:       perl(File/Temp.pm)
Requires:       perl(Getopt/Long.pm)
Requires:       perl(IPC/Run.pm)
Requires:       perl(Pod/Find.pm)
# Recommended:
Requires:       perl(Sort/Key/Natural.pm)
# We do not (build-)require CPAN on purpose

# Remove under-specified dependencies

Source44: import.info
%filter_from_requires /^perl\\(File.Spec.pm\\)$/d

%description
PodLinkCheck parses Perl POD from a script, module or documentation
and checks that L<> links within it refer to a known program, module,
or man page.

%prep
%setup -q -n podlinkcheck-%{version}

%build
perl Makefile.PL INSTALLMAN1DIR=%_man1dir INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
# %{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc Changes COPYING
%{_bindir}/*
%{perl_vendor_privlib}/*
%{_mandir}/man1/*

%changelog
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

