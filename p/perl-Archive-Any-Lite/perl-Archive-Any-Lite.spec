# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl-devel perl-podlators
# END SourceDeps(oneline)
%define fedora 19
Name:		perl-Archive-Any-Lite
Version:	0.07
Release:	alt1_2
Summary:	Simple CPAN package extractor 
License:	GPL+ or Artistic
Group:		Development/Perl
URL:		https://metacpan.org/release/Archive-Any-Lite
Source0:	http://cpan.metacpan.org/authors/id/I/IS/ISHIGAKI/Archive-Any-Lite-%{version}.tar.gz
BuildArch:	noarch
# Build
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
%if 0%{?fedora} > 14 || 0%{?rhel} > 5
# Needs 0.7.6 for data structure retrieval
BuildRequires:	perl(Parallel/ForkManager.pm)
%endif
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

# Test::More->note() requires Test::More ≥ 0.82
%if %(perl -MTest::More -e 'print (($Test::More::VERSION < 0.82) ? 1 : 0);' 2>/dev/null || echo 0)
sed -i -e '/ note /d' t/30_fork.t
%endif

%build
perl Makefile.PL INSTALLMAN1DIR=%_man1dir INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -exec rm -f {} \;
# %{_fixperms} %{buildroot}

%check
make test TEST_POD=1

%files
%doc Changes README
%{perl_vendor_privlib}/Archive/

%changelog
* Thu Nov 14 2013 Igor Vlasenko <viy@altlinux.ru> 0.07-alt1_2
- Sisyphus build

* Mon Sep 09 2013 Igor Vlasenko <viy@altlinux.ru> 0.07-alt1
- initial import by package builder

