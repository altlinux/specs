%define _unpackaged_files_terminate_build 1
# BEGIN SourceDeps(oneline):
BuildRequires: perl(Carp.pm) perl(Crypt/CBC.pm) perl(Crypt/Rijndael.pm) perl(Crypt/URandom.pm) perl(Digest/SHA.pm) perl(ExtUtils/MakeMaker.pm) perl(File/Find.pm) perl(File/Spec/Functions.pm) perl(File/Temp.pm) perl(List/Util.pm) perl(MIME/Base64.pm) perl(Math/Random/ISAAC/XS.pm) perl(Moo.pm) perl(MooX/Types/MooseLike/Base.pm) perl(Sereal/Decoder.pm) perl(Sereal/Encoder.pm) perl(String/Compare/ConstantTime.pm) perl(Test/Deep.pm) perl(Test/Fatal.pm) perl(Test/More.pm) perl(Test/Tolerant.pm) perl(namespace/clean.pm) perl(strict.pm) perl(warnings.pm)
# END SourceDeps(oneline)
%define module_name Session-Storage-Secure
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 0.011
Release: alt1
Summary: Encrypted, expiring, compressed, serialized session data with integrity
Group: Development/Perl
License: apache
URL: https://metacpan.org/release/Session-Storage-Secure

Source0: http://www.cpan.org/authors/id/D/DA/DAGOLDEN/%{module_name}-%{version}.tar.gz
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
%doc README LICENSE Changes
%perl_vendor_privlib/S*

%changelog
* Wed Apr 25 2018 Igor Vlasenko <viy@altlinux.ru> 0.011-alt1
- automated CPAN update

* Tue May 13 2014 Igor Vlasenko <viy@altlinux.ru> 0.010-alt1
- automated CPAN update

* Tue Apr 22 2014 Igor Vlasenko <viy@altlinux.ru> 0.009-alt1
- automated CPAN update

* Wed Oct 16 2013 Igor Vlasenko <viy@altlinux.ru> 0.007-alt1
- build for Sisyphus (required for perl update)

