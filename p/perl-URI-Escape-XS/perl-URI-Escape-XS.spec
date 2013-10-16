Group: Other
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl(Carp.pm) perl-devel perl-podlators
# END SourceDeps(oneline)
Name:           perl-URI-Escape-XS
Version:        0.10
Release:        alt3_5
Summary:        Drop-In replacement for URI::Escape
License:        GPL+ or Artistic

URL:            http://search.cpan.org/dist/URI-Escape-XS/
Source0:        http://www.cpan.org/authors/id/D/DA/DANKOGAI/URI-Escape-XS-%{version}.tar.gz

BuildRequires:  perl(base.pm)
BuildRequires:  perl(Encode.pm)
BuildRequires:  perl(Exporter.pm)
BuildRequires:  perl(ExtUtils/MakeMaker.pm)
BuildRequires:  perl(Test/More.pm)
BuildRequires:  perl(Test/Pod.pm)
BuildRequires:  perl(Test/Pod/Coverage.pm)
BuildRequires:  perl(XSLoader.pm)
Requires:       perl(Carp.pm)


Source44: import.info

%description
This is a drop-in replacement for the URI::Escape module. Since it
uses XS, it is really fast except for uri_escape("noop").

%prep
%setup -q -n URI-Escape-XS-%{version}

%build
%{__perl} Makefile.PL INSTALLMAN1DIR=%_man1dir INSTALLDIRS=vendor OPTIMIZE="$RPM_OPT_FLAGS"
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -type f -name '*.bs' -size 0 -exec rm -f {} \;

# %{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc Changes README
%{perl_vendor_archlib}/auto/URI*
%{perl_vendor_archlib}/URI*

%changelog
* Thu Oct 17 2013 Igor Vlasenko <viy@altlinux.ru> 0.10-alt3_5
- Sisyphus build

* Thu Sep 05 2013 Cronbuild Service <cronbuild@altlinux.org> 0.10-alt2_5
- rebuild to get rid of unmets

* Mon Sep 02 2013 Igor Vlasenko <viy@altlinux.ru> 0.10-alt1_5
- update to new release by fcimport

* Mon Aug 05 2013 Igor Vlasenko <viy@altlinux.ru> 0.10-alt1_4
- update to new release by fcimport

* Fri Apr 26 2013 Igor Vlasenko <viy@altlinux.ru> 0.10-alt1_3
- initial fc import

