%define module_version 0.07
%define module_name Proc-Guard
# BEGIN SourceDeps(oneline):
BuildRequires: perl(Class/Accessor/Lite.pm) perl(Errno.pm) perl(Exporter.pm) perl(ExtUtils/MakeMaker.pm) perl(IO/Socket/INET.pm) perl(Module/Build.pm) perl(Test/More.pm) perl(Test/Requires.pm)
# END SourceDeps(oneline)
%define _unpackaged_files_terminate_build 1
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 0.07
Release: alt2
Summary: process runner with RAII pattern
Group: Development/Perl
License: perl
URL: https://github.com/tokuhirom/Proc-Guard

Source0: http://cpan.org.ua/authors/id/T/TO/TOKUHIROM/%{module_name}-%{module_version}.tar.gz
BuildArch: noarch

%description
Proc::Guard runs process, and destroys it when the perl script exits.

This is useful for testing code working with server process.


%prep
%setup -n %{module_name}-%{module_version}

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README.mkdn README.md LICENSE Changes
%perl_vendor_privlib/P*

%changelog
* Sun Jan 15 2017 Igor Vlasenko <viy@altlinux.ru> 0.07-alt2
- to Sisyphus

* Thu Apr 02 2015 Igor Vlasenko <viy@altlinux.ru> 0.07-alt1
- regenerated from template by package builder

* Wed Sep 04 2013 Igor Vlasenko <viy@altlinux.ru> 0.06-alt1
- initial import by package builder

