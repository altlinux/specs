%define module_name Test-MemoryGrowth
# BEGIN SourceDeps(oneline):
BuildRequires: /proc perl(Module/Build.pm) perl(Test/Builder.pm) perl(Test/Builder/Tester.pm) perl(Test/More.pm) perl(base.pm)
# END SourceDeps(oneline)
%define _unpackaged_files_terminate_build 1
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 0.04
Release: alt2
Summary: assert that code does not cause growth in memory usage
Group: Development/Perl
License: perl
Url: %CPAN %module_name

Source0: http://mirror.yandex.ru/mirrors/cpan/authors/id/P/PE/PEVANS/%{module_name}-%{version}.tar.gz
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
%doc LICENSE README Changes
%perl_vendor_privlib/T*

%changelog
* Thu Jun 25 2020 Igor Vlasenko <viy@altlinux.ru> 0.04-alt2
- to Sisyphus as perl-Sereal-Decoder dep

* Fri Jun 19 2020 Igor Vlasenko <viy@altlinux.ru> 0.04-alt1
- updated by package builder

* Wed Jan 16 2019 Igor Vlasenko <viy@altlinux.ru> 0.03-alt1
- regenerated from template by package builder

* Sat May 03 2014 Igor Vlasenko <viy@altlinux.ru> 0.02-alt1
- initial import by package builder

