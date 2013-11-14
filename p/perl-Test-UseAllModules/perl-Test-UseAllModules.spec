# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl-devel perl-podlators
# END SourceDeps(oneline)
Name:           perl-Test-UseAllModules
Version:        0.14
Release:        alt2_4
Summary:        Do use_ok() for all the MANIFESTed modules
License:        GPL+ or Artistic
Group:          Development/Perl
URL:            http://search.cpan.org/dist/Test-UseAllModules/
Source0:        http://www.cpan.org/authors/id/I/IS/ISHIGAKI/Test-UseAllModules-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl(Exporter.pm)
BuildRequires:  perl(ExtUtils/MakeMaker.pm)
BuildRequires:  perl(ExtUtils/Manifest.pm)
# perl(Test::Builder) needed for lib/Test/UseAllModules.pm:55:
# Test::More->builder->{Have_Plan};
BuildRequires:  perl(Test/Builder.pm)
BuildRequires:  perl(Test/More.pm)
# Tests only:
BuildRequires:  perl(FindBin.pm)
BuildRequires:  perl(lib.pm)
Requires:       perl(Test/Builder.pm) >= 0.30
Requires:       perl(Test/More.pm) >= 0.60

# Remove underspecifies dependencies

Source44: import.info
%filter_from_requires /perl\\(Test.More.pm\\)/d

%description
I'm sick of writing 00_load.t (or something like that) that will do use_ok()
for every module I write. I'm sicker of updating 00_load.t when I add
another file to the distribution. This module reads MANIFEST to find modules
to be tested and does use_ok() for each of them. Now all you have to do is
update MANIFEST. You don't have to modify the test any more (hopefully).

%prep
%setup -q -n Test-UseAllModules-%{version}
for F in Changes README; do
    tr -d '\r' <"$F" >"$F.unix"
    touch -r "$F"{,.unix}
    mv "${F}"{.unix,}
done

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
%doc Changes README
%{perl_vendor_privlib}/*

%changelog
* Thu Nov 14 2013 Igor Vlasenko <viy@altlinux.ru> 0.14-alt2_4
- Sisyphus build

* Mon Sep 02 2013 Igor Vlasenko <viy@altlinux.ru> 0.14-alt1_4
- update to new release by fcimport

* Mon Aug 05 2013 Igor Vlasenko <viy@altlinux.ru> 0.14-alt1_3
- update to new release by fcimport

* Mon Mar 04 2013 Igor Vlasenko <viy@altlinux.ru> 0.14-alt1_2
- update to new release by fcimport

* Mon Aug 27 2012 Igor Vlasenko <viy@altlinux.ru> 0.14-alt1_1
- update to new release by fcimport

* Tue Jul 31 2012 Igor Vlasenko <viy@altlinux.ru> 0.13-alt2_4
- update to new release by fcimport

* Fri May 25 2012 Igor Vlasenko <viy@altlinux.ru> 0.13-alt2_2
- fc import

* Thu May 24 2012 Igor Vlasenko <viy@altlinux.ru> 0.13-alt1_2
- fc import

