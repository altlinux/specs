# BEGIN SourceDeps(oneline):
BuildRequires: perl(Exporter.pm) perl(ExtUtils/MakeMaker.pm) perl(Lingua/EN/FindNumber.pm) perl(Test/Fatal.pm) perl(Test/More.pm) perl(Try/Tiny.pm)
# END SourceDeps(oneline)
%define module_version 0.05
%define module_name Lingua-EN-Number-IsOrdinal
%define _unpackaged_files_terminate_build 1
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 0.05
Release: alt1
Summary: detect if English number is ordinal or cardinal
Group: Development/Perl
License: perl
URL: http://metacpan.org/release/Lingua-EN-Number-IsOrdinal

Source: http://www.cpan.org/authors/id/R/RK/RKITOVER/Lingua-EN-Number-IsOrdinal-%{version}.tar.gz
BuildArch: noarch

%description
%summary

%prep
%setup -n %module_name-%module_version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README LICENSE Changes
%perl_vendor_privlib/L*

%changelog
* Wed Apr 01 2015 Igor Vlasenko <viy@altlinux.ru> 0.05-alt1
- automated CPAN update

* Wed Sep 18 2013 Igor Vlasenko <viy@altlinux.ru> 0.04-alt2
- regenerated from template by package builder

* Wed Sep 04 2013 Igor Vlasenko <viy@altlinux.ru> 0.04-alt1
- initial import by package builder

