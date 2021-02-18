%define module_name HTTP-Tiny-Mech
# BEGIN SourceDeps(oneline):
BuildRequires: perl(ExtUtils/MakeMaker.pm) perl(File/Spec.pm) perl(HTTP/Request.pm) perl(HTTP/Response.pm) perl(HTTP/Tiny.pm) perl(Test/More.pm) perl(WWW/Mechanize.pm) perl(lib.pm) perl(parent.pm) perl(strict.pm) perl(warnings.pm)
# END SourceDeps(oneline)
%define _unpackaged_files_terminate_build 1
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 1.001002
Release: alt2
Summary: Wrap a WWW::Mechanize instance in an HTTP::Tiny compatible interface.
Group: Development/Perl
License: perl
URL: https://github.com/kentnl/HTTP-Tiny-Mech

Source0: http://mirror.yandex.ru/mirrors/cpan/authors/id/K/KE/KENTNL/%{module_name}-%{version}.tar.gz
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
%doc README Changes LICENSE
%perl_vendor_privlib/H*

%changelog
* Thu Feb 18 2021 Igor Vlasenko <viy@altlinux.org> 1.001002-alt2
- to Sisyphus as MetaCPAN-Client dep

* Tue Mar 14 2017 Igor Vlasenko <viy@altlinux.ru> 1.001002-alt1
- regenerated from template by package builder

* Fri Sep 05 2014 Igor Vlasenko <viy@altlinux.ru> 1.001001-alt1
- regenerated from template by package builder

* Mon Jun 23 2014 Igor Vlasenko <viy@altlinux.ru> 1.000000-alt1
- regenerated from template by package builder

* Tue Nov 26 2013 Igor Vlasenko <viy@altlinux.ru> 0.2.1-alt1
- regenerated from template by package builder

* Mon Oct 07 2013 Igor Vlasenko <viy@altlinux.ru> 0.1.3-alt1
- initial import by package builder

