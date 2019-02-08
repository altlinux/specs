%define module_version 0.003003
%define module_name Log-Any-Adapter-TAP
# BEGIN SourceDeps(oneline):
BuildRequires: perl(Carp.pm) perl(Data/Dumper.pm) perl(Exporter.pm) perl(ExtUtils/MakeMaker.pm) perl(FindBin.pm) perl(Log/Any.pm) perl(Log/Any/Adapter.pm) perl(Log/Any/Adapter/Base.pm) perl(Log/Any/Proxy.pm) perl(Pod/Coverage/TrustPod.pm) perl(Scalar/Util.pm) perl(Test/More.pm) perl(Test/Pod.pm) perl(Test/Pod/Coverage.pm) perl(Try/Tiny.pm) perl(lib.pm) perl(parent.pm) perl(strict.pm) perl(warnings.pm)
# END SourceDeps(oneline)
%define _unpackaged_files_terminate_build 1
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 0.003003
Release: alt2
Summary: Logger suitable for use with TAP test files
Group: Development/Perl
License: perl
URL: https://github.com/silverdirk/perl-Log-Any-Adapter-TAP

Source0: http://mirror.yandex.ru/mirrors/cpan/authors/id/N/NE/NERDVANA/%{module_name}-%{module_version}.tar.gz
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
%doc LICENSE Changes README
%perl_vendor_privlib/L*

%changelog
* Fri Feb 08 2019 Igor Vlasenko <viy@altlinux.ru> 0.003003-alt2
- to Sisyphus as devscripts dep

* Fri Feb 19 2016 Igor Vlasenko <viy@altlinux.ru> 0.003003-alt1
- regenerated from template by package builder

* Wed Oct 14 2015 Igor Vlasenko <viy@altlinux.ru> 0.003002-alt1
- regenerated from template by package builder

* Mon Sep 22 2014 Igor Vlasenko <viy@altlinux.ru> 0.002000-alt1
- regenerated from template by package builder

* Tue Jul 15 2014 Igor Vlasenko <viy@altlinux.ru> 0.001000-alt1
- initial import by package builder

