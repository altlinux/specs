%define _unpackaged_files_terminate_build 1
Group: Development/Perl
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl(Test/EOL.pm) perl(Test/Pod.pm) perl-podlators perl(Test/Most.pm)
# END SourceDeps(oneline)
#BuildRequires: perl(Test/Fixme.pm) perl(Test/NoTabs.pm)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           perl-Graphics-ColorNames
Version:        3.4.0
Release:        alt1
Summary:        Defines RGB values for common color names
License:        Artistic 2.0
URL:            https://metacpan.org/release/Graphics-ColorNames
Source0:        http://www.cpan.org/authors/id/R/RR/RRWO/Graphics-ColorNames-v%{version}.tar.gz
BuildArch:      noarch
# Build
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  rpm-build-perl
BuildRequires:  perl-devel
BuildRequires:  perl(ExtUtils/MakeMaker.pm)
BuildRequires:  perl(strict.pm)
BuildRequires:  perl(warnings.pm)
# Runtime
BuildRequires:  perl(Carp.pm)
BuildRequires:  perl(Exporter.pm)
BuildRequires:  perl(File/Spec/Functions.pm)
BuildRequires:  perl(integer.pm)
BuildRequires:  perl(Module/Load.pm)
BuildRequires:  perl(Module/Loaded.pm)
BuildRequires:  perl(Tie/Sub.pm)
BuildRequires:  perl(version.pm)
# Tests only
BuildRequires:  perl(Color/Library.pm)
BuildRequires:  perl(Color/Library/Dictionary/NBS_ISCC/B.pm)
BuildRequires:  perl(constant.pm)
BuildRequires:  perl(File/Spec.pm)
BuildRequires:  perl(FileHandle.pm)
BuildRequires:  perl(IO/File.pm)
BuildRequires:  perl(Module/Metadata.pm)
BuildRequires:  perl(Test/Exception.pm)
BuildRequires:  perl(Test/More.pm)
Requires:       perl(Tie/Sub.pm)
Source44: import.info

%description
This module provides a common interface for obtaining the RGB values of
colors by standard names. The intention is to (1) provide a common module
that authors can use with other modules to specify colors by name; and (2)
free module authors from having to "re-invent the wheel" whenever they
decide to give the users the option of specifying a color by name rather
than RGB value.

%prep
%setup -q -n Graphics-ColorNames-v%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
%make_build

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
# %{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc LICENSE
%doc Changes README.md
%{perl_vendor_privlib}/*

%changelog
* Tue Nov 20 2018 Igor Vlasenko <viy@altlinux.ru> 3.4.0-alt1
- automated CPAN update

* Sun Oct 28 2018 Igor Vlasenko <viy@altlinux.ru> 3.3.3-alt1
- automated CPAN update

* Wed Oct 10 2018 Igor Vlasenko <viy@altlinux.ru> 3.2.1-alt1_1
- new version

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 2.11-alt2_20
- update to new release by fcimport

* Mon Oct 27 2014 Igor Vlasenko <viy@altlinux.ru> 2.11-alt2_18
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 2.11-alt2_17
- update to new release by fcimport

* Thu Feb 20 2014 Igor Vlasenko <viy@altlinux.ru> 2.11-alt2_16
- moved to Sisyphus for Slic3r (by dd@ request)

* Tue Aug 27 2013 Igor Vlasenko <viy@altlinux.ru> 2.11-alt1_16
- update to new release by fcimport

* Mon Aug 05 2013 Igor Vlasenko <viy@altlinux.ru> 2.11-alt1_15
- update to new release by fcimport

* Mon Mar 04 2013 Igor Vlasenko <viy@altlinux.ru> 2.11-alt1_14
- update to new release by fcimport

* Tue Jul 31 2012 Igor Vlasenko <viy@altlinux.ru> 2.11-alt1_13
- update to new release by fcimport

* Fri May 25 2012 Igor Vlasenko <viy@altlinux.ru> 2.11-alt1_11
- fc import

