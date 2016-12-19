Group: Development/Perl
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl(Module/Build.pm) perl-podlators
# END SourceDeps(oneline)
%global pkgname DateTime-Format-Excel

Summary:	Convert between DateTime and Excel dates
Name:		perl-DateTime-Format-Excel
Epoch:		1
Version:	0.31
Release:	alt2_18
# lib/DateTime/Format/Excel.pm -> GPL+ or Artistic
License:	GPL+ or Artistic
URL:		http://search.cpan.org/dist/%{pkgname}/
Source:		http://search.cpan.org/CPAN/authors/id/A/AB/ABURS/%{pkgname}-%{version}.tar.gz
Patch0:		perl-DateTime-Format-Excel-0.31-versioning.patch
BuildRequires:	coreutils
BuildRequires:	perl
BuildRequires:	perl(ExtUtils/MakeMaker.pm)
BuildRequires:	sed
# Run-time
BuildRequires:	perl(Carp.pm)
BuildRequires:	perl(DateTime.pm)
BuildRequires:	perl(strict.pm)
BuildRequires:	perl(vars.pm)
# Tests
BuildRequires:	perl(Test/More.pm)
# Optional tests
BuildRequires:	perl(Test/Pod.pm)
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
perl Makefile.PL INSTALLMAN1DIR=%_man1dir INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
chmod -R u+w $RPM_BUILD_ROOT/*

# Remove any non-unix line breaks
sed -e 's/\r//g' Changes > Changes.new
touch -c -r Changes Changes.new
mv -f Changes.new Changes

%check
make test

%files
%doc Artistic COPYING
%doc Changes README
%{perl_vendor_privlib}/DateTime/

%changelog
* Mon Dec 19 2016 Igor Vlasenko <viy@altlinux.ru> 1:0.31-alt2_18
- update to new release by fcimport

* Mon Mar 07 2016 Igor Vlasenko <viy@altlinux.ru> 1:0.31-alt2_16
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 1:0.31-alt2_14
- update to new release by fcimport

* Mon Oct 27 2014 Igor Vlasenko <viy@altlinux.ru> 1:0.31-alt2_12
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 1:0.31-alt2_11
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 1:0.31-alt2_10
- update to new release by fcimport

* Mon Aug 05 2013 Igor Vlasenko <viy@altlinux.ru> 1:0.31-alt2_9
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 1:0.31-alt2_8
- update to new release by fcimport

* Tue Dec 11 2012 Igor Vlasenko <viy@altlinux.ru> 1:0.31-alt2_7
- moved to Sisyphus (Tapper dep)

* Tue Jul 31 2012 Igor Vlasenko <viy@altlinux.ru> 1:0.31-alt1_7
- update to new release by fcimport

* Fri May 25 2012 Igor Vlasenko <viy@altlinux.ru> 1:0.31-alt1_5
- fc import

