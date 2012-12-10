# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl(CPAN.pm) perl(Config.pm) perl(Convert/NLS_DATE_FORMAT.pm) perl(DBI.pm) perl(Date/Manip.pm) perl(DateTime/Event/ICal.pm) perl(DateTime/Infinite.pm) perl(DateTime/LeapSecond.pm) perl(DateTime/Span.pm) perl(ExtUtils/MakeMaker.pm) perl(Fcntl.pm) perl(File/Spec/Functions.pm) perl(List/MoreUtils.pm) perl(Math/BigInt.pm) perl(Module/Build.pm) perl(Module/Pluggable.pm) perl(Params/Validate.pm) perl(Test/MockTime.pm) perl(Test/NoWarnings.pm) perl-devel perl-podlators
# END SourceDeps(oneline)
Name:           perl-DateTime-Format-Pg
Version:        0.16007
Release:        alt2_4
Summary:        Parse and format PostgreSQL dates and times
License:        GPL+ or Artistic
Group:          Development/Perl
URL:            http://search.cpan.org/dist/DateTime-Format-Pg/
Source0:        http://search.cpan.org/CPAN/authors/id/D/DM/DMAKI/DateTime-Format-Pg-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  perl(inc/Module/Install.pm)
BuildRequires:  perl(Module/Install/Repository.pm)
# run-time
BuildRequires:  perl(Carp.pm)
BuildRequires:  perl(DateTime.pm)
BuildRequires:  perl(DateTime/Duration.pm)
BuildRequires:  perl(DateTime/Format/Builder.pm)
BuildRequires:  perl(DateTime/TimeZone.pm)
BuildRequires:  perl(DateTime/TimeZone/UTC.pm)
BuildRequires:  perl(DateTime/TimeZone/Floating.pm)
# tests
BuildRequires:  perl(Data/Dumper.pm)
BuildRequires:  perl(Test/More.pm)
# optional tests
BuildRequires:  perl(Test/Pod.pm)
BuildRequires:  perl(Test/Pod/Coverage.pm)
Source44: import.info


%description
This module understands the formats used by PostgreSQL for its DATE, TIME,
TIMESTAMP, and INTERVAL data types. It can be used to parse these formats
in order to create DateTime or DateTime::Duration objects, and it can take
a DateTime or DateTime::Duration object and produce a string representing
it in a format accepted by PostgreSQL.

%prep
%setup -q -n DateTime-Format-Pg-%{version}

# Unbundle modules
rm -rf inc
sed -i -e '/^inc\//d' MANIFEST

cat README | iconv -f iso8859-1 -t utf8 > foo ; mv foo README

perl -pi -e 's|^#!perl|#!/usr/bin/perl|' t/*.t

%build
%{__perl} Makefile.PL INSTALLMAN1DIR=%_man1dir INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install PERL_INSTALL_ROOT=%{buildroot}

find %{buildroot} -type f -name .packlist -exec rm -f {} \;
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null \;


%check
make test

%files
%doc Changes LICENSE t/
%{perl_vendor_privlib}/*

%changelog
* Tue Dec 11 2012 Igor Vlasenko <viy@altlinux.ru> 0.16007-alt2_4
- moved to Sisyphus (Tapper dep)

* Tue Jul 31 2012 Igor Vlasenko <viy@altlinux.ru> 0.16007-alt1_4
- update to new release by fcimport

* Thu May 24 2012 Igor Vlasenko <viy@altlinux.ru> 0.16007-alt1_2
- fc import

