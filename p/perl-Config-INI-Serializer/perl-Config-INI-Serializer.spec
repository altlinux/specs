%define module_version 0.002
%define module_name Config-INI-Serializer
# BEGIN SourceDeps(oneline):
BuildRequires: perl(Data/Dumper.pm) perl(ExtUtils/MakeMaker.pm) perl(File/Spec.pm) perl(IO/Handle.pm) perl(IPC/Open3.pm) perl(Pod/Coverage/TrustPod.pm) perl(Test/Deep.pm) perl(Test/EOL.pm) perl(Test/More.pm) perl(Test/NoTabs.pm) perl(Test/Pod.pm) perl(Test/Pod/Coverage.pm) perl(blib.pm) perl(strict.pm) perl(warnings.pm)
# END SourceDeps(oneline)
%define _unpackaged_files_terminate_build 1
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 0.002
Release: alt2
Summary: Round-trip INI serializer for nested data
Group: Development/Perl
License: perl
URL: http://metacpan.org/release/Config-INI-Serializer

Source0: http://cpan.org.ua/authors/id/S/SC/SCHWIGON/%{module_name}-%{module_version}.tar.gz
BuildArch: noarch

%description
%summary

%prep
%setup -n %{module_name}-%{module_version}

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes LICENSE README
%perl_vendor_privlib/C*

%changelog
* Mon Mar 21 2016 Igor Vlasenko <viy@altlinux.ru> 0.002-alt2
- to Sisyphus

* Wed Oct 14 2015 Igor Vlasenko <viy@altlinux.ru> 0.002-alt1
- regenerated from template by package builder

* Tue Sep 03 2013 Igor Vlasenko <viy@altlinux.ru> 0.001-alt1
- initial import by package builder

