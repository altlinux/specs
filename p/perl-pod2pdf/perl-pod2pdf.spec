# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl-devel perl-podlators
# END SourceDeps(oneline)
Name:           perl-pod2pdf
Version:        0.42
Release:        alt2_11
Summary:        Converts Pod to PDF format
License:        Artistic 2.0
Group:          Development/Perl
URL:            http://search.cpan.org/dist/pod2pdf/
Source0:        http://www.cpan.org/authors/id/J/JO/JONALLEN/pod2pdf-%{version}.tar.gz
BuildArch:      noarch
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
Requires:       perl(Paper/Specs.pm) >= 0.10
Source44: import.info

%description
pod2pdf converts documents written in Perl's POD (Plain Old Documentation)
format to PDF files.

%prep
%setup -q -n pod2pdf-%{version}

%build
%{__perl} Makefile.PL INSTALLMAN1DIR=%_man1dir INSTALLDIRS=vendor
make %{?_smp_mflags}

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

