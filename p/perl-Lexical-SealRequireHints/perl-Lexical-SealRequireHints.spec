# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl(CPAN.pm) perl(Cwd.pm) perl(ExtUtils/MakeMaker.pm) perl(File/Spec.pm) perl-Module-Build perl-devel perl-podlators
# END SourceDeps(oneline)
Name:           perl-Lexical-SealRequireHints
Version:        0.007
Release:        alt3_6
Summary:        Prevent leakage of lexical hints
License:        GPL+ or Artistic
Group:          Development/Perl
URL:            http://search.cpan.org/dist/Lexical-SealRequireHints/
Source0:        http://www.cpan.org/authors/id/Z/ZE/ZEFRAM/Lexical-SealRequireHints-%{version}.tar.gz
BuildRequires:  perl
BuildRequires:  perl(Module/Build.pm)
# Tests
BuildRequires:  perl(Test/More.pm)
BuildRequires:  perl(XSLoader.pm)
# Optional tests
BuildRequires:  perl(Test/Pod.pm)
BuildRequires:  perl(Test/Pod/Coverage.pm)
BuildRequires:  perl(threads.pm)
BuildRequires:  perl(Thread/Semaphore.pm)
Conflicts:      perl(B:Hooks/OP/Check.pm) < 0.19


Source44: import.info

%description
This module works around two historical bugs in Perl's handling of the %^H
(lexical hints) variable. One bug causes lexical state in one file to leak
into another that is required/used from it. This bug, [perl #68590], was
present from Perl 5.6 up to Perl 5.10, fixed in Perl 5.11.0. The second bug
causes lexical state (normally a blank %^H once the first bug is fixed) to
leak outwards from utf8.pm, if it is automatically loaded during Unicode
regular expression matching, into whatever source is compiling at the time
of the regexp match. This bug, [perl #73174], was present from Perl 5.8.7
up to Perl 5.11.5, fixed in Perl 5.12.0.

%prep
%setup -q -n Lexical-SealRequireHints-%{version}

%build
%{__perl} Build.PL --install_path bindoc=%_man1dir installdirs=vendor optimize="$RPM_OPT_FLAGS"
./Build

%install
./Build install destdir=$RPM_BUILD_ROOT create_packlist=0
find $RPM_BUILD_ROOT -type f -name '*.bs' -size 0 -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;
# %{_fixperms} $RPM_BUILD_ROOT/*

%check
./Build test

%files
%doc Changes
%{perl_vendor_archlib}/auto/*
%{perl_vendor_archlib}/Lexical*

%changelog
* Thu Nov 14 2013 Igor Vlasenko <viy@altlinux.ru> 0.007-alt3_6
- Sisyphus build

* Thu Sep 05 2013 Cronbuild Service <cronbuild@altlinux.org> 0.007-alt2_6
- rebuild to get rid of unmets

* Tue Aug 27 2013 Igor Vlasenko <viy@altlinux.ru> 0.007-alt1_6
- update to new release by fcimport

* Mon Aug 05 2013 Igor Vlasenko <viy@altlinux.ru> 0.007-alt1_5
- update to new release by fcimport

* Mon Mar 04 2013 Igor Vlasenko <viy@altlinux.ru> 0.007-alt1_4
- update to new release by fcimport

* Fri Sep 28 2012 Igor Vlasenko <viy@altlinux.ru> 0.007-alt1_3
- new version

