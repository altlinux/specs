%define module_version 0.009
%define module_name Test-Exception-LessClever
# BEGIN SourceDeps(oneline):
BuildRequires: perl(Carp.pm) perl(Exporter.pm) perl(ExtUtils/MakeMaker.pm) perl(Mock/Quick.pm) perl(Test/Builder.pm) perl(Test/Builder/Tester.pm) perl(Test/More.pm) perl(base.pm) perl(strict.pm) perl(warnings.pm)
# END SourceDeps(oneline)
%define _unpackaged_files_terminate_build 1
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 0.009
Release: alt2
Summary: Test::Exception simplified
Group: Development/Perl
License: perl
URL: https://github.com/exodist/Test-Exception-LessClever

Source0: http://mirror.yandex.ru/mirrors/cpan/authors/id/E/ET/ETHER/%{module_name}-%{module_version}.tar.gz
BuildArch: noarch

%description
%summary

%prep
%setup -q -n %{module_name}-%{module_version}

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README Changes
%perl_vendor_privlib/T*

%changelog
* Wed Jul 13 2022 Igor Vlasenko <viy@altlinux.org> 0.009-alt2
- to Sisyphus as perl-Sub-HandlesVia build dep

* Sun Nov 20 2016 Igor Vlasenko <viy@altlinux.ru> 0.009-alt1
- regenerated from template by package builder

* Sat Nov 19 2016 Igor Vlasenko <viy@altlinux.ru> 0.008-alt1
- regenerated from template by package builder

* Wed Jul 06 2016 Igor Vlasenko <viy@altlinux.ru> 0.007-alt1
- regenerated from template by package builder

* Tue Sep 17 2013 Igor Vlasenko <viy@altlinux.ru> 0.006-alt1
- initial import by package builder

