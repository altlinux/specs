%define module_version 0.005
%define module_name PBKDF2-Tiny
# BEGIN SourceDeps(oneline):
BuildRequires: perl(Carp.pm) perl(Config.pm) perl(Dist/Zilla/Role/MetaProvider.pm) perl(Encode.pm) perl(Encode/CN.pm) perl(Encode/JP.pm) perl(Encode/KR.pm) perl(Encode/TW.pm) perl(Exporter.pm) perl(ExtUtils/MakeMaker.pm) perl(File/Spec.pm) perl(Moose.pm) perl(Test/More.pm) perl(Text/ParseWords.pm) perl(strict.pm) perl(utf8.pm) perl(warnings.pm) perl(Digest/SHA.pm)
# END SourceDeps(oneline)
%define _unpackaged_files_terminate_build 1
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 0.005
Release: alt2
Summary: Minimalist PBKDF2 (RFC 2898) with HMAC-SHA1 or HMAC-SHA2
Group: Development/Perl
License: apache
URL: https://github.com/dagolden/PBKDF2-Tiny

Source0: http://cpan.org.ua/authors/id/D/DA/DAGOLDEN/%{module_name}-%{module_version}.tar.gz
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
%doc Changes README LICENSE
%perl_vendor_privlib/P*

%changelog
* Sat Dec 20 2014 Igor Vlasenko <viy@altlinux.ru> 0.005-alt2
- moved to Sisyphus as dependency

* Mon Nov 24 2014 Igor Vlasenko <viy@altlinux.ru> 0.005-alt1
- regenerated from template by package builder

* Wed Oct 22 2014 Igor Vlasenko <viy@altlinux.ru> 0.004-alt1
- regenerated from template by package builder

* Mon Oct 06 2014 Igor Vlasenko <viy@altlinux.ru> 0.003-alt1
- initial import by package builder

