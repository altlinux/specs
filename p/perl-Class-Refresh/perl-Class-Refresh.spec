%define module_version 0.05
%define module_name Class-Refresh
# BEGIN SourceDeps(oneline):
BuildRequires: perl(B.pm) perl(Class/Load.pm) perl(Class/Unload.pm) perl(Devel/OverrideGlobalRequire.pm) perl(Exporter.pm) perl(ExtUtils/MakeMaker.pm) perl(File/Copy.pm) perl(File/Find.pm) perl(File/Temp.pm) perl(Moose.pm) perl(Moose/Role.pm) perl(Test/Fatal.pm) perl(Test/More.pm) perl(Test/Requires.pm) perl(Try/Tiny.pm) perl(strict.pm) perl(warnings.pm)
# END SourceDeps(oneline)
%define _unpackaged_files_terminate_build 1
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 0.05
Release: alt2
Summary: refresh your classes during runtime
Group: Development/Perl
License: perl
URL: http://metacpan.org/release/Class-Refresh

Source0: http://cpan.org.ua/authors/id/D/DO/DOY/%module_name-%module_version.tar.gz
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
%doc LICENSE Changes README
%perl_vendor_privlib/C*

%changelog
* Wed Dec 04 2013 Igor Vlasenko <viy@altlinux.ru> 0.05-alt2
- uploaded to Sisyphus as Scalar-Does dependency

* Thu Sep 19 2013 Igor Vlasenko <viy@altlinux.ru> 0.05-alt1
- initial import by package builder

