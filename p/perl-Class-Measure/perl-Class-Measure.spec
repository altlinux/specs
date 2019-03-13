%define module_name Class-Measure
# BEGIN SourceDeps(oneline):
BuildRequires: perl(Carp.pm) perl(Module/Build/Tiny.pm) perl(Sub/Exporter.pm) perl(Test2/V0.pm)
# END SourceDeps(oneline)
%define _unpackaged_files_terminate_build 1
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 0.07
Release: alt2
Summary: Create, compare, and convert units of measurement.
Group: Development/Perl
License: perl
URL: https://github.com/bluefeet/Class-Measure

Source0: http://mirror.yandex.ru/mirrors/cpan/authors/id/B/BL/BLUEFEET/%{module_name}-%{version}.tar.gz
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
%doc Changes README.md LICENSE
%perl_vendor_privlib/C*

%changelog
* Wed Mar 13 2019 Igor Vlasenko <viy@altlinux.ru> 0.07-alt2
- to Sisyphus as GEO-Distance dep

* Sat Mar 09 2019 Igor Vlasenko <viy@altlinux.ru> 0.07-alt1
- updated by package builder

* Mon Feb 18 2019 Igor Vlasenko <viy@altlinux.ru> 0.06-alt1
- updated by package builder

* Thu Sep 19 2013 Igor Vlasenko <viy@altlinux.ru> 0.05-alt1
- initial import by package builder

