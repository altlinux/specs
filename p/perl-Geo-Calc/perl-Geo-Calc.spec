# BEGIN SourceDeps(oneline):
BuildRequires: perl(ExtUtils/MakeMaker.pm) perl(Math/BigFloat.pm) perl(Math/BigInt.pm) perl(Math/Trig.pm) perl(Math/Units.pm) perl(Moose.pm) perl(MooseX/FollowPBP.pm) perl(MooseX/Method/Signatures.pm) perl(Test/More.pm)
# END SourceDeps(oneline)
%define module_version 0.12
%define module_name Geo-Calc
%define _unpackaged_files_terminate_build 1
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 0.12
Release: alt2
Summary: Geographical Calc
Group: Development/Perl
License: perl
Url: %CPAN %module_name

Source0: http://cpan.org.ua/authors/id/A/AS/ASP/%module_name-%module_version.tar.gz
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
%doc README ChangeLog
%perl_vendor_privlib/G*

%changelog
* Sat Oct 08 2022 Igor Vlasenko <viy@altlinux.org> 0.12-alt2
- to Sisyphus as perl-Geo-Gpx dep

* Thu Sep 19 2013 Igor Vlasenko <viy@altlinux.ru> 0.12-alt1
- initial import by package builder

