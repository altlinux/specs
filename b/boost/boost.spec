
%define boost_include %_includedir/%name
%define boost_doc %_docdir/%name

%def_with devel
%if_with devel
%def_with boost_build
%def_with devel_static
%else
%def_without boost_build
%def_without devel_static
%endif

%def_with strict_deps

%def_disable bootstrap
%if_enabled bootstrap
%force_disable mpi
%force_disable python
%else
# mpi
%def_with mpi
%def_with python
%endif

# long_double
%ifarch %arm ppc64le
%def_without long_double
%else
%def_with long_double
%endif

# context
%def_with context
%def_with coroutine

%if_with mpi
%define mpiimpl openmpi
%define mpidir %_libdir/%mpiimpl
%endif

# legacy python2 script
%add_findprov_skiplist %_datadir/b2/src/tools/doxproc.py
%add_findreq_skiplist  %_datadir/b2/src/tools/doxproc.py

%define ver_maj 1
%define ver_min 83
%define ver_rel 0

%define namesuff %{ver_maj}.%{ver_min}.%{ver_rel}

%define _unpackaged_files_terminate_build 1


# https://lore.altlinux.org/devel/20210824182050.GA5179@altlinux.org/
# https://lore.altlinux.org/devel/20210825003351.GA9752@altlinux.org/
%{?optflags_lto:%global optflags_lto %optflags_lto -ffat-lto-objects}


Name: boost
Epoch: 1
Version: %ver_maj.%ver_min.%ver_rel
Release: alt6

Summary: Boost libraries
License: BSL-1.0
Group: Development/C++
Url: https://www.boost.org

Source: boost-%version.tar

# https://bugzilla.redhat.com/show_bug.cgi?id=1190039
Patch65: boost-1.83.0-fedora-build-optflags.patch

# https://bugzilla.redhat.com/show_bug.cgi?id=1318383
Patch82: boost-1.83.0-fedora-no-rpath.patch

# https://bugzilla.redhat.com/show_bug.cgi?id=1541035
Patch83: boost-1.83.0-fedora-b2-build-flags.patch

# https://lists.boost.org/Archives/boost/2020/04/248812.php
Patch88: boost-1.73.0-fedora-cmakedir.patch

# https://github.com/boostorg/phoenix/issues/111
Patch89: boost-1.81.0-upstream-phoenix-fix-uargN.patch

# https://github.com/boostorg/mpi/issues/149
Patch90: boost-1.83.0-alt-mpi-nonreturn-abort.patch

# https://github.com/boostorg/context/pull/234
Patch91: boost-1.83.0-alt-context-fix-platform-detection.patch

# https://github.com/boostorg/context/issues/235
# https://github.com/boostorg/context/pull/236
Patch92: boost-1.83.0-alt-context-fix-macos-detection.patch

# https://github.com/boostorg/unordered/issues/205
Patch93: boost-1.83.0-upstream-unordered-fix-copy-assign.patch

Patch2000: boost-1.83-e2k-makecontext.patch

# we use %%_python3_abiflags
# we use %%requires_python_ABI, introduced in rpm-build-python3-0.1.9.3-alt1
%if_with python
# XXX: (pre) dependencies are installed anyway.
# XXX: The only way around is to remove them manually :(
BuildRequires(pre): rpm-build-python3 >= 0.1.9.3-alt1
BuildRequires: python3-devel libnumpy-py3-devel
%endif

%if_with mpi
BuildRequires: %mpiimpl-devel
%endif

BuildRequires: gcc-c++ libstdc++-devel zlib-devel bzlib-devel libicu-devel

%if_with devel
%description
The Boost web site provides free peer-reviewed portable C++ source
libraries.  The emphasis is on libraries which work well with the C++
Standard Library. One goal is to establish "existing practice" and
provide reference implementations so that the Boost libraries are
suitable for eventual standardization. Some of the libraries have
already been included in the C++ 2011 standard and others have been
proposed to the C++ Standards Committee for inclusion in future
standards.

Although Boost was begun by members of the C++ Standards Committee
Library Working Group, membership has expanded to include nearly two
thousand members of the C++ community at large.
%else
%description
This is legacy package build to ease transition to new version of
Boost.
%endif


%if_with devel

%package devel-headers
Summary: Boost libraries header files
Group: Development/C++
AutoReq: yes, nocpp
BuildArch: noarch
Requires: %name-devel = %EVR

%description devel-headers
The Boost web site provides free peer-reviewed portable C++ source
libraries.  The emphasis is on libraries which work well with the C++
Standard Library. One goal is to establish "existing practice" and
provide reference implementations so that the Boost libraries are
suitable for eventual standardization. Some of the libraries have
already been included in the C++ 2011 standard and others have been
proposed to the C++ Standards Committee for inclusion in future
standards.

This package contains header files only.


%package devel
Summary: Boost libraries
Group: Development/C++

Requires(pre,postun): %name-devel-headers = %EVR
Requires: libboost_atomic%version = %EVR
Requires: libboost_chrono%version = %EVR
Requires: libboost_container%version = %EVR
Requires: libboost_contract%version = %EVR
Requires: libboost_date_time%version = %EVR
Requires: libboost_graph%version = %EVR
Requires: libboost_iostreams%version = %EVR
Requires: libboost_json%version = %EVR
Requires: libboost_random%version = %EVR
Requires: libboost_regex%version = %EVR
Requires: libboost_serialization%version = %EVR
Requires: libboost_system%version = %EVR
Requires: libboost_test%version = %EVR
Requires: libboost_timer%version = %EVR
Requires: libboost_thread%version = %EVR
Requires: libboost_url%version = %EVR

Provides: boost-atomic-devel = %EVR
Obsoletes: boost-atomic-devel < %EVR
Provides: boost-chrono-devel = %EVR
Obsoletes: boost-chrono-devel < %EVR
Provides: boost-datetime-devel = %EVR
Obsoletes: boost-datetime-devel < %EVR
Provides: boost-graph-devel = %EVR
Obsoletes: boost-graph-devel < %EVR
Provides: boost-iostreams-devel = %EVR
Obsoletes: boost-iostreams-devel < %EVR
Provides: boost-regex-common-devel = %EVR
Obsoletes: boost-regex-common-devel < %EVR
Provides: boost-regex-devel = %EVR
Obsoletes: boost-regex-devel < %EVR
Provides: boost-regex-gcc2-devel = %EVR
Provides: boost-regex-gcc3-devel = %EVR
Obsoletes: boost-regex-gcc2-devel, boost-regex-gcc3-devel, boost-regex-common-devel
Provides: boost-serialization-devel = %EVR
Obsoletes: boost-serialization-devel < %EVR
Provides: boost-system-devel = %EVR
Obsoletes: boost-system-devel < %EVR
Provides: boost-test-devel = %EVR
Obsoletes: boost-test-devel < %EVR
Provides: boost-timer-devel = %EVR
Obsoletes: boost-timer-devel < %EVR
Provides: boost-thread-devel = %EVR
Obsoletes: boost-thread-devel < %EVR
Provides: boost-multiprecision-devel = %EVR
Obsoletes: boost-multiprecision-devel < %EVR

Provides: %name-intrusive-devel = %EVR
Obsoletes: %name-intrusive-devel < %EVR
Provides: %name-units-devel = %EVR
Obsoletes: %name-units-devel < %EVR

Provides: %name-process-devel = %EVR
Obsoletes: %name-process-devel < %EVR

# See: http://gcc.gnu.org/bugzilla/show_bug.cgi?id=80753
# Architectures: %%e2k + %%libquadmath_arches
# from https://git.altlinux.org/gears/g/gcc-defaults.git?a=blob;f=gcc-defaults.spec
%ifarch %ix86 x86_64 ppc64le %e2k
Requires: libquadmath-devel
%endif


%description devel
The Boost web site provides free peer-reviewed portable C++ source
libraries.  The emphasis is on libraries which work well with the C++
Standard Library. One goal is to establish "existing practice" and
provide reference implementations so that the Boost libraries are
suitable for eventual standardization. Some of the libraries have
already been included in the C++ 2011 standard and others have been
proposed to the C++ Standards Committee for inclusion in future
standards.


%package complete
Summary: Boost libraries -- complete release
Group: Development/C++
BuildArch: noarch

Requires: %name-devel-headers = %EVR
Requires: %name-devel = %EVR
Requires: %name-asio-devel = %EVR
Requires: %name-chrono-devel = %EVR
%if_with context
Requires: %name-context-devel = %EVR
%if_with coroutine
Requires: %name-coroutine-devel = %EVR
%endif
%endif
Requires: %name-filesystem-devel = %EVR
Requires: %name-flyweight-devel = %EVR
Requires: %name-geometry-devel = %EVR
%if_with mpi
Requires: %name-graph-parallel-devel = %EVR
%endif
Requires: %name-interprocess-devel = %EVR
Requires: %name-intrusive-devel = %EVR
Requires: %name-locale-devel = %EVR
Requires: %name-lockfree-devel = %EVR
Requires: %name-log-devel = %EVR
Requires: %name-math-devel = %EVR
%if_with mpi
Requires: %name-mpi-devel = %EVR
%endif
Requires: %name-msm-devel = %EVR
Requires: %name-polygon-devel = %EVR
Requires: %name-program_options-devel = %EVR
%if_with python
Requires: %name-python3-devel = %EVR
%endif
Requires: %name-signals-devel = %EVR
Requires: %name-timer-devel = %EVR
Requires: %name-units-devel = %EVR
Requires: %name-wave-devel = %EVR

%description complete
The Boost web site provides free peer-reviewed portable C++ source
libraries.  The emphasis is on libraries which work well with the C++
Standard Library. One goal is to establish "existing practice" and
provide reference implementations so that the Boost libraries are
suitable for eventual standardization. Some of the libraries have
already been included in the C++ 2011 standard and others have been
proposed to the C++ Standards Committee for inclusion in future
standards.

This is a virtual package which depends on all Boost packages except
static libraries. Install it if you need complete Boost distribution in
your system.


%package asio-devel
Summary: The Boost Asio Library development files
Group: Development/C++
BuildArch: noarch
AutoReq: yes, nocpp

Requires(pre,postun): %name-devel = %EVR
%if_with context
Requires: %name-context-devel = %EVR
%if_with coroutine
Requires: %name-coroutine-devel = %EVR
%endif
%endif

%description asio-devel
asio is a cross-platform C++ library for network programming that
provides developers with a consistent asynchronous I/O model using a
modern C++ approach.


%package context-devel
Summary: The Boost Context Library development files
Group: Development/C++
AutoReq: yes, nocpp

Requires(pre,postun): %name-devel = %EVR
Requires: libboost_context%version = %EVR

%description context-devel
Boost.Context is a foundational library that provides a sort of
cooperative multitasking on a single thread. By providing an abstraction
of the current execution state in the current thread, including the
stack (with local variables) and stack pointer, all registers and CPU
flags, and the instruction pointer, a fcontext_t instance represents a
specific point in the application's execution path. This is useful for
building higher-level abstractions, like coroutines, cooperative threads
(userland threads) or an equivalent to C# keyword yield in C++.


%package coroutine-devel
Summary: The Boost Coroutine Library development files
Group: Development/C++
AutoReq: yes, nocpp

Requires(pre,postun): %name-devel = %EVR
Requires: %name-context-devel = %EVR
Requires: libboost_coroutine%version = %EVR

%description coroutine-devel
Boost.Coroutine provides templates for generalized subroutines which
allow multiple entry points for suspending and resuming execution at
certain locations. It preserves the local state of execution and allows
re-entering subroutines more than once (useful if state must be kept
across function calls).

In contrast to threads, which are pre-emptive, coroutine switches are
cooperative (programmer controls when a switch will happen). The kernel
is not involved in the coroutine switches.

The implementation uses Boost.Context for context switching.


%package filesystem-devel
Summary: The Boost Filesystem Library development files
Group: Development/C++
AutoReq: yes, nocpp

Requires(pre,postun): %name-devel = %EVR
Requires: libboost_filesystem%version = %EVR

%description filesystem-devel
The Boost Filesystem Library provides portable facilities to query and
manipulate paths, files, and directories.


%package flyweight-devel
Summary: The Boost Flyweight Library development files
Group: Development/C++
BuildArch: noarch
AutoReq: yes, nocpp

Requires(pre,postun): %name-devel = %EVR
Requires: %name-interprocess-devel = %EVR

%description flyweight-devel
Flyweights are small-sized handle classes granting constant access to
shared common data, thus allowing for the management of large amounts of
entities within reasonable memory limits. Boost.Flyweight makes it easy
to use this common programming idiom by providing the class template
flyweight<T>, which acts as a drop-in replacement for const T.

It is header-only library. This package contains the headers.


%package geometry-devel
Summary: The Boost Geometry Library development files
Group: Development/C++
BuildArch: noarch
AutoReq: yes, nocpp

Requires(pre,postun): %name-devel = %EVR
Requires: %name-polygon-devel = %EVR

%description geometry-devel
Boost.Geometry, defines concepts, primitives and algorithms for solving
geometry problems. It Boost.Geometry contains a dimension-agnostic,
coordinate-system-agnostic and scalable kernel, based on concepts,
meta-functions and tag dispatching. On top of that kernel, algorithms
are built.

Boost.Geometry contains instantiable geometry classes, but library
users can also use their own. Using registration macros or traits
classes their geometries can be adapted to fulfil Boost.Geometry
concepts.

It is header-only library. This package contains the headers.


%if_with mpi
%package graph-parallel-devel
Summary: Development files for Parallel Boost Graph Library
Group: Development/C++
AutoReq: yes, nocpp

Requires(pre,postun): %name-devel = %EVR
Requires: %name-mpi-devel = %EVR
Requires: libboost_graph%version = %EVR
Requires: libboost_graph_parallel%version = %EVR

%description graph-parallel-devel
The Parallel Boost Graph Library is an extension to the Boost Graph
Library (BGL) for parallel and distributed computing. It offers
distributed graphs and graph algorithms to exploit coarse-grained
parallelism along with parallel algorithms that exploit fine-grained
parallelism, while retaining the same interfaces as the (sequential)
BGL.
%endif


%package locale-devel
Summary: The Boost Locale Library development files
Group: Development/C++
AutoReq: yes, nocpp

Requires(pre,postun): %name-devel = %EVR
Requires: libboost_locale%version = %EVR

%description locale-devel
Boost.Locale is a library that provides high quality localization
facilities in a C++ way. It gives powerful tools for development
of cross platform localized software - the software that talks
to user in its language.


%package lockfree-devel
Summary: The Boost Lockfree Library development files
Group: Development/C++
BuildArch: noarch
AutoReq: yes, nocpp

Requires(pre,postun): %name-devel = %EVR

%description lockfree-devel
Boost.Lockfree library provides lockfree data structures, like
lockfree queue and stack.


%package log-devel
Summary: The Boost Locale Library development files
Group: Development/C++
AutoReq: yes, nocpp

Requires(pre,postun): %name-devel = %EVR
Requires: libboost_log%version = %EVR

%description log-devel
Boost.Log v2 is a library that aims to make logging significantly easier
for the application developer. It provides a wide range of
out-of-the-box tools along with public interfaces for extending the
library.


%package interprocess-devel
Summary: The Boost Interprocess Library development files
Group: Development/C++
BuildArch: noarch
AutoReq: yes, nocpp

Requires(pre,postun): %name-devel = %EVR
Requires: %name-intrusive-devel = %EVR

%description interprocess-devel
Boost.Interprocess provides portable access to shared memory, memory
mapped files, process-shared mutexes, condition variables, containers
and allocators.

It is header-only library. This package contains the headers.

%package math-devel
Summary: The Boost Math Library development files.
Group: Development/C++

Requires(pre,postun): %name-devel = %EVR
Requires: libboost_math_c99%version = %EVR
Requires: libboost_math_c99f%version = %EVR
%if_with long_double
Requires: libboost_math_c99l%version = %EVR
%endif
Requires: libboost_math_tr1%version = %EVR
Requires: libboost_math_tr1f%version = %EVR
%if_with long_double
Requires: libboost_math_tr1l%version = %EVR
%endif

%description math-devel
The Boost Math Library development files. You'll need to install this
package if you want to link with Boost.Math shared libraries.


%if_with mpi
%package mpi-devel
Summary: The Boost MPI Library development files
Group: Development/C++
AutoReq: yes, nocpp

Requires(pre,postun): %name-devel = %EVR
Requires(pre,postun): %name-python3-devel = %EVR
Requires: libboost_mpi%version = %EVR
Requires: libboost_mpi_python3-%version = %EVR
Requires: %mpiimpl-devel

%description mpi-devel
Boost.MPI is a library for message passing in high-performance parallel
applications.
%endif


%package msm-devel
Summary: The Boost MSM Library development files
Group: Development/C++
BuildArch: noarch
AutoReq: yes, nocpp

Requires(pre,postun): %name-devel = %EVR

%description msm-devel
Ths Boost Meta State Machine (MSM) is a library allowing you to easily
and quickly define state machines of very high performance.

It is header-only library. This package contains the headers.


%package polygon-devel
Summary: The Boost Polygon Library development files
Group: Development/C++
BuildArch: noarch
AutoReq: yes, nocpp

Requires(pre,postun): %name-devel = %EVR

%description polygon-devel
The Boost.Polygon library provides algorithms focused on manipulating
planar polygon geometry data.  Specific algorithms provided are the
polygon set operations (intersection, union, difference, disjoint-union)
and related algorithms such as polygon connectivity graph extraction,
offsetting and map-overlay.

It is header-only library. This package contains the headers.


%package program_options-devel
Summary: The Boost Filesystem Library development files
Group: Development/C++
AutoReq: yes, nocpp

Requires(pre,postun): %name-devel = %EVR
Requires: libboost_program_options%version = %EVR

Obsoletes: program_options-devel
Provides: program_options-devel  =  %EVR
Provides: boost-program-options-devel = %EVR

%description program_options-devel
Boost Program Options library allows program developers to obtain
program options, that is (name, value) pairs from the user, via
conventional methods.

%package python-headers
Summary: Boost.Python header files.
Group: Development/C++
AutoReq: yes, nocpp

%description python-headers
Header files for Boost.Python libraries. This files are shared between
libraries compiled with Python 3.

%package python3-devel
Summary: The Boost Python Library (Boost.Python) development files
Group: Development/C++
AutoReq: yes, nocpp

Requires: python3-devel = %_python3_abi_version
Requires: %name-python-headers = %EVR
Requires: libboost_python3-%version = %EVR
Requires: libboost_numpy3-%version = %EVR
Requires(pre,postun): %name-devel = %EVR

%description python3-devel
Use the Boost Python Library to quickly and easily export a C++ library
to Python such that the Python interface is very similar to the C++
interface. It is designed to be minimally intrusive on your C++ design.
In most cases, you should not have to alter your C++ classes in any way
in order to use them with Boost.Python. The system should simply
``reflect'' your C++ classes and functions into Python.

This package contains development files for Boost.Python build with
Python 3.

%package signals-devel
Summary: The Boost Signals Library development files
Group: Development/C++
AutoReq: yes, nocpp

Requires(pre,postun): %name-devel = %EVR

%description signals-devel
The  Boost.Signals  library  is an implementation of a managed signals
and slots  system. Signals represent callbacks with multiple targets,
and  are also called publishers or events in similar systems. Signals
are connected to some set of slots, which are callback receivers (also
called event targets or subscribers), which are called when the signal
is "emitted."

%package wave-devel
Summary: Boost.Wave Library development files.
Group: Development/C++
AutoReq: yes, nocpp

Requires: libboost_wave%version = %EVR
Requires(pre,postun): %name-devel = %EVR
Requires: %name-filesystem-devel = %EVR

%description wave-devel
The Boost Wave Library development files.


%package doc
Summary: Boost libraries documentation
Group: Development/C++
BuildArch: noarch

Requires(pre,postun): %name-devel

%description doc
The Boost web site provides free peer-reviewed portable C++ source
libraries.  The emphasis is on libraries which work well with the C++
Standard Library. One goal is to establish "existing practice" and
provide reference implementations so that the Boost libraries are
suitable for eventual standardization. Some of the libraries have
already been included in the C++ 2011 standard and others have been
proposed to the C++ Standards Committee for inclusion in future
standards.

This package contains Boost libraries documentation.
%endif #with devel

%if_with boost_build
%package build
License: GPL
Summary: Cross platform build system for C++ projects
Group: Development/Other
Obsoletes: %name-jam < %EVR

%description build
B2 (formerly Boost.Jam) is the low-level build engine tool for Boost.Build.
Historically, B2 was based on on FTJam and on Perforce Jam but has grown
a number of significant features and is now developed independently.
%endif


%if_with devel_static
%package devel-static
Summary: Boost libraries
Group: Development/C++

Requires(pre,postun): %name-devel = %EVR
Requires: %name-atomic-devel = %EVR
Requires: %name-chrono-devel = %EVR
%if_with context
Requires: %name-context-devel = %EVR
%endif
Requires: %name-filesystem-devel = %EVR
%if_with mpi
Requires: %name-graph-parallel-devel = %EVR
Requires: %name-mpi-devel = %EVR
%endif
Requires: %name-locale-devel = %EVR
Requires: %name-log-devel = %EVR
Requires: %name-program_options-devel = %EVR
%if_with python
Requires: %name-python3-devel = %EVR
%endif
Requires: %name-signals-devel = %EVR
Requires: %name-timer-devel = %EVR
Requires: %name-wave-devel = %EVR

Obsoletes: program_options-devel-static
Provides: boost-datetime-devel-static = %EVR
Provides: boost-filesystem-devel-static = %EVR
Provides: boost-graph-devel-static = %EVR
Provides: boost-iostreams-devel-static = %EVR
Provides: boost-program-options-devel-static = %EVR
Provides: boost-regex-common-devel-static = %EVR
Provides: boost-regex-devel-static = %EVR
Provides: boost-regex-gcc2-devel-static = %EVR
Provides: boost-regex-gcc3-devel-static = %EVR
Provides: boost-serialization-devel-static = %EVR
Provides: boost-signals-devel-static = %EVR
Provides: boost-system-devel-static = %EVR
Provides: boost-test-devel-static = %EVR
Provides: boost-thread-devel-static = %EVR
Provides: boost-wave-devel-static = %EVR
Provides: program_options-devel-static  =  %EVR

%description devel-static
The Boost web site provides free peer-reviewed portable C++ source
libraries.  The emphasis is on libraries which work well with the C++
Standard Library. One goal is to establish "existing practice" and
provide reference implementations so that the Boost libraries are
suitable for eventual standardization. Some of the libraries have
already been included in the C++ 2011 standard and others have been
proposed to the C++ Standards Committee for inclusion in future
standards.

This package contains static libraries.
%endif #with devel-static


%package -n libboost_atomic%version
Summary: Boost.Atomic Library
Group: Development/C++

%if_with strict_deps
Requires: libboost_system%version = %EVR
%endif

%description -n libboost_atomic%version
Boost.Atomic is a library that provides atomic data types and operations
on these data types, as well as memory ordering constraints required for
coordinating multiple threads through atomic variables. It implements
the interface as defined by the C++11 standard, but makes this feature
available for platforms lacking system/compiler support for this
particular C++11 feature.


%package -n libboost_chrono%version
Summary: Boost.Chrono Library
Group: Development/C++

%if_with strict_deps
Requires: libboost_system%version = %EVR
%endif

%description -n libboost_chrono%version
Boost.Chrono aims to implement the new time facilities in C++0x,
as proposed in N2661 document. To make the timing facilities of
Boost.Chrono more generally useful, the library provides a number
of clocks that are thin wrappers around the operating system's process
time API, thereby allowing the extraction of wall clock time,
user CPU time, and system CPU time of the process.


%package -n libboost_container%version
Summary: Boost.Container Library
Group: Development/C++

%description -n libboost_container%version
Boost.Container library implements several well-known containers,
including STL containers. The aim of the library is to offers advanced
features not present in standard containers or to offer the latest
standard draft features for compilers that comply with C++03.

%package -n libboost_contract%version
Summary: Boost.Contract Library
Group: Development/C++

%if_with strict_deps
Requires: libboost_system%version = %EVR
%endif

%description -n libboost_contract%version
Boost.Contract library implements contract programming for C++.
All contract programming features are supported:
Subcontracting, class invariants, postconditions (with old and return values),
preconditions, customizable actions
on assertion failure (e.g., terminate or throw),
optional compilation and checking of assertions, etc, from Lorenzo Caminiti. 


%package -n libboost_context%version
Summary: Boost.Context Library
Group: Development/C++

%description -n libboost_context%version
Boost.Context is a foundational library that provides a sort of
cooperative multitasking on a single thread.


%package -n libboost_coroutine%version
Summary: Boost.Coroutine Library
Group: Development/C++

%if_with strict_deps
Requires: libboost_context%version = %EVR
Requires: libboost_thread%version = %EVR
Requires: libboost_system%version = %EVR
%endif

%description -n libboost_coroutine%version
Boost.Coroutine provides templates for generalized subroutines which
allow suspending and resuming execution at certain locations. It
preserves the local state of execution and allows re-entering
subroutines more than once.

Coroutines can be viewed as a language-level construct providing a
special kind of control flow. In contrast to threads, which are
pre-emptive, coroutine switches are cooperative (programmer controls
when a switch will happen). The kernel is not involved in the coroutine
switches. The implementation uses Boost.Context for context switching.


%package -n libboost_date_time%version
Summary: Boost Date-Time Library.
Group: Development/C++
Provides: boost-datetime = %EVR

%description -n libboost_date_time%version
Programming  with  dates  and  times  should  be  almost as simple and
natural  as  programming  with strings and integers. Applications with
lots  of temporal logic can be radically simplified by having a robust
set  of operators and calculation capabilities. Classes should provide
the ability to compare dates and times, add lengths or time durations,
retrieve dates and times from clocks, and work naturally with date and
time intervals.


%package -n libboost_filesystem%version
Summary: Filesystem Library
Group: Development/C++
Provides: boost-filesystem = %EVR

%if_with strict_deps
Requires: libboost_system%version = %EVR
%endif

%description -n libboost_filesystem%version
The Boost Filesystem Library provides portable facilities to query and
manipulate paths, files, and directories.


%package -n libboost_graph%version
Summary: Graph Library
Group: Development/C++
Provides: boost-graph = %EVR

%if_with strict_deps
Requires: libboost_regex%version = %EVR
%endif

%description -n libboost_graph%version
The Boost Graph Library provides  graph components and algorithms.


%if_with mpi
%package -n libboost_graph_parallel%version
Summary: Parallel Boost Graph Library
Group: Development/C++

%if_with strict_deps
Requires: libboost_serialization%version = %EVR
Requires: libboost_mpi%version = %EVR
%endif

%description -n libboost_graph_parallel%version
The Parallel Boost Graph Library is an extension to the Boost Graph
Library (BGL) for parallel and distributed computing. It offers
distributed graphs and graph algorithms to exploit coarse-grained
parallelism along with parallel algorithms that exploit fine-grained
parallelism, while retaining the same interfaces as the (sequential)
BGL.

This package contains shared libraries.
%endif

%package -n libboost_json%version
Summary: Json Library
Group: Development/C++

%description -n libboost_json%version
The Boost Json Library is a library for parsing and serializing JSON
to and from a DOM container in memory.

%package -n libboost_locale%version
Summary: Boost.Locale Library
Group: Development/C++

%if_with strict_deps
Requires: libboost_thread%version = %EVR
Requires: libboost_system%version = %EVR
%endif

%description -n libboost_locale%version
Boost.Locale is a library that provides high quality localization
facilities in a C++ way. It gives powerful tools for development
of cross platform localized software - the software that talks
to user in its language.


%package -n libboost_log%version
Summary: Boost.Log Library
Group: Development/C++

%if_with strict_deps
Requires: libboost_filesystem%version = %EVR
Requires: libboost_regex%version = %EVR
Requires: libboost_thread%version = %EVR
Requires: libboost_system%version = %EVR
%endif

%description -n libboost_log%version
Boost.Log v2 is a library that aims to make logging significantly easier
for the application developer. It provides a wide range of
out-of-the-box tools along with public interfaces for extending the
library.


%package -n libboost_iostreams%version
Summary: I/O streams Library
Group: Development/C++
Provides: boost-iostreams = %EVR

%description -n libboost_iostreams%version
The Boost Iostreams Library provides various iostreams support.


%package -n libboost_math_c99%version
Summary: Boost.Math shared library.
Group: Development/C++
Provides: boost-math = %EVR

%description -n libboost_math_c99%version
Boost.Math shared library.


%package -n libboost_math_c99f%version
Summary: Boost.Math shared library.
Group: Development/C++
Provides: boost-math = %EVR

%description -n libboost_math_c99f%version
Boost.Math shared library.

%if_with long_double
%package -n libboost_math_c99l%version
Summary: Boost.Math shared library.
Group: Development/C++
Provides: boost-math = %EVR

%description -n libboost_math_c99l%version
Boost.Math shared library.
%endif // with long_double


%package -n libboost_math_tr1%version
Summary: Boost.Math shared library.
Group: Development/C++
Provides: boost-math = %EVR

%description -n libboost_math_tr1%version
Boost.Math shared library.


%package -n libboost_math_tr1f%version
Summary: Boost.Math shared library.
Group: Development/C++
Provides: boost-math = %EVR

%description -n libboost_math_tr1f%version
Boost.Math shared library.


%if_with long_double
%package -n libboost_math_tr1l%version
Summary: Boost.Math shared library.
Group: Development/C++
Provides: boost-math = %EVR

%description -n libboost_math_tr1l%version
Boost.Math shared library.
%endif


%if_with mpi
%package -n libboost_mpi%version
Summary: Boost.MPI shared library
Group: Development/C++
Provides: boost-mpi = %EVR
%if_with strict_deps
Requires: libboost_serialization%version = %EVR
%endif

%description -n libboost_mpi%version
Boost.MPI is a library for message passing in high-performance parallel
applications. This package contains shared library.

%package -n libboost_mpi_python3-%version
Summary: Boost.MPI python 3 shared library
Group: Development/C++

%requires_python3_ABI_for_files %_libdir/*boost_mpi_python3*.so.*

%description -n libboost_mpi_python3-%version
Boost.MPI is a library for message passing in high-performance parallel
applications. This package contains shared library for python3 bindings.
%endif

%package -n libboost_nowide%version
Summary: Standard library functions with UTF-8 API on Windows
Group: Development/C++

%description -n libboost_nowide%version
Run-time support for Boost.Nowide.

%package -n libboost_program_options%version
Summary: The Boost Program_options Library (Boost.Program_options)
Group: Development/C++

Obsoletes: program_options
Provides: program_options = %EVR
Provides: boost-program-options = %EVR

%description -n libboost_program_options%version
The program_options library allows program developers to obtain program
options, that is (name, value) pairs from the user, via conventional
methods such as command line and config file.


%package -n libboost_python3-%version
Summary: The Boost Python Library (Boost.Python) for Python 3
Group: Development/C++

%requires_python3_ABI_for_files %_libdir/*boost_python3*.so.*

%description -n libboost_python3-%version
Use the Boost Python Library to quickly and easily export a C++ library
to Python such that the Python interface is very similar to the C++
interface. It is designed to be minimally intrusive on your C++ design.
In most cases, you should not have to alter your C++ classes in any way
in order to use them with Boost.Python. The system should simply
``reflect'' your C++ classes and functions into Python.

%package -n libboost_numpy3-%version
Summary: The Boost NumPy Library (Boost.NumPy) for Python 3
Group: Development/C++
Requires: libboost_python3-%version = %EVR
Requires: python3-module-numpy

%requires_python3_ABI_for_files %_libdir/*boost_numpy3*.so.*

%description -n libboost_numpy3-%version
The Boost.Numpy library exposes quite a few methods to create ndarrays.
ndarrays can be created in a variety of ways,
include empty arrays and zero filled arrays.
ndarrays can also be created from arbitrary python sequences
as well as from data and dtypes.

%package -n libboost_random%version
Summary: The Boost.Random library
Group: Development/C++

%description -n libboost_random%version
The Boost Random Number Library (Boost.Random for short) provides
a variety of generators and distributions to produce random numbers
having useful properties.


%package -n libboost_regex%version
Summary: Regular expressions library for C++
Group: Development/C++
Obsoletes: boost-regex-gcc2, boost-regex-gcc3
Provides: boost-regex-gcc2 = %EVR
Provides: boost-regex-gcc3 = %EVR
Provides: boost-regex = %EVR

%description -n libboost_regex%version
Regular expressions are a form of pattern-matching that are often used
in text processing; many users will be familiar with the Unix utilities
grep, sed and awk, and the programming language perl, each of which make
extensive use of regular expressions. Traditionally C++ users have been
limited to the POSIX C API's for manipulating regular expressions, and
while regex++ does provide these API's, they do not represent the best
way to use the library. For example regex++ can cope with wide character
strings, or search and replace operations (in a manner analogous to
either sed or perl), something that traditional C libraries can not do.


%package -n libboost_serialization%version
Summary: The Boost Serialization Library (Boost.Serialization)
Group: Development/C++
Provides: boost-serialization = %EVR

%description -n libboost_serialization%version
Here, we use the term "serialization" to mean the reversible
deconstruction of an arbitrary set of C++ data structures to a sequence
of bytes. Such a system can be used to reconstitute an equivalent
structure in another program context.  Depending on this context, this
might used implement object persistence, remote parameter passing or
other facility.  In this system we use the term "archive" to refer to a
specific rendering of this stream of bytes. This could be a file of
binary data, text data, XML, or some other created by the user of this
library.

%package -n libboost_stacktrace%version
Summary: The Boost Stacktrace Library (Boost.Stacktrace)
Group: Development/C++

%description -n libboost_stacktrace%version
Boost.Stacktrace library is a simple C++03 library that provides
information about call sequence in a human-readable form.

%package -n libboost_system%version
Summary: Boost System Library
Group: Development/C++
Provides: boost-system = %EVR

%description -n libboost_system%version
Boost.System library provides operating system support, including
the diagnostics support that will be part of the C++0x standard library.


%package -n libboost_test%version
Summary: Test Library
Group: Development/C++
Provides: boost-test = %EVR

%description -n libboost_test%version
The Boost Test Library provides a matched set of components for writing
test programs, organizing tests in to simple test cases and test suites,
and controlling their runtime execution. The Program Execution Monitor
is also useful in some production (non-test) environments.


%package -n libboost_thread%version
Group: Development/C++
Summary: The Boost Threads Library (Boost.Threads)

%if_with strict_deps
Requires: libboost_system%version = %EVR
%endif

Obsoletes: boost-thread-gcc2, boost-thread-gcc3
Provides: boost-thread-gcc2 = %EVR
Provides: boost-thread-gcc3 = %EVR
Provides: boost-thread = %EVR

%description -n libboost_thread%version
Boost.Threads allows C++ programs to execute as multiple, asynchronous,
independent, threads-of-execution. Each thread has its own machine state
including program instruction counter and registers. Programs which
execute as multiple threads are called multi-threaded programs to
distinguish them from traditional single-threaded programs. Definitions
gives a more complete description of the multi-threading execution
environment.


%package -n libboost_timer%version
Summary: Boost.Timer Library
Group: Development/C++

%if_with strict_deps
Requires: libboost_chrono%version = %EVR
%endif

%description -n libboost_timer%version
Knowing how long a program takes to execute is useful in both test and
production environments.  Boost.Timer provides classes to measures wall
clock time, user CPU process time, system CPU process time, and more.


%package -n libboost_wave%version
Summary: Boost.Wave Library
Group: Development/C++
Provides: boost-wave = %EVR

%if_with strict_deps
Requires: libboost_system%version = %EVR
Requires: libboost_thread%version = %EVR
%endif

%description -n libboost_wave%version
The Boost Wave Library.

%package -n libboost_fiber%version
Summary: Boost.Fiber Library
Group: Development/C++
Provides: boost-fiber = %EVR

%if_with strict_deps
Requires: libboost_context%version = %EVR
%endif

%description -n libboost_fiber%version
The Boost Fiber Library.

%package -n libboost_type_erasure%version
Summary: Boost.TypeErasure Library
Group: Development/C++
Provides: boost-type_erasure = %EVR

%if_with strict_deps
Requires: libboost_system%version = %EVR
Requires: libboost_thread%version = %EVR
%endif

%description -n libboost_type_erasure%version
The Boost TypeErasure Library.

%package -n libboost_url%version
Summary: Boost.TypeErasure Library
Group: Development/C++
Provides: boost-url = %EVR

%description -n libboost_url%version
The Boost URL Library.

%if_with mpi
%if_with devel
%package -n python3-module-boost-mpi
Summary: Boost.MPI python module
Group: Development/Python3
%if_with strict_deps
Requires: libboost_mpi%version = %EVR
Requires: libboost_mpi_python3-%version = %EVR
Requires: libboost_python3-%version = %EVR
Requires: libboost_serialization%version = %EVR
%endif

%description -n python3-module-boost-mpi
Boost.MPI is a library for message passing in high-performance parallel
applications. This package contains python module.
%endif
%endif

%prep

%setup -n boost-%version
%autopatch -p2

COMPILER_FLAGS="%optflags -fno-strict-aliasing"

%ifarch %e2k
COMPILER_FLAGS="$COMPILER_FLAGS -fno-error-always-inline"
cat >> boost/config/user.hpp << EOF

#if defined(__e2k__) && !defined(BOOST_USE_UCONTEXT)
#define BOOST_USE_UCONTEXT
#endif
EOF
sed -i 's/BOOST_GCC >= 70000/0/' boost/assert/source_location.hpp
# "expression not folded to a constant due to excessive constexpr function call complexity"
sed -i 's/static constexpr/static const/' libs/url/src/detail/replacement_field_rule.cpp
sed -i '/large_power_of_5\[\] =/s/\[\]/[5]/' \
	boost/json/detail/charconv/detail/fast_float/bigint.hpp
%endif

cat >> ./tools/build/src/user-config.jam << EOF
# There are many strict aliasing warnings, and it's not feasible to go
# through them all at this time.
using gcc : : : <compileflags>"$COMPILER_FLAGS" <linkflags>"$COMPILER_FLAGS" ;
%if_with mpi
using mpi ;
%endif
using python : %_python3_version ;
EOF

%build

LINK_BOOST=shared
%if_with devel_static
LINK_BOOST=$LINK_BOOST,static
%endif

%if_with mpi
mpi-selector --yes --set %mpiimpl
source %mpidir/bin/mpivars.sh
export OMPI_LDFLAGS="-Wl,--as-needed,-rpath=%mpidir/lib -L%mpidir/lib"
%endif

./bootstrap.sh --with-toolset=gcc --with-icu

# Form Fedora spec:
# N.B. When we build the following with PCH, parts of boost (math
# library in particular) end up being built second time during
# installation.  Unsure why that is, but all sub-builds need to be
# built with pch=off to avoid this.
./b2 -d+2 -q \
        -j${NPROCS:=%__nprocs} \
	--layout=system \
	--toolset=gcc \
	variant=release \
	threading=multi \
	link=$LINK_BOOST \
	optimization=off \
	debug-symbols=off \
	pch=off \
%ifarch %e2k
	context-impl=ucontext \
	define=BOOST_USE_UCONTEXT \
%endif
	-sHAVE_ICU=1 \
	--prefix=%{_prefix} \
	--libdir=%{_libdir} \
%if_without context
	--without-context \
	--without-fiber \
%endif
%if_without coroutine
	--without-coroutine \
%endif
%if_without mpi
	--without-mpi \
%endif
%if_with python
	python=%_python3_version \
%else
	--without-python \
%endif
	%nil


%if_with boost_build
pushd tools/build
./bootstrap.sh --with-toolset=gcc
popd
%endif

%install

LINK_BOOST=shared
%if_with devel_static
LINK_BOOST=$LINK_BOOST,static
%endif

%if_with mpi
mpi-selector --yes --set %mpiimpl
source %mpidir/bin/mpivars.sh
export OMPI_LDFLAGS="-Wl,--as-needed,-rpath=%mpidir/lib -L%mpidir/lib"
%endif

./b2 -d+2 -q \
	-j${NPROCS:=%__nprocs} \
	--layout=system \
	--toolset=gcc \
	variant=release \
	threading=multi \
	link=$LINK_BOOST \
	optimization=off \
	debug-symbols=off \
	pch=off \
%ifarch %e2k
	context-impl=ucontext \
	define=BOOST_USE_UCONTEXT \
%endif
	-sHAVE_ICU=1 \
	--prefix=%{buildroot}%{_prefix} \
	--libdir=%{buildroot}%{_libdir} \
%if_without context
	--without-context \
	--without-fiber \
%endif
%if_without coroutine
	--without-coroutine \
%endif
%if_without mpi
	--without-mpi \
%endif
%if_with python
	python=%_python3_version \
%else
	--without-python \
%endif
	install

# install mpi python3 module
%if_with mpi
%if_with devel
mkdir -p %buildroot/%python3_sitelibdir/boost
install -Dm644 libs/mpi/build/__init__.py %buildroot/%python3_sitelibdir/boost/
mv %buildroot%_libdir/boost-python%{_python3_version}/mpi.so %buildroot/%python3_sitelibdir/boost/
%else
# The python module won't be created
# if we are a building just library compat pkgs.
# (mpi.so belongs exclusively to the python module.)
rm %buildroot%_libdir/boost-python%{_python3_version}/mpi.so
%endif
%endif

%if_with devel

# make symbolic links for compatibility
for i in %buildroot%_libdir/*.so; do
    [ "$i" != "${i%%-st.so}" ] && continue
    ln -s  `basename $i` ${i%%.so}-mt.so
done

mkdir -p %buildroot%boost_doc

#  install examples
find . -type d -name 'example*' \
    -exec mkdir -p   %buildroot%boost_doc/{} \; \
    -exec sh -c "cp -Rdp {}/* %buildroot%boost_doc/{}" \;

#  install documentation
find . \( -name \*.htm      \
          -or -name \*.html \
          -or -name \*.css  \
          -or -name \*.js   \
          -or -name \*.png  \
          -or -name \*.jpeg \
          -or -name \*.jpg  \
          -or -name \*.svg  \
          -or -name \*.gif  \
          -or -name \*.txt  \
        \) \
        \( -not -name CMakeLists.txt \) \
        -exec install -Dm644 {} %buildroot%boost_doc/{} \;

rm -rf %buildroot%boost_doc/libs/beast/test/extern

if [ -d %buildroot%boost_doc/boost ] ; then
    cp -Rdpf %buildroot%boost_doc/boost/* %buildroot%_includedir/%name/
    rm -rf %buildroot%boost_doc/boost
fi

# some documentation have hyperlinks to real headers; this makes them work
ln -s %_includedir/%name %buildroot%boost_doc/boost

# Programs that link with Boost.Thread and Boost.Filesystem need to link
# with Boost.System explicitly. For thread, this is new requirement since
# boost 1.50.0. To avoid breaking build of too many Boost.Thread clients,
# we introduce some linker scripts.

boost_make_linker_script()
{
    local so_path="%buildroot%_libdir/libboost_${1}.so"

    rm -f "${so_path}"
    echo '/* GNU ld script */' > ${so_path}

    echo -n 'GROUP(' >> ${so_path}
    for name in "$@"; do
        echo -n " %_libdir/libboost_${name}.so.%version" >> ${so_path}
    done
    echo ' )' >> ${so_path}
}

boost_make_linker_script thread system
boost_make_linker_script filesystem system
boost_make_linker_script filesystem-st system-st

%endif

%if_with boost_build
pushd tools/build
./b2 --prefix=%buildroot%_prefix install
# Fix some permissions
chmod +x %buildroot%_datadir/b2/src/tools/doxproc.py
sed -i -e '1s|^#!/usr/bin/python$|#!/usr/bin/python2|' %buildroot%_datadir/b2/src/tools/doxproc.py
popd
%endif

%if_without devel
rm -f %buildroot%_libdir/*.so || :
rm -rf %buildroot%_includedir/boost || :
rm -rf %buildroot%_libdir/cmake/Boost* || :
rm -rf %buildroot%_libdir/cmake/boost* || :
%endif

%if_without devel_static
rm -f %buildroot%_libdir/*.a || :
%endif

%if_without long_double
rm -rf %buildroot%_libdir/*math_c99l*.so*
rm -rf %buildroot%_libdir/*math_tr1l*.so*
%endif


#files

%if_with devel
%files devel-headers
%_includedir/%name
%exclude %_includedir/%name/asio*
%if_with context
%exclude %_includedir/%name/context
%if_with coroutine
%exclude %_includedir/%name/coroutine
%endif
%endif
%exclude %_includedir/%name/filesystem*
%exclude %_includedir/%name/flyweight*
%exclude %_includedir/%name/geometry*
%exclude %_includedir/%name/interprocess*
%exclude %_includedir/%name/locale*
%exclude %_includedir/%name/log/
%exclude %_includedir/%name/lockfree
%if_with mpi
%exclude %_includedir/%name/mpi
%exclude %_includedir/%name/graph/parallel/
%exclude %_includedir/%name/graph/distributed/
%endif
%exclude %_includedir/%name/msm
%exclude %_includedir/%name/polygon
%exclude %_includedir/%name/program_options*
%if_with python
%exclude %_includedir/%name/python*
%endif
%exclude %_includedir/%name/signal*
%exclude %_includedir/%name/wave*

%files devel
%_libdir/*.so
%if_with context
%exclude %_libdir/*_context*.so
%if_with coroutine
%exclude %_libdir/*_coroutine*.so
%endif
%endif
%exclude %_libdir/*_filesystem*.so
%exclude %_libdir/*_locale*.so
%exclude %_libdir/*_log*.so
%exclude %_libdir/*_math*.so
%if_with mpi
%exclude %_libdir/*_mpi*.so
%exclude %_libdir/*_graph_parallel*.so
%endif
%exclude %_libdir/*_program_options*.so
%exclude %_libdir/*_wave*.so
%if_with python
%exclude %_libdir/*_python*.so
%exclude %_libdir/*boost_numpy3*.so
%endif
%_libdir/cmake/*
%if_with context
%exclude %_libdir/cmake/boost_context-%version
%if_with coroutine
%exclude %_libdir/cmake/boost_coroutine-%version
%endif
%endif
%exclude %_libdir/cmake/boost_filesystem-%version
%exclude %_libdir/cmake/boost_locale-%version
%exclude %_libdir/cmake/boost_log-%version
%exclude %_libdir/cmake/boost_math*-%version
%if_with mpi
%exclude %_libdir/cmake/boost_mpi*-%version
%exclude %_libdir/cmake/boost_graph_parallel-%version
%endif
%exclude %_libdir/cmake/boost_program_options-%version
%if_with python
%exclude %_libdir/cmake/boost_python*-%version
%endif
%exclude %_libdir/cmake/boost_wave-%version

%dir %boost_doc/
%doc %boost_doc/LICENSE_1_0.txt

%files complete

%files asio-devel
%_includedir/%name/asio*

%if_with context
%files context-devel
%_includedir/%name/context
%_libdir/*_context*.so
%_libdir/cmake/boost_context-%version

%if_with coroutine
%files coroutine-devel
%_includedir/%name/coroutine
%_libdir/*_coroutine*.so
%_libdir/cmake/boost_coroutine-%version
%endif
%endif

%files filesystem-devel
%_includedir/%name/filesystem*
%_libdir/*_filesystem*.so
%_libdir/cmake/boost_filesystem-%version

%files flyweight-devel
%_includedir/%name/flyweight*

%files geometry-devel
%_includedir/%name/geometry*

%if_with mpi
%files graph-parallel-devel
%_includedir/%name/graph/parallel/
%_includedir/%name/graph/distributed/
%_libdir/*_graph_parallel*.so
%_libdir/cmake/boost_graph_parallel-%version
%endif

%files interprocess-devel
%_includedir/%name/interprocess*

%files locale-devel
%_includedir/%name/locale*
%_libdir/*_locale*.so
%_libdir/cmake/boost_locale-%version

%files lockfree-devel
%_includedir/%name/lockfree

%files log-devel
%_includedir/%name/log/
%_libdir/*_log*.so
%_libdir/cmake/boost_log-%version

%files math-devel
%_libdir/*_math*.so
%_libdir/cmake/boost_math*-%version

%if_with mpi
%files mpi-devel
%_includedir/%name/mpi
%_libdir/*_mpi*.so
%_libdir/cmake/boost_mpi*-%version
%endif

%files msm-devel
%_includedir/%name/msm

%files polygon-devel
%_includedir/%name/polygon

%files program_options-devel
%_includedir/%name/program_options*
%_libdir/*_program_options*.so
%_libdir/cmake/boost_program_options-%version

%if_with python
%files python-headers
%_includedir/%name/python*
%_libdir/cmake/boost_python*-%version

%files python3-devel
%_libdir/*boost_python3*.so
%_libdir/*boost_numpy3*.so
%endif

%files signals-devel
%_includedir/%name/signal*

%files wave-devel
%_includedir/%name/wave*
%_libdir/*_wave*.so
%_libdir/cmake/boost_wave-%version


%files doc
#everything but license
%doc %boost_doc/[^L]*

%endif #with devel

%if_with boost_build
%files build
%_bindir/*
%_datadir/b2
%endif

%if_with devel_static
%files devel-static
%_libdir/*.a
%endif

%files -n libboost_atomic%version
%_libdir/*_atomic*.so.*

%files -n libboost_chrono%version
%_libdir/*_chrono*.so.*

%files -n libboost_container%version
%_libdir/*_container*.so.*

%files -n libboost_contract%version
%_libdir/*_contract*.so.*

%if_with context
%files -n libboost_context%version
%_libdir/*_context*.so.*

%if_with coroutine
%files -n libboost_coroutine%version
%_libdir/*_coroutine*.so.*
%endif
%endif

%files -n libboost_date_time%version
%_libdir/*_date_time*.so.*

%files -n libboost_filesystem%version
%_libdir/*_filesystem*.so.*

%files -n libboost_graph%version
%_libdir/*_graph[^_]*so.*

%if_with mpi
%files -n libboost_graph_parallel%version
%_libdir/*_graph_parallel*.so.*
%endif

%files -n libboost_iostreams%version
%_libdir/*_iostreams*.so.*

%files -n libboost_json%version
%_libdir/*_json*.so.*

%files -n libboost_locale%version
%_libdir/*_locale*.so.*

%files -n libboost_log%version
%_libdir/*_log*.so.*

%files -n libboost_math_c99%version
%_libdir/*_math_c99[^lf]*so.*

%files -n libboost_math_c99f%version
%_libdir/*_math_c99f*.so.*

%if_with long_double
%files -n libboost_math_c99l%version
%_libdir/*_math_c99l*.so.*
%endif


%files -n libboost_math_tr1%version
%_libdir/*_math_tr1[^lf]*so.*

%files -n libboost_math_tr1f%version
%_libdir/*_math_tr1f*.so.*

%if_with long_double
%files -n libboost_math_tr1l%version
%_libdir/*_math_tr1l*.so.*
%endif

%if_with mpi
%files -n libboost_mpi%version
%_libdir/*_mpi.so.*

%files -n libboost_mpi_python3-%version
%_libdir/*_mpi_python3*.so.*
%endif

%files -n libboost_nowide%version
%_libdir/*_nowide*.so.*

%files -n libboost_program_options%version
%_libdir/*_program_options*.so.*

%if_with python
%files -n libboost_python3-%version
%_libdir/*boost_python3*.so.*

%files -n libboost_numpy3-%version
%_libdir/*boost_numpy3*.so.*
%endif

%files -n libboost_random%version
%_libdir/*_random*.so.*

%files -n libboost_regex%version
%_libdir/*_regex*.so.*

%files -n libboost_serialization%version
%_libdir/*_serialization*.so.*
%_libdir/*_wserialization*.so.*

%files -n libboost_stacktrace%version
%_libdir/*_stacktrace*.so.*

%files -n libboost_system%version
%_libdir/*_system*.so.*

%files -n libboost_test%version
%_libdir/*_test*.so.*
%_libdir/*_prg_exec_monitor*.so.*

%files -n libboost_thread%version
%_libdir/*_thread*.so.*

%files -n libboost_timer%version
%_libdir/*_timer*.so.*

%files -n libboost_wave%version
%_libdir/*_wave*.so.*

%if_with context
%files -n libboost_fiber%version
%_libdir/*_fiber*.so.*
%endif

%files -n libboost_type_erasure%version
%_libdir/*_type_erasure*.so.*

%files -n libboost_url%version
%_libdir/*_url*.so.*

%if_with mpi
%if_with devel
%files -n python3-module-boost-mpi
%python3_sitelibdir/boost
%endif
%endif

%if_with devel
# Since 1.31.0 and until 1.34.1 /usr/include/boost was a symbolic link
# We have to add this triggers to avoid upgrade problems

%pre devel
if [ -L "%_includedir/%name" ]; then
    mv -f "%_includedir/%name" "%_includedir/%name.BOOST_UPGRADE_RPMSAVE"
fi


%triggerpostun devel -p /bin/bash -- boost-devel

link="%_includedir/%name.BOOST_UPGRADE_RPMSAVE"
if [ -L $link ]; then
    dir=`readlink -f $link`
    echo $dir | grep -q '^/usr/include/boost[_-]1[^/]\+/boost/\?$'
    if [ $? -eq 0 ]; then
        # we have something to delete
        rm -rf $dir
    fi
    rm -f $link
fi

# and one more cleanup
for dir in %_includedir/boost[_-]1*/ ; do
    [ -d $dir/boost ] && rmdir $dir/boost || :
    [ -d $dir ] && rmdir $dir || :
done

%endif #with devel


%changelog
* Sat Dec 16 2023 Grigory Ustinov <grenka@altlinux.org> 1:1.83.0-alt6
- Build without distutils

* Tue Dec 12 2023 Michael Shigorin <mike@altlinux.org> 1:1.83.0-alt5
- E2K: fix ceph build (ilyakurdyukov@)

* Wed Nov 22 2023 Michael Shigorin <mike@altlinux.org> 1:1.83.0-alt4
- E2K: drop special coroutine handling in spec (ilyakurdyukov@)

* Thu Oct 05 2023 Ivan A. Melnikov <iv@altlinux.org> 1:1.83.0-alt3
- E2K: replacement_field_rule is moved in 1.83.0 (thx ilyakurdyukov@)
- Context: fix Mac OS detection in ucontext
- Add upstream fix for potential crash in Boost.Unordered

* Thu Aug 17 2023 Ivan A. Melnikov <iv@altlinux.org> 1:1.83.0-alt2
- Fix platform detection in Boost.Context (fixes build
  on riscv64 and mipsel)
- Drop obsolete mips-specific patch 2001

* Tue Aug 15 2023 Ivan A. Melnikov <iv@altlinux.org> 1:1.83.0-alt1
- Updated to upstream version 1.83.0

* Thu Aug 03 2023 Michael Shigorin <mike@altlinux.org> 1:1.82.0-alt3
- E2K: lcc 1.26 ftbfs workaround (ilyakurdyukov@)

* Sat Jul 22 2023 Ivan A. Melnikov <iv@altlinux.org> 1:1.82.0-alt2
- Add patch from upstream github to fix linker errors
  related to boost::phoenix::placeholders::uargN

* Fri Jul 21 2023 Ivan A. Melnikov <iv@altlinux.org> 1:1.82.0-alt1
- Updated to upstream version 1.82.0

* Fri Jul 21 2023 Ivan A. Melnikov <iv@altlinux.org> 1:1.81.0-alt3
- sync with sisyphus

* Mon Jun 12 2023 Michael Shigorin <mike@altlinux.org> 1:1.80.0-alt3
- boost-devel-headers R: libquadmath-devel sans ARM (see also gcc#80753)

* Thu May 18 2023 Alexey Sheplyakov <asheplyakov@altlinux.org> 1:1.80.0-alt2
- Added missing bits for LoongArch support (closes: #46181)
- Added --enable=bootstrap knob for a simpler initial build (closes: #46182)

* Thu Dec 15 2022 Ivan A. Melnikov <iv@altlinux.org> 1:1.81.0-alt1
- Updated to upstream version 1.81.0

* Fri Sep 09 2022 Ivan A. Melnikov <iv@altlinux.org> 1:1.80.0-alt1
- Updated to upstream version 1.80.0

* Wed Jun 22 2022 Anton Midyukov <antohami@altlinux.org> 1:1.77.0-alt5
- add upstream patch for fix build packages with CGAL and gcc12 on ppc64le
  (e.g. openscad)

* Fri Jan 14 2022 Aleksei Nikiforov <darktemplar@altlinux.org> 1:1.77.0-alt4
- Fixed compatibility with python-3.10.

* Wed Dec 15 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 1:1.77.0-alt3
- Fixed passing LTO flags to linker.

* Thu Aug 26 2021 Ivan A. Melnikov <iv@altlinux.org> 1:1.77.0-alt2
- Fix build with lto-enabling rpm-build.
- Simplified build and install.

* Mon Aug 16 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 1:1.77.0-alt1
- Updated to upstream version 1.77.0.

* Mon Aug 16 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 1:1.76.0-alt3
- Rebuilt without python-2 support (Closes: #40722).

* Wed Jun 23 2021 Ilya Kurdyukov <ilyakurdyukov@altlinux.org> 1:1.76.0-alt2
- added makecontext patch for Elbrus

* Wed Apr 28 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 1:1.76.0-alt1
- Updated to upstream version 1.76.0.
- Disabled compat python symlinks.
- Enabled cmake support.

* Mon Mar 15 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 1:1.75.0-alt3
- Packaged boost-build instead of boost-jam.

* Thu Jan 21 2021 Ivan A. Melnikov <iv@altlinux.org> 1:1.75.0-alt2
- Fix build on %%mips32
- Don't package external parts of Boost.Beast into boost-doc

* Wed Jan 13 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 1:1.75.0-alt1
- Updated to upstream version 1.75.0.

* Fri Aug 28 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 1:1.74.0-alt1
- Updated to upstream version 1.74.0.

* Tue Jun 16 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 1:1.73.0-alt3
- Applied upstream patch for disabling versioned symlinks.

* Mon Jun 15 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 1:1.73.0-alt2
- Removed versioned symlinks (Closes: #38611).

* Mon Jun 08 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 1:1.73.0-alt1
- Updated to upstream version 1.73.0.

* Wed Jan 22 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 1:1.72.0-alt2
- Fixed issue in boost coroutine module.

* Tue Jan 21 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 1:1.72.0-alt1
- Updated to upstream version 1.72.0.

* Fri Nov 08 2019 Aleksei Nikiforov <darktemplar@altlinux.org> 1:1.71.0-alt1
- Updated to upstream version 1.71.0.
- Spec cleanup.

* Sun Jun 02 2019 Michael Shigorin <mike@altlinux.org> 1:1.67.0-alt8
- Don't disable mpi knob on e2k by default anymore.

* Mon May 27 2019 Nikita Ermakov <arei@altlinux.org> 1:1.67.0-alt7
- Add RISC-V support.

* Thu Apr 04 2019 Michael Shigorin <mike@altlinux.org> 1:1.67.0-alt6
- Support build on e2kv4 through %%e2k macro.

* Mon Dec 10 2018 Ivan A. Melnikov <iv@altlinux.org> 1:1.67.0-alt5
- Make boost-devel replace boost-process-devel.

* Mon Jul 30 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 1:1.67.0-alt4
- Rebuilt with numpy support (Closes: #35190).

* Mon Jun 04 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 1:1.67.0-alt3
- Provided compatibility symlinks for boost-python-devel and boost-python3-devel.

* Wed May 30 2018 Sergey Bolshakov <sbolshakov@altlinux.ru> 1:1.67.0-alt2
- built with MPI support on arm

* Mon May 28 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 1:1.67.0-alt1
- Updated to 1.67.0.
- Packaged libboost_contract.
- Removed libboost_mpi_python3.

* Thu Mar 22 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 1:1.66.0-alt1.1
- (NMU) Rebuilt with python-3.6.4.

* Tue Feb 27 2018 Alexey Shabalin <shaba@altlinux.ru> 1:1.66.0-alt1
- Update to 1.66.0.

* Fri Aug 25 2017 Mikhail Efremov <sem@altlinux.org> 1:1.65.0-alt1
- Fix build without context.
- Package libboost_stacktrace*.
- Package libboost_mpi_python3.
- Use _unpackaged_files_terminate_build.
- Support build for e2k.
- Add with/without context switch.
- Fix build without mpi.
- Use Boost build system v2.
- Updated to 1.65.0.

* Mon Jan 23 2017 Gleb F-Malinovskiy <glebfm@altlinux.org> 1:1.63.0-alt1
- Updated to 1.63.0.

* Thu May 12 2016 Igor Vlasenko <viy@altlinux.ru> 1:1.58.0-alt4
- NMU: added patch37 (closes: #32001)

* Fri Apr  1 2016 Ivan Zakharyaschev <imz@altlinux.org> 1:1.58.0-alt3
- rebuild with python3.5 (for ABI changes)
- this will also rename the autoreqs to the new python3(*) form
- (.spec) fix the build of lib compat pkgs (%%if_without devel)

* Thu Mar 31 2016 Ivan Zakharyaschev <imz@altlinux.org> 1:1.58.0-alt2
- (.spec) ugly LD_PRELOAD replaced with nice new
  %%requires_python{,3}_ABI_for_files.

* Mon Mar 21 2016 Denis Medvedev <nbr@altlinux.org> 1:1.58.0-alt1.1.2
- (NMU) fix typo in patch that makes errors for python 3.5

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1:1.58.0-alt1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Tue Feb 09 2016 Gleb F-Malinovskiy <glebfm@altlinux.org> 1:1.58.0-alt1.1
- Rebuilt with libicui18n.so.56 and libicuuc.so.56.

* Wed May 20 2015 Gleb F-Malinovskiy <glebfm@altlinux.org> 1:1.58.0-alt1
- Updated to 1.58.0.

* Sun Jan 04 2015 Ivan A. Melnikov <iv@altlinux.org> 1:1.57.0-alt4
- improve Qt4 moc workaround

* Sat Jan 03 2015 Ivan A. Melnikov <iv@altlinux.org> 1:1.57.0-alt3
- move Boost.Intrusive to boost-devel-headers, as it is now
  required by Boost.Thread;
- fix boost/logic/ packaging (it went to boost-log-devel by mistake).

* Mon Dec 29 2014 Ivan A. Melnikov <iv@altlinux.org> 1:1.57.0-alt2
- correctly mark coroutine-devel subpackage as
  architecture-dependant;
- fix few spelling errors in package summaries and descriptions.

* Sun Dec 28 2014 Ivan A. Melnikov <iv@altlinux.org> 1:1.57.0-alt1
- new version;
- subpackages for new libraries:
  - now Boost.Context and Boost.Coroutine have binaries;
  - Boost.Log was put into separate subpackages;
- import bunch of patches for unused typedefs from Fedora;
- add patch 34 to fix unused typedef in boost/python/cast.hpp;
- drop single-threaded (-st) binaries;
- get rid of version suffix in documentation directory.

* Sat Feb 16 2013 Ivan A. Melnikov <iv@altlinux.org> 1:1.53.0-alt3
- build with python3-3.3.0.

* Sat Feb 09 2013 Ivan A. Melnikov <iv@altlinux.org> 1:1.53.0-alt2
- add patch 29 to make qt4 moc work even when some boost headers
  included.

* Wed Feb 06 2013 Ivan A. Melnikov <iv@altlinux.org> 1:1.53.0-alt1
- new version;
- subpackages for Boost.Atomic, Boost.Coroutine, Boost.Lockfree and
  Boost.Multiprecision.

* Mon Feb 04 2013 Ivan A. Melnikov <iv@altlinux.org> 1:1.52.0-alt2
- fix Boost.Locale UTF issue (CVE-2013-0252).

* Sun Nov 18 2012 Ivan A. Melnikov <iv@altlinux.org> 1:1.52.0-alt1
- new version;
- removed patch #27, already applied by upstream;
- fixed packaging for builds without long_double and mpi.

* Mon Oct 01 2012 Ivan A. Melnikov <iv@altlinux.org> 1:1.51.0-alt4
- support Python 3 in Boost.Python:
  - a separate library, install boost-python3-devel to build with it;
  - no MPI with Python 3 (yet);
- fix Boost.Polygon build with gcc 4.7 (patch from Scott Tsai).

* Tue Sep 04 2012 Ivan A. Melnikov <iv@altlinux.org> 1:1.51.0-alt3
- add patch #27 to make BGL use traits to make null_vertex
  (see https://svn.boost.org/trac/boost/ticket/7327).

* Fri Aug 31 2012 Ivan A. Melnikov <iv@altlinux.org> 1:1.51.0-alt2
- fixed headers packaging;
- updated %%description to reflect current state of C++
  standardization (wording taken from fedora package by Petr Machata).

* Thu Aug 30 2012 Ivan A. Melnikov <iv@altlinux.org> 1:1.51.0-alt1
- new version;
- new library, Boost.Context, put to separate subpackages;
- updated patches, removed obsolete patches;
- introduced linker scripts for Boost.Thread and Boost.Filesystem.

* Wed Aug 29 2012 Ivan A. Melnikov <iv@altlinux.org> 1:1.49.0-alt4
- dirty fix to build with new glibc
  (see https://svn.boost.org/trac/boost/ticket/6940).

* Tue Jun 26 2012 Ivan A. Melnikov <iv@altlinux.org> 1:1.49.0-alt3
- rebuild with openmpi 1.6.

* Thu Apr 05 2012 Ivan A. Melnikov <iv@altlinux.org> 1:1.49.0-alt2
- don't link libboost_python with libpython.

* Sun Mar 18 2012 Ivan A. Melnikov <iv@altlinux.org> 1:1.49.0-alt1
- new version.

* Sat Jan 28 2012 Ivan A. Melnikov <iv@altlinux.org> 1:1.48.0-alt2
- fix compilation when foreach #defined as BOOST_FOREACH (upstream
  ticket 6131) (closes: #26840).

* Mon Nov 28 2011 Ivan A. Melnikov <iv@altlinux.org> 1:1.48.0-alt1
- new version;
- packaging updated:
  + Boost.Locale and Boost.Geometry put into separate subpackages;
  + Boost.Chrono development files put into boost-devel;
  + packaged Boost.Timer library;
- updated strict dependencies;
- removed obsolete patch.

* Fri Oct 21 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1:1.47.0-alt2.1
- Rebuild with Python-2.7

* Wed Oct 19 2011 Ivan A. Melnikov <iv@altlinux.org> 1:1.47.0-alt2
- import patch 25 from Fedora to allow some of Boost.NumericConversion
  functions compile with BOOST_NO_EXCEPTIONS (ALTBUG #26426);
- don't pre-require mpi (ALTBUG #26289);
- wrap everything connected with long double Boost.Math variants with
  if_with long_double (ALTBUG #26289).

* Wed Jul 13 2011 Ivan A. Melnikov <iv@altlinux.org> 1:1.47.0-alt1
- new version;
- patches updated;
- Boost.Chrono put into separate subpackage.

* Sat Mar 12 2011 Ivan A. Melnikov <iv@altlinux.org> 1:1.46.1-alt1
- new version;
- added patch 24 to fix some missed includes (thx to cpp.req for
  revealing this);
- disabled cpp.req;
- minor spec improvements.

* Fri Mar 11 2011 Ivan A. Melnikov <iv@altlinux.org> 1:1.46.0-alt2.1
- fixed build requirements for python:
  + do not pre-require python-devel;
  + pre-require right version of rpm-build-python (thx Myke Lykov
    for reporting a problem with this).

* Sat Feb 26 2011 Ivan A. Melnikov <iv@altlinux.org> 1:1.46.0-alt2
- fixed documentation and examples installation regressions.

* Tue Feb 22 2011 Ivan A. Melnikov <iv@altlinux.org> 1:1.46.0-alt1
- new version (1.46.0);
- added strict dependencies between sub-packages;
- added missed and removed extra dependencies related to mpi;
- added boost-complete subpackage.

* Sun Jan 02 2011 Ivan A. Melnikov <iv@altlinux.org> 1:1.45.0-alt6
- fixed a typo in boost-mpi-devel requirements.

* Sun Jan 02 2011 Ivan A. Melnikov <iv@altlinux.org> 1:1.45.0-alt5
- put Parallel Boost Graph Library and it's development files into
  separate subpackages;
- updated patch 23 to disable single-threaded graph_parallel library.

* Sat Jan 01 2011 Ivan A. Melnikov <iv@altlinux.org> 1:1.45.0-alt4
- build Boost.MPI;
- minor spec cleanup.

* Thu Dec 16 2010 Ivan A. Melnikov <iv@altlinux.org> 1:1.45.0-alt3
- rebuild with new icu.

* Mon Nov 22 2010 Ivan A. Melnikov <iv@altlinux.org> 1:1.45.0-alt2
- updated patch 22 to fix rpath issue;
- merged Boost.Units to main devel subpackage, since it's internals
  are used by Boost.Exception (see upstream ticket 4876).

* Sun Nov 21 2010 Ivan A. Melnikov <iv@altlinux.org> 1:1.45.0-alt1
- new version (1.45.0);
- updated patches, removed patches already applied by upstream;
- put new libraries, Boost.MSM and Boost.Polygon, into separate
  subpackages;
- split headers from boost-devel and made them noarch;
- link libboost_python with libpython;
- added subpackage for Boost.Random library;
- minor spec improvements.

* Sat Nov 20 2010 Ivan A. Melnikov <iv@altlinux.org> 1:1.42.0-alt3
- added patch 21 to fix Boost.MPL with gcc 4.5 (closes: #25498);
- fixed installing of examples;
- fixed incorrect Provides: tag in libboost_math*;
- minor spec improvements.

* Mon Feb 08 2010 Alexey Voinov <voins@altlinux.org> 1:1.42.0-alt2
- deps from boost.parameter on boost.python removed

* Thu Feb 04 2010 Alexey Voinov <voins@altlinux.org> 1:1.42.0-alt1
- new version (1.42.0)

* Tue Feb 02 2010 Alexey Voinov <voins@altlinux.org> 1:1.41.0-alt1
- new version (1.41.0)
- multipass-warnings patch is obsolete and removed

* Mon Feb 01 2010 Alexey Voinov <voins@altlinux.org> 1:1.40.0-alt1
- new version (1.40.0)
- exlicit-st patch updated
- function_template patch is obsolete and removed

* Fri Nov 13 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:1.39.0-alt3.1
- Rebuilt with python 2.6

* Sat Jun 13 2009 Ivan A. Melnikov <iv@altlinux.org> 1:1.39.0-alt3
- Added patch #16 from shrek@ to make Boost.Function compile under
  BOOST_NO_EXCEPTIONS. 

* Thu Jun 11 2009 Ivan A. Melnikov <iv@altlinux.org> 1:1.39.0-alt2
- Re-enabled static libraries (closes #20407).

* Wed Jun 03 2009 Ivan A. Melnikov <iv@altlinux.org> 1:1.39.0-alt1
- New version:
  + new libraries since 1.36.0: Flyweight, ScopeExit, Signals2,
    Swap, Proto;
  + lots of bugfixes and improvements in most of libraries.
- Put Boost.Flyweight into separate subpackage.
- Adapted building to new features of Boost.Build with layout=system:
  + following Boost.Build defaults, multi-threaded libraries now
    don't have '-mt' suffix (this means that -lboost_regex brings in
    multi-threaded version of Boost.Regex library);
  + single-threaded libraries have '-st' suffix (updated patch #3,
    put patch #4 back);
  + added "*-mt.so" symbolic links for compatibility with build
    systems which expect older boost libraries naming.
- Removed obsolete patches.
- Several minor spec improvements.

* Wed May 27 2009 Ivan A. Melnikov <iv@altlinux.org> 1:1.36.0-alt7
- Added patch #16 with several Boost.Datetime fixes (fixes #20186)

* Fri May 08 2009 Ivan A. Melnikov <iv@altlinux.org> 1:1.36.0-alt6
- Added patch #15 from shrek@ to fix building with gcc 4.4

* Fri May 08 2009 Ivan A. Melnikov <iv@altlinux.org> 1:1.36.0-alt5
- Added patch #14 which fixes MPL for gcc 4.4.
- Removed obsoletes and provides from asio, because in fact
  Boost.Asio does not provide nor obsoletes asio.

* Fri Dec 12 2008 Ivan A. Melnikov <iv@altlinux.org> 1:1.36.0-alt4
- Added sophisticated triggers to fix problems with upgrade
  and workaround strange rpm behaviour.
- Removed obsolete ldconfig-related triggers.
- Added patch 13 to remove some gcc4.3 warnings;
- Added *.gif files to documentation.
- Specfile cleanup and requirements improvements:
  - made development subpackages pre-require boost-devel;
  - added more Obsolete: tags;
  - removed %%__* macros usage.

* Thu Oct 16 2008 Ivan A. Melnikov <iv@altlinux.org> 1:1.36.0-alt3
- Added patch 11 by Alex Ott, found in boost trac ticket 2304,
  to fix warinigs in Boost.Spirit (closes #15718)
- Added patch 12 to fix more warnings in Boost.Spirit
- Really applied (not just attached) patches #8-#10

* Mon Sep 29 2008 Ivan A. Melnikov <iv@altlinux.org> 1:1.36.0-alt2
- Removed experimental patch 4 and modified spec to get back
  traditional library naming, without -st suffix on single-threaded libs.

* Mon Sep 15 2008 Ivan A. Melnikov <iv@altlinux.org> 1:1.36.0-alt1
- New version (fixes #15168)
- Significantly rewrote specfile to simplify it
- Reviewed libraries separation to reflect interdependencies of boost
  libraries better. This also fixes #15421 and #15397
- Changed build architecture of header-only development packages to noarch
- Changed build layout to system and applied patch from Mandriva
  and our own patch to improve ABI versioning in this case
- Added patch #5, to make location of bjam binary platform-independent.
  This should fix #17004, build on ppc and other platforms as well
- Renamed library packages to confirm Shared Libs Policy
- Joined all static libraries into one package
- Switched to use bjam directly instead of calling configure and make,
  which became insufficient
- Applied all hotfixes from
    https://svn.boost.org/trac/boost/wiki/ReleasePractices/HotFixes
- Removed debug versions of libraries
- Removed patch #1, as it is not needed now
- Removed patch #2, as it was applied by upstream

* Sun Mar 23 2008 Damir Shayhutdinov <damir@altlinux.ru> 1:1.34.1-alt1
- New version

* Tue Feb 05 2008 Damir Shayhutdinov <damir@altlinux.ru> 1:1.34.0-alt5.1
- Applied bga@'s patch for building with python2.5

* Sat Feb 02 2008 Grigory Batalov <bga@altlinux.ru> 1:1.34.0-alt5
- Build without exact python version

* Wed Jan 16 2008 Damir Shayhutdinov <damir@altlinux.ru> 1:1.34.0-alt4
- Fixed invalid memory access in boost-regex++ (thanks ldv@ for noticing)
  + CVE-2008-171
  + CVE-2008-172

* Sun Sep 09 2007 Damir Shayhutdinov <damir@altlinux.ru> 1:1.34.0-alt3
- Provide backward-compatibility symlinks for static libraries (libboost_foo.a->libboost_foo-gcc41-mt.a)

* Tue Jul 03 2007 Damir Shayhutdinov <damir@altlinux.ru> 1:1.34.0-alt2
- Use symlinks, not hardlinks for .so files
- Provide backward-compatibility symlinks for libraries (libboost_foo.so->libboost_foo-gcc41-mt.so)

* Mon May 14 2007 Damir Shayhutdinov <damir@altlinux.ru> 1:1.34.0-alt1
- New version
- New subpackage (graph)

* Sat Apr 07 2007 Damir Shayhutdinov <damir@altlinux.ru> 1:1.33.1-alt4
- boost-devel now requires boost-serialization-devel (#11298)

* Mon Jan 08 2007 Damir Shayhutdinov <damir@altlinux.ru> 1:1.33.1-alt3
- Added missing dependancy for boost-program-options-devel (#10578) 

* Fri Dec 22 2006 Damir Shayhutdinov <damir@altlinux.ru> 1:1.33.1-alt2
- Added missing dependancy for boost-serialization-devel (#10485)

* Thu Sep 14 2006 Damir Shayhutdinov <damir@altlinux.ru> 1:1.33.1-alt1
- New version
- New subpackage (iostreams)

* Mon Apr 25 2005 Anton D. Kachalov <mouse@altlinux.org> 1:1.32.0-alt2
- rebuild with python 2.4
- x86_64 support

* Mon Jan 17 2005 Alexey Voinov <voins@altlinux.ru> 1:1.32.0-alt1
- new version (1.32.0)
- program-options* subpackages added
- serialization subpackage added

* Mon May 24 2004 Alexey Voinov <voins@altlinux.ru> 1:1.31.0-alt2
- builddep on python-devel is now versioned

* Thu Apr 22 2004 Alexey Voinov <voins@altlinux.ru> 1:1.31.0-alt1
- new version (1.31.0)
- license changed to Boost Software License
- Reqs on boost-devel changed to PreReqs to enforce order of installation
- lots of triggers added to provide smooth upgrade

* Mon Aug 25 2003 Alexey Voinov <voins@altlinux.ru> 1:1.30.2-alt1
- new version (1.30.2)

* Wed Aug 13 2003 Alexey Voinov <voins@altlinux.ru> 1:1.30.0-alt1
- new version (1.30.0)
- build system changed, so %%build section does
- added subpackages for datetime, filesystem and test libraries
- description for signals library added
- epoch added (all .so's uses %version as so-version, regex library
  should be updated)
- removed all subpackage specific versions

* Tue Jan 21 2003 Alexey Voinov <voins@voins.program.ru> 1.29.0-alt1
- new version (1.29.0) now we know about g++-3.2
- fixes bug #0001863
- docs added
- new subpackage -signals- added
- boost-threads-devel-static temporarily removed, because static
  libraries for it is not built with boost build system.

* Tue Sep 10 2002 Alexey Voinov <voins@voins.program.ru> 1.28.0-alt0.4
- fixed version numbere for gcc-3.2. 
(this is temporary release)

* Mon Aug 19 2002 Alexey Voinov <voins@voins.program.ru> 1.28.0-alt0.3
- ...-config scripts renamed (s/_/-/g)
- added macros to control compilers version for which to build library

* Sun Aug 18 2002 Alexey Voinov <voins@voins.program.ru> 1.28.0-alt0.2
- spec rewrite: subpackages rearranged, files rearranged
- use gcc-version specific directories instead of update-alternatives
- remake patch updated (soname added)
- pytmake patch updated (soname fixed)
- buildreqs fixed

* Mon Jun 10 2002 Alexey Voinov <voins@voins.program.ru> 1.28.0-alt0.1
- new version (1.28.0)
- .makefile patch split into .remake and .pytmake patches
- buildreqs fixed

* Thu Jun 06 2002 Alexey Voinov <voins@voins.program.ru> 1.27.0-alt0.2
- gcc2/gcc3 variants added for regex subpackages
- /usr/bin/*_config files added
- python subpackages added
- buildreqs fixed

