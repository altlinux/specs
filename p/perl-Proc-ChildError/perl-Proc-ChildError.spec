%define module_version 0.04
%define module_name Proc-ChildError
# BEGIN SourceDeps(oneline):
BuildRequires: perl(Exporter.pm) perl(ExtUtils/MakeMaker.pm) perl(File/Spec.pm) perl(IO/Handle.pm) perl(IPC/Open3.pm) perl(Pod/Coverage/TrustPod.pm) perl(Test/More.pm) perl(Test/Pod.pm) perl(Test/Pod/Coverage.pm) perl(blib.pm)
# END SourceDeps(oneline)
%define _unpackaged_files_terminate_build 1
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 0.04
Release: alt2
Summary: Explain process child error
Group: Development/Perl
License: perl
URL: https://metacpan.org/release/Proc-ChildError

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
%doc README Changes LICENSE
%perl_vendor_privlib/P*

%changelog
* Thu Jul 28 2016 Igor Vlasenko <viy@altlinux.ru> 0.04-alt2
- to Sisyphus

* Fri Feb 19 2016 Igor Vlasenko <viy@altlinux.ru> 0.04-alt1
- regenerated from template by package builder

* Wed Oct 14 2015 Igor Vlasenko <viy@altlinux.ru> 0.03-alt1
- regenerated from template by package builder

* Mon Nov 24 2014 Igor Vlasenko <viy@altlinux.ru> 0.02-alt1
- regenerated from template by package builder

* Thu Apr 17 2014 Igor Vlasenko <viy@altlinux.ru> 0.01-alt1
- initial import by package builder

