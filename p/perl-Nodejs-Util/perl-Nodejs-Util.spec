%define _unpackaged_files_terminate_build 1
%define module_name Nodejs-Util
# BEGIN SourceDeps(oneline):
BuildRequires: perl(Exporter.pm) perl(ExtUtils/MakeMaker.pm) perl(File/Spec.pm) perl(File/Which.pm) perl(IO/Handle.pm) perl(IPC/Open3.pm) perl(IPC/System/Options.pm) perl(Pod/Coverage/TrustPod.pm) perl(Test/More.pm) perl(Test/Pod.pm) perl(Test/Pod/Coverage.pm) perl(strict.pm) perl(warnings.pm) perl(File/chdir.pm) perl(File/Slurper.pm)
# END SourceDeps(oneline)
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 0.009
Release: alt1
Summary: Utilities related to Node.js
Group: Development/Perl
License: perl
URL: https://metacpan.org/release/Nodejs-Util

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
%perl_vendor_privlib/N*

%changelog
* Tue Jan 16 2018 Igor Vlasenko <viy@altlinux.ru> 0.009-alt1
- automated CPAN update

* Thu Jul 28 2016 Igor Vlasenko <viy@altlinux.ru> 0.006-alt2
- to Sisyphus

* Mon Jul 25 2016 Igor Vlasenko <viy@altlinux.ru> 0.006-alt1
- regenerated from template by package builder

* Sun Jul 03 2016 Igor Vlasenko <viy@altlinux.ru> 0.005-alt1
- initial import by package builder

