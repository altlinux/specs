%define kernel_base_version 4.4
%define kernel_source kernel-source-%kernel_base_version

Name: cpupower
Version: %kernel_base_version
Release: alt1

Summary: Linux kernel tool to examine and tune power saving related features of your processor
License: GPLv2
Group: System/Kernel and hardware
URL: http://www.kernel.org/

Patch: %name-%version-%release.patch

Requires: lib%name = %version-%release

Provides: cpufrequtils = 009-%release
Obsoletes: cpufrequtils < 009-%release

BuildRequires: libpci-devel
BuildRequires: rpm-build-kernel
BuildRequires: %kernel_source = 1.0.0

%description
This package contains the tools/power directory from the kernel source
and the supporting document

%package -n lib%name
Summary: Library for %name
License: GPLv2
Group: System/Libraries

Conflicts: %name < %version-%release

%description -n lib%name
This packages contains some library needed by %name.

%package -n lib%name-devel
Summary: Development files for %name
Group: Development/C
Requires: lib%name = %version-%release
Provides: %name-devel = %version-%release
Obsoletes:%name-devel < %version-%release

%description -n lib%name-devel
The lib%name-devel package contains libraries and header files for
developing applications that use %name.

%prep
%setup -cT
tar -xf %kernel_src/%kernel_source.tar
cd %kernel_source
%patch -p1

%build
chmod +x %kernel_source/tools/power/cpupower/utils/version-gen.sh
%make_build -C %kernel_source/tools/power/cpupower CPUFREQ_BENCH=false

%ifarch %{ix86}
    pushd %kernel_source/tools/power/cpupower/debug/i386
    %make_build centrino-decode powernow-k8-decode
    popd
%endif

%ifarch x86_64
    pushd %kernel_source/tools/power/cpupower/debug/x86_64
    %make_build centrino-decode powernow-k8-decode
    popd
%endif

%ifarch %{ix86} x86_64
   pushd %kernel_source/tools/power/x86/x86_energy_perf_policy
   %make_build
   popd
   pushd %kernel_source/tools/power/x86/turbostat
   %make_build
   popd
%endif


%install
%make -C %kernel_source/tools/power/cpupower DESTDIR=%buildroot libdir=%_libdir mandir=%_mandir CPUFREQ_BENCH=false install
rm -f %buildroot%_libdir/*.{a,la}
%find_lang cpupower

%ifarch %{ix86}
    pushd %kernel_source/tools/power/cpupower/debug/i386
    install -m755 centrino-decode %buildroot%_bindir/centrino-decode
    install -m755 powernow-k8-decode %buildroot%_bindir/powernow-k8-decode
    popd
%endif

%ifarch x86_64
    pushd %kernel_source/tools/power/cpupower/debug/x86_64
    install -m755 centrino-decode %buildroot%_bindir/centrino-decode
    install -m755 powernow-k8-decode %buildroot%_bindir/powernow-k8-decode
    popd
%endif

%ifarch %{ix86} x86_64
   mkdir -p %buildroot%_mandir/man8
   pushd %kernel_source/tools/power/x86/x86_energy_perf_policy
   make DESTDIR=%buildroot install
   popd
   pushd %kernel_source/tools/power/x86/turbostat
   make DESTDIR=%buildroot install
   popd
%endif

%files -f cpupower.lang
%_bindir/cpupower
%_mandir/man[1-8]/cpupower*

%ifarch %{ix86} x86_64
%_bindir/centrino-decode
%_bindir/powernow-k8-decode
%_bindir/x86_energy_perf_policy
%_man8dir/x86_energy_perf_policy*
%_bindir/turbostat
%_man8dir/turbostat*
%endif

%files -n lib%name
%_libdir/*.so.*

%files -n lib%name-devel
%_libdir/*.so
%_includedir/*

%changelog
* Tue Jan 26 2016 Alexey Shabalin <shaba@altlinux.ru> 4.4-alt1
- build from kernel-source-4.4

* Wed Sep 16 2015 Alexey Shabalin <shaba@altlinux.ru> 4.2-alt1
- build from kernel-source-4.2

* Tue Apr 21 2015 Alexey Shabalin <shaba@altlinux.ru> 3.19-alt1
- build from kernel-source-3.19

* Thu Oct 09 2014 Alexey Shabalin <shaba@altlinux.ru> 3.17-alt1
- build from kernel-source-3.17

* Wed Apr 16 2014 Alexey Shabalin <shaba@altlinux.ru> 3.14.1-alt1
- build from kernel-source-3.14
- add libcpupower package
- rename cpupower-devel package to libcpupower-devel

* Thu Oct 18 2012 Andriy Stepanov <stanv@altlinux.ru> 3.5.4-alt2
- Bug 27867

* Thu Sep 27 2012 Andriy Stepanov <stanv@altlinux.ru> 3.5.4-alt1
- RPM package for ALT Linux

