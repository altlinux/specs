%def_disable bootstrap
%def_enable profile
%def_enable sanitizers

Name:     simpletest
Version:  10
Release:  alt2

Summary:  Simple toolchain test
License:  GPL-3
Group:    Other
Url:      http://git.altlinux.org/people/bircoph/packages/simpletest.git

Packager: Andrew Savchenko <bircoph@altlinux.org>

Source:   %name-%version.tar

BuildRequires: gcc-c++ gcc-fortran libgfortran-devel
%{?!_enable_bootstrap:BuildRequires: libgomp-devel}
%if_enabled sanitizers
BuildRequires: /proc libasan-devel-static
%ifarch %e2k
BuildRequires: liblsan-devel-static libmsan-devel-static
%else
%ifarch i586
BuildRequires: libubsan-devel-static
%else
BuildRequires: liblsan-devel-static libtsan-devel-static libubsan-devel-static
%endif
%endif
%endif

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
    %{subst_enable bootstrap} \
    %{subst_enable profile} \
    %{subst_enable sanitizers}

%make_build -O

# No need to check since all checks are done during build

%install
%makeinstall_std

%files
%_bindir/*
%doc README

%changelog
* Fri May 15 2020 Andrew Savchenko <bircoph@altlinux.org> 10-alt2
- Fix build issues on aarch64 and i586.

* Fri May 15 2020 Andrew Savchenko <bircoph@altlinux.org> 10-alt1
- Add sanitizers support.

* Thu May 14 2020 Andrew Savchenko <bircoph@altlinux.org> 9-alt2
- Disable bootstrap, reenable profile.

* Mon Apr 27 2020 Andrew Savchenko <bircoph@altlinux.org> 9-alt1
- Add bootstap support (for lcc updates) with minimal test.

* Fri Jan 17 2020 Andrew Savchenko <bircoph@altlinux.org> 8-alt3
- Use subst_enable macro.

* Sat Jan 11 2020 Andrew Savchenko <bircoph@altlinux.org> 8-alt2
- Update summary.
- Fix macro type, thanks ldv@ for noticing.

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

* Fri Nov 16 2018 Andrew Savchenko <bircoph@altlinux.org> 2-alt2
- Use flags properly (they are not exported by rpm by default)

* Fri Nov 16 2018 Andrew Savchenko <bircoph@altlinux.org> 2-alt1
- Add C++ and Fortran tests.

* Wed Mar 21 2018 Andrew Savchenko <bircoph@altlinux.org> 1-alt1
- Initial release.
