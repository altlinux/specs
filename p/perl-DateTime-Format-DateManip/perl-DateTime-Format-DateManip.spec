# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl(DateTime/Duration.pm) perl-devel perl-podlators
# END SourceDeps(oneline)
Name:           perl-DateTime-Format-DateManip
Version:        0.04
Release:        alt2_12
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


%check
./Build test

%files
%doc Changes LICENSE README t/
%{perl_vendor_privlib}/*

%changelog
* Tue Dec 11 2012 Igor Vlasenko <viy@altlinux.ru> 0.04-alt2_12
- moved to Sisyphus (Tapper dep)

* Tue Jul 31 2012 Igor Vlasenko <viy@altlinux.ru> 0.04-alt1_12
- update to new release by fcimport

* Wed May 23 2012 Igor Vlasenko <viy@altlinux.ru> 0.04-alt1_10
- fc import

