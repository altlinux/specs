%define module_name Clone-Choose
# BEGIN SourceDeps(oneline):
BuildRequires: perl(ExtUtils/MakeMaker.pm) perl(Storable.pm) perl(Test/More.pm)
# END SourceDeps(oneline)
%define _unpackaged_files_terminate_build 1
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 0.008
Release: alt2
Summary: Choose appropriate clone utility
Group: Development/Perl
License: perl
URL: https://metacpan.org/release/Clone-Choose

Source0: http://mirror.yandex.ru/mirrors/cpan/authors/id/H/HE/HERMES/%{module_name}-%{version}.tar.gz
BuildArch: noarch

%description
`Clone::Choose' checks several different modules which provides a
`clone()' function and selects an appropriate one. The default preferrence
is

  Clone
  Storable
  Clone::PP

This list might evolve in future. Please see the EXPORTS entry elsewhere in this document how to pick a
particular one.
%prep
%setup -q -n %{module_name}-%{version}

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README.md Changes
%perl_vendor_privlib/C*

%changelog
* Fri Nov 24 2017 Igor Vlasenko <viy@altlinux.ru> 0.008-alt2
- to Sisyphus as perl-Hash-Merge dep

* Fri Oct 27 2017 Igor Vlasenko <viy@altlinux.ru> 0.008-alt1
- regenerated from template by package builder

* Wed Oct 25 2017 Igor Vlasenko <viy@altlinux.ru> 0.005-alt1
- regenerated from template by package builder

* Tue Oct 17 2017 Igor Vlasenko <viy@altlinux.ru> 0.003-alt1
- regenerated from template by package builder

* Sun Oct 08 2017 Igor Vlasenko <viy@altlinux.ru> 0.002-alt1
- regenerated from template by package builder

* Sat Sep 30 2017 Igor Vlasenko <viy@altlinux.ru> 0.001-alt1
- initial import by package builder

