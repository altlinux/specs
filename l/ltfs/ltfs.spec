%global optflags_lto %optflags_lto -ffat-lto-objects

Name:    ltfs
Version: 3.5.0
Release: alt1

Summary: HPE Linear Tape File System
License: LGPL-2.1
Group:   Archiving/Backup
Url:     https://support.hpe.com/connect/s/softwaredetails?language=en_US&softwareId=MTX_5d96a1ab949d415dab03d26ae1

Packager: Sergey Gvozdetskiy <serjigva@altlinux.org>

Source:  %name-%version.tar
Source1: ltfs.service
Source2: %name.pc.in
Patch:  service_file.patch

BuildRequires: libicu-devel
BuildRequires: fuse libfuse-devel
BuildRequires: libxml2-devel
BuildRequires: pkgconfig(uuid)

Requires: %name-libs = %version-%release
Requires: lsb-init >= 5.0

%description
HPE LTFS makes tape self-describing, file-based, and easy-to-use and provides
users with the ability to use standard file operations on tape media for
accessing, managing and sharing files with an interface that behaves as a hard
disk.

%package devel
Summary: LTFS development files
Group: Development/C
License: LGPL-2.1
Requires: %name-libs = %version-%release

%description devel
Development files for building applications under Linear Tape File System

%package libs
Summary: Linear Tape File System shared libraries
Group: System/Libraries
License: LGPL-2.1

%description libs
Shared libraries for running LTFS applications

%prep
%setup
%patch -p1
# Changing due to https://elixir.bootlin.com/glibc/glibc-2.32/source/NEWS#L614
subst 's|sys/sysctl.h|linux/sysctl.h|g' src/libltfs/arch/arch_info.c

# Avoid creation native root directories and files inside there
subst 's|$(sysconfdir)\/|%buildroot$(sysconfdir)\/|g' conf/Makefile.in
subst 's|@datadir@\/|%buildroot@datadir@\/|g' init.d/Makefile.in
subst 's|$(prefix)/share|%buildroot$(datadir)|g' src/libltfs/Makefile.in

%build
%add_optflags "-DU_DEFINE_FALSE_AND_TRUE"
%configure --enable-fast
%make_build

%install
%makeinstall_std
mkdir -p %buildroot{%_unitdir,%_initdir}
install -m644 %SOURCE1 %buildroot%_unitdir
install -pDm755 {init.d,%buildroot%_initdir}/%name

install -d %buildroot%_includedir/%name/arch
install -m644 src/lib%name/arch/{arch_info.h,signal_internal.h,time_internal.h} \
%buildroot%_includedir/%name/arch

install -m644 src/ltfsprintf.h %buildroot%_includedir/%name

install -d %buildroot%_includedir/%name/tape_drivers
install -m644 src/tape_drivers/tape_drivers.h \
%buildroot%_includedir/%name/tape_drivers

ln -s %_includedir/ltfs %buildroot%_includedir/libltfs

# pkg-config for devel
sed -e 's|@VERSION@|%version|g' -e 's|@LIBDIR@|%_libdir|g' \
-e 's|@INCLUDEDIR@|%_includedir/lib%name|' %SOURCE2 > %name.pc

install -d -m755 %buildroot%_pkgconfigdir
install -m644 %name.pc %buildroot%_pkgconfigdir

find %buildroot -type f '(' -iname \*.a -o -iname \*.la ')' -print -delete

%files
%doc doc/COPYING.LIB doc/README doc/NOTICES.txt
%_bindir/ltfs
%_bindir/ltfsck
%_bindir/mkltfs
%_bindir/unltfs
%dir %_datadir/%name
%_datadir/%name/ltfs
%dir %_datadir/snmp
%_datadir/snmp/*.txt
%_unitdir/%name.service
%config %_initdir/%name
%config(noreplace) %_sysconfdir/ltfs.conf
%config(noreplace) %_sysconfdir/ltfs.conf.local

%files devel
%_libdir/lib%name.so
%dir %_includedir/%name
%_includedir/%name/*.h
%dir %_includedir/%name/arch
%_includedir/%name/arch/*.h
%dir %_includedir/%name/tape_drivers
%_includedir/%name/tape_drivers/*.h
%_includedir/lib%name
%dir %_libdir/%name
%_libdir/%name/*.so
%_pkgconfigdir/%name.pc

%files libs
%_libdir/lib%name.so.*

%changelog
* Fri Mar 29 2024 Sergey Gvozdetskiy <serjigva@altlinux.org> 3.5.0-alt1
- Initial build for Sisyphus (Closes: #48688)
