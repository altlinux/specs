%define _unpackaged_files_terminate_build 1

%def_without clang

Name: afl
Version: 2.57b
Release: alt1

Summary: american fuzzy lop - a security-oriented fuzzer
License: Apache-2.0
Group: Development/Tools
URL: https://lcamtuf.coredump.cx/afl/

ExclusiveArch: %ix86 x86_64

# https://github.com/google/AFL.git
Source0: %name-%version.tar
Source1: afl-hsh-rebuild

Patch0: alt-afl-clang-linking.patch
Patch1: %name-%version-coverage.patch

%add_verify_elf_skiplist %_datadir/%name/testcases/*

%if_with clang
BuildRequires: clang llvm llvm-devel
BuildRequires: libstdc++-devel
%endif

%description
American fuzzy lop is a security-oriented fuzzer that employs a novel type
of compile-time instrumentation and genetic algorithms
to automatically discover clean, interesting test cases that trigger
new internal states in the targeted binary.
This substantially improves the functional coverage for the fuzzed code.
The compact synthesized corpora produced by the tool are also useful
for seeding other, more labor- or resource-intensive testing regimes down the road.

Compared to other instrumented fuzzers, afl-fuzz is designed to be practical:
it has modest performance overhead, uses a variety of highly effective fuzzing strategies
and effort minimization tricks, requires essentially no configuration,
and seamlessly handles complex, real-world use cases - say,
common image parsing or file compression libraries.

%prep
%setup
%patch0 -p1
%patch1 -p1

%build
%make_build PREFIX=%_prefix

%if_with clang
pushd llvm_mode
%make_build PREFIX=%_prefix
popd
%endif

%install
%makeinstall_std PREFIX=%_prefix
install -m0755 -D %SOURCE1 %buildroot/%_bindir/afl-hsh-rebuild

%files
%doc LICENSE
%doc README.md CONTRIBUTING.md
%_bindir/*
%_libexecdir/%name
%_datadir/%name
%_defaultdocdir/%name

%changelog
* Mon Jun 06 2022 Paul Wolneykien <manowar@altlinux.org> 2.57b-alt1
- Version 2.57b.
- Build without clang.

* Mon Mar 30 2020 Paul Wolneykien <manowar@altlinux.org> 2.56-alt4.b.git.f10d601
- Added afl-hsh-rebuild wrapper.

* Mon Mar 30 2020 Paul Wolneykien <manowar@altlinux.org> 2.56-alt3.b.git.f10d601
- Support AFL_COVERAGE adding -fprofile-arcs -ftest-coverage -lgcov (patch).

* Wed Mar 18 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 2.56-alt2.b.git.f10d601
- Built afl-clang toolkit.

* Mon Mar 16 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 2.56-alt1.b.git.f10d601
- Initial build for ALT
