%define oname userspace-rcu
Name: libuserspace-rcu
Version: 0.13.1
Release: alt1

Summary: RCU (read-copy-update) implementation in user space

Group: System/Libraries
License: LGPLv2+
Url: http://lttng.org/urcu/

Packager: Vitaly Lipatov <lav@altlinux.ru>

# Source-url: http://www.lttng.org/files/urcu/userspace-rcu-%version.tar.bz2
Source: %name-%version.tar

Patch: userspace-rcu-aarch64.patch
Patch2000: userspace-rcu-e2k.patch

BuildRequires: autoconf automake libtool

# need for test
BuildRequires: perl-devel

# Upstream do not yet support mips
ExcludeArch: mips
#Source44: import.info

Provides: %oname = %version-%release
Obsoletes: %oname

%description
This data synchronization library provides read-side access which scales
linearly with the number of cores. It does so by allowing multiples copies
of a given data structure to live at the same time, and by monitoring
the data structure accesses to detect grace periods after which memory
reclamation is possible.

%package devel
Summary: Development files for %name
Group: Development/C
Requires: %name = %version-%release

Provides: %oname-devel = %version-%release
Obsoletes: %oname-devel

%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%prep
%setup
#patch0 -p1
%ifarch %e2k
%patch2000 -p2
%endif

%build
# Patch for AArch64 and PPC64LE needs it
#autoreconf -vif
%configure --disable-static
#Remove Rpath from build system
%__subst 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
%__subst 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool

%make_build

%install
%makeinstall_std

rm -vf %buildroot/%_libdir/*.la
rm -rf %buildroot/%_docdir/%oname/

# move to /lib (ALT bug #33268)
mkdir -p %buildroot/%_lib/
mv %buildroot%_libdir/lib*.so.* %buildroot/%_lib/
for i in %buildroot%_libdir/lib*.so ; do
    ln -srf %buildroot/%_lib/$(readlink $i) $i
done

cd doc/examples && make clean

%check
export LD_LIBRARY_PATH=$(pwd)/src/.libs
make check

%files
/%_lib/liburcu*.so.*

%files devel
%doc README.md doc/*.md
%_includedir/urcu/
%_includedir/urcu*.h
%_libdir/*.so
%_pkgconfigdir/liburcu*.pc

%changelog
* Sun Apr 03 2022 Vitaly Lipatov <lav@altlinux.ru> 0.13.1-alt1
- new version 0.13.1 (with rpmrb script)

* Tue Sep 21 2021 Ilya Kurdyukov <ilyakurdyukov@altlinux.org> 0.13.0-alt2
- added patch for Elbrus (uses generic code)
- added LD_LIBRARY_PATH for tests

* Tue Jul 06 2021 Vitaly Lipatov <lav@altlinux.ru> 0.13.0-alt1
- new version 0.13.0 (with rpmrb script)

* Wed Feb 24 2021 Vitaly Lipatov <lav@altlinux.ru> 0.12.2-alt1
- new version 0.12.2 (with rpmrb script)

* Sat Aug 01 2020 Vitaly Lipatov <lav@altlinux.ru> 0.12.1-alt1
- new version 0.12.1 (with rpmrb script)

* Thu Feb 20 2020 Vitaly Lipatov <lav@altlinux.ru> 0.11.1-alt1
- new version 0.11.1 (with rpmrb script)

* Sun Feb 10 2019 Vitaly Lipatov <lav@altlinux.ru> 0.10.2-alt1
- new version 0.10.2 (with rpmrb script)

* Wed Feb 07 2018 Vitaly Lipatov <lav@altlinux.ru> 0.10.1-alt1
- new version 0.10.1 (with rpmrb script)

* Sat Jul 22 2017 Vitaly Lipatov <lav@altlinux.ru> 0.10.0-alt1
- new version 0.10.0 (with rpmrb script)

* Mon Jul 17 2017 Vitaly Lipatov <lav@altlinux.ru> 0.9.4-alt1
- new version 0.9.4 (with rpmrb script)
- drop doc/examples (use source git for it)

* Tue Mar 28 2017 Vitaly Lipatov <lav@altlinux.ru> 0.9.3-alt3
- override NMU: move libs to %_lib (ALT bug #33268)
- enable tests

* Thu Mar 23 2017 Alexey Shabalin <shaba@altlinux.ru> 0.9.3-alt2
- Relocate shared libraries from %_libdir/ to /%_lib/.

* Mon Jan 02 2017 Vitaly Lipatov <lav@altlinux.ru> 0.9.3-alt1
- new version 0.9.3 (with rpmrb script)

* Wed Jul 27 2016 Vitaly Lipatov <lav@altlinux.ru> 0.9.2-alt1
- new version 0.9.2 (with rpmrb script)

* Wed Feb 24 2016 Vitaly Lipatov <lav@altlinux.ru> 0.9.1-alt1
- new version 0.9.1 (with rpmrb script)
- move sources to subdir

* Sun Jun 14 2015 Vitaly Lipatov <lav@altlinux.ru> 0.8.7-alt2
- clean examples before packing

* Sun Jun 14 2015 Vitaly Lipatov <lav@altlinux.ru> 0.8.7-alt1
- new version 0.8.7 (with rpmrb script)

* Sun Jun 14 2015 Vitaly Lipatov <lav@altlinux.ru> 0.8.1-alt2
- rename package to libuserspace-rcu

* Thu Jun 04 2015 Danil Mikhailov <danil@altlinux.org> 0.8.1-alt1
- initial build for ALT Linux Sisyphus

