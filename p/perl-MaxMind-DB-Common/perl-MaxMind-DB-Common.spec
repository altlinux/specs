%define module_version 0.040001
%define module_name MaxMind-DB-Common
# BEGIN SourceDeps(oneline):
BuildRequires: perl(Carp.pm) perl(Data/Dumper/Concise.pm) perl(DateTime.pm) perl(Exporter.pm) perl(ExtUtils/MakeMaker.pm) perl(File/Spec.pm) perl(IO/Handle.pm) perl(IPC/Open3.pm) perl(List/AllUtils.pm) perl(Math/BigInt.pm) perl(Moo.pm) perl(Moo/Role.pm) perl(MooX/StrictConstructor.pm) perl(Pod/Wordlist.pm) perl(Scalar/Util.pm) perl(Sub/Quote.pm) perl(Test/CPAN/Changes.pm) perl(Test/EOL.pm) perl(Test/More.pm) perl(Test/NoTabs.pm) perl(Test/Pod.pm) perl(Test/Spelling.pm) perl(Test/Synopsis.pm) perl(Test/Version.pm) perl(autodie.pm) perl(blib.pm) perl(constant.pm) perl(namespace/autoclean.pm) perl(overload.pm) perl(strict.pm) perl(warnings.pm)
# END SourceDeps(oneline)
%define _unpackaged_files_terminate_build 1
BuildRequires(pre): rpm-build-licenses
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 0.040001
Release: alt2
Summary: Code shared by the MaxMind DB reader and writer modules
Group: Development/Perl
License: %artistic_license_v2
URL: http://metacpan.org/release/MaxMind-DB-Common/

Source0: http://mirror.yandex.ru/mirrors/cpan/authors/id/M/MA/MAXMIND/%{module_name}-%{module_version}.tar.gz
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
%doc README.md LICENSE Changes
%perl_vendor_privlib/T*
%perl_vendor_privlib/M*

%changelog
* Tue Mar 07 2023 L.A. Kostis <lakostis@altlinux.ru> 0.040001-alt2
- Fix License.

* Fri Feb 19 2016 Igor Vlasenko <viy@altlinux.ru> 0.040001-alt1
- regenerated from template by package builder

* Fri May 22 2015 Igor Vlasenko <viy@altlinux.ru> 0.040000-alt1
- initial import by package builder

