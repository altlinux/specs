# BEGIN SourceDeps(oneline):
BuildRequires: perl(Metrics/Any/Adapter.pm) perl(Metrics/Any/Adapter/Test.pm) perl(Module/Build.pm) perl(Test/Builder/Module.pm) perl(Test/More.pm) perl(base.pm)
# END SourceDeps(oneline)
%define module_name Test-Metrics-Any
%define _unpackaged_files_terminate_build 1
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 0.01
Release: alt2
Summary: assert that code produces metrics via L<Metrics::Any>
Group: Development/Perl
License: perl
Url: %CPAN %module_name

Source0: http://mirror.yandex.ru/mirrors/cpan/authors/id/P/PE/PEVANS/%{module_name}-%{version}.tar.gz
BuildArch: noarch

%description
This test module helps write unit tests which assert that the code under test
reports metrics via the Metrics::Any manpage.

Loading this module automatically sets the the Metrics::Any::Adapter manpage type to
`Test'.

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
* Thu Oct 01 2020 Igor Vlasenko <viy@altlinux.ru> 0.01-alt2
- to Sisyphus as IO-Async dep

* Sat May 09 2020 Igor Vlasenko <viy@altlinux.ru> 0.01-alt1
- initial import by package builder

