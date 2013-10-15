%define module_version 0.34
%define module_name Crypt-URandom
# BEGIN SourceDeps(oneline):
BuildRequires: perl(Carp.pm) perl(Encode.pm) perl(English.pm) perl(Exporter.pm) perl(ExtUtils/MakeMaker.pm) perl(FileHandle.pm) perl(Module/Build.pm) perl(Test/More.pm)
# END SourceDeps(oneline)
%define _unpackaged_files_terminate_build 1
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 0.34
Release: alt2
Summary: Provide non blocking randomness
Group: Development/Perl
License: perl
Url: %CPAN %module_name

Source0: http://cpan.org.ua/authors/id/D/DD/DDICK/%module_name-%module_version.tar.gz
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
%doc README Changes
%perl_vendor_privlib/C*

%changelog
* Wed Oct 16 2013 Igor Vlasenko <viy@altlinux.ru> 0.34-alt2
- build for Sisyphus (required for perl update)

* Thu Sep 19 2013 Igor Vlasenko <viy@altlinux.ru> 0.34-alt1
- initial import by package builder

