%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1

Name: libnitrokey
Version: 3.8
Release: alt2

Summary: A library to communicate with Nitrokey devices

Group: System/Libraries
License: LGPLv3+
Url: https://github.com/Nitrokey/libnitrokey

Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-macros-cmake
BuildRequires: gcc-c++ cmake
BuildRequires: libhidapi-devel libusb-devel
BuildRequires: doxygen graphviz

%global desc \
libnitrokey is a project to communicate with Nitrokey Pro and \
Storage devices in a clean and easy manner. Written in C++14, \
with C API, Python access.

%description
%desc

%package devel
Summary: A library to communicate with Nitrokey development devices
Group: System/Libraries

%description devel
%desc

This package contains libnitrokey headers and other devel files.

%package doc
Group: System/Libraries
Summary: The libnitrokey API documentation 
Buildarch: noarch

%description doc
%desc

This package contains doxygen-generated libnitrokey API HTML documentation.

%prep
%setup
%patch -p1
# upstream forgot to bump the library version
sed '/project.*libnitrokey.*VERSION/ s/3.7.0/%version.0/' -i CMakeLists.txt
# support systems without systemd-logind
sed 's/TAG+="uaccess"/MODE="0660", GROUP+="_cryptodev", TAG+="uaccess"/' -i data/41-nitrokey.rules

%build
%cmake -DADD_GIT_INFO=off

%cmake_build
%cmake_build -t doc

%install
%cmakeinstall_std

%pre
groupadd -r _cryptodev ||:

%files
%_libdir/%name.so.*
%_udev_rulesdir/*
%doc *.md

%files devel
%_libdir/%name.so
%_includedir/%name
%_pkgconfigdir/*.pc

%files doc
%doc %_cmake__builddir/doc/html/*

%changelog
* Mon Dec 02 2024 Andrew Savchenko <bircoph@altlinux.org> 3.8-alt2
- Support setups without systemd-logind in udev rules.

* Thu Nov 07 2024 Andrew Savchenko <bircoph@altlinux.org> 3.8-alt1
- Initial version.
