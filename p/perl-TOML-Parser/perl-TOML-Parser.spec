%define module_version 0.03
%define module_name TOML-Parser
# BEGIN SourceDeps(oneline):
BuildRequires: perl(Benchmark.pm) perl(CPAN/Meta.pm) perl(CPAN/Meta/Prereqs.pm) perl(Encode.pm) perl(Exporter.pm) perl(JSON.pm) perl(MIME/Base64.pm) perl(Module/Build.pm) perl(Path/Tiny.pm) perl(Storable.pm) perl(TOML.pm) perl(Test/More.pm) perl(Types/Serialiser.pm) perl(constant.pm) perl(parent.pm)
# END SourceDeps(oneline)
%define _unpackaged_files_terminate_build 1
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 0.03
Release: alt2
Summary: simple toml parser
Group: Development/Perl
License: perl
URL: https://github.com/karupanerura/TOML-Parser

Source0: http://cpan.org.ua/authors/id/K/KA/KARUPA/%{module_name}-%{module_version}.tar.gz
BuildArch: noarch

%description
From summary: %summary

%prep
%setup -n %{module_name}-%{module_version}

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc LICENSE Changes README.md
%perl_vendor_privlib/T*

%changelog
* Wed Jun 25 2014 Igor Vlasenko <viy@altlinux.ru> 0.03-alt2
- moved to Sisyphus as dependency

* Mon Jun 23 2014 Igor Vlasenko <viy@altlinux.ru> 0.03-alt1
- regenerated from template by package builder

* Tue May 20 2014 Igor Vlasenko <viy@altlinux.ru> 0.01-alt1
- initial import by package builder

