Group: Development/Other
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl-podlators
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           perl-pod2pdf
Version:        0.42
Release:        alt2_21
Summary:        Converts Pod to PDF format
License:        Artistic 2.0
URL:            https://metacpan.org/release/pod2pdf
Source0:        https://cpan.metacpan.org/authors/id/J/JO/JONALLEN/pod2pdf-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  rpm-build-perl
BuildRequires:  perl(ExtUtils/MakeMaker.pm)
BuildRequires:  perl(Carp.pm)
BuildRequires:  perl(constant.pm)
BuildRequires:  perl(File/Spec/Functions.pm)
BuildRequires:  perl(File/Type.pm)
BuildRequires:  perl(Getopt/ArgvFile.pm)
BuildRequires:  perl(Getopt/Long.pm)
BuildRequires:  perl(Image/Size.pm)
BuildRequires:  perl(Paper/Specs.pm)
BuildRequires:  perl(PDF/API2.pm)
BuildRequires:  perl(Pod/Escapes.pm)
BuildRequires:  perl(Pod/ParseLink.pm)
BuildRequires:  perl(Pod/Parser.pm)
BuildRequires:  perl(List/Util.pm)
BuildRequires:  perl(Test/More.pm)
BuildRequires:  perl(Test/Pod.pm)
Requires:       perl(File/Type.pm)
Requires:       perl(Image/Size.pm)
Requires:       perl(Paper/Specs.pm) >= 0.100
Source44: import.info

%description
pod2pdf converts documents written in Perl's POD (Plain Old Documentation)
format to PDF files.

%prep
%setup -q -n pod2pdf-%{version}

%build
/usr/bin/perl Makefile.PL INSTALLDIRS=vendor
%make_build

%install
make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;

# %{_fixperms} $RPM_BUILD_ROOT/*


%check
make test

%files
%doc artistic-2_0.txt Changes README
%{perl_vendor_privlib}/*
%{_mandir}/man1/*
%{_bindir}/*

%changelog
* Wed Nov 20 2019 Igor Vlasenko <viy@altlinux.ru> 0.42-alt2_21
- update to new release by fcimport

* Sat Jul 14 2018 Igor Vlasenko <viy@altlinux.ru> 0.42-alt2_17
- update to new release by fcimport

* Wed Sep 27 2017 Igor Vlasenko <viy@altlinux.ru> 0.42-alt2_15
- update to new release by fcimport

* Thu Aug 03 2017 Igor Vlasenko <viy@altlinux.ru> 0.42-alt2_14
- update to new release by fcimport

* Thu Mar 16 2017 Igor Vlasenko <viy@altlinux.ru> 0.42-alt2_13
- update to new release by fcimport

* Tue Jul 26 2016 Igor Vlasenko <viy@altlinux.ru> 0.42-alt2_12
- update to new release by fcimport

* Mon Mar 07 2016 Igor Vlasenko <viy@altlinux.ru> 0.42-alt2_11
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 0.42-alt2_10
- update to new release by fcimport

* Mon Oct 27 2014 Igor Vlasenko <viy@altlinux.ru> 0.42-alt2_8
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 0.42-alt2_7
- update to new release by fcimport

* Tue Oct 22 2013 Igor Vlasenko <viy@altlinux.ru> 0.42-alt2_6
- update to new release by fcimport

* Tue Oct 15 2013 Igor Vlasenko <viy@altlinux.ru> 0.42-alt2
- build for Sisyphus

* Mon Sep 02 2013 Igor Vlasenko <viy@altlinux.ru> 0.42-alt1_6
- update to new release by fcimport

* Mon Aug 05 2013 Igor Vlasenko <viy@altlinux.ru> 0.42-alt1_5
- update to new release by fcimport

* Fri Apr 26 2013 Igor Vlasenko <viy@altlinux.ru> 0.42-alt1_4
- initial fc import

