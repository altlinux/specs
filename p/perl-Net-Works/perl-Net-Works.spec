# exclude 32-bit due Int128 dependency
ExcludeArch: %ix86 armh
# BEGIN SourceDeps(oneline):
BuildRequires: perl(B.pm) perl(Carp.pm) perl(Exporter.pm) perl(ExtUtils/MakeMaker.pm) perl(File/Spec.pm) perl(List/AllUtils.pm) perl(Math/BigInt.pm) perl(Math/Int128.pm) perl(Moo.pm) perl(Moo/Role.pm) perl(Pod/Coverage/Moose.pm) perl(Pod/Coverage/TrustPod.pm) perl(Pod/Wordlist.pm) perl(Scalar/Util.pm) perl(Socket.pm) perl(Sub/Quote.pm) perl(Test/CPAN/Changes.pm) perl(Test/Code/TidyAll.pm) perl(Test/EOL.pm) perl(Test/Fatal.pm) perl(Test/More.pm) perl(Test/NoTabs.pm) perl(Test/Pod.pm) perl(Test/Pod/Coverage.pm) perl(Test/Spelling.pm) perl(Test/Synopsis.pm) perl(Test/Version.pm) perl(integer.pm) perl(namespace/autoclean.pm) perl(overload.pm) perl(parent.pm) perl(strict.pm) perl(warnings.pm)
# END SourceDeps(oneline)
%define module_name Net-Works
%define _unpackaged_files_terminate_build 1
BuildRequires: rpm-build-perl perl-devel perl-podlators
BuildRequires(pre): rpm-build-licenses

Name: perl-%module_name
Version: 0.22
Release: alt3
Summary: Sane APIs for IP addresses and networks
Group: Development/Perl
License: %perl_license
Url: %CPAN %module_name

Source0: http://mirror.yandex.ru/mirrors/cpan/authors/id/M/MA/MAXMIND/%{module_name}-%{version}.tar.gz

%description
The the NetAddr::IP manpage module is very complete, correct, and useful. However, its
API design is a bit crufty. This distro provides an alternative API that aims
to address the biggest problems with that module's API, as well as adding some
additional features.

This distro contains two modules, the Net::Works::Address manpage and
the Net::Works::Network manpage.

NOTE: This distro's APIs are still in flux. Use at your own risk.

%prep
%setup -q -n %{module_name}-%{version}

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README.md LICENSE Changes
%perl_vendor_privlib/N*

%changelog
* Fri Mar 10 2023 L.A. Kostis <lakostis@altlinux.ru> 0.22-alt3
- Exclude 32-bit arches (due Int128 deps).

* Thu Mar 09 2023 L.A. Kostis <lakostis@altlinux.ru> 0.22-alt2
- Fix license.

* Mon Feb 25 2019 Igor Vlasenko <viy@altlinux.ru> 0.22-alt1
- initial import by package builder

