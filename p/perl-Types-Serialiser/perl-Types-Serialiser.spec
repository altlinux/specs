# BEGIN SourceDeps(oneline):
BuildRequires: perl(Carp.pm) perl(ExtUtils/MakeMaker.pm) perl(common/sense.pm) perl(overload.pm)
# END SourceDeps(oneline)
%define module_version 0.03
%define module_name Types-Serialiser
%define _unpackaged_files_terminate_build 1
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 0.03
Release: alt1
Summary: simple data types for common serialisation formats
Group: Development/Perl
License: perl
Url: %CPAN %module_name

Source0: http://cpan.org.ua/authors/id/M/ML/MLEHMANN/%module_name-%module_version.tar.gz
BuildArch: noarch

%description
This module provides some extra datatypes that are used by common
serialisation formats such as JSON or CBOR. The idea is to have a
repository of simple/small constants and containers that can be shared by
different implementations so they become interoperable between each other.


%prep
%setup -n %module_name-%module_version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README COPYING
%perl_vendor_privlib/T*

%changelog
* Fri Nov 01 2013 Igor Vlasenko <viy@altlinux.ru> 0.03-alt1
- initial import by package builder

