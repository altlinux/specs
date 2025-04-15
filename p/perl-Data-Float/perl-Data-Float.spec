Group: Development/Other
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl-podlators
# END SourceDeps(oneline)
# fedora bcond_with macro
%define bcond_with() %{expand:%%{?_with_%{1}:%%global with_%{1} 1}}
%define bcond_without() %{expand:%%{!?_without_%{1}:%%global with_%{1} 1}}
# redefine altlinux specific with and without
%define with()         %{expand:%%{?with_%{1}:1}%%{!?with_%{1}:0}}
%define without()      %{expand:%%{?with_%{1}:0}%%{!?with_%{1}:1}}
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
# Run optional test
%{bcond_without perl_Data_Float_enables_optional_test}

Name:           perl-Data-Float
Version:        0.015
Release:        alt1_1
Summary:        Details of the floating point data type
# README:       GPL-1.0-or-later OR Artistic-1.0-Perl
# SECURITY.md:  Relicensed by the author from CC-BY-SA-4.0 to
#               GPL-1.0-or-later OR Artistic-1.0-Perl
#               <https://github.com/robrwo/Data-Float/issues/3>
#               Later, CC-BY-SA-4.0 changed to CC0-1.0.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Data-Float
Source0:        https://cpan.metacpan.org/authors/id/R/RR/RRWO/Data-Float-%{version}.tar.gz
# License clarification for SECURITY.md
Source1:        security.md.license_clarification
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  rpm-build-perl
BuildRequires:  perl-devel
BuildRequires:  perl
BuildRequires:  perl(ExtUtils/MakeMaker.pm)
# Run-time:
BuildRequires:  perl(Carp.pm)
BuildRequires:  perl(constant.pm)
BuildRequires:  perl(Exporter.pm)
BuildRequires:  perl(integer.pm)
BuildRequires:  perl(parent.pm)
BuildRequires:  perl(strict.pm)
BuildRequires:  perl(warnings.pm)
# Tests:
BuildRequires:  perl(Test/More.pm)
%if %{with perl_Data_Float_enables_optional_test}
# Optional tests:
BuildRequires:  perl(Test/Pod.pm)
BuildRequires:  perl(Test/Pod/Coverage.pm)
%endif
Requires:       perl(constant.pm)
Requires:       perl(integer.pm)
Source44: import.info

%description
This module is about the native floating point numerical data type. A floating
point number is one of the types of datum that can appear in the numeric part
of a Perl scalar. This module supplies constants describing the native
floating point type, classification functions, and functions to manipulate
floating point values at a low level.

%package tests
Group: Development/Other
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
%setup -q -n Data-Float-%{version}
install -m 0644 %{SOURCE1} security.md.license_clarification

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{makeinstall_std}
# %{_fixperms} %{buildroot}/*
# Install tests
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
# POD tests only work on ./lib modules
rm %{buildroot}%{_libexecdir}/%{name}/t/pod_*.t
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
#!/bin/sh
cd %{_libexecdir}/%{name} && exec prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test

%check
export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
make test

%files
%doc --no-dereference security.md.license_clarification
%doc Changes README SECURITY.md
%dir %{perl_vendor_privlib}/Data
%{perl_vendor_privlib}/Data/Float.pm

%files tests
%{_libexecdir}/%{name}

%changelog
* Tue Apr 15 2025 Igor Vlasenko <viy@altlinux.org> 0.015-alt1_1
- converted for ALT Linux by srpmconvert tools

* Wed Nov 20 2019 Igor Vlasenko <viy@altlinux.ru> 0.013-alt1_7
- update to new release by fcimport

* Sat Jul 14 2018 Igor Vlasenko <viy@altlinux.ru> 0.013-alt1_3
- update to new release by fcimport

* Mon May 07 2018 Igor Vlasenko <viy@altlinux.ru> 0.013-alt1_2
- update to new release by fcimport

* Wed Aug 02 2017 Igor Vlasenko <viy@altlinux.ru> 0.013-alt1
- automated CPAN update

* Thu Mar 16 2017 Igor Vlasenko <viy@altlinux.ru> 0.012-alt2_10
- update to new release by fcimport

* Mon Dec 19 2016 Igor Vlasenko <viy@altlinux.ru> 0.012-alt2_9
- update to new release by fcimport

* Mon Mar 07 2016 Igor Vlasenko <viy@altlinux.ru> 0.012-alt2_8
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 0.012-alt2_7
- update to new release by fcimport

* Mon Oct 27 2014 Igor Vlasenko <viy@altlinux.ru> 0.012-alt2_5
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 0.012-alt2_4
- update to new release by fcimport

* Tue Feb 18 2014 Igor Vlasenko <viy@altlinux.ru> 0.012-alt2_3
- moved to Sisyphus for Slic3r (by dd@ request)

* Tue Aug 27 2013 Igor Vlasenko <viy@altlinux.ru> 0.012-alt1_3
- update to new release by fcimport

* Mon Aug 05 2013 Igor Vlasenko <viy@altlinux.ru> 0.012-alt1_2
- update to new release by fcimport

* Fri Apr 26 2013 Igor Vlasenko <viy@altlinux.ru> 0.012-alt1_1
- initial fc import

