%define module_name FFI-CheckLib
# BEGIN SourceDeps(oneline):
BuildRequires: perl(Capture/Tiny.pm) perl(Config.pm) perl(DynaLoader.pm) perl(Env.pm) perl(Exporter.pm) perl(ExtUtils/MakeMaker.pm) perl(File/Basename.pm) perl(File/Spec.pm) perl(Test/Exit.pm) perl(Test2/API.pm) perl(Test2/Mock.pm) perl(Test2/Require/Module.pm) perl(Test2/V0.pm) perl(base.pm)
# END SourceDeps(oneline)
%define _unpackaged_files_terminate_build 1
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 0.18
Release: alt2
Summary: Check that a library is available for FFI
Group: Development/Perl
License: perl
URL: https://metacpan.org/pod/FFI::CheckLib

Source0: http://mirror.yandex.ru/mirrors/cpan/authors/id/P/PL/PLICEASE/%{module_name}-%{version}.tar.gz
BuildArch: noarch

%description
From summary: %summary

%prep
%setup -q -n %{module_name}-%{version}

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc LICENSE Changes author.yml README example
%perl_vendor_privlib/F*

%changelog
* Fri Dec 29 2017 Igor Vlasenko <viy@altlinux.ru> 0.18-alt2
- to Sisyphus

* Tue Dec 26 2017 Igor Vlasenko <viy@altlinux.ru> 0.18-alt1
- regenerated from template by package builder

* Thu May 26 2016 Igor Vlasenko <viy@altlinux.ru> 0.15-alt1
- regenerated from template by package builder

* Wed Oct 14 2015 Igor Vlasenko <viy@altlinux.ru> 0.14-alt1
- regenerated from template by package builder

* Thu Apr 02 2015 Igor Vlasenko <viy@altlinux.ru> 0.11-alt1
- regenerated from template by package builder

* Thu Feb 05 2015 Igor Vlasenko <viy@altlinux.ru> 0.09-alt1
- regenerated from template by package builder

* Mon Jan 26 2015 Igor Vlasenko <viy@altlinux.ru> 0.08-alt1
- regenerated from template by package builder

* Mon Jan 19 2015 Igor Vlasenko <viy@altlinux.ru> 0.07-alt1
- regenerated from template by package builder

* Mon Jan 05 2015 Igor Vlasenko <viy@altlinux.ru> 0.04-alt1
- regenerated from template by package builder

* Mon Oct 27 2014 Igor Vlasenko <viy@altlinux.ru> 0.03-alt1
- initial import by package builder

