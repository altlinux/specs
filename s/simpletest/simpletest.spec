%def_enable profile
%ifarch %e2k
%def_enable m32
%endif

Name:     simpletest
Version:  8
Release:  alt1

Summary:  Simple uname test.
License:  GPL-3
Group:    Other
Url:      https://altlinux.org

Packager: Andrew Savchenko <bircoph@altlinux.org>

Source:   %name-%version.tar

BuildRequires: gcc-c++ gcc-fortran libgfortran-devel libgomp-devel
%ifarch %e2k
%if_enabled m32
BuildRequires: e2k32-gcc e2k32-gcc-c++
# For lib.req (and debuginfo etc.) to work properly:
BuildPreReq: e2k32-glibc
# Work-around lib.req not knowing that lib32 is in our default search path.
# TODO: change lib.req to get the idea of the default search path
# from the corresponding ld.so interpreter.
%filter_from_requires \:/lib.*\( = \|(\): s:^\(/usr\)\?/lib32/::
%endif
%if_enabled profiler
BuildRequires: lcc1.23 >= 1.23.20-alt5
%endif
%endif
#ifarch x86_64
#if_enabled m32
#BuildRequires: i586-gcc9 i586-gcc9-c++
#endif
#endif

%description
Simple suit for testing basic runtime toolchain functionality:
- build chroot installability;
- C/C++/Fortran base testing (compiles & works);
- OpenMP tests for both C and Fortran (C++ OpenMP is the same as C);
- profiler testing.

Also provides useful information about system:
- running CPU version and architecture;
- active instruction set, bitness, optlevel;
- uname information;
- effective compiler version and supported standards.

%prep
%setup

%build
%configure \
%if_enabled m32
    --enable-m32 \
%endif
%if_enabled profile
    --enable-profile \
%endif

%make_build

%check
%make check

%install
%makeinstall_std

%files
%_bindir/*
%doc README

%changelog
* Sat Jan 11 2020 Andrew Savchenko <bircoph@altlinux.org> 8-alt1
- Add gcc support.
- Disable m32 tests for non-e2k arches. It can be used on x86_64,
  but outside of build infra, since x86_64-i586 is a separate arepo
  generated repository.
- Refactor build system, add configure.
- Install 32-bit binaries on e2k and docs.

* Thu Nov 21 2019 Andrew Savchenko <bircoph@altlinux.org> 7-alt1
- Add profiler testing (eprof).
- Refactoring.

* Thu Nov 07 2019 Andrew Savchenko <bircoph@altlinux.org> 6-alt1
- Add libgfortran-devel dummy dependency to check libgfortran installability.

* Mon Jul 01 2019 Andrew Savchenko <bircoph@altlinux.org> 5-alt1
- Add CPU model and arch run-time information.

* Wed Feb 13 2019 Andrew Savchenko <bircoph@altlinux.org> 4-alt1
- Add 32-bit C and C++ tests.

* Tue Dec 18 2018 Andrew Savchenko <bircoph@altlinux.org> 3-alt1
- Extend compiler and language standard information.
- Add OpenMP C and Fortran checks.
- Add run-time tests.

* Fri Nov 15 2018 Andrew Savchenko <bircoph@altlinux.org> 2-alt2
- Use flags properly (they are not exported by rpm by default)

* Fri Nov 15 2018 Andrew Savchenko <bircoph@altlinux.org> 2-alt1
- Add C++ and Fortran tests.

* Wed Mar 21 2018 Andrew Savchenko <bircoph@altlinux.org> 1-alt1
- Initial release.
