%define module_name AnyEvent-XSPromises
# BEGIN SourceDeps(oneline):
BuildRequires: libsowing-devel perl(AnyEvent.pm) perl(Exporter.pm) perl(ExtUtils/MakeMaker.pm) perl(XSLoader.pm)
# END SourceDeps(oneline)
%define _unpackaged_files_terminate_build 1
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 0.003
Release: alt2
Summary: Another Promises library, this time implemented in XS for performance
Group: Development/Perl
License: perl
Url: %CPAN %module_name

Source0: http://mirror.yandex.ru/mirrors/cpan/authors/id/T/TV/TVDW/%{module_name}-%{version}.tar.gz

%description
This library provides a Promises interface, written in XS for performance, conforming to the Promises/A+ specification.

Performance may not immediately seem important, but when promises are used as the building block for sending thousands
of database queries per second from a single Perl process, those extra microseconds suddenly start to matter.

%prep
%setup -q -n %{module_name}-%{version}

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes
%perl_vendor_archlib/A*
%perl_vendor_autolib/*

%changelog
* Thu Feb 14 2019 Igor Vlasenko <viy@altlinux.ru> 0.003-alt2
- to Sisyphus as perl-Cassandra-Client dep

* Sat Feb 09 2019 Igor Vlasenko <viy@altlinux.ru> 0.003-alt1
- regenerated from template by package builder

* Fri Feb 08 2019 Igor Vlasenko <viy@altlinux.ru> 0.002-alt1
- initial import by package builder

