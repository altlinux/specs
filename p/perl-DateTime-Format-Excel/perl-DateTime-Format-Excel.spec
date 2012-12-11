# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl(DBI.pm) perl(Date/Manip.pm) perl(DateTime/Duration.pm) perl(DateTime/Format/Builder.pm) perl(DateTime/LeapSecond.pm) perl(Math/BigInt.pm) perl(Module/Build.pm) perl(Params/Validate.pm) perl(Test/NoWarnings.pm) perl-devel perl-podlators
# END SourceDeps(oneline)
%global pkgname DateTime-Format-Excel

Summary:	Convert between DateTime and Excel dates
Name:		perl-DateTime-Format-Excel 
Epoch:		1
Version:	0.31
Release:	alt2_7
# lib/DateTime/Format/Excel.pm -> GPL+ or Artistic
License:	GPL+ or Artistic 
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{pkgname}/
Source:		http://search.cpan.org/CPAN/authors/id/A/AB/ABURS/%{pkgname}-%{version}.tar.gz
Patch0:		perl-DateTime-Format-Excel-0.31-versioning.patch
BuildRequires:	perl(ExtUtils/MakeMaker.pm) perl(DateTime.pm)
BuildRequires:	perl(Test/More.pm) perl(Test/Pod.pm)
BuildArch:	noarch
Source44: import.info

%description
Excel uses a different system for its dates than most Unix programs.
This module allows to convert between a few of the Excel raw formats
and DateTime objects, which can then be further converted via any of
the other DateTime::Format::* modules, or with DateTime's methods.

%prep
%setup -q -n %{pkgname}-%{version}
%patch0 -p1

%build
%{__perl} Makefile.PL INSTALLMAN1DIR=%_man1dir INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} ';'
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null ';'
chmod -R u+w $RPM_BUILD_ROOT/*

# Remove any non-unix line breaks
sed -e 's/\r//g' Changes > Changes.new
touch -c -r Changes Changes.new
mv -f Changes.new Changes

%check
make test

%files
%doc Artistic Changes COPYING README
%{perl_vendor_privlib}/DateTime/

%changelog
* Tue Dec 11 2012 Igor Vlasenko <viy@altlinux.ru> 1:0.31-alt2_7
- moved to Sisyphus (Tapper dep)

* Tue Jul 31 2012 Igor Vlasenko <viy@altlinux.ru> 1:0.31-alt1_7
- update to new release by fcimport

* Fri May 25 2012 Igor Vlasenko <viy@altlinux.ru> 1:0.31-alt1_5
- fc import

