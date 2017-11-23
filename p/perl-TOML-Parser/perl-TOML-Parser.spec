%define _unpackaged_files_terminate_build 1
%define module_name TOML-Parser
# BEGIN SourceDeps(oneline):
BuildRequires: perl(Benchmark.pm) perl(CPAN/Meta.pm) perl(CPAN/Meta/Prereqs.pm) perl(Encode.pm) perl(Exporter.pm) perl(JSON.pm) perl(MIME/Base64.pm) perl(Module/Build.pm) perl(Path/Tiny.pm) perl(Storable.pm) perl(TOML.pm) perl(Test/More.pm) perl(Types/Serialiser.pm) perl(constant.pm) perl(parent.pm) perl(Module/Build/Tiny.pm) perl(Test/Deep.pm) perl(Test/Deep/Fuzzy.pm)
# END SourceDeps(oneline)
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 0.91
Release: alt1
Summary: simple toml parser
Group: Development/Perl
License: perl
URL: https://github.com/karupanerura/TOML-Parser

Source0: http://www.cpan.org/authors/id/K/KA/KARUPA/%{module_name}-%{version}.tar.gz
BuildArch: noarch

%description
From summary: %summary

%prep
%setup -q -n %{module_name}-%{version}

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc LICENSE Changes README.md
%perl_vendor_privlib/T*

%changelog
* Thu Nov 23 2017 Igor Vlasenko <viy@altlinux.ru> 0.91-alt1
- automated CPAN update

* Mon Oct 02 2017 Igor Vlasenko <viy@altlinux.ru> 0.90-alt1
- automated CPAN update

* Tue May 09 2017 Igor Vlasenko <viy@altlinux.ru> 0.10-alt1
- automated CPAN update

* Thu Nov 17 2016 Igor Vlasenko <viy@altlinux.ru> 0.08-alt1
- automated CPAN update

* Thu Apr 07 2016 Igor Vlasenko <viy@altlinux.ru> 0.07-alt1
- automated CPAN update

* Mon Dec 07 2015 Igor Vlasenko <viy@altlinux.ru> 0.06-alt1
- automated CPAN update

* Wed Apr 01 2015 Igor Vlasenko <viy@altlinux.ru> 0.05-alt1
- automated CPAN update

* Mon Oct 20 2014 Igor Vlasenko <viy@altlinux.ru> 0.04-alt1
- automated CPAN update

* Wed Jun 25 2014 Igor Vlasenko <viy@altlinux.ru> 0.03-alt2
- moved to Sisyphus as dependency

* Mon Jun 23 2014 Igor Vlasenko <viy@altlinux.ru> 0.03-alt1
- regenerated from template by package builder

* Tue May 20 2014 Igor Vlasenko <viy@altlinux.ru> 0.01-alt1
- initial import by package builder

