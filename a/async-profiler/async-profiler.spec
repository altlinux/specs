%define _unpackaged_files_terminate_build 1

%add_findreq_skiplist %_bindir/jfrconv
Name: async-profiler
Version: 4.4
Release: alt2

Summary: Sampling CPU and HEAP profiler for Java featuring AsyncGetCallTrace + perf_events
License: Apache-2.0
Group: Development/Tools
Url: https://github.com/async-profiler/async-profiler
VCS: https://github.com/async-profiler/async-profiler

# Source-url: https://github.com/async-profiler/%name/archive/refs/tags/v%version.tar.gz
Source: %name-%version.tar

BuildRequires(pre): rpm-build-java
BuildRequires: gcc-c++
BuildRequires: java-devel >= 17.0
BuildRequires: libstdc++-devel-static
BuildRequires: /proc

%description
This project is a low overhead sampling profiler for Java that does not
suffer from the Safepoint bias problem. It features HotSpot-specific
API to collect stack traces and to track memory allocations. The
profiler works with OpenJDK and other Java runtimes based on the HotSpot
JVM.

Unlike traditional Java profilers, async-profiler monitors non-Java
threads (e.g., GC and JIT compiler threads) and shows native and kernel
frames in stack traces.

What can be profiled:
    * CPU time
    * Allocations in Java Heap
    * Native memory allocations and leaks
    * Contended locks
    * Hardware and software performance counters like cache misses, page
    faults, context switches
    * and more.

%prep
%setup
sed -i "s;\(..\)/lib/\(libasyncProfiler.so\);\1/%_lib/%name/\2;" src/main/main.cpp

%build
%make_build

%install
%__mkdir_p %buildroot{%_bindir,%_javadir}
%__mkdir_p %buildroot{%_libdir,%_includedir}/%name
install -pm 755 build/bin/{asprof,jfrconv} %buildroot%_bindir/
install -pm 644 build/include/*.h %buildroot%_includedir/%name/
install -pm 644 build/lib/*.so %buildroot%_libdir/%name/
install -pm 644 build/jar/*.jar %buildroot%_javadir/

%files
%doc README.md CHANGELOG.md
%_bindir/asprof
%_bindir/jfrconv
%_libdir/%name
%_includedir/%name
%_javadir/*.jar

%changelog
* Thu Jun 18 2026 Andrey Cherepanov <cas@altlinux.org> 4.4-alt2
- Rebuilt with java >= 17.

* Fri Apr 24 2026 Dmitrii Fomchenkov <sirius@altlinux.org> 4.4-alt1
- new version

* Thu Jan 22 2026 Dmitrii Fomchenkov <sirius@altlinux.org> 4.3-alt1
- initial build for ALT Linux
