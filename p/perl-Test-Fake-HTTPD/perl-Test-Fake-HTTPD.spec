%define module_name Test-Fake-HTTPD
# BEGIN SourceDeps(oneline):
BuildRequires: perl(Carp.pm) perl(Exporter.pm) perl(ExtUtils/MakeMaker.pm) perl(HTTP/Daemon.pm) perl(HTTP/Daemon/SSL.pm) perl(HTTP/Message/PSGI.pm) perl(LWP/Protocol/https.pm) perl(LWP/UserAgent.pm) perl(Module/Build/Tiny.pm) perl(Scalar/Util.pm) perl(Test/Exception.pm) perl(Test/More.pm) perl(Test/SharedFork.pm) perl(Test/TCP.pm) perl(Test/UseAllModules.pm) perl(Time/HiRes.pm) perl(URI.pm)
# END SourceDeps(oneline)
%define _unpackaged_files_terminate_build 1
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 0.09
Release: alt2
Summary: a fake HTTP server
Group: Development/Perl
License: perl
URL: https://github.com/masaki/Test-Fake-HTTPD

Source0: http://mirror.yandex.ru/mirrors/cpan/authors/id/M/MA/MASAKI/%{module_name}-%{version}.tar.gz
BuildArch: noarch

%description
Test::Fake::HTTPD is a fake HTTP server module for testing.


%prep
%setup -q -n %{module_name}-%{version}

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README.md Changes LICENSE
%perl_vendor_privlib/T*

%changelog
* Thu Apr 10 2025 Igor Vlasenko <viy@altlinux.org> 0.09-alt2
- to Sisyphus as Tapper-Reports-Web dep

* Fri Aug 28 2020 Igor Vlasenko <viy@altlinux.ru> 0.09-alt1
- updated by package builder

* Fri Dec 21 2018 Igor Vlasenko <viy@altlinux.ru> 0.08-alt1
- regenerated from template by package builder

* Tue Sep 10 2013 Igor Vlasenko <viy@altlinux.ru> 0.06-alt1
- initial import by package builder

