%define module_name Hash-Ordered
# BEGIN SourceDeps(oneline):
BuildRequires: perl(Array/AsHash.pm) perl(Array/OrdHash.pm) perl(ExtUtils/MakeMaker.pm) perl(File/Spec.pm) perl(List/Util.pm) perl(Test/Deep.pm) perl(Test/FailWarnings.pm) perl(Test/Fatal.pm) perl(Test/More.pm) perl(Tie/IxHash.pm) perl(constant.pm) perl(overload.pm)
# END SourceDeps(oneline)
#BuildRequires: perl(Data/XHash.pm) perl(Math/Random/MT/Auto.pm) perl(Tie/Hash/Indexed.pm) perl(Tie/LLHash.pm)
%define _unpackaged_files_terminate_build 1
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 0.014
Release: alt2
Summary: A compact, pure-Perl ordered hash class
Group: Development/Perl
License: apache
URL: https://github.com/dagolden/Hash-Ordered

Source0: http://mirror.yandex.ru/mirrors/cpan/authors/id/D/DA/DAGOLDEN/%{module_name}-%{version}.tar.gz
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
%perl_vendor_privlib/H*

%changelog
* Tue Apr 18 2023 Igor Vlasenko <viy@altlinux.org> 0.014-alt2
- to Sisyphus as perl-User-Identity dep

* Tue Jul 09 2019 Igor Vlasenko <viy@altlinux.ru> 0.014-alt1
- updated by package builder

* Thu Mar 09 2017 Igor Vlasenko <viy@altlinux.ru> 0.012-alt1
- regenerated from template by package builder

* Fri Feb 19 2016 Igor Vlasenko <viy@altlinux.ru> 0.010-alt1
- regenerated from template by package builder

* Wed Oct 14 2015 Igor Vlasenko <viy@altlinux.ru> 0.009-alt1
- regenerated from template by package builder

* Tue Jul 15 2014 Igor Vlasenko <viy@altlinux.ru> 0.002-alt1
- initial import by package builder

