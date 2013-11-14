# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl(Exporter.pm) perl(overload.pm) perl-devel perl-podlators
# END SourceDeps(oneline)
Name:           perl-Set-Scalar
Version:        1.25
Release:        alt2_11
Summary:        Basic set operations

Group:          Development/Perl
License:        GPL+ or Artistic
URL:            http://search.cpan.org/dist/Set-Scalar/
Source0:        http://www.cpan.org/authors/id/J/JH/JHI/Set-Scalar-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  perl(ExtUtils/MakeMaker.pm)
Source44: import.info

%description
%{summary}.


%prep
%setup -q -n Set-Scalar-%{version}


%build
%{__perl} Makefile.PL INSTALLMAN1DIR=%_man1dir INSTALLDIRS=vendor
make %{?_smp_mflags}


%install
make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} ';'
find $RPM_BUILD_ROOT -type d -depth -exec rmdir {} 2>/dev/null ';'
chmod -R u+w $RPM_BUILD_ROOT/*


%check
make test


%files
%doc ChangeLog README
%{perl_vendor_privlib}/Set/


%changelog
* Thu Nov 14 2013 Igor Vlasenko <viy@altlinux.ru> 1.25-alt2_11
- Sisyphus build

* Mon Sep 02 2013 Igor Vlasenko <viy@altlinux.ru> 1.25-alt1_11
- update to new release by fcimport

* Mon Aug 05 2013 Igor Vlasenko <viy@altlinux.ru> 1.25-alt1_10
- update to new release by fcimport

* Mon Mar 04 2013 Igor Vlasenko <viy@altlinux.ru> 1.25-alt1_9
- update to new release by fcimport

* Tue Jul 31 2012 Igor Vlasenko <viy@altlinux.ru> 1.25-alt1_8
- update to new release by fcimport

* Thu May 24 2012 Igor Vlasenko <viy@altlinux.ru> 1.25-alt1_6
- fc import

