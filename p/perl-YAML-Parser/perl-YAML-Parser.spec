# internal virtual
%filter_from_requires /^perl.PerlYamlReferenceParser/d
# BEGIN SourceDeps(oneline):
BuildRequires: perl(Encode.pm) perl(ExtUtils/MakeMaker.pm) perl(JSON/PP.pm) perl(Test/Pod.pm) perl(XXX.pm) perl(YAML/PP.pm) perl(boolean.pm)
# END SourceDeps(oneline)
%define module_name YAML-Parser
%define _unpackaged_files_terminate_build 1
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 0.0.5
Release: alt1
Summary: Generated Reference Parser for YAML 1.2
Group: Development/Perl
License: perl
URL: https://github.com/ingydotnet/yaml-parser-pm

Source0: http://cpan.org.ua/authors/id/I/IN/INGY/%{module_name}-%{version}.tar.gz
BuildArch: noarch

%description
YAML::Parser is the first 100%% YAML 1.2 spec compliant parser for Perl. The
Perl code is generated directly from the YAML 1.2 specification.

%prep
%setup -q -n %{module_name}-%{version}

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc LICENSE README Changes CONTRIBUTING
%perl_vendor_privlib/Y*

%changelog
* Fri Mar 25 2022 Igor Vlasenko <viy@altlinux.org> 0.0.5-alt1
- initial import by package builder

