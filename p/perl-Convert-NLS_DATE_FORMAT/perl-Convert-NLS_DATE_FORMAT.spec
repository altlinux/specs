# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl-devel perl-podlators
# END SourceDeps(oneline)
Name:           perl-Convert-NLS_DATE_FORMAT
Version:        0.05
Release:        alt2_3
Summary:        Convert Oracle NLS_DATE_FORMAT <-> strftime Format Strings
License:        GPL+ or Artistic
Group:          Development/Perl
URL:            http://search.cpan.org/dist/Convert-NLS_DATE_FORMAT/
Source0:        http://www.cpan.org/authors/id/K/KO/KOLIBRIE/Convert-NLS_DATE_FORMAT-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl(Exporter.pm)
BuildRequires:  perl(ExtUtils/MakeMaker.pm)
BuildRequires:  perl(Test/More.pm)
Source44: import.info

%description
Convert Oracle's NLS_DATE_FORMAT string into a strptime format string, or
the reverse.

%prep
%setup -q -n Convert-NLS_DATE_FORMAT-%{version}

%build
perl Makefile.PL INSTALLMAN1DIR=%_man1dir INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install PERL_INSTALL_ROOT=%{buildroot}
find %{buildroot} -type f -name .packlist -exec rm -f {} +
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null \;

%check
make test

%files
%doc Changes README t/
%{perl_vendor_privlib}/*

%changelog
* Tue Dec 11 2012 Igor Vlasenko <viy@altlinux.ru> 0.05-alt2_3
- moved to Sisyphus (Tapper dep)

* Tue Jul 31 2012 Igor Vlasenko <viy@altlinux.ru> 0.05-alt1_3
- update to new release by fcimport

* Wed May 23 2012 Igor Vlasenko <viy@altlinux.ru> 0.05-alt1_1
- fc import

