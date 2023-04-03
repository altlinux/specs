%define _unpackaged_files_terminate_build 1
%define module_name Sub-Exporter-Lexical
# BEGIN SourceDeps(oneline):
BuildRequires: perl(B/Hooks/EndOfScope.pm) perl(ExtUtils/MakeMaker.pm) perl(Lexical/Sub.pm) perl(Sub/Exporter.pm) perl(Sub/Install.pm) perl(Test/More.pm) perl(lib.pm) perl(namespace/autoclean.pm) perl(namespace/clean.pm) perl(strict.pm) perl(warnings.pm)
# END SourceDeps(oneline)
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 1.000
Release: alt1
Summary: to export lexically-available subs with Sub::Exporter
Group: Development/Perl
License: perl
URL: https://github.com/rjbs/Sub-Exporter-Lexical

Source0: http://www.cpan.org/authors/id/R/RJ/RJBS/%{module_name}-%{version}.tar.gz
BuildArch: noarch

%description
%summary

%prep
%setup -q -n %{module_name}-%{version}

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_privlib/S*

%changelog
* Mon Apr 03 2023 Igor Vlasenko <viy@altlinux.org> 1.000-alt1
- automated CPAN update

* Wed Dec 04 2013 Igor Vlasenko <viy@altlinux.ru> 0.092292-alt2
- uploaded to Sisyphus as Scalar-Does deep dependency

* Tue Nov 26 2013 Igor Vlasenko <viy@altlinux.ru> 0.092292-alt1
- regenerated from template by package builder

* Thu Sep 26 2013 Igor Vlasenko <viy@altlinux.ru> 0.092291-alt1
- initial import by package builder

