# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl(CPAN.pm) perl(Config.pm) perl(Convert/NLS_DATE_FORMAT.pm) perl(DBI.pm) perl(Date/Manip.pm) perl(DateTime.pm) perl(DateTime/Duration.pm) perl(DateTime/Event/ICal.pm) perl(DateTime/Format/Builder.pm) perl(DateTime/Infinite.pm) perl(DateTime/LeapSecond.pm) perl(DateTime/Span.pm) perl(DateTime/TimeZone.pm) perl(DateTime/TimeZone/Floating.pm) perl(DateTime/TimeZone/UTC.pm) perl(Fcntl.pm) perl(File/Spec/Functions.pm) perl(List/MoreUtils.pm) perl(Math/BigInt.pm) perl(Module/Build.pm) perl(Module/Pluggable.pm) perl(Params/Validate.pm) perl(Test/MockTime.pm) perl(Test/NoWarnings.pm) perl-devel perl-podlators
# END SourceDeps(oneline)
Name:           perl-DateTime-Format-XSD
Version:        0.2
Release:        alt2_4
Summary:        Format DateTime according to xsd:dateTime
License:        GPL+ or Artistic
Group:          Development/Perl
URL:            http://search.cpan.org/dist/DateTime-Format-XSD/
Source0:        http://www.cpan.org/modules/by-module/DateTime/DateTime-Format-XSD-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl(DateTime/Format/ISO8601.pm)
BuildRequires:  perl(ExtUtils/MakeMaker.pm)
BuildRequires:  perl(Test/More.pm)
Requires:       perl(DateTime/Format/ISO8601.pm)

#Not autodetermined.
Provides:       perl(DateTime/Format/XSD.pm) = %{version}
Source44: import.info

%description
XML Schema defines a usage profile which is a subset of the ISO8601
profile. This profile defines that
  'YYYY-MM-DD"T"HH:MI:SS(Z|[+-]zh:zm)' 
is the only possible representation for a dateTime, despite 
all other options ISO provides.

%prep
%setup -q -n DateTime-Format-XSD-%{version}

%build
%{__perl} Makefile.PL INSTALLMAN1DIR=%_man1dir INSTALLDIRS=vendor
make %{?_smp_mflags}

%install

make pure_install DESTDIR=%{buildroot}

find %{buildroot} -type f -name .packlist -exec rm -f {} \;
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null \;


%check
make test

%files
%doc Changes README
%{perl_vendor_privlib}/*

%changelog
* Tue Dec 11 2012 Igor Vlasenko <viy@altlinux.ru> 0.2-alt2_4
- moved to Sisyphus (Tapper dep)

* Tue Jul 31 2012 Igor Vlasenko <viy@altlinux.ru> 0.2-alt1_4
- update to new release by fcimport

* Wed May 23 2012 Igor Vlasenko <viy@altlinux.ru> 0.2-alt1_2
- fc import

