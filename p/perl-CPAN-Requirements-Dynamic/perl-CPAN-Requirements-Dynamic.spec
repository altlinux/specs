# BEGIN SourceDeps(oneline):
BuildRequires: perl(CPAN/Meta/Prereqs.pm) perl(CPAN/Meta/Requirements/Range.pm) perl(Carp.pm) perl(ExtUtils/Config.pm) perl(ExtUtils/HasCompiler.pm) perl(ExtUtils/MakeMaker.pm) perl(IPC/Cmd.pm) perl(Parse/CPAN/Meta.pm) perl(Perl/OSType.pm) perl(Test/More.pm) perl(strict.pm) perl(warnings.pm)
# END SourceDeps(oneline)
%define module_name CPAN-Requirements-Dynamic
%define _unpackaged_files_terminate_build 1
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 0.002
Release: alt2
Summary: Dynamic prerequisites in meta files
Group: Development/Perl
License: perl
Url: %CPAN %module_name

Source0: http://mirror.yandex.ru/mirrors/cpan/authors/id/L/LE/LEONT/%{module_name}-%{version}.tar.gz
BuildArch: noarch

%description
This module implements a format for describing dynamic prerequisites of a distribution.

%prep
%setup -q -n %{module_name}-%{version}

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc LICENSE Changes README
%perl_vendor_privlib/C*

%changelog
* Wed Apr 09 2025 Igor Vlasenko <viy@altlinux.org> 0.002-alt2
- to Sisyphus as Module-Build-Tiny dep

* Mon Apr 07 2025 Igor Vlasenko <viy@altlinux.org> 0.002-alt1
- initial import by package builder

