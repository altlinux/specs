%define module_version 0.06
%define module_name Regexp-Stringify
# BEGIN SourceDeps(oneline):
BuildRequires: perl(Exporter.pm) perl(ExtUtils/MakeMaker.pm) perl(File/Spec.pm) perl(IO/Handle.pm) perl(IPC/Open3.pm) perl(Pod/Coverage/TrustPod.pm) perl(Test/More.pm) perl(Test/Pod.pm) perl(Test/Pod/Coverage.pm) perl(re.pm) perl(strict.pm) perl(warnings.pm)
# END SourceDeps(oneline)
%define _unpackaged_files_terminate_build 1
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 0.06
Release: alt2
Summary: Stringify a Regexp object
Group: Development/Perl
License: perl
URL: https://metacpan.org/release/Regexp-Stringify

Source0: http://mirror.yandex.ru/mirrors/cpan/authors/id/P/PE/PERLANCAR/%{module_name}-%{module_version}.tar.gz
BuildArch: noarch

%description
From summary: %summary

%prep
%setup -q -n %{module_name}-%{module_version}

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes LICENSE README
%perl_vendor_privlib/R*

%changelog
* Thu Sep 28 2017 Igor Vlasenko <viy@altlinux.ru> 0.06-alt2
- to Sisyphus

* Tue Nov 01 2016 Igor Vlasenko <viy@altlinux.ru> 0.06-alt1
- regenerated from template by package builder

* Sat Mar 19 2016 Igor Vlasenko <viy@altlinux.ru> 0.05-alt1
- regenerated from template by package builder

* Wed Oct 14 2015 Igor Vlasenko <viy@altlinux.ru> 0.04-alt1
- regenerated from template by package builder

* Mon Jan 12 2015 Igor Vlasenko <viy@altlinux.ru> 0.03-alt1
- initial import by package builder

