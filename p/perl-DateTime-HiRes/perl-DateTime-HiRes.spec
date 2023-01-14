%define module_name DateTime-HiRes
# BEGIN SourceDeps(oneline):
BuildRequires: perl(DateTime.pm) perl(ExtUtils/MakeMaker.pm) perl(File/Spec.pm) perl(Test/More.pm) perl(Time/HiRes.pm) perl(strict.pm) perl(warnings.pm)
# END SourceDeps(oneline)
%define _unpackaged_files_terminate_build 1
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 0.04
Release: alt2
Summary: perl module %module_name
Group: Development/Perl
License: perl
URL: https://metacpan.org/release/DateTime-HiRes

Source0: http://mirror.yandex.ru/mirrors/cpan/authors/id/D/DR/DROLSKY/%{module_name}-%{version}.tar.gz
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
%doc Todo CONTRIBUTING.md README.md Changes LICENSE CODE_OF_CONDUCT.md
%perl_vendor_privlib/D*

%changelog
* Sun Jan 15 2023 Igor Vlasenko <viy@altlinux.org> 0.04-alt2
- to Sisyphus as perl-DateTime-Format-Natural dep

* Wed Jul 29 2020 Igor Vlasenko <viy@altlinux.ru> 0.04-alt1
- updated by package builder

* Thu Sep 19 2013 Igor Vlasenko <viy@altlinux.ru> 0.01-alt1
- initial import by package builder

