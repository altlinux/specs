%define _unpackaged_files_terminate_build 1
%define module_name Geo-FIT
# BEGIN SourceDeps(oneline):
BuildRequires: perl(ExtUtils/MakeMaker.pm) perl(File/Spec.pm) perl(HTML/Entities.pm) perl(IPC/System/Simple.pm) perl(Math/BigInt.pm) perl(Module/Build.pm) perl(Test/More.pm)
# END SourceDeps(oneline)
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 1.05
Release: alt1
Summary: Decode Garmin FIT files
Group: Development/Perl
License: perl
URL: https://github.com/patjoly/geo-fit

Source0: http://www.cpan.org/authors/id/P/PA/PATJOL/%{module_name}-%{version}.tar.gz
BuildArch: noarch

%description
`Geo::FIT' is a Perl class to provide interfaces to decode Garmin FIT files (*.fit).

The module also provides a script to read and print the contents for FIT files (`fitdump.pl'), as well as a script to convert FIT files to TCX files (`fit2tcx.pl').

%package scripts
Summary: %module_name scripts
Group: Development/Perl
Requires: %name = %EVR

%description scripts
scripts for %module_name

%prep
%setup -q -n %{module_name}-%{version}

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README.md
%perl_vendor_privlib/G*

%files scripts
%_man1dir/*
%_bindir/*

%changelog
* Mon Mar 20 2023 Igor Vlasenko <viy@altlinux.org> 1.05-alt1
- automated CPAN update

* Sat Dec 24 2022 Igor Vlasenko <viy@altlinux.org> 1.04-alt2
- to Sisyphus as Geo-GPX dependency

* Wed Dec 14 2022 Igor Vlasenko <viy@altlinux.org> 1.04-alt1
- updated by package builder

* Tue Dec 06 2022 Igor Vlasenko <viy@altlinux.org> 1.03-alt1
- initial import by package builder

