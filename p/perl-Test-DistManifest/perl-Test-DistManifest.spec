# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl-devel perl-podlators
# END SourceDeps(oneline)
Name:           perl-Test-DistManifest
Version:        1.012
Release:        alt1_6
Summary:        Author test that validates a package MANIFEST
License:        GPL+ or Artistic
Group:          Development/Perl
URL:            http://search.cpan.org/dist/Test-DistManifest/
Source0:        http://www.cpan.org/authors/id/E/ET/ETHER/Test-DistManifest-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl(ExtUtils/MakeMaker.pm)
# Run-time:
BuildRequires:  perl(Carp.pm)
BuildRequires:  perl(Cwd.pm)
BuildRequires:  perl(ExtUtils/Manifest.pm)
BuildRequires:  perl(File/Spec.pm)
BuildRequires:  perl(File/Spec/Unix.pm)
BuildRequires:  perl(Module/Manifest.pm)
BuildRequires:  perl(Test/Builder.pm)
BuildRequires:  perl(Test/More.pm)
# Tests only:
BuildRequires:  perl(Test/Builder/Tester.pm)
BuildRequires:  perl(Test/NoWarnings.pm)
Requires:       perl(Module/Manifest.pm) >= 0.07
Requires:       perl(Test/Builder.pm)
# This is a plug-in into Test::More. Depend on it even if not mentioned in the
# code
Requires:       perl(Test/More.pm) >= 0.62

# Filter underspecifed dependencies

Source44: import.info
%filter_from_requires /perl\\((Module.Manifest|Test.Builder).pm\\)$/d

%description
This module provides a simple method of testing that a MANIFEST matches the
distribution.

%prep
%setup -q -n Test-DistManifest-%{version}

%build
%{__perl} Makefile.PL INSTALLMAN1DIR=%_man1dir INSTALLDIRS=perl OPTIMIZE="$RPM_OPT_FLAGS"
make %{?_smp_mflags}

%install
make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -type f -name '*.bs' -size 0 -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;
# %{_fixperms} $RPM_BUILD_ROOT/*

%check
# post-install rpmbuild scripts contaminates RPM_BUILD_ROOT (bug #672538).
#rm *.list
make test

%files
%doc Changes examples LICENSE README
%{perl_vendor_privlib}/*

%changelog
* Thu Nov 14 2013 Igor Vlasenko <viy@altlinux.ru> 1.012-alt1_6
- Sisyphus build

* Mon Mar 04 2013 Igor Vlasenko <viy@altlinux.ru> 1.012-alt1_5
- update to new release by fcimport

* Tue Jul 31 2012 Igor Vlasenko <viy@altlinux.ru> 1.012-alt1_3
- update to new release by fcimport

* Mon May 28 2012 Igor Vlasenko <viy@altlinux.ru> 1.012-alt1_1
- fc import

