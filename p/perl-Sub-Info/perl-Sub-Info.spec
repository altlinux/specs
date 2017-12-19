# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl-podlators
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           perl-Sub-Info
Version:        0.002
Release:        alt1_4
Summary:        Tool for inspecting Perl subroutines
License:        GPL+ or Artistic
Group:          Development/Other
URL:            http://search.cpan.org/dist/Sub-Info/
Source0:        http://www.cpan.org/authors/id/E/EX/EXODIST/Sub-Info-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  findutils
BuildRequires:  perl-devel
BuildRequires:  rpm-build-perl
BuildRequires:  perl
BuildRequires:  perl(ExtUtils/MakeMaker.pm)
BuildRequires:  perl(strict.pm)
BuildRequires:  perl(warnings.pm)
# Run-time:
BuildRequires:  perl(B.pm)
BuildRequires:  perl(Carp.pm)
BuildRequires:  perl(Importer.pm)
# Tests:
BuildRequires:  perl(Test2/Tools/Tiny.pm)
Requires:       perl(Importer.pm) >= 0.024


Source44: import.info
%filter_from_requires /^perl\\(Importer.pm\\)$/d

%description
This allows to inspect Perl subroutines.

%prep
%setup -q -n Sub-Info-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make_build

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -delete
# %{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc LICENSE
%doc Changes README
%{perl_vendor_privlib}/*

%changelog
* Tue Dec 19 2017 Igor Vlasenko <viy@altlinux.ru> 0.002-alt1_4
- new version

