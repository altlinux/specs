%define _unpackaged_files_terminate_build 1
# BEGIN SourceDeps(oneline):
BuildRequires: perl(Crypt/URandom.pm) perl(Exporter.pm) perl(ExtUtils/MakeMaker.pm) perl(File/Spec.pm) perl(Test/More.pm) perl(strict.pm) perl(warnings.pm)
# END SourceDeps(oneline)
%define module_name UUID-URandom
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 0.001
Release: alt2
Summary: UUIDs based on /dev/urandom or the Windows Crypto API
Group: Development/Perl
License: apache
URL: https://github.com/dagolden/UUID-URandom

Source0: http://mirror.yandex.ru/mirrors/cpan/authors/id/D/DA/DAGOLDEN/%{module_name}-%{version}.tar.gz
BuildArch: noarch

%description
This module provides a portable, secure generator of
RFC-4122 version 4
(random) UUIDs.  It is a thin wrapper around the Crypt::URandom manpage to set
the UUID version and variant bits required by the RFC.

%prep
%setup -q -n %{module_name}-%{version}

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes LICENSE README
%perl_vendor_privlib/U*

%changelog
* Fri Jun 29 2018 Igor Vlasenko <viy@altlinux.ru> 0.001-alt2
- to Sisyphus as perl-MongoDB dep

* Wed Apr 04 2018 Igor Vlasenko <viy@altlinux.ru> 0.001-alt1
- initial import by package builder

