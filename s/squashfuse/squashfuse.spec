%define _unpackaged_files_terminate_build 1
%define soname 0


Name: squashfuse
Version: 0.5.2
Release: alt1

Summary: FUSE filesystem to mount squashfs archives
License: BSD-2-Clause
Group: File tools
URL: https://github.com/vasi/squashfuse

Source0: %name-%version.tar
Patch0: %name-%version-%release.patch

BuildRequires: libfuse3-devel
BuildRequires: libattr-devel, libzstd-devel, liblz4-devel, liblzma-devel, zlib-devel
Requires: lib%name%soname = %EVR

%description
Squashfuse lets you mount SquashFS archives in user-space. It supports almost
all features of the SquashFS format, yet is still fast and memory-efficient.
SquashFS is an efficiently compressed, read-only storage format. Support for it
has been built into the Linux kernel since 2009. It is very common on Live CDs
and embedded Linux distributions.

%package devel
Group: Development/C
Summary: Development files for %name
Requires: lib%name%soname = %EVR

%description devel
Libraries and header files for developing applications that use %name.

%package -n lib%name%soname
Group: System/Libraries
Summary: Libraries for %name

%description -n lib%name%soname
Libraries for running %name applications.

%prep
%setup
%patch0 -p1

%build
./autogen.sh
%configure --disable-static --disable-demo
%make_build

%install
%makeinstall_std
find ./ -name '*.la' -print -delete

%files
%doc LICENSE README
%_bindir/*
%_man1dir/*

%files devel
%_includedir/squashfuse/
%_pkgconfigdir/squashfuse*.pc
%_libdir/*.so

%files -n lib%name%soname
%_libdir/*.so.%{soname}*


%changelog
* Thu May 23 2024 Danil Shein <dshein@altlinux.org> 0.5.2-alt1
 - new version 0.5.2

* Fri Jul 08 2022 Danil Shein <dshein@altlinux.org> 0.1.105-alt1
 - new version 0.1.105

* Fri Dec 17 2021 Danil Shein <dshein@altlinux.org> 0.1.104-alt0.git.e51978c
- initial build for ALT

