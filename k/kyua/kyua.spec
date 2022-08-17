%def_enable snapshot
%define _libexecdir %_prefix/libexec
%define pkgtestsdir %_libexecdir/%name/tests

%def_without doxygen
%def_disable check

Name: kyua
Version: 0.13
Release: alt1

Summary: Testing framework for infrastructure software
Group: Development/Tools
License: BSD-3-Clause
Url: https://github.com/jmmv/kyua

%if_disabled snapshot
Source: %url/releases/download/%name-%version/%name-%version.tar.gz
%else
Vcs: https://github.com/jmmv/kyua.git
Source: %name-%version.tar
%endif
Patch1: %name-0.13-alt-testsdir.patch

BuildRequires: gcc-c++
BuildRequires: libatf-c++-devel >= 0.17
BuildRequires: libatf-sh-devel >= 0.15
BuildRequires: pkgconfig(lutok) >= 0.4
BuildRequires: pkgconfig(sqlite3) >= 3.6.22
%{?_with_doxygen:BuildRequires: doxygen}

%description
Kyua is a testing framework for infrastructure software, originally designed
to equip BSD-based operating systems with a test suite. This means that
Kyua is lightweight and simple, and that Kyua integrates well with various
build systems and continuous integration frameworks.

Kyua features an expressive test suite definition language, a safe runtime
engine for test suites and a powerful report generation engine.

Kyua is for both developers and users, from the developer applying a simple
fix to a library to the system administrator deploying a new release
on a production machine.

Kyua is able to execute test programs written with a plethora of
testing libraries and languages. The library of choice is ATF, for which
Kyua was originally designed, but simple, framework-less test programs and
TAP-compliant test programs can also be executed through Kyua.

%package tests
Summary: Runtime tests of the Kyua toolchain
Group: Development/Tools
Requires: %name = %EVR

%description tests
This package provides runtime tests for Kyua -- testing framework for
infrastructure software.

%prep
%setup
%patch1 -p1 -b .testsdir

%build
%autoreconf
%add_optflags %(getconf LFS_CFLAGS) -Wno-error=return-type
%configure \
    --disable-developer \
    %{subst_with doxygen} \
    --with-atf=yes \
    KYUA_PLATFORM=%_target_platform \
    UMOUNT=/bin/umount \
    GDB=/usr/bin/gdb
%nil
%make_build

%install
%makeinstall_std

%check
%make -k check VERBOSE=1

%files
%_bindir/%name
%_datadir/%name/
%_man1dir/%{name}*.1*
%_man5dir/%{name}*.5*
%doc AUTHORS CONTRIBUTORS NEWS.md README.md

%files tests
%pkgtestsdir/

%changelog
* Wed Aug 17 2022 Yuri N. Sedunov <aris@altlinux.org> 0.13-alt1
- first build for Sisyphus (0.13-19-ga685f91)




