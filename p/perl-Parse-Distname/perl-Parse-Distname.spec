%define module_name Parse-Distname
# BEGIN SourceDeps(oneline):
BuildRequires: perl(Exporter.pm) perl(ExtUtils/MakeMaker.pm) perl(ExtUtils/MakeMaker/CPANfile.pm) perl(JSON/PP.pm) perl(Test/Differences.pm) perl(Test/More.pm) perl(Test/UseAllModules.pm)
# END SourceDeps(oneline)
%define _unpackaged_files_terminate_build 1
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 0.05
Release: alt2
Summary: parse a distribution name
Group: Development/Perl
License: perl
Url: %CPAN %module_name

Source0: http://mirror.yandex.ru/mirrors/cpan/authors/id/I/IS/ISHIGAKI/%{module_name}-%{version}.tar.gz
BuildArch: noarch

%description
Parse::Distname is yet another distribution name parser. It works
almost the same as the CPAN::DistnameInfo manpage, but Parse::Distname takes
a different approach. It tries to extract a version part of a
distribution and treat the rest as a distribution name, contrary to
CPAN::DistnameInfo which tries to define a name part and treat
the rest as a version.

Because of this difference, when Parse::Distname parses a weird
distribution name such as "AUTHOR/v1.0.tar.gz", it says the name
is empty and the version is "v1.0", while CPAN::DistnameInfo
says the name is "v" and the version is "1.0". See test files
in this distribution if you need more details. As of this writing,
Parse::Distname returns a different result for about 200+
distributions among about 320000 BackPan distributions.

%prep
%setup -q -n %{module_name}-%{version}

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README Changes LICENSE
%perl_vendor_privlib/P*

%changelog
* Fri Apr 08 2022 Igor Vlasenko <viy@altlinux.org> 0.05-alt2
- to Sisyphus as Perl-PrereqScanner-NotQuiteLite dep

* Mon Sep 30 2019 Igor Vlasenko <viy@altlinux.ru> 0.05-alt1
- updated by package builder

* Sat Aug 10 2019 Igor Vlasenko <viy@altlinux.ru> 0.04-alt1
- updated by package builder

* Tue Nov 20 2018 Igor Vlasenko <viy@altlinux.ru> 0.03-alt1
- regenerated from template by package builder

* Thu Nov 15 2018 Igor Vlasenko <viy@altlinux.ru> 0.02-alt1
- initial import by package builder

