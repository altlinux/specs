# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl-devel perl-podlators
# END SourceDeps(oneline)
Name:		perl-ExtUtils-InstallPaths
Version:	0.010
Release:	alt1_1
Summary:	Build.PL install path logic made easy
Group:		Development/Perl
License:	GPL+ or Artistic
URL:		https://metacpan.org/release/ExtUtils-InstallPaths
Source0:	http://cpan.metacpan.org/authors/id/L/LE/LEONT/ExtUtils-InstallPaths-%{version}.tar.gz
BuildArch:	noarch
# Build
BuildRequires:	perl(ExtUtils/MakeMaker.pm)
# Module
BuildRequires:	perl(Carp.pm)
BuildRequires:	perl(ExtUtils/Config.pm)
BuildRequires:	perl(File/Spec.pm)
# Test Suite
BuildRequires:	perl(Config.pm)
BuildRequires:	perl(File/Spec/Functions.pm)
BuildRequires:	perl(File/Temp.pm)
BuildRequires:	perl(IO/Handle.pm)
BuildRequires:	perl(IPC/Open3.pm)
BuildRequires:	perl(Test/More.pm)
# Release Tests
# perl-Pod-Coverage-TrustPod -> perl-Pod-Eventual -> perl-Mixin-Linewise ->
#   perl-YAML-Tiny -> perl-Module-Build-Tiny -> perl-ExtUtils-InstallPaths
%if 0%{!?perl_bootstrap:1}
BuildRequires:	perl(Pod/Coverage/TrustPod.pm)
BuildRequires:	perl(Test/Pod.pm)
BuildRequires:	perl(Test/Pod/Coverage.pm)
%endif
Source44: import.info
# Runtime

%description
This module tries to make install path resolution as easy as possible.

When you want to install a module, it needs to figure out where to install
things. The nutshell version of how this works is that default installation
locations are determined from ExtUtils::Config, and they may be individually
overridden by using the install_path attribute. An install_base attribute lets
you specify an alternative installation root like /home/foo and prefix does
something similar in a rather different (and more complicated) way. destdir
lets you specify a temporary installation directory like /tmp/install in case
you want to create bundled-up installable packages.

%prep
%setup -q -n ExtUtils-InstallPaths-%{version}

%build
perl Makefile.PL INSTALLMAN1DIR=%_man1dir INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
# %{_fixperms} %{buildroot}

%check
make test RELEASE_TESTING=1

%files
%doc Changes LICENSE README
%{perl_vendor_privlib}/ExtUtils/

%changelog
* Fri Nov 15 2013 Igor Vlasenko <viy@altlinux.ru> 0.010-alt1_1
- update to new release by fcimport

* Fri Nov 01 2013 Igor Vlasenko <viy@altlinux.ru> 0.010-alt1
- automated CPAN update

* Sun Sep 15 2013 Igor Vlasenko <viy@altlinux.ru> 0.009-alt1_6
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 0.009-alt1_5
- update to new release by fcimport

* Mon Aug 05 2013 Igor Vlasenko <viy@altlinux.ru> 0.009-alt1_4
- update to new release by fcimport

* Mon Jul 29 2013 Igor Vlasenko <viy@altlinux.ru> 0.009-alt1_3
- converted for ALT Linux by srpmconvert tools

