# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl-devel perl-podlators
# END SourceDeps(oneline)
# Test suite needs patching if we have Test::More < 0.88
%global old_test_more %(perl -MTest::More -e 'print (($Test::More::VERSION) < 0.88 ? 1 : 0);' 2>/dev/null || echo 0)

Name:		perl-ExtUtils-Config
Version:	0.007
Release:	alt1_3
Summary:	A wrapper for perl's configuration
Group:		Development/Perl
License:	GPL+ or Artistic
URL:		https://metacpan.org/release/ExtUtils-Config
Source0:	http://cpan.metacpan.org/authors/id/L/LE/LEONT/ExtUtils-Config-%{version}.tar.gz
Patch1:		ExtUtils-Config-0.007-old-Test::More.patch
BuildArch:	noarch
# Build
BuildRequires:	perl(ExtUtils/MakeMaker.pm)
# Module
BuildRequires:	perl(Config.pm)
BuildRequires:	perl(Data/Dumper.pm)
# Test Suite
BuildRequires:	perl(File/Find.pm)
BuildRequires:	perl(File/Temp.pm)
BuildRequires:	perl(Test/More.pm)
# Release Tests
BuildRequires:	perl(Pod/Coverage/TrustPod.pm)
# Test::Kwalitee builds using Module::Build::Tiny, which requires ExtUtils::Config
%if 0%{!?perl_bootstrap:1}
#BuildRequires:	perl(Test/Kwalitee.pm)
%endif
BuildRequires:	perl(Test/Pod.pm)
BuildRequires:	perl(Test/Pod/Coverage.pm)
Source44: import.info
# Runtime

%description
ExtUtils::Config is an abstraction around the %%Config hash.

%prep
%setup -q -n ExtUtils-Config-%{version}

# Test suite needs patching if we have Test::More < 0.88
%if %{old_test_more}
%patch1
%endif

%build
perl Makefile.PL INSTALLMAN1DIR=%_man1dir INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
# %{_fixperms} %{buildroot}

%check
rm t/release-kwalitee.t
make test RELEASE_TESTING=1

%files
%doc Changes LICENSE README
%{perl_vendor_privlib}/ExtUtils/

%changelog
* Mon Jul 29 2013 Igor Vlasenko <viy@altlinux.ru> 0.007-alt1_3
- converted for ALT Linux by srpmconvert tools

