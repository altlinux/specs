%define _unpackaged_files_terminate_build 1
%define sover 0
%define libname signatureimage
%define lib_c_wrapper_name signimage_c_wrapper

Name: signature-image
Version: 0.1
Release: alt1

Summary: A library for creating a digital signature image
License: GPL-2.0-only
Group: System/Libraries
Url: https://gitlab.basealt.space/fomchenkovda/signatureimg

Source: %name-%version.tar

BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: libImageMagick-devel

%description
%summary

%package -n lib%libname%sover
Summary: %summary
Group: System/Libraries

%description -n lib%libname%sover
%summary

%package -n lib%libname-devel
Summary: Development files for the %name library
Group: System/Libraries
Requires: lib%libname%sover = %EVR

%description -n lib%libname-devel
%summary

%package -n lib%lib_c_wrapper_name%sover
Summary: A C wrapper for working with the %name library
Group: System/Libraries
Requires: lib%libname%sover = %EVR

%description -n lib%lib_c_wrapper_name%sover
%summary

%package -n lib%lib_c_wrapper_name-devel
Summary: Development files for the %lib_c_wrapper_name library
Group: System/Libraries
Requires: lib%lib_c_wrapper_name%sover = %EVR

%description -n lib%lib_c_wrapper_name-devel
%summary

%prep
%setup
%cmake -DBUILD_TESTS=OFF
%cmake_build

%install
%cmake_install

%files -n lib%libname%sover
%_libdir/lib%libname.so.%{sover}*

%files -n lib%lib_c_wrapper_name%sover
%_libdir/lib%lib_c_wrapper_name.so.%{sover}*

%files -n lib%libname-devel
%_libdir/lib%libname.so
%_includedir/SignatureImage/*.hpp
%_libdir/cmake/SignatureImage/*.cmake

%files -n lib%lib_c_wrapper_name-devel
%_libdir/lib%lib_c_wrapper_name.so
%_includedir/SignatureImageCWrapper/*.hpp
%_libdir/cmake/SignatureImageCWrapper/*.cmake

%changelog
* Tue Nov 12 2024 Dmitrii Fomchenkov <sirius@altlinux.org> 0.1-alt1
- Initial build for ALT Linux
