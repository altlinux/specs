%define module_name Env-ShellWords
# BEGIN SourceDeps(oneline):
BuildRequires: perl(Carp.pm) perl(ExtUtils/MakeMaker.pm) perl(Test2/V0.pm)
# END SourceDeps(oneline)
%define _unpackaged_files_terminate_build 1
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 0.02
Release: alt2
Summary: Environment variables for arguments as array
Group: Development/Perl
License: perl
URL: https://metacpan.org/pod/Env::ShellWords

Source0: http://mirror.yandex.ru/mirrors/cpan/authors/id/P/PL/PLICEASE/%{module_name}-%{version}.tar.gz
BuildArch: noarch

%description
This module provides an array like interface to environment variables
that contain flags.  For example Autoconf can uses the environment
variables like `CFLAGS' or `LDFLAGS', and this allows you to manipulate
those variables without doing space quoting and other messy mucky stuff.

The intent is to use this from the alienfile manpage to deal with hierarchical
prerequisites.
%prep
%setup -q -n %{module_name}-%{version}

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc LICENSE README author.yml Changes
%perl_vendor_privlib/E*

%changelog
* Tue Jan 02 2018 Igor Vlasenko <viy@altlinux.ru> 0.02-alt2
- to Sisyphus as Alien-Build dep

* Tue Dec 26 2017 Igor Vlasenko <viy@altlinux.ru> 0.02-alt1
- regenerated from template by package builder

* Sat Feb 18 2017 Igor Vlasenko <viy@altlinux.ru> 0.01-alt1
- initial import by package builder

