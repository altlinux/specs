# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl(Color/Library/Dictionary/NBS_ISCC/B.pm) perl(Exporter.pm) perl(ExtUtils/MakeMaker.pm) perl(FileHandle.pm) perl(IO/File.pm) perl(Test/More.pm) perl(base.pm) perl-Module-Build perl-devel perl-podlators
# END SourceDeps(oneline)
Name:           perl-Graphics-ColorNames
Version:        2.11
Release:        alt2_17
Summary:        Defines RGB values for common color names
License:        GPL+ or Artistic
Group:          Development/Perl
URL:            http://search.cpan.org/dist/Graphics-ColorNames/
Source0:        http://www.cpan.org/authors/id/R/RR/RRWO/Graphics-ColorNames-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl(Color/Library.pm)
BuildRequires:  perl(Module/Build.pm)
BuildRequires:  perl(Module/Load.pm)
BuildRequires:  perl(Module/Loaded.pm)
BuildRequires:  perl(Pod/Readme.pm)
BuildRequires:  perl(Test/Exception.pm)
BuildRequires:  perl(Test/Pod.pm)
BuildRequires:  perl(Test/Pod/Coverage.pm)
BuildRequires:  perl(Test/Portability/Files.pm)
# Not in Fedora (yet)
# BuildRequires:  perl(Tie::Sub)
Requires:       perl(Module/Load.pm) >= 0.10
Source44: import.info

%description
This module provides a common interface for obtaining the RGB values of
colors by standard names. The intention is to (1) provide a common module
that authors can use with other modules to specify colors by name; and (2)
free module authors from having to "re-invent the wheel" whenever they
decide to give the users the option of specifying a color by name rather
than RGB value.

%prep
%setup -q -n Graphics-ColorNames-%{version}
%{__perl} -pi -e 's/\r//g' Changes README

%build
%{__perl} Build.PL --install_path bindoc=%_man1dir installdirs=vendor
./Build

%install

./Build install destdir=$RPM_BUILD_ROOT create_packlist=0
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;

# %{_fixperms} $RPM_BUILD_ROOT/*

%check
DEVEL_TESTS=1 ./Build test

%files
%doc Changes README
%{perl_vendor_privlib}/*

%changelog
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

