%define module_name Authen-SCRAM
# BEGIN SourceDeps(oneline):
BuildRequires: perl(Authen/SASL/SASLprep.pm) perl(Carp.pm) perl(Crypt/URandom.pm) perl(Encode.pm) perl(Encode/CN.pm) perl(Encode/JP.pm) perl(Encode/KR.pm) perl(Encode/TW.pm) perl(Exporter.pm) perl(ExtUtils/MakeMaker.pm) perl(File/Spec.pm) perl(MIME/Base64.pm) perl(Moo.pm) perl(Moo/Role.pm) perl(PBKDF2/Tiny.pm) perl(String/Compare/ConstantTime.pm) perl(Test/FailWarnings.pm) perl(Test/Fatal.pm) perl(Test/More.pm) perl(Try/Tiny.pm) perl(Types/Standard.pm) perl(base.pm) perl(lib.pm) perl(namespace/clean.pm) perl(strict.pm) perl(warnings.pm) perl(Digest/SHA.pm)
# END SourceDeps(oneline)
%define _unpackaged_files_terminate_build 1
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 0.006
Release: alt1
Summary: Salted Challenge Response Authentication Mechanism (RFC 5802)
Group: Development/Perl
License: apache
URL: https://github.com/dagolden/Authen-SCRAM

Source0: http://www.cpan.org/authors/id/D/DA/DAGOLDEN/%{module_name}-%{version}.tar.gz
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
%doc LICENSE Changes README
%perl_vendor_privlib/A*

%changelog
* Thu Nov 23 2017 Igor Vlasenko <viy@altlinux.ru> 0.006-alt1
- automated CPAN update

* Sat Dec 20 2014 Igor Vlasenko <viy@altlinux.ru> 0.005-alt2
- moved to Sisyphus as dependency

* Wed Oct 22 2014 Igor Vlasenko <viy@altlinux.ru> 0.005-alt1
- regenerated from template by package builder

* Wed Oct 15 2014 Igor Vlasenko <viy@altlinux.ru> 0.004-alt1
- initial import by package builder

