Group: Development/Perl
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl(Module/Build.pm) perl-podlators
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%global pkgname DateTime-Format-Excel

Summary:	Convert between DateTime and Excel dates
Name:		perl-DateTime-Format-Excel
Epoch:		1
Version:	0.31
Release:	alt2_27
# lib/DateTime/Format/Excel.pm -> GPL+ or Artistic
License:	GPL+ or Artistic
URL:		https://metacpan.org/release/%{pkgname}
Source:		https://cpan.metacpan.org/authors/id/A/AB/ABURS/%{pkgname}-%{version}.tar.gz
Patch0:		perl-DateTime-Format-Excel-0.31-versioning.patch
BuildRequires:	coreutils
BuildRequires:	perl-devel
BuildRequires:	rpm-build-perl
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
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
%make_build

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
%doc --no-dereference Artistic COPYING
%doc Changes README
%{perl_vendor_privlib}/DateTime/

%changelog
* Wed Nov 20 2019 Igor Vlasenko <viy@altlinux.ru> 1:0.31-alt2_27
- update to new release by fcimport

* Wed Oct 10 2018 Igor Vlasenko <viy@altlinux.ru> 1:0.31-alt2_24
- update to new release by fcimport

* Sat Jul 14 2018 Igor Vlasenko <viy@altlinux.ru> 1:0.31-alt2_23
- update to new release by fcimport

* Mon May 07 2018 Igor Vlasenko <viy@altlinux.ru> 1:0.31-alt2_22
- update to new release by fcimport

* Mon Oct 02 2017 Igor Vlasenko <viy@altlinux.ru> 1:0.31-alt2_21
- update to new release by fcimport

* Thu Aug 03 2017 Igor Vlasenko <viy@altlinux.ru> 1:0.31-alt2_20
- update to new release by fcimport

* Thu Mar 16 2017 Igor Vlasenko <viy@altlinux.ru> 1:0.31-alt2_19
- update to new release by fcimport

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

