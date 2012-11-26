# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl-devel perl-podlators
# END SourceDeps(oneline)
Name:           perl-Term-Size-Perl
Version:        0.029
Release:        alt3_11
Summary:        Perl extension for retrieving terminal size (Perl version)
License:        GPL+ or Artistic
Group:          Development/Perl
URL:            http://search.cpan.org/dist/Term-Size-Perl/
Source0:        http://www.cpan.org/authors/id/F/FE/FERREIRA/Term-Size-Perl-%{version}.tar.gz
BuildRequires:  perl(ExtUtils/CBuilder.pm)
BuildRequires:  perl(ExtUtils/MakeMaker.pm)
BuildRequires:  perl(Test/More.pm)
BuildRequires:  perl(Test/Pod.pm)
BuildRequires:  perl(Test/Pod/Coverage.pm)
BuildArch: noarch
# although the resulting rpm appears to be noarch, the build is arch-dependent
# and produces different code for ppc and x86
%global  debug_package %nil
Source44: import.info

%description
Yet another implementation of Term::Size. Now in pure Perl, with the
exception of a C probe run on build time.

%prep
%setup -q -n Term-Size-Perl-%{version}

%build
%{__perl} Makefile.PL INSTALLMAN1DIR=%_man1dir INSTALLDIRS=vendor
make %{?_smp_mflags}

%install

make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;


%check
make test

%files
%doc Changes README
%{perl_vendor_privlib}/*

%changelog
* Mon Nov 26 2012 Igor Vlasenko <viy@altlinux.ru> 0.029-alt3_11
- sisyphus release

* Mon Sep 10 2012 Cronbuild Service <cronbuild@altlinux.org> 0.029-alt2_11
- rebuild with new perl

* Tue Jul 31 2012 Igor Vlasenko <viy@altlinux.ru> 0.029-alt1_11
- update to new release by fcimport

* Wed May 23 2012 Igor Vlasenko <viy@altlinux.ru> 0.029-alt1_9
- fc import

