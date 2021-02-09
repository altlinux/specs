%def_without test
%define module_name WebService-Gyazo-B
%define _without_test 1
# BEGIN SourceDeps(oneline):
BuildRequires: perl(Data/Dumper.pm) perl(File/Spec.pm) perl(File/Temp.pm) perl(HTTP/Request/Common.pm) perl(IO/Handle.pm) perl(IPC/Open3.pm) perl(LWP/Protocol/https.pm) perl(LWP/Protocol/socks.pm) perl(LWP/UserAgent.pm) perl(Module/Build.pm) perl(Pod/Coverage/TrustPod.pm) perl(Test/CPAN/Changes.pm) perl(Test/More.pm) perl(Test/Pod.pm) perl(Test/Pod/Coverage.pm) perl(URI/Simple.pm) perl(constant.pm) perl(lib.pm) perl(strict.pm) perl(warnings.pm)
# END SourceDeps(oneline)
%define _unpackaged_files_terminate_build 1
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 0.0406
Release: alt2
Summary: a Perl image upload library for gyazo.com
Group: Development/Perl
License: perl
Url: %CPAN %module_name

Source0: http://mirror.yandex.ru/mirrors/cpan/authors/id/S/SH/SHLOMIF/%{module_name}-%{version}.tar.gz
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
%doc README Changes~ LICENSE README.md Changes
%perl_vendor_privlib/W*

%changelog
* Tue Feb 09 2021 Igor Vlasenko <viy@altlinux.ru> 0.0406-alt2
- to Sisyphus as shutter dep

* Sun Jun 28 2020 Igor Vlasenko <viy@altlinux.ru> 0.0406-alt1
- updated by package builder

* Sat Dec 05 2015 Igor Vlasenko <viy@altlinux.ru> 0.0405-alt1
- initial import by package builder

