# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl-devel perl-podlators
# END SourceDeps(oneline)
Name:           perl-Term-Size-Any
Version:        0.002
Release:        alt2_10
Summary:        Retrieve terminal size
License:        GPL+ or Artistic
Group:          Development/Perl
URL:            http://search.cpan.org/dist/Term-Size-Any/
Source0:        http://www.cpan.org/authors/id/F/FE/FERREIRA/Term-Size-Any-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl(Devel/Hide.pm)
BuildRequires:  perl(ExtUtils/MakeMaker.pm)
BuildRequires:  perl(Module/Load/Conditional.pm)
BuildRequires:  perl(Term/Size/Perl.pm)
BuildRequires:  perl(Test/More.pm)
BuildRequires:  perl(Test/Pod.pm)
BuildRequires:  perl(Test/Pod/Coverage.pm)
Requires:       perl(Term/Size/Perl.pm)


Source44: import.info

%description
This is a unified interface to retrieve terminal size. It loads one module
of a list of known alternatives, each implementing some way to get the
desired terminal information. This loaded module will actually do the job
on behalf of Term::Size::Any.

%prep
%setup -q -n Term-Size-Any-%{version}

%build
%{__perl} Makefile.PL INSTALLMAN1DIR=%_man1dir INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;


%check
make test

%files
%doc Changes README
%{perl_vendor_privlib}/*

%changelog
* Tue Jul 31 2012 Igor Vlasenko <viy@altlinux.ru> 0.002-alt2_10
- update to new release by fcimport

* Fri May 25 2012 Igor Vlasenko <viy@altlinux.ru> 0.002-alt2_8
- fc import

* Thu May 24 2012 Igor Vlasenko <viy@altlinux.ru> 0.002-alt1_8
- fc import

