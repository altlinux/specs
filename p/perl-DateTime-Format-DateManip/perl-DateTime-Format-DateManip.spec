# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl(CPAN.pm) perl(Cwd.pm) perl(DateTime/Duration.pm) perl(ExtUtils/MakeMaker.pm) perl(File/Spec.pm) perl-Module-Build perl-devel perl-podlators
# END SourceDeps(oneline)
Name:           perl-DateTime-Format-DateManip
Version:        0.04
Release:        alt2_16
Summary:        Convert Date::Manip to DateTime and vice versa
License:        GPL+ or Artistic
Group:          Development/Perl
URL:            http://search.cpan.org/dist/DateTime-Format-DateManip/
Source0:        http://www.cpan.org/authors/id/B/BB/BBENNETT/dt-fmt-datemanip/DateTime-Format-DateManip-%{version}.tar.gz
Patch0:         DateTime-Format-DateManip-01conversion.patch
BuildArch:      noarch

BuildRequires:  perl(Class/ISA.pm)
BuildRequires:  perl(Date/Manip.pm)
BuildRequires:  perl(DateTime.pm)
BuildRequires:  perl(Module/Build.pm)
BuildRequires:  perl(Test/More.pm)
Source44: import.info
#Requires:       perl(Date::Manip)
#Requires:       perl(DateTime)

%description
DateTime::Format::DateManip is a class that knows how to convert between
Date::Manip dates and durations and DateTime and DateTime::Duration
objects. Recurrences are note yet supported.

%prep
%setup -q -n DateTime-Format-DateManip-%{version}
%patch0 -p1

%build
%{__perl} Build.PL --install_path bindoc=%_man1dir installdirs=vendor
./Build

%install

./Build install destdir=%{buildroot} create_packlist=0
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null \;

# %{_fixperms} %{buildroot}/*

%check
./Build test

%files
%doc Changes LICENSE README t/
%{perl_vendor_privlib}/*

%changelog
* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 0.04-alt2_16
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 0.04-alt2_15
- update to new release by fcimport

* Mon Aug 05 2013 Igor Vlasenko <viy@altlinux.ru> 0.04-alt2_14
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 0.04-alt2_13
- update to new release by fcimport

* Tue Dec 11 2012 Igor Vlasenko <viy@altlinux.ru> 0.04-alt2_12
- moved to Sisyphus (Tapper dep)

* Tue Jul 31 2012 Igor Vlasenko <viy@altlinux.ru> 0.04-alt1_12
- update to new release by fcimport

* Wed May 23 2012 Igor Vlasenko <viy@altlinux.ru> 0.04-alt1_10
- fc import

