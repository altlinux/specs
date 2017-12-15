%define _unpackaged_files_terminate_build 1
%def_with bootstrap
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl(Benchmark.pm) perl(CPAN.pm) perl(ExtUtils/MM_Unix.pm) perl(ExtUtils/Manifest.pm) perl(Fcntl.pm) perl(File/Find.pm) perl(JSON.pm) perl(Module/Build.pm) perl(Parse/CPAN/Meta.pm) perl(Scalar/Util.pm) perl(YAML/Tiny.pm) perl(base.pm) perl-devel perl-podlators
# END SourceDeps(oneline)
# Pick up the right dictionary for the spell check
%if %(perl -e 'print $] >= 5.010000 ? 1 : 0;')
%global speller hunspell
%else
%global speller aspell
%endif

# some arches don't have valgrind so we need to disable its support on them
%ifarch %{ix86} x86_64 ppc ppc64 ppc64le s390x %{arm} aarch64
%global with_valgrind 1
%endif

Name:		perl-Test-LeakTrace
Summary:	Trace memory leaks
Version:	0.16
Release:	alt1.1
License:	GPL+ or Artistic
Group:		Development/Perl
URL:		http://search.cpan.org/dist/Test-LeakTrace/
Source0:	http://www.cpan.org/authors/id/L/LE/LEEJO/Test-LeakTrace-%{version}.tar.gz
# Module Build
BuildRequires:	perl
BuildRequires:	perl(ExtUtils/MakeMaker.pm)
BuildRequires:	perl(inc/Module/Install.pm)
BuildRequires:	perl(Module/Install/AuthorTests.pm)
BuildRequires:	perl(Module/Install/Repository.pm)
# Module Runtime
BuildRequires:	perl(Exporter.pm)
BuildRequires:	perl(strict.pm)
BuildRequires:	perl(Test/Builder/Module.pm)
BuildRequires:	perl(warnings.pm)
BuildRequires:	perl(XSLoader.pm)
# Test Suite
BuildRequires:	perl(autouse.pm)
BuildRequires:	perl(Class/Struct.pm)
BuildRequires:	perl(constant.pm)
BuildRequires:	perl(Data/Dumper.pm)
BuildRequires:	perl(Test/More.pm)
BuildRequires:	perl(threads.pm)
# Extra Tests
BuildRequires:	perl(Test/Pod.pm)
BuildRequires:	perl(Test/Pod/Coverage.pm)
%if !%{defined perl_bootstrap}
# Cycle: perl-Test-LeakTrace a.. perl-Test-Spelling a.. perl-Pod-Spell
# a.. perl-File-SharedDir-ProjectDistDir a.. perl-Path-Tiny a.. perl-Unicode-UTF8
# a.. perl-Test-LeakTrace
BuildRequires:	perl(Test/Spelling.pm) %{speller}-en
%endif
BuildRequires:	perl(Test/Synopsis.pm)
%if 0%{?with_valgrind}
BuildRequires:	perl(Test/Valgrind.pm)
%endif
# Runtime

# Don't provide private perl libs

Source44: import.info

%description
Test::LeakTrace provides several functions that trace memory leaks. This module
scans arenas, the memory allocation system, so it can detect any leaked SVs in
given blocks.

Leaked SVs are SVs that are not released after the end of the scope they have
been created. These SVs include global variables and internal caches. For
example, if you call a method in a tracing block, perl might prepare a cache
for the method. Thus, to trace true leaks, no_leaks_ok() and leaks_cmp_ok()
executes a block more than once.

%prep
%setup -q -n Test-LeakTrace-%{version}

# Remove redundant exec bits
chmod -c -x lib/Test/LeakTrace/Script.pm t/lib/foo.pl

# Fix up shellbangs in doc scripts
sed -i -e 's|^#!perl|#!/usr/bin/perl|' benchmark/*.pl example/*.{pl,t} {t,xt}/*.t

# Avoid bundled Module::Install and use the system version instead
rm -rf inc/
sed -i -e '/^inc\//d' MANIFEST

%if_with bootstrap
rm xt/05_valgrind.t
sed -i -e '/^xt\/05_valgrind\.t/d' MANIFEST
%endif

%build
perl Makefile.PL INSTALLMAN1DIR=%_man1dir INSTALLDIRS=vendor OPTIMIZE="%{optflags}"
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -type f -name '*.bs' -a -size 0 -exec rm -f {} ';'
# %{_fixperms} %{buildroot}

%check
make test

# Run the release tests
# Don't spell-check JA.pod as it can generate false positives
mv lib/Test/LeakTrace/JA.pod ./
touch lib/Test/LeakTrace/JA.pod
%if 0%{?with_valgrind}
DICTIONARY=en_US make test TEST_FILES="xt/*.t"
%else
DICTIONARY=en_US make test TEST_FILES="$(echo xt/*.t | sed 's|xt/05_valgrind.t||')"
%endif
rm lib/Test/LeakTrace/JA.pod
mv ./JA.pod lib/Test/LeakTrace/

%files
%doc Changes README benchmark/ example/ %{?perl_default_filter:t/ xt/} example
%{perl_vendor_archlib}/auto/Test/
%{perl_vendor_archlib}/Test/

%changelog
* Fri Dec 15 2017 Igor Vlasenko <viy@altlinux.ru> 0.16-alt1.1
- rebuild with new perl 5.26.1

* Wed Aug 02 2017 Igor Vlasenko <viy@altlinux.ru> 0.16-alt1
- automated CPAN update

* Sun Feb 12 2017 Igor Vlasenko <viy@altlinux.ru> 0.15-alt2.2.1.1
- unbootstrap after rebuild with new perl 5.24.1

* Fri Feb 03 2017 Igor Vlasenko <viy@altlinux.ru> 0.15-alt2.2.1
- rebuild with new perl 5.24.1

* Sat Nov 28 2015 Igor Vlasenko <viy@altlinux.ru> 0.15-alt2.2
- unbootstrap

* Wed Nov 25 2015 Igor Vlasenko <viy@altlinux.ru> 0.15-alt2.1.1
- rebuild with new perl 5.22.0

* Tue Dec 09 2014 Igor Vlasenko <viy@altlinux.ru> 0.15-alt2.1
- rebuild with new perl 5.20.1

* Fri Dec 05 2014 Igor Vlasenko <viy@altlinux.ru> 0.15-alt2
- support for bootstrap

* Tue Nov 25 2014 Igor Vlasenko <viy@altlinux.ru> 0.15-alt1
- automated CPAN update

* Mon Oct 27 2014 Igor Vlasenko <viy@altlinux.ru> 0.14-alt3_13
- update to new release by fcimport

* Wed Aug 27 2014 Igor Vlasenko <viy@altlinux.ru> 0.14-alt3_10
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 0.14-alt3_9
- update to new release by fcimport

* Thu Apr 10 2014 Igor Vlasenko <viy@altlinux.ru> 0.14-alt3_8
- update to new release by fcimport

* Thu Oct 10 2013 Igor Vlasenko <viy@altlinux.ru> 0.14-alt3_7
- update to new release by fcimport

* Thu Sep 05 2013 Cronbuild Service <cronbuild@altlinux.org> 0.14-alt3_4
- rebuild to get rid of unmets

* Thu Oct 11 2012 Igor Vlasenko <viy@altlinux.ru> 0.14-alt2_4
- update to new release by fcimport

* Mon Sep 10 2012 Cronbuild Service <cronbuild@altlinux.org> 0.14-alt2_2
- rebuild with new perl

* Tue May 29 2012 Igor Vlasenko <viy@altlinux.ru> 0.14-alt1_2
- fc import

