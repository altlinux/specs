%define module_version 0.11
%define module_name Dir-Self
# BEGIN SourceDeps(oneline):
BuildRequires: perl(Carp.pm) perl(File/Spec.pm) perl(lib.pm) perl(strict.pm) perl-devel
# END SourceDeps(oneline)
Name:           perl-Dir-Self
Version:        0.11
Release:        alt1
Summary:        A __DIR__ constant for the directory your source file is in
License:        perl
Group:          Development/Perl
URL:            http://search.cpan.org/dist/Dir-Self/
Source0:        http://cpan.org.ua/authors/id/M/MA/MAUKE/%module_name-%module_version.tar.gz
BuildArch:      noarch
BuildRequires:  perl(ExtUtils/MakeMaker.pm)
BuildRequires:  perl(Test/More.pm)


Source44: import.info

%description
Perl has two pseudo-constants describing the current location in your
source code, __FILE__ and __LINE__. This module adds __DIR__, which expands
to the directory your source file is in, as an absolute pathname.

%prep
%setup -n %module_name-%module_version

%build
%{__perl} Makefile.PL INSTALLMAN1DIR=%_man1dir INSTALLDIRS=vendor
make %{?_smp_mflags}

%install

make pure_install DESTDIR=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;

# %{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc Changes README
%{perl_vendor_privlib}/*

%changelog
* Wed Dec 04 2013 Igor Vlasenko <viy@altlinux.ru> 0.11-alt1
- uploaded to Sisyphus as Scalar-Does dependency

* Tue Aug 27 2013 Igor Vlasenko <viy@altlinux.ru> 0.10-alt1_10
- update to new release by fcimport

* Mon Aug 05 2013 Igor Vlasenko <viy@altlinux.ru> 0.10-alt1_9
- update to new release by fcimport

* Wed Feb 27 2013 Igor Vlasenko <viy@altlinux.ru> 0.10-alt1_8
- update to new release by fcimport

* Tue Jul 31 2012 Igor Vlasenko <viy@altlinux.ru> 0.10-alt1_7
- update to new release by fcimport

* Wed May 23 2012 Igor Vlasenko <viy@altlinux.ru> 0.10-alt1_5
- fc import

