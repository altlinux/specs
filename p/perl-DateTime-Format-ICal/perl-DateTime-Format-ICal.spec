# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl(DBI.pm) perl(Date/Manip.pm) perl(DateTime/Duration.pm) perl(DateTime/Format/Builder.pm) perl(DateTime/Infinite.pm) perl(DateTime/LeapSecond.pm) perl(DateTime/Span.pm) perl(File/Spec/Functions.pm) perl(List/MoreUtils.pm) perl(Math/BigInt.pm) perl(Module/Pluggable.pm) perl(Test/MockTime.pm) perl(Test/NoWarnings.pm) perl-devel perl-podlators
# END SourceDeps(oneline)
Name:           perl-DateTime-Format-ICal
Version:        0.09
Release:        alt2_12
Summary:        Parse and format iCal datetime and duration strings
License:        GPL+ or Artistic
Group:          Development/Perl
URL:            http://search.cpan.org/dist/DateTime-Format-ICal/
Source0:        http://www.cpan.org/authors/id/D/DR/DROLSKY/DateTime-Format-ICal-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl(Class/ISA.pm)
BuildRequires:  perl(DateTime.pm)
BuildRequires:  perl(DateTime/Event/ICal.pm)
BuildRequires:  perl(DateTime/Set.pm)
BuildRequires:  perl(DateTime/TimeZone.pm)
BuildRequires:  perl(Module/Build.pm)
BuildRequires:  perl(Params/Validate.pm)
BuildRequires:  perl(Test/More.pm)
Requires:       perl(DateTime/Set.pm) >= 0.1
Requires:       perl(DateTime/TimeZone.pm) >= 0.22
Source44: import.info

%description
This module understands the ICal date/time and duration formats, as defined
in RFC 2445. It can be used to parse these formats in order to create the
appropriate objects.

%prep
%setup -q -n DateTime-Format-ICal-%{version}

%build
%{__perl} Build.PL --install_path bindoc=%_man1dir installdirs=vendor
./Build

%install

./Build install destdir=$RPM_BUILD_ROOT create_packlist=0
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;


%check
./Build test

%files
%doc Changes LICENSE TODO
%{perl_vendor_privlib}/*

%changelog
* Tue Dec 11 2012 Igor Vlasenko <viy@altlinux.ru> 0.09-alt2_12
- moved to Sisyphus (Tapper dep)

* Tue Jul 31 2012 Igor Vlasenko <viy@altlinux.ru> 0.09-alt1_12
- update to new release by fcimport

* Fri May 25 2012 Igor Vlasenko <viy@altlinux.ru> 0.09-alt1_10
- fc import

