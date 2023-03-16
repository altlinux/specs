ExcludeArch: %ix86 armh
# BEGIN SourceDeps(oneline):
BuildRequires: libsowing-devel perl(Dist/Zilla/File/InMemory.pm) perl(Dist/Zilla/Plugin/MakeMaker/Awesome.pm) perl(Exporter.pm) perl(ExtUtils/CBuilder.pm) perl(ExtUtils/MakeMaker.pm) perl(File/Spec.pm) perl(IO/Handle.pm) perl(IPC/Open3.pm) perl(Math/BigInt.pm) perl(Math/Int64.pm) perl(Module/CAPIMaker.pm) perl(Moose.pm) perl(Pod/Wordlist.pm) perl(Test/CPAN/Changes.pm) perl(Test/EOL.pm) perl(Test/More.pm) perl(Test/NoTabs.pm) perl(Test/Pod.pm) perl(Test/Spelling.pm) perl(Test/Synopsis.pm) perl(XSLoader.pm) perl(autodie.pm) perl(constant.pm) perl(integer.pm) perl(overload.pm) perl(strict.pm) perl(warnings.pm)
# END SourceDeps(oneline)
%define module_name Math-Int128
%define _unpackaged_files_terminate_build 1
BuildRequires: rpm-build-perl perl-devel perl-podlators
BuildRequires(pre): rpm-build-licenses

Name: perl-%module_name
Version: 0.22
Release: alt5
Summary: Manipulate 128 bits integers in Perl
Group: Development/Perl
License: %perl_license
URL: http://metacpan.org/release/Math-Int128

Source0: http://mirror.yandex.ru/mirrors/cpan/authors/id/S/SA/SALVA/%{module_name}-%{version}.tar.gz

%description
This module adds support for 128 bit integers, signed and unsigned, to
Perl.

In order to compile this module, your compiler must support one of either the
`__int128' or `int __attribute__ ((__mode__ (TI)))' types. Both GCC and
Clang have supported one or the other type for some time, but they may only do
so on 64-bit platforms.

%prep
%setup -q -n %{module_name}-%{version}

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README.md Changes
%perl_vendor_archlib/M*
%perl_vendor_autolib/*

%changelog
* Fri Mar 10 2023 L.A. Kostis <lakostis@altlinux.ru> 0.22-alt5
- Exclude 32-bit arches.

* Thu Mar 09 2023 L.A. Kostis <lakostis@altlinux.ru> 0.22-alt4
- Rebuild by human.

* Wed Jun 16 2021 Igor Vlasenko <viy@altlinux.org> 0.22-alt3
- rebuild with perl 5.34.0

* Thu Oct 01 2020 Igor Vlasenko <viy@altlinux.ru> 0.22-alt2
- rebuild with perl 5.30

* Mon Feb 25 2019 Igor Vlasenko <viy@altlinux.ru> 0.22-alt1
- initial import by package builder

