Name:           cpupower
Version:        3.5.4
Release:        alt2
Summary:        Linux kernel tool to examine and tune power saving related features of your processor
Group:          System/Kernel and hardware
License:        GPLv2
URL:            http://www.kernel.org/
Source0:        cpupower-%{version}.tar
Source1:        Makefile
Patch0:         power-x86-destdir.patch
Packager: Andriy Stepanov <stanv@altlinux.ru>
BuildRequires: libpci-devel gettext

Provides:  cpufrequtils = 009
Obsoletes: cpufrequtils < 008
Obsoletes: cpuspeed < 1.5

%description
This package contains the tools/power directory from the kernel source
and the supporting document

%package        devel
Summary:        Development files for %{name}
Group:          Development/C
Requires:       %{name} = %{version}-%{release}
Requires:       pkgconfig
Conflicts:      libcpufreq-devel

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%setup -q -c -n %name-%version/tools/power
%patch0 -p3

# Fetch version
install -m0644 -p %{S:1} %_builddir/%name-%version


%build
%make -C cpupower CPUFREQ_BENCH=false

%ifarch %{ix86}
    cd cpupower/debug/i386
    %make centrino-decode powernow-k8-decode
    cd -
%endif

%ifarch x86_64
    cd cpupower/debug/x86_64
    %make centrino-decode powernow-k8-decode
    cd -
%endif

%ifarch %{ix86} x86_64
   cd x86/x86_energy_perf_policy/
   %make
   cd -
   cd x86/turbostat
   %make
   cd -
%endif


%install
%make -C cpupower DESTDIR=$RPM_BUILD_ROOT libdir=%{_libdir} mandir=%{_mandir} CPUFREQ_BENCH=false install
rm -f %{buildroot}%{_libdir}/*.{a,la}
chmod 0755 %{buildroot}%{_libdir}/libcpupower.so*
%find_lang cpupower

%ifarch %{ix86}
    cd cpupower/debug/i386
    install -m755 centrino-decode %{buildroot}%{_bindir}/centrino-decode
    install -m755 powernow-k8-decode %{buildroot}%{_bindir}/powernow-k8-decode
    cd -
%endif

%ifarch x86_64
    cd cpupower/debug/x86_64
    install -m755 centrino-decode %{buildroot}%{_bindir}/centrino-decode
    install -m755 powernow-k8-decode %{buildroot}%{_bindir}/powernow-k8-decode
    cd -
%endif

%ifarch %{ix86} x86_64
   mkdir -p %{buildroot}%{_mandir}/man8
   cd x86/x86_energy_perf_policy
   make DESTDIR=%{buildroot} install
   cd -
   cd x86/turbostat
   make DESTDIR=%{buildroot} install
   cd -
%endif

%files -f cpupower.lang
%{_bindir}/cpupower
%{_libdir}/libcpupower.so.0
%{_libdir}/libcpupower.so.0.0.0
%{_mandir}/man[1-8]/cpupower*

%ifarch %{ix86} x86_64
%{_bindir}/centrino-decode
%{_bindir}/powernow-k8-decode
%{_bindir}/x86_energy_perf_policy
%{_mandir}/man8/x86_energy_perf_policy*
%{_bindir}/turbostat
%{_mandir}/man8/turbostat*
%endif

%files devel
%defattr(-,root,root,-)
%{_libdir}/libcpupower.so
%{_includedir}/cpufreq.h

%changelog
* Thu Oct 18 2012 Andriy Stepanov <stanv@altlinux.ru> 3.5.4-alt2
- Bug 27867

* Thu Sep 27 2012 Andriy Stepanov <stanv@altlinux.ru> 3.5.4-alt1
- RPM package for ALT Linux

