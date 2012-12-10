# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl(DateTime/TimeZone.pm) perl(File/Spec/Functions.pm) perl-devel perl-podlators
# END SourceDeps(oneline)
Name:           perl-DateTime-Format-Natural
Version:        1.01
Release:        alt2_1
Summary:        Create machine readable date/time with natural parsing logic
License:        GPL+ or Artistic
Group:          Development/Perl
URL:            http://search.cpan.org/dist/DateTime-Format-Natural/
Source0:        http://www.cpan.org/authors/id/S/SC/SCHUBIGER/DateTime-Format-Natural-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl(boolean.pm)
BuildRequires:  perl(Carp.pm)
BuildRequires:  perl(Class/ISA.pm)
BuildRequires:  perl(Clone.pm)
BuildRequires:  perl(Cwd.pm)
BuildRequires:  perl(DateTime.pm)
BuildRequires:  perl(Date/Calc.pm)
BuildRequires:  perl(DateTime.pm)
BuildRequires:  perl(Exporter.pm)
BuildRequires:  perl(File/Find.pm)
BuildRequires:  perl(File/Spec.pm)
BuildRequires:  perl(FindBin.pm)
BuildRequires:  perl(Getopt/Long.pm)
BuildRequires:  perl(List/MoreUtils.pm)
BuildRequires:  perl(Module/Build.pm)
BuildRequires:  perl(Module/Util.pm)
BuildRequires:  perl(Params/Validate.pm)
BuildRequires:  perl(Scalar/Util.pm)
BuildRequires:  perl(Storable.pm)
BuildRequires:  perl(Term/ReadLine.pm)
BuildRequires:  perl(Test/MockTime.pm)
BuildRequires:  perl(Test/More.pm)


Source44: import.info

%description
DateTime::Format::Natural takes a string with a human readable date/time
and creates a machine readable one by applying natural parsing logic.

%package -n perl-DateTime-Format-Natural-Test
Group: Development/Perl
Summary:        Common test routines/data for perl-DateTime-Format-Natural
Requires:       %{name} = %{version}-%{release}

%description -n perl-DateTime-Format-Natural-Test
The DateTime::Format::Natural::Test class exports common test routines.

%prep
%setup -q -n DateTime-Format-Natural-%{version}
for f in Changes README; do
        iconv -f iso8859-1 -t utf-8 $f >$f.conf && mv $f.conf $f
done

%build
%{__perl} Build.PL --install_path bindoc=%_man1dir installdirs=vendor
./Build

%install
./Build install destdir=$RPM_BUILD_ROOT create_packlist=0


%check
./Build test

%files
%doc Changes README
%exclude %{perl_vendor_privlib}/DateTime/Format/Natural/Test.pm
%{perl_vendor_privlib}/*
%{_bindir}/dateparse
%{_mandir}/man1/*

%files -n perl-DateTime-Format-Natural-Test
%{perl_vendor_privlib}/DateTime/Format/Natural/Test.pm


%changelog
* Mon Dec 10 2012 Igor Vlasenko <viy@altlinux.ru> 1.01-alt2_1
- moved to Sisyphus

* Sat Nov 10 2012 Igor Vlasenko <viy@altlinux.ru> 1.01-alt1_1
- update to new release by fcimport

* Tue Jul 31 2012 Igor Vlasenko <viy@altlinux.ru> 1.00-alt1_3
- update to new release by fcimport

* Sun May 27 2012 Igor Vlasenko <viy@altlinux.ru> 0.99-alt1_1
- fc import

