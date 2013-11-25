%define _unpackaged_files_terminate_build 1
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl-devel perl-podlators
# END SourceDeps(oneline)
Name:           perl-Pod-Markdown
Version:        1.500
Release:        alt1
Summary:        Convert POD to Markdown
License:        GPL+ or Artistic
Group:          Development/Perl
URL:            http://search.cpan.org/dist/Pod-Markdown/
Source:        http://www.cpan.org/authors/id/R/RW/RWSTAUNER/Pod-Markdown-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl(ExtUtils/MakeMaker.pm)
BuildRequires:  perl(File/Spec.pm)
BuildRequires:  perl(File/Spec/Functions.pm)
BuildRequires:  perl(File/Temp.pm)
BuildRequires:  perl(IPC/Open3.pm)
BuildRequires:  perl(IO/Handle.pm)
BuildRequires:  perl(List/Util.pm)
BuildRequires:  perl(parent.pm)
BuildRequires:  perl(Pod/ParseLink.pm)
BuildRequires:  perl(Pod/Parser.pm)
BuildRequires:  perl(strict.pm)
BuildRequires:  perl(Test/Differences.pm)
BuildRequires:  perl(Test/More.pm)
BuildRequires:  perl(Test/Script.pm)
BuildRequires:  perl(warnings.pm)
Source44: import.info

%description
This module subclasses Pod::Parser and converts POD to Markdown.

%prep
%setup -q -n Pod-Markdown-%{version}

%build
perl Makefile.PL INSTALLMAN1DIR=%_man1dir INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;

# %{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc Changes README
%{perl_vendor_privlib}/*
%{_mandir}/man[13]/*
%{_bindir}/*

%changelog
* Mon Nov 25 2013 Igor Vlasenko <viy@altlinux.ru> 1.500-alt1
- automated CPAN update

* Fri Nov 15 2013 Igor Vlasenko <viy@altlinux.ru> 1.401-alt1_1
- update to new release by fcimport

* Wed Nov 13 2013 Igor Vlasenko <viy@altlinux.ru> 1.401-alt1
- automated CPAN update

* Wed Nov 06 2013 Igor Vlasenko <viy@altlinux.ru> 1.400-alt1
- automated CPAN update

* Tue Sep 17 2013 Igor Vlasenko <viy@altlinux.ru> 1.322-alt2_4
- Sisyphus build; switch to fc import

* Tue Aug 27 2013 Igor Vlasenko <viy@altlinux.ru> 1.322-alt1_4
- update to new release by fcimport

* Mon Aug 05 2013 Igor Vlasenko <viy@altlinux.ru> 1.322-alt1_3
- update to new release by fcimport

* Fri Apr 26 2013 Igor Vlasenko <viy@altlinux.ru> 1.322-alt1_2
- initial fc import

