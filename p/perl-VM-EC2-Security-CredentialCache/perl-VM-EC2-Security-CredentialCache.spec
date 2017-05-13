%define module_name VM-EC2-Security-CredentialCache
# BEGIN SourceDeps(oneline):
BuildRequires: perl(DateTime/Format/ISO8601.pm) perl(ExtUtils/MakeMaker.pm) perl(Test/More.pm) perl(VM/EC2/Instance/Metadata.pm) perl(lib.pm) perl(strict.pm) perl(warnings.pm)
# END SourceDeps(oneline)
%define _unpackaged_files_terminate_build 1
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 0.25
Release: alt2
Summary: Cache credentials respecting expriation time for IAM roles.
Group: Development/Perl
License: perl
URL: http://search.cpan.org/dist/VM-EC2-Security-CredentialCache/

Source0: http://mirror.yandex.ru/mirrors/cpan/authors/id/R/RC/RCONOVER/%{module_name}-%{version}.tar.gz
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
%doc LICENSE README CHANGES
%perl_vendor_privlib/V*

%changelog
* Sat May 13 2017 Igor Vlasenko <viy@altlinux.ru> 0.25-alt2
- to Sisyphus

* Thu Oct 15 2015 Igor Vlasenko <viy@altlinux.ru> 0.25-alt1
- regenerated from template by package builder

* Mon Jan 19 2015 Igor Vlasenko <viy@altlinux.ru> 0.21-alt1
- regenerated from template by package builder

* Mon Jan 05 2015 Igor Vlasenko <viy@altlinux.ru> 0.20-alt1
- regenerated from template by package builder

* Wed Oct 22 2014 Igor Vlasenko <viy@altlinux.ru> 0.18-alt1
- regenerated from template by package builder

* Thu Oct 16 2014 Igor Vlasenko <viy@altlinux.ru> 0.12-alt1
- regenerated from template by package builder

* Wed Oct 15 2014 Igor Vlasenko <viy@altlinux.ru> 0.001-alt1
- initial import by package builder

