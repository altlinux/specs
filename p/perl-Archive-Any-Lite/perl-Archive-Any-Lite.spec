Group: Development/Perl
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl(ExtUtils/MakeMaker/CPANfile.pm) perl-podlators
# END SourceDeps(oneline)
Name:		perl-Archive-Any-Lite
Version:	0.11
Release:	alt1_2
Summary:	Simple CPAN package extractor 
License:	GPL+ or Artistic
URL:		https://metacpan.org/release/Archive-Any-Lite
Source0:	http://cpan.metacpan.org/authors/id/I/IS/ISHIGAKI/Archive-Any-Lite-%{version}.tar.gz
Patch0:		Archive-Any-Lite-0.08-EU:MM.patch
BuildArch:	noarch
# Build
BuildRequires:	coreutils
BuildRequires:	findutils
BuildRequires:	perl
BuildRequires:	perl(ExtUtils/MakeMaker.pm)
# Module
BuildRequires:	perl(Archive/Tar.pm)
BuildRequires:	perl(Archive/Zip.pm)
BuildRequires:	perl(File/Spec.pm)
BuildRequires:	perl(IO/Uncompress/Bunzip2.pm)
BuildRequires:	perl(IO/Zlib.pm)
BuildRequires:	perl(strict.pm)
BuildRequires:	perl(warnings.pm)
# Test Suite
BuildRequires:	perl(File/Path.pm)
BuildRequires:	perl(File/Spec/Functions.pm)
BuildRequires:	perl(File/Temp.pm)
BuildRequires:	perl(FindBin.pm)
BuildRequires:	perl(Test/More.pm)
BuildRequires:	perl(Test/UseAllModules.pm)
# Optional Tests
BuildRequires:	perl(Parallel/ForkManager.pm)
BuildRequires:	perl(Test/Pod.pm)
BuildRequires:	perl(Test/Pod/Coverage.pm)
# Runtime
Requires:	perl(IO/Uncompress/Bunzip2.pm)
Requires:	perl(IO/Zlib.pm)
Source44: import.info

%description
This is a fork of Archive::Any by Michael Schwern and Clint Moore. The main
difference is that this works properly even when you fork(), and may require
less memory to extract a tarball. On the other hand, this isn't pluggable
(it only supports file formats used in the CPAN toolchains), and it doesn't
check MIME types.

%prep
%setup -q -n Archive-Any-Lite-%{version}

# Build with ExtUtils::MakeMaker rather than ExtUtils::MakeMaker::CPANfile
%patch0

%build
perl Makefile.PL INSTALLMAN1DIR=%_man1dir INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -delete
# %{_fixperms} %{buildroot}

%check
make test TEST_POD=1

%files
%doc LICENSE
%doc Changes README
%{perl_vendor_privlib}/Archive/

%changelog
* Mon Dec 19 2016 Igor Vlasenko <viy@altlinux.ru> 0.11-alt1_2
- update to new release by fcimport

* Sun May 08 2016 Igor Vlasenko <viy@altlinux.ru> 0.11-alt1_1
- update to new release by fcimport

* Tue May 03 2016 Igor Vlasenko <viy@altlinux.ru> 0.11-alt1
- automated CPAN update

* Mon Mar 07 2016 Igor Vlasenko <viy@altlinux.ru> 0.10-alt1_5
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 0.10-alt1_4
- update to new release by fcimport

* Thu Dec 18 2014 Igor Vlasenko <viy@altlinux.ru> 0.10-alt1_2
- update to new release by fcimport

* Tue Aug 19 2014 Igor Vlasenko <viy@altlinux.ru> 0.10-alt1
- automated CPAN update

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 0.09-alt1_2
- update to new release by fcimport

* Tue Jun 03 2014 Igor Vlasenko <viy@altlinux.ru> 0.09-alt1_1
- update to new release by fcimport

* Tue Apr 22 2014 Igor Vlasenko <viy@altlinux.ru> 0.09-alt1
- automated CPAN update

* Thu Nov 14 2013 Igor Vlasenko <viy@altlinux.ru> 0.07-alt1_2
- Sisyphus build

* Mon Sep 09 2013 Igor Vlasenko <viy@altlinux.ru> 0.07-alt1
- initial import by package builder

