%define _unpackaged_files_terminate_build 1
Group: Development/Other
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl-podlators
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Summary:	A tiny replacement for Module::Build
Name:		perl-Module-Build-Tiny
Version:	0.047
Release:	alt1
License:	GPL+ or Artistic
URL:		https://metacpan.org/release/Module-Build-Tiny
Source0:	http://www.cpan.org/authors/id/L/LE/LEONT/Module-Build-Tiny-%{version}.tar.gz
BuildArch:	noarch
# Module Build
BuildRequires:	rpm-build-perl
BuildRequires:	perl-devel
# Module
BuildRequires:	perl(CPAN/Meta.pm)
BuildRequires:	perl(DynaLoader.pm)
BuildRequires:	perl(Exporter.pm)
BuildRequires:	perl(ExtUtils/CBuilder.pm)
BuildRequires:	perl(ExtUtils/Config.pm)
BuildRequires:	perl(ExtUtils/Helpers.pm)
BuildRequires:	perl(ExtUtils/Install.pm)
BuildRequires:	perl(ExtUtils/InstallPaths.pm)
BuildRequires:	perl(ExtUtils/ParseXS.pm)
BuildRequires:	perl(File/Path.pm)
BuildRequires:	perl(File/Spec/Functions.pm)
BuildRequires:	perl(Getopt/Long.pm)
BuildRequires:	perl(JSON/PP.pm)
BuildRequires:	perl(Pod/Man.pm)
BuildRequires:	perl(TAP/Harness/Env.pm)
# Test
BuildRequires:	perl(blib.pm)
BuildRequires:	perl(Carp.pm)
BuildRequires:	perl(Cwd.pm)
BuildRequires:	perl(Data/Dumper.pm)
BuildRequires:	perl(File/ShareDir.pm)
BuildRequires:	perl(File/Spec.pm)
BuildRequires:	perl(File/Temp.pm)
BuildRequires:	perl(IO/File.pm)
BuildRequires:	perl(IO/Handle.pm)
BuildRequires:	perl(IPC/Open2.pm)
BuildRequires:	perl(IPC/Open3.pm)
BuildRequires:	perl(Test/More.pm)
BuildRequires:	perl(Test/Pod.pm)
BuildRequires:	perl(XSLoader.pm)
# Runtime
Requires:	perl(DynaLoader.pm)
Requires:	perl(ExtUtils/CBuilder.pm)
Requires:	perl(ExtUtils/ParseXS.pm)
Requires:	perl(Pod/Man.pm)
Requires:	perl(TAP/Harness/Env.pm)

# ExtUtils::CBuilder in EL-8 has no dependency on gcc or c++ (#1547165)
# so pull them in ourselves
%if 0%{?el8}
BuildRequires:	gcc, gcc-c++
Requires:	gcc, gcc-c++
%endif
Source44: import.info

%description
Many Perl distributions use a Build.PL file instead of a Makefile.PL file to
drive distribution configuration, build, test and installation. Traditionally,
Build.PL uses Module::Build as the underlying build system. This module
provides a simple, lightweight, drop-in replacement.

Whereas Module::Build has over 6,700 lines of code; this module has less than
70, yet supports the features needed by most pure-Perl distributions.

%prep
%setup -q -n Module-Build-Tiny-%{version}
rm t/simple.t

%build
perl Build.PL --installdirs=vendor
./Build

%install
./Build install --destdir=%{buildroot} --create_packlist=0

%check
AUTHOR_TESTING=1 RELEASE_TESTING=1 ./Build test

%files
%doc Changes README Todo
%{perl_vendor_privlib}/Module/

%changelog
* Sun Oct 01 2023 Igor Vlasenko <viy@altlinux.org> 0.047-alt1
- automated CPAN update

* Tue Jun 13 2023 Igor Vlasenko <viy@altlinux.org> 0.046-alt1
- automated CPAN update

* Sun May 21 2023 Igor Vlasenko <viy@altlinux.org> 0.045-alt1
- automated CPAN update

* Sat Apr 29 2023 Igor Vlasenko <viy@altlinux.org> 0.044-alt1
- automated CPAN update

* Wed Apr 19 2023 Igor Vlasenko <viy@altlinux.org> 0.043-alt1
- automated CPAN update

* Wed Nov 20 2019 Igor Vlasenko <viy@altlinux.ru> 0.039-alt1_15
- update to new release by fcimport

* Sat Jul 14 2018 Igor Vlasenko <viy@altlinux.ru> 0.039-alt1_10
- update to new release by fcimport

* Mon Oct 02 2017 Igor Vlasenko <viy@altlinux.ru> 0.039-alt1_8
- update to new release by fcimport

* Thu Aug 03 2017 Igor Vlasenko <viy@altlinux.ru> 0.039-alt1_7
- update to new release by fcimport

* Thu Mar 16 2017 Igor Vlasenko <viy@altlinux.ru> 0.039-alt1_6
- update to new release by fcimport

* Mon Dec 19 2016 Igor Vlasenko <viy@altlinux.ru> 0.039-alt1_5
- update to new release by fcimport

* Mon Mar 07 2016 Igor Vlasenko <viy@altlinux.ru> 0.039-alt1_4
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 0.039-alt1_3
- update to new release by fcimport

* Thu Dec 18 2014 Igor Vlasenko <viy@altlinux.ru> 0.039-alt1_1
- update to new release by fcimport

* Tue Dec 16 2014 Igor Vlasenko <viy@altlinux.ru> 0.039-alt1
- automated CPAN update

* Mon Jun 02 2014 Igor Vlasenko <viy@altlinux.ru> 0.036-alt1
- automated CPAN update

* Wed Mar 05 2014 Igor Vlasenko <viy@altlinux.ru> 0.035-alt1_1
- update to new release by fcimport
- tmp patch not to use new Test::Harness::Env

* Mon Oct 07 2013 Igor Vlasenko <viy@altlinux.ru> 0.028-alt1_1
- update to new release by fcimport

* Mon Sep 30 2013 Igor Vlasenko <viy@altlinux.ru> 0.028-alt1
- automated CPAN update

* Thu Sep 19 2013 Igor Vlasenko <viy@altlinux.ru> 0.027-alt2_1
- man1 support patch

* Sun Sep 15 2013 Igor Vlasenko <viy@altlinux.ru> 0.027-alt1_1
- update to new release by fcimport

* Thu Sep 12 2013 Igor Vlasenko <viy@altlinux.ru> 0.027-alt1
- automated CPAN update

* Tue Aug 27 2013 Igor Vlasenko <viy@altlinux.ru> 0.026-alt1
- automated CPAN update

* Mon Aug 05 2013 Igor Vlasenko <viy@altlinux.ru> 0.025-alt1_2
- update to new release by fcimport

* Mon Jul 29 2013 Igor Vlasenko <viy@altlinux.ru> 0.025-alt1_1
- converted for ALT Linux by srpmconvert tools

