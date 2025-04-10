# BEGIN SourceDeps(oneline):
BuildRequires: perl(Capture/Tiny.pm) perl(ExtUtils/MakeMaker.pm) perl(IO/Handle.pm) perl(Test2/API.pm) perl(Test2/V0.pm)
# END SourceDeps(oneline)
%define module_name Test2-Plugin-IOEvents
%define _unpackaged_files_terminate_build 1
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 0.001001
Release: alt2
Summary: Turn STDOUT and STDERR into Test2 events.
Group: Development/Perl
License: perl
Url: %CPAN %module_name

Source0: http://mirror.yandex.ru/mirrors/cpan/authors/id/E/EX/EXODIST/%{module_name}-%{version}.tar.gz
BuildArch: noarch

%description
This plugin turns prints to STDOUT and STDERR (including warnings) into proper
Test2 events.

%prep
%setup -q -n %{module_name}-%{version}

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README.md LICENSE Changes README
%perl_vendor_privlib/T*

%changelog
* Thu Apr 10 2025 Igor Vlasenko <viy@altlinux.org> 0.001001-alt2
- to Sisyphus as App-perlbrew dep

* Wed Oct 07 2020 Igor Vlasenko <viy@altlinux.ru> 0.001001-alt1
- initial import by package builder

