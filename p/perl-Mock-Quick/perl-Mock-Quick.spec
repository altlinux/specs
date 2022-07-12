%define module_version 1.111
%define module_name Mock-Quick
# BEGIN SourceDeps(oneline):
BuildRequires: perl(Carp.pm) perl(Exporter/Declare.pm) perl(Fennec/Lite.pm) perl(Module/Build.pm) perl(Path/Class.pm) perl(Scalar/Util.pm) perl(Test/Exception.pm) perl(Test/Simple.pm)
# END SourceDeps(oneline)
%define _unpackaged_files_terminate_build 1
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 1.111
Release: alt2
Summary: Quickly mock objects and classes, even temporarily replace them,
Group: Development/Perl
License: perl
Url: %CPAN %module_name

Source0: http://mirror.yandex.ru/mirrors/cpan/authors/id/E/EX/EXODIST/%{module_name}-%{module_version}.tar.gz
BuildArch: noarch

%description
%summary

%prep
%setup -q -n %{module_name}-%{module_version}

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README Changes
%perl_vendor_privlib/O*
%perl_vendor_privlib/M*

%changelog
* Tue Jul 12 2022 Igor Vlasenko <viy@altlinux.org> 1.111-alt2
- to Sisyphus as perl-Sub-HandlesVia build dep

* Sun May 29 2016 Igor Vlasenko <viy@altlinux.ru> 1.111-alt1
- regenerated from template by package builder

* Wed Oct 14 2015 Igor Vlasenko <viy@altlinux.ru> 1.110-alt1
- regenerated from template by package builder

* Fri Sep 05 2014 Igor Vlasenko <viy@altlinux.ru> 1.108-alt1
- regenerated from template by package builder

* Mon Sep 16 2013 Igor Vlasenko <viy@altlinux.ru> 1.107-alt1
- regenerated from template by package builder

* Mon Sep 09 2013 Igor Vlasenko <viy@altlinux.ru> 1.106-alt1
- initial import by package builder

