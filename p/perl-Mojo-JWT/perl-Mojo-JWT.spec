%define module_name Mojo-JWT
# BEGIN SourceDeps(oneline):
BuildRequires: perl(Crypt/OpenSSL/Bignum.pm) perl(Crypt/OpenSSL/RSA.pm) perl(Digest/SHA.pm) perl(MIME/Base64.pm) perl(Module/Build/Tiny.pm) perl(Mojolicious.pm)
# END SourceDeps(oneline)
%define _unpackaged_files_terminate_build 1
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 0.09
Release: alt2
Summary: JSON Web Token the Mojo way
Group: Development/Perl
License: perl
Url: %CPAN %module_name

Source0: http://mirror.yandex.ru/mirrors/cpan/authors/id/J/JB/JBERGER/%{module_name}-%{version}.tar.gz
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
%perl_vendor_privlib/M*

%changelog
* Mon Nov 01 2021 Igor Vlasenko <viy@altlinux.org> 0.09-alt2
- to Sisyphus for Mojolicious-Plugin-OAuth2

* Sun Nov 22 2020 Igor Vlasenko <viy@altlinux.ru> 0.09-alt1
- updated by package builder

* Fri Jan 18 2019 Igor Vlasenko <viy@altlinux.ru> 0.08-alt1
- regenerated from template by package builder

* Fri Jan 13 2017 Igor Vlasenko <viy@altlinux.ru> 0.05-alt1
- regenerated from template by package builder

* Fri May 22 2015 Igor Vlasenko <viy@altlinux.ru> 0.04-alt1
- initial import by package builder

