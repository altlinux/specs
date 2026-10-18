%define abiversion 1
%define ctlabiversion 6

Name: liblttng-ust
Version: 2.16.0
Release: alt1

Summary: Linux Trace Toolkit Userspace Tracer library

License: GPLv2
Group: Development/C++
Url: http://lttng.org

# Source-url: https://lttng.org/files/lttng-ust/lttng-ust-%version.tar.bz2
Source: %name-%version.tar
Patch100: lttng-gen-tp-shebang.patch
Patch101: liblttng-ust-ctl-default-sigbus-state.patch

BuildRequires(pre): rpm-build-python3

BuildRequires: gcc-c++
BuildRequires: libuserspace-rcu-devel
BuildRequires: libuuid-devel
BuildRequires: libnuma-devel

# for man pages
BuildRequires: asciidoc xmlto

%description
This library may be used by user space applications to generate tracepoints within the kernel LTT subsystem.

%package -n %name%abiversion
Summary: Linux Trace Toolkit Userspace Tracer library
Group: System/Libraries
Provides: %name = %EVR
# liblttng-ust 2.12.2 contained all libraries (.so.0 is now in legacy liblttng-ust0)
Obsoletes: %name < %EVR

%description -n %name%abiversion
This library may be used by user space applications to generate tracepoints
within the kernel LTT subsystem.

%package -n liblttng-ust-ctl%ctlabiversion
Summary: Linux Trace Toolkit Userspace Tracer control library
Group: System/Libraries

%description -n liblttng-ust-ctl%ctlabiversion
This package contains the LTTng UST control library used by lttng-tools.

%package devel

Summary: Linux Trace Toolkit Userspace Tracer library
Group: Development/C++
Requires: %name%abiversion = %EVR
Requires: liblttng-ust-ctl%ctlabiversion = %EVR
Requires: libuserspace-rcu-devel

%description devel
This library provides support for developing programs using LTTng userspace tracing.

%package docs

Summary: Linux Trace Toolkit Userspace Tracer Documentation
Group: Development/C++
BuildArch: noarch

%description docs
This package includes documentation and examples for developing programs using LTTng userspace tracing.

# liblttng-ust-ctl uses urcu symbols provided by its user (lttng-sessiond/consumerd)
%add_verify_elf_skiplist %_libdir/liblttng-ust-ctl.so.%ctlabiversion.*

%prep
%setup
%patch100 -p1
%patch101 -p1
%ifarch %e2k
# this is wrong code, but GCC allows it
sed -i '/__asm__ __volatile__/s|)\[0\])|)[0][0])|' src/lib/lttng-ust/lttng-context-procname.c
%endif

%build
# to fix rpath
%autoreconf
%configure --docdir=%_docdir/%name --disable-static --disable-maintainer-mode
%make_build

%install
%makeinstall_std
rm -vf %buildroot%_libdir/*.la
rm -rf %buildroot/tmp/lttng-ust-divert

%files -n %name%abiversion
%_libdir/liblttng-ust.so.%abiversion
%_libdir/liblttng-ust.so.%abiversion.*
%_libdir/liblttng-ust-common.so.%abiversion
%_libdir/liblttng-ust-common.so.%abiversion.*
%_libdir/liblttng-ust-tracepoint.so.%abiversion
%_libdir/liblttng-ust-tracepoint.so.%abiversion.*
%_libdir/liblttng-ust-cyg-profile.so.%abiversion
%_libdir/liblttng-ust-cyg-profile.so.%abiversion.*
%_libdir/liblttng-ust-cyg-profile-fast.so.%abiversion
%_libdir/liblttng-ust-cyg-profile-fast.so.%abiversion.*
%_libdir/liblttng-ust-dl.so.%abiversion
%_libdir/liblttng-ust-dl.so.%abiversion.*
%_libdir/liblttng-ust-fd.so.%abiversion
%_libdir/liblttng-ust-fd.so.%abiversion.*
%_libdir/liblttng-ust-fork.so.%abiversion
%_libdir/liblttng-ust-fork.so.%abiversion.*
%_libdir/liblttng-ust-libc-wrapper.so.%abiversion
%_libdir/liblttng-ust-libc-wrapper.so.%abiversion.*
%_libdir/liblttng-ust-pthread-wrapper.so.%abiversion
%_libdir/liblttng-ust-pthread-wrapper.so.%abiversion.*

%files -n liblttng-ust-ctl%ctlabiversion
%_libdir/liblttng-ust-ctl.so.%ctlabiversion
%_libdir/liblttng-ust-ctl.so.%ctlabiversion.*

%files devel
%_bindir/lttng-gen-tp
%_includedir/lttng/
%_libdir/liblttng-ust*.so
%_pkgconfigdir/lttng-ust.pc
%_pkgconfigdir/lttng-ust-ctl.pc

%files docs
%_docdir/%name/
%_man1dir/lttng-gen-tp.1.*
%_man3dir/*.3.*

%changelog
* Sun Oct 11 2026 Vitaly Lipatov <lav@altlinux.ru> 2.16.0-alt1
- new version 2.16.0 (SONAME liblttng-ust.so.0 -> liblttng-ust.so.1)
- split libraries to liblttng-ust1 and liblttng-ust-ctl6 (Shared Libs Policy)
- docs: make noarch
- update Elbrus build fix for the new source layout
- liblttng-ust-ctl: define default lttng_ust_sigbus_state (no unresolved symbols)

* Tue Sep 21 2021 Ilya Kurdyukov <ilyakurdyukov@altlinux.org> 2.12.2-alt2
- fixed build for Elbrus

* Tue Jul 06 2021 Vitaly Lipatov <lav@altlinux.ru> 2.12.2-alt1
- new version 2.12.2 (with rpmrb script)

* Tue Mar 31 2020 Vitaly Lipatov <lav@altlinux.ru> 2.11.1-alt1
- new version 2.11.1 (with rpmrb script)

* Thu Feb 20 2020 Vitaly Lipatov <lav@altlinux.ru> 2.11.0-alt1
- new version 2.11.0 (with rpmrb script)

* Wed Jun 05 2019 Alexey Shabalin <shaba@altlinux.org> 2.10.4-alt1
- 2.10.4
- switch to use python3

* Mon Dec 10 2018 Vitaly Lipatov <lav@altlinux.ru> 2.10.2-alt2
- drop ExclusiveArch (ALT bug 35661)

* Sat Nov 24 2018 Vitaly Lipatov <lav@altlinux.ru> 2.10.2-alt1
- new version 2.10.2 (with rpmrb script)

* Sat Jun 30 2018 Vitaly Lipatov <lav@altlinux.ru> 2.10.1-alt1
- new version 2.10.1 (with rpmrb script)

* Sun Nov 12 2017 Vitaly Lipatov <lav@altlinux.ru> 2.8.3-alt1.1
- autorebuild with libuserspace-rcu.git=0.10.0-alt1

* Fri Jul 14 2017 Vitaly Lipatov <lav@altlinux.ru> 2.8.3-alt1
- new version 2.8.3 (with rpmrb script)
- fix dl linking (see https://github.com/lttng/lttng-ust/pull/48)

* Mon Apr 10 2017 Vitaly Lipatov <lav@altlinux.ru> 2.8.0-alt1
- new version 2.8.0 (with rpmrb script)

* Mon Apr 10 2017 Vitaly Lipatov <lav@altlinux.ru> 2.7.0-alt1
- initial build for ALT Linux Sisyphus
