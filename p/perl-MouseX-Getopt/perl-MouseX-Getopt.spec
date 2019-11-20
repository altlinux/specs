Group: Development/Perl
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl-podlators
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:		perl-MouseX-Getopt
Summary:	Mouse role for processing command line options
Version:	0.38
Release:	alt1_5
License:	GPL+ or Artistic
URL:		https://metacpan.org/release/MouseX-Getopt
Source0:	https://cpan.metacpan.org/modules/by-module/MouseX/MouseX-Getopt-%{version}.tar.gz
BuildArch:	noarch
# Module Build
BuildRequires:	rpm-build-perl
BuildRequires:	perl-devel
BuildRequires:	perl(Module/Build/Tiny.pm)
BuildRequires:	perl(strict.pm)
BuildRequires:	perl(warnings.pm)
# Module Runtime
BuildRequires:	perl(Carp.pm)
BuildRequires:	perl(Getopt/Long.pm)
BuildRequires:	perl(Getopt/Long/Descriptive.pm)
BuildRequires:	perl(Mouse.pm)
BuildRequires:	perl(Mouse/Meta/Attribute.pm)
BuildRequires:	perl(Mouse/Role.pm)
BuildRequires:	perl(Mouse/Util/TypeConstraints.pm)
# Test Suite
BuildRequires:	perl(File/Spec.pm)
BuildRequires:	perl(Mouse/Meta/Class.pm)
BuildRequires:	perl(Scalar/Util.pm)
BuildRequires:	perl(Test/Exception.pm)
BuildRequires:	perl(Test/More.pm)
BuildRequires:	perl(Test/Mouse.pm)
BuildRequires:	perl(Test/Warn.pm)
# Optional Tests (have circular dependencies)
%if 0%{!?perl_bootstrap:1}
BuildRequires:	perl(MouseX/ConfigFromFile.pm)
BuildRequires:	perl(MouseX/SimpleConfig.pm)
%endif
# Runtime
Requires:	perl(Mouse.pm) >= 0.640
Requires:	perl(Mouse/Meta/Attribute.pm)

# Filter under-specified dependency

Source44: import.info
%filter_from_requires /^perl(Mouse.pm)/d

%description
This is a Mouse role that provides an alternate constructor for creating
objects using parameters passed in from the command line.

%prep
%setup -q -n MouseX-Getopt-%{version}

%build
perl Build.PL --installdirs=vendor
./Build

%install
./Build install --destdir=%{buildroot} --create_packlist=0

%check
./Build test

%files
# Note: malformed LICENSE file in 0.35 .. 0.38 not shipped
# https://github.com/gfx/mousex-getopt/issues/2
%doc Changes README.md
%{perl_vendor_privlib}/MouseX/

%changelog
* Wed Nov 20 2019 Igor Vlasenko <viy@altlinux.ru> 0.38-alt1_5
- update to new release by fcimport

* Sat Feb 09 2019 Igor Vlasenko <viy@altlinux.ru> 0.38-alt1_1
- update to new release by fcimport

* Wed Jan 30 2019 Igor Vlasenko <viy@altlinux.ru> 0.38-alt1
- automated CPAN update

* Wed Oct 10 2018 Igor Vlasenko <viy@altlinux.ru> 0.37-alt1_10
- update to new release by fcimport

* Sat Jul 14 2018 Igor Vlasenko <viy@altlinux.ru> 0.37-alt1_8
- update to new release by fcimport

* Mon Oct 02 2017 Igor Vlasenko <viy@altlinux.ru> 0.37-alt1_5
- update to new release by fcimport

* Thu Aug 03 2017 Igor Vlasenko <viy@altlinux.ru> 0.37-alt1_4
- update to new release by fcimport

* Thu Mar 16 2017 Igor Vlasenko <viy@altlinux.ru> 0.37-alt1_2
- update to new release by fcimport

* Mon Dec 19 2016 Igor Vlasenko <viy@altlinux.ru> 0.37-alt1_1
- update to new release by fcimport

* Mon Jul 25 2016 Igor Vlasenko <viy@altlinux.ru> 0.37-alt1
- automated CPAN update

* Mon Mar 07 2016 Igor Vlasenko <viy@altlinux.ru> 0.36-alt1_5
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 0.36-alt1_4
- update to new release by fcimport

* Tue Apr 07 2015 Igor Vlasenko <viy@altlinux.ru> 0.36-alt1_1
- update to new release by fcimport

* Mon Oct 27 2014 Igor Vlasenko <viy@altlinux.ru> 0.35-alt1_6
- update to new release by fcimport

* Mon Jun 30 2014 Igor Vlasenko <viy@altlinux.ru> 0.35-alt1_4
- moved to Sisyphus as dependency

* Mon Apr 16 2012 Vladimir Lettiev <crux@altlinux.ru> 0.34-alt1
- 0.34

* Thu Feb 17 2011 Vladimir Lettiev <crux@altlinux.ru> 0.33-alt1
- initial build
