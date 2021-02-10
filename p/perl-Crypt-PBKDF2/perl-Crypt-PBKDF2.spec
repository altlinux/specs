%define module_version 0.161520
%define module_name Crypt-PBKDF2
# BEGIN SourceDeps(oneline):
BuildRequires: perl(Carp.pm) perl(Digest.pm) perl(Digest/HMAC.pm) perl(Digest/SHA.pm) perl(Digest/SHA3.pm) perl(Encode.pm) perl(Encode/CN.pm) perl(Encode/JP.pm) perl(Encode/KR.pm) perl(Encode/TW.pm) perl(ExtUtils/MakeMaker.pm) perl(MIME/Base64.pm) perl(Module/Runtime.pm) perl(Moo.pm) perl(Moo/Role.pm) perl(Scalar/Util.pm) perl(Test/Fatal.pm) perl(Test/More.pm) perl(Try/Tiny.pm) perl(Type/Tiny.pm) perl(Types/Standard.pm) perl(constant.pm) perl(namespace/autoclean.pm) perl(strict.pm) perl(strictures.pm) perl(warnings.pm)
# END SourceDeps(oneline)
%define _unpackaged_files_terminate_build 1
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 0.161520
Release: alt2
Summary: The PBKDF2 password hash algorithm
Group: Development/Perl
License: perl
URL: http://metacpan.org/release/Crypt-PBKDF2

Source0: http://mirror.yandex.ru/mirrors/cpan/authors/id/A/AR/ARODLAND/%{module_name}-%{module_version}.tar.gz
BuildArch: noarch

%description
%summary

%prep
%setup -q -n %{module_name}-%{module_version}

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc LICENSE Changes
%perl_vendor_privlib/C*

%changelog
* Wed Feb 10 2021 Igor Vlasenko <viy@altlinux.ru> 0.161520-alt2
- to Sisyphus as Crypt-CBC dep

* Thu Jun 09 2016 Igor Vlasenko <viy@altlinux.ru> 0.161520-alt1
- regenerated from template by package builder

* Fri Feb 19 2016 Igor Vlasenko <viy@altlinux.ru> 0.160410-alt1
- regenerated from template by package builder

* Thu Apr 02 2015 Igor Vlasenko <viy@altlinux.ru> 0.150900-alt1
- regenerated from template by package builder

* Fri Sep 05 2014 Igor Vlasenko <viy@altlinux.ru> 0.142390-alt1
- regenerated from template by package builder

* Tue Apr 01 2014 Igor Vlasenko <viy@altlinux.ru> 0.140890-alt1
- regenerated from template by package builder

* Mon Dec 02 2013 Igor Vlasenko <viy@altlinux.ru> 0.133330-alt1
- regenerated from template by package builder

* Tue Sep 03 2013 Igor Vlasenko <viy@altlinux.ru> 0.131750-alt1
- initial import by package builder

