%define _unpackaged_files_terminate_build 1
%define module_name Log-Any-IfLOG
# BEGIN SourceDeps(oneline):
BuildRequires: perl(ExtUtils/MakeMaker.pm) perl(File/Spec.pm) perl(IO/Handle.pm) perl(IPC/Open3.pm) perl(Log/Any.pm) perl(Pod/Coverage/TrustPod.pm) perl(Test/More.pm) perl(Test/Pod.pm) perl(Test/Pod/Coverage.pm)
# END SourceDeps(oneline)
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 0.090
Release: alt1
Summary: Load Log::Any only if LOG environment variable is true
Group: Development/Perl
License: perl
URL: https://metacpan.org/release/Log-Any-IfLOG

Source0: http://www.cpan.org/authors/id/P/PE/PERLANCAR/%{module_name}-%{version}.tar.gz
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
%doc Changes README LICENSE
%perl_vendor_privlib/L*

%changelog
* Mon Jan 21 2019 Igor Vlasenko <viy@altlinux.ru> 0.090-alt1
- automated CPAN update

* Thu Jul 28 2016 Igor Vlasenko <viy@altlinux.ru> 0.08-alt2
- to Sisyphus

* Thu Jun 16 2016 Igor Vlasenko <viy@altlinux.ru> 0.08-alt1
- regenerated from template by package builder

* Wed Oct 14 2015 Igor Vlasenko <viy@altlinux.ru> 0.07-alt1
- regenerated from template by package builder

* Wed Apr 01 2015 Igor Vlasenko <viy@altlinux.ru> 0.02-alt1
- initial import by package builder

