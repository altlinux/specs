%define _unpackaged_files_terminate_build 1
%define soversion 6

Name: hashcat
Version: 6.2.6
Release: alt2

Summary: Advanced password recovery utility
Group: System/Base
License: MIT
Url: https://hashcat.net
VCS: https://github.com/hashcat/hashcat

Source: %name-%version.tar

BuildRequires: gcc-c++
BuildRequires: ocl-icd
BuildRequires: zlib-devel
BuildRequires: opencl-headers
BuildRequires: libxxhash-devel
BuildRequires: libminizip-ng-compat-devel

# we disable unrar, so suppress headers depending on it
%add_findreq_skiplist %_includedir/%name/emu_inc*
# we dont have fully packaged lzma-sdk, so suppress headers depending on it
%add_findreq_skiplist %_includedir/%name/types.h %_includedir/%name/ext_lzma.h
# we dont want to make dependencies based on extra tools
%add_findprov_skiplist %_datadir/%name/tools/*
%add_findreq_skiplist %_datadir/%name/tools/*
%add_findreq_skiplist %_datadir/%name/extra/*

%description
Hashcat is the world's fastest and most advanced password recovery utility,
supporting five unique modes of attack for over
300 highly-optimized hashing algorithms.
Hashcat currently supports CPUs, GPUs, and other hardware accelerators on
Linux, Windows, and macOS, and has facilities to help
enable distributed password cracking.

%package -n lib%name%soversion
Summary: Advanced password recovery utility - library
Group: System/Libraries

%description -n lib%name%soversion
Hashcat is the world's fastest and most advanced password recovery utility,
supporting five unique modes of attack for over
300 highly-optimized hashing algorithms.
Hashcat currently supports CPUs, GPUs, and other hardware accelerators on
Linux, Windows, and macOS, and has facilities to help
enable distributed password cracking.

%package -n lib%name-devel
Summary: Advanced password recovery utility - development files
Group: Development/C

%description -n lib%name-devel
%summary.

%package docs
Summary: Advanced password recovery utility - documentation
Group: Development/Documentation
BuildArch: noarch

%description docs
%summary.

# use system deps and usrmerged folders
%global mflags PREFIX=%prefix SHARED=1 SHARED_FOLDER=%_libdir/%name ENABLE_UNRAR=0
%global mflags %mflags LIBRARY_FOLDER=%_libdir DOCUMENT_FOLDER=%_datadir/%name
%global mflags %mflags USE_SYSTEM_XXHASH=1 USE_SYSTEM_OPENCL=1 USE_SYSTEM_ZLIB=1

%prep
%setup

# change flags to keep debuginfo
sed -i 's|+= -s|+= -g|' src/Makefile
sed -i 's|+= -O2|+= -O2 -g|' src/Makefile

# we use system deps, so remove bundled ones
rm -rf deps/{OpenCL-Headers,unrar,xxHash,zlib}

%build
%make_build %mflags

%install
%makeinstall_std %mflags

# create shared lib links
ln -s libhashcat.so.%version %buildroot%_libdir/libhashcat.so.%soversion
ln -s libhashcat.so.%soversion %buildroot%_libdir/libhashcat.so

# remove installed docs
rm -r %buildroot%_datadir/hashcat/docs

%files
%_bindir/hashcat
%_libdir/hashcat
%_datadir/hashcat

%files -n lib%name%soversion
%_libdir/libhashcat.so.%soversion
%_libdir/libhashcat.so.%version

%files -n lib%name-devel
%_libdir/libhashcat.so
%_includedir/*

%files docs
%doc docs/*

%changelog
* Tue Jul 30 2024 Alexander Kuznetsov <kuznetsovam@altlinux.org> 6.2.6-alt2
- Drop extra dependencies.

* Tue Jul 16 2024 Alexander Kuznetsov <kuznetsovam@altlinux.org> 6.2.6-alt1
- New spec.
- Update to 6.2.6.
- Split lib, devel and docs packages.

* Mon Dec 07 2015 Michael Shigorin <mike@altlinux.org> 2.00-alt1
- initial build for ALT Linux Sisyphus (based on openSUSE package)
