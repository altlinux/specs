Group: Development/Perl
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
# Perform optional tests
%bcond_without perl_Const_Fast_enables_optional_test

Name:           perl-Const-Fast
Version:        0.014
Release:        alt2_19
Summary:        Facility for creating read-only scalars, arrays, and hashes
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/Const-Fast
Source0:        https://cpan.metacpan.org/authors/id/L/LE/LEONT/Const-Fast-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  findutils
BuildRequires:  rpm-build-perl
BuildRequires:  perl-devel
BuildRequires:  perl
BuildRequires:  perl(Module/Build/Tiny.pm)
# Run-time
BuildRequires:  perl(Carp.pm)
BuildRequires:  perl(Scalar/Util.pm)
BuildRequires:  perl(Storable.pm)
BuildRequires:  perl(strict.pm)
BuildRequires:  perl(Sub/Exporter/Progressive.pm)
BuildRequires:  perl(warnings.pm)
# Tests
BuildRequires:  perl(Data/Dumper.pm)
BuildRequires:  perl(File/Find.pm)
BuildRequires:  perl(File/Temp.pm)
BuildRequires:  perl(Test/Fatal.pm)
BuildRequires:  perl(Test/More.pm)
%if %{with perl_Const_Fast_enables_optional_test}
# Optional tests
# Pod::Coverage::TrustPod not used
# Test::Pod not used
# Test::Pod::Coverage not used
BuildRequires:  perl(Test/Script.pm)
%endif


Source44: import.info

%description
This the only function of this module and it is exported by default. It takes
a scalar, array or hash left-value as first argument, and a list of one or
more values depending on the type of the first argument as the value for the
variable. It will set the variable to that value and subsequently make it
read-only. Arrays and hashes will be made deeply read-only.


%prep
%setup -q -n Const-Fast-%{version}


%build
perl Build.PL --installdirs vendor
./Build


%install
./Build install --destdir $RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -delete
# %{_fixperms} $RPM_BUILD_ROOT/*


%check
unset RELEASE_TESTING
./Build test


%files
%doc --no-dereference LICENSE
%doc Changes README
%{perl_vendor_privlib}/*


%changelog
* Wed Nov 20 2019 Igor Vlasenko <viy@altlinux.ru> 0.014-alt2_19
- update to new release by fcimport

* Sat Jul 14 2018 Igor Vlasenko <viy@altlinux.ru> 0.014-alt2_14
- update to new release by fcimport

* Wed Sep 27 2017 Igor Vlasenko <viy@altlinux.ru> 0.014-alt2_12
- update to new release by fcimport

* Thu Aug 03 2017 Igor Vlasenko <viy@altlinux.ru> 0.014-alt2_11
- update to new release by fcimport

* Thu Mar 16 2017 Igor Vlasenko <viy@altlinux.ru> 0.014-alt2_10
- update to new release by fcimport

* Thu Nov 17 2016 Igor Vlasenko <viy@altlinux.ru> 0.014-alt2
- to Sisyphus

* Tue Oct 15 2013 Igor Vlasenko <viy@altlinux.ru> 0.014-alt1
- update

* Wed Feb 27 2013 Igor Vlasenko <viy@altlinux.ru> 0.013-alt1_2
- update to new release by fcimport

* Tue Oct 09 2012 Igor Vlasenko <viy@altlinux.ru> 0.013-alt1_1
- update to new release by fcimport

* Tue Jul 31 2012 Igor Vlasenko <viy@altlinux.ru> 0.011-alt1_3
- update to new release by fcimport

* Wed May 23 2012 Igor Vlasenko <viy@altlinux.ru> 0.006-alt1_4
- fc import

