Group: Development/Perl
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl(Test.pm) perl-devel perl-podlators
# END SourceDeps(oneline)
%global pkgname Tie-Function

Name:           perl-Tie-Function
Version:        0.02
Release:        alt1_4
Summary:        Wrap functions in tied hash sugar
License:        GPL+ or Artistic
URL:            http://search.cpan.org/dist/Tie-Function/
Source0:        http://www.cpan.org/authors/id/D/DA/DAVIDNICO/handy_tied_functions/%{pkgname}-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl(ExtUtils/MakeMaker.pm)
Source44: import.info

%description
Tie::Function simplifies wrapping functions in tied hash syntax so they can
be interpolated in double-quoted literals without messy intermediate
variables.

%prep
%setup -qn %{pkgname}-%{version}

%build
%{__perl} Makefile.PL INSTALLMAN1DIR=%_man1dir INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install PERL_INSTALL_ROOT=%{buildroot}
find %{buildroot} -type f -name .packlist -exec rm -f {} \;
# %{_fixperms} %{buildroot}/*

%check
make test

%files
%doc README
%{perl_vendor_privlib}/*

%changelog
* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 0.02-alt1_4
- update to new release by fcimport

* Wed Feb 19 2014 Igor Vlasenko <viy@altlinux.ru> 0.02-alt1_3
- moved to Sisyphus for Slic3r (by dd@ request)

* Tue Sep 03 2013 Igor Vlasenko <viy@altlinux.ru> 0.02-alt1
- initial import by package builder

