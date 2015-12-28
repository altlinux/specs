%define module_version 0.10
%define module_name JSON-WebToken
# BEGIN SourceDeps(oneline):
BuildRequires: perl(Carp.pm) perl(Crypt/OpenSSL/RSA.pm) perl(Digest/SHA.pm) perl(Exporter.pm) perl(JSON.pm) perl(MIME/Base64.pm) perl(Module/Build.pm) perl(Module/Runtime.pm) perl(Test/Mock/Guard.pm) perl(Test/More.pm) perl(Test/Requires.pm) perl(overload.pm) perl(parent.pm)
# END SourceDeps(oneline)
%define _unpackaged_files_terminate_build 1
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 0.10
Release: alt2
Summary: JSON Web Token (JWT) implementation
Group: Development/Perl
License: perl
URL: https://github.com/xaicron/p5-JSON-WebToken

Source0: http://cpan.org.ua/authors/id/X/XA/XAICRON/%{module_name}-%{module_version}.tar.gz
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
%doc README.md LICENSE Changes
%perl_vendor_privlib/J*

%changelog
* Mon Dec 28 2015 Lenar Shakirov <snejok@altlinux.ru> 0.10-alt2
- build for Sisyphus

* Thu Apr 02 2015 Igor Vlasenko <viy@altlinux.ru> 0.10-alt1
- regenerated from template by package builder

* Mon Dec 22 2014 Igor Vlasenko <viy@altlinux.ru> 0.09-alt1
- regenerated from template by package builder

* Mon Feb 24 2014 Igor Vlasenko <viy@altlinux.ru> 0.08-alt1
- regenerated from template by package builder

* Thu Sep 26 2013 Igor Vlasenko <viy@altlinux.ru> 0.07-alt1
- initial import by package builder

