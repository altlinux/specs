#define _without_test 1
# BEGIN SourceDeps(oneline):
BuildRequires: perl(DateTime.pm) perl(DateTime/Format/ISO8601.pm) perl(ExtUtils/MakeMaker.pm) perl(File/Spec.pm) perl(Geo/Calc.pm) perl(Geo/FIT.pm) perl(Geo/Gpx.pm) perl(IPC/System/Simple.pm) perl(Module/Build.pm) perl(Test/More.pm)
# END SourceDeps(oneline)
%define module_name Geo-TCX
%define _unpackaged_files_terminate_build 1
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 1.06
Release: alt1
Summary: Parse and edit and TCX activity and course files from GPS training devices
Group: Development/Perl
License: perl
URL: https://github.com/patjoly/geo-tcx

Source0: http://mirror.yandex.ru/mirrors/cpan/authors/id/P/PA/PATJOL/%{module_name}-%{version}.tar.gz
BuildArch: noarch

%description
`Geo::TCX' enables the parsing and editing of TCX activity and course files, including those from FIT files. TCX files follow an XML schema developed by Garmin and common to its GPS sports devices. Among other methods, the module enables laps from an activity to be saved as individual *.tcx files, split into separate laps based on a given point, merged, or converted to courses to plan a future activity.

FIT activity and course files are supported provided that the Geo::FIT manpage is installed and that the `fit2tcx.pl' script it provides appears on the user's path.

The module supports files containing a single Activity or Course. Database files consisting of multiple activities or courses are not supported.

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
%doc LICENSE README.md Changes
%perl_vendor_privlib/G*

%files scripts
%_bindir/*
%_man1dir/*

%changelog
* Sat Dec 24 2022 Igor Vlasenko <viy@altlinux.org> 1.06-alt1
- enabled tests

* Sat Dec 24 2022 Igor Vlasenko <viy@altlinux.org> 1.06-alt0.1
- bootstrap w/o tests; wait for Geo-Gpx > 0.08

