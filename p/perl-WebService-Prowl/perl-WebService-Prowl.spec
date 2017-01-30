%define module_version 0.08
%define module_name WebService-Prowl
# BEGIN SourceDeps(oneline):
BuildRequires: perl(AnyEvent/HTTP.pm) perl(AnyEvent/Twitter/Stream.pm) perl(Carp.pm) perl(DateTime.pm) perl(Encode.pm) perl(File/HomeDir.pm) perl(LWP/Protocol/https.pm) perl(LWP/UserAgent.pm) perl(Module/Build/Tiny.pm) perl(Test/More.pm) perl(URI/Escape.pm) perl(XML/Simple.pm) perl(YAML.pm)
# END SourceDeps(oneline)
%define _unpackaged_files_terminate_build 1
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 0.08
Release: alt2
Summary: a interface to Prowl Public API
Group: Development/Perl
License: perl
URL: https://github.com/sekimura/WebService-Prowl

Source0: http://mirror.yandex.ru/mirrors/cpan/authors/id/S/SE/SEKIMURA/%{module_name}-%{module_version}.tar.gz
BuildArch: noarch

%description
WebService::Prowl is a interface to Prowl Public API


%prep
%setup -q -n %{module_name}-%{module_version}

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README.md LICENSE Changes
%perl_vendor_privlib/W*

%changelog
* Mon Jan 30 2017 Igor Vlasenko <viy@altlinux.ru> 0.08-alt2
- to Sisyphus

* Thu May 26 2016 Igor Vlasenko <viy@altlinux.ru> 0.08-alt1
- regenerated from template by package builder

* Tue Sep 10 2013 Igor Vlasenko <viy@altlinux.ru> 0.07-alt1
- initial import by package builder

