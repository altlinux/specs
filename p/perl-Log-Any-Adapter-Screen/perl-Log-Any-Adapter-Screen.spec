%define module_name Log-Any-Adapter-Screen
# BEGIN SourceDeps(oneline):
BuildRequires: perl(ExtUtils/MakeMaker.pm) perl(File/Spec.pm) perl(IO/Handle.pm) perl(IPC/Open3.pm) perl(Log/Any.pm) perl(Log/Any/Adapter.pm) perl(Pod/Coverage/TrustPod.pm) perl(Term/ANSIColor.pm) perl(Test/More.pm) perl(Test/Perl/Critic.pm) perl(Test/Pod.pm) perl(Test/Pod/Coverage.pm) perl(Time/HiRes.pm) perl(parent.pm) perl(strict.pm) perl(warnings.pm)
# END SourceDeps(oneline)
%define _unpackaged_files_terminate_build 1
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 0.140
Release: alt2
Summary: Send logs to screen, with colors and some other features
Group: Development/Perl
License: perl
URL: https://metacpan.org/release/Log-Any-Adapter-Screen

Source0: http://mirror.yandex.ru/mirrors/cpan/authors/id/P/PE/PERLANCAR/%{module_name}-%{version}.tar.gz
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
%doc README LICENSE Changes
%perl_vendor_privlib/L*

%changelog
* Fri Feb 08 2019 Igor Vlasenko <viy@altlinux.ru> 0.140-alt2
- to Sisyphus as devscripts dep

* Mon Dec 24 2018 Igor Vlasenko <viy@altlinux.ru> 0.140-alt1
- regenerated from template by package builder

* Wed Oct 12 2016 Igor Vlasenko <viy@altlinux.ru> 0.13-alt1
- regenerated from template by package builder

* Sat Mar 19 2016 Igor Vlasenko <viy@altlinux.ru> 0.12-alt1
- regenerated from template by package builder

* Fri Feb 19 2016 Igor Vlasenko <viy@altlinux.ru> 0.11-alt1
- regenerated from template by package builder

* Mon Oct 12 2015 Igor Vlasenko <viy@altlinux.ru> 0.09-alt1
- initial import by package builder

