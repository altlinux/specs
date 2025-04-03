%define module_name Set-Tiny
# BEGIN SourceDeps(oneline):
BuildRequires: perl(Exporter.pm) perl(ExtUtils/MakeMaker.pm) perl(Test/More.pm)
# END SourceDeps(oneline)
%define _unpackaged_files_terminate_build 1
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 0.06
Release: alt1
Summary: Simple sets of strings
Group: Development/Perl
License: perl
Url: %CPAN %module_name

Source0: http://www.cpan.org/authors/id/H/HA/HAARG/%{module_name}-%{version}.tar.gz
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
%doc README Changes examples
%perl_vendor_privlib/S*

%changelog
* Thu Apr 03 2025 Igor Vlasenko <viy@altlinux.org> 0.06-alt1
- automated CPAN update

* Tue Jan 31 2017 Igor Vlasenko <viy@altlinux.ru> 0.04-alt2
- to Sisyphus

* Sat Mar 19 2016 Igor Vlasenko <viy@altlinux.ru> 0.04-alt1
- regenerated from template by package builder

* Thu Oct 15 2015 Igor Vlasenko <viy@altlinux.ru> 0.03-alt1
- regenerated from template by package builder

* Wed Oct 08 2014 Igor Vlasenko <viy@altlinux.ru> 0.02-alt1
- regenerated from template by package builder

* Tue Sep 10 2013 Igor Vlasenko <viy@altlinux.ru> 0.01-alt1
- initial import by package builder

