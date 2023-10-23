%define module_name Test-ExpectAndCheck
# BEGIN SourceDeps(oneline):
BuildRequires: perl(List/Util.pm) perl(Module/Build.pm) perl(Test/Builder.pm) perl(Test/Builder/Tester.pm) perl(Test/Deep.pm) perl(Test/Future/Deferred.pm) perl(Test2/V0.pm)
# END SourceDeps(oneline)
%define _unpackaged_files_terminate_build 1
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 0.06
Release: alt2
Summary: C<expect/check>-style unit testing with object methods
Group: Development/Perl
License: perl
Url: %CPAN %module_name

Source0: http://mirror.yandex.ru/mirrors/cpan/authors/id/P/PE/PEVANS/%{module_name}-%{version}.tar.gz
BuildArch: noarch

%description
This package creates objects that assist in writing unit tests with mocked
object instances. Each mocked "puppet" instance will expect to receive a given
list of method calls. Each method call is checked that it received the right
arguments, and will return a prescribed result. At the end of each test, each
object is checked to ensure all the expected methods were called.

%prep
%setup -q -n %{module_name}-%{version}

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README Changes LICENSE
%perl_vendor_privlib/T*

%changelog
* Mon Oct 23 2023 Igor Vlasenko <viy@altlinux.org> 0.06-alt2
- moved to Sisyphus as perl-Future-IO test dep

* Sat Oct 21 2023 Igor Vlasenko <viy@altlinux.org> 0.06-alt1
- updated by package builder

* Sat Oct 08 2022 Igor Vlasenko <viy@altlinux.org> 0.05-alt1
- updated by package builder

* Tue Oct 04 2022 Igor Vlasenko <viy@altlinux.org> 0.04-alt1
- updated by package builder

* Sun May 01 2022 Igor Vlasenko <viy@altlinux.org> 0.03-alt1
- updated by package builder

* Sun Jan 03 2021 Igor Vlasenko <viy@altlinux.ru> 0.02-alt1
- updated by package builder

* Thu Nov 26 2020 Igor Vlasenko <viy@altlinux.ru> 0.01-alt1
- initial import by package builder

