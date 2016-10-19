%define module_version 1.100
%define module_name Authen-SASL-SASLprep
# BEGIN SourceDeps(oneline):
BuildRequires: perl(Exporter.pm) perl(ExtUtils/MakeMaker.pm) perl(Module/Build.pm) perl(Test/More.pm) perl(Test/NoWarnings.pm) perl(Unicode/Stringprep.pm) perl(Unicode/Stringprep/Mapping.pm) perl(Unicode/Stringprep/Prohibited.pm)
# END SourceDeps(oneline)
%define _unpackaged_files_terminate_build 1
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 1.100
Release: alt1
Summary: A Stringprep Profile for User Names and Passwords (RFC 4013)
Group: Development/Perl
License: perl
Url: %CPAN %module_name

Source: http://www.cpan.org/authors/id/C/CF/CFAERBER/Authen-SASL-SASLprep-%{version}.tar.gz
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
%doc README Changes LICENSE
%perl_vendor_privlib/A*

%changelog
* Wed Oct 19 2016 Igor Vlasenko <viy@altlinux.ru> 1.100-alt1
- automated CPAN update

* Wed Oct 14 2015 Igor Vlasenko <viy@altlinux.ru> 1.011-alt1
- regenerated from template by package builder

* Sat Dec 20 2014 Igor Vlasenko <viy@altlinux.ru> 1.01-alt2
- moved to Sisyphus as dependency

* Thu Sep 19 2013 Igor Vlasenko <viy@altlinux.ru> 1.01-alt1
- initial import by package builder

