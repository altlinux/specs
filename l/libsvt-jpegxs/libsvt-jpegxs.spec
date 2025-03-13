%define _unpackaged_files_terminate_build 1
%def_enable snapshot

%define _name svt-jpegxs
%define __name SvtJpegxs
%define libname lib%__name
%define git_name SVT-JPEG-XS
%define ver_major 0.9

%def_enable tools
%def_enable check

Name: lib%_name
Version: %ver_major.0
Release: alt1

Summary: Intel JPEG-XS Library
License: BSD-2-Clause-Patent and GPL-2.0-only
Group: System/Libraries
Url: https://github.com/OpenVisualCloud/SVT-JPEG-XS

Vcs: https://github.com/OpenVisualCloud/SVT-JPEG-XS.git

%if_disabled snapshot
Source: https://github.com/OpenVisualCloud/SVT-JPEG-XS/archive/v%version/%git_name-%version.tar.gz
%else
Source: %git_name-%version.tar
%endif

ExcludeArch: aarch64

BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake gcc-c++ yasm
%{?_enable_check:BuildRequires: libgtest-devel}

%description
This library is implementation of ISO/IEC 21122 protocol.

%package devel
Summary: Development files for JPEG-XS library
Group: Development/C
Requires: %name = %EVR

%description devel
This package provides JPEG-XS development files.

%package tools
Summary: The JPEG-XS library command line tools
Group: Sound
Requires: %name = %EVR

%description tools
This package provides JPEG-XS tools.

%prep
%setup -n %git_name-%version

%build
# see CMakeLists.txt:210
%add_optflags -D_FORTIFY_SOURCE=2
%cmake -DCMAKE_BUILD_TYPE=Release \
    %{?_enable_check:-DBUILD_TESTING=ON}
%nil
%cmake_build

%install
%cmake_install

%check
#%%cmake_build -t test

%files
%_libdir/%libname.so.*
%doc README* LICENSE*

%files devel
%_includedir/%_name/
%_libdir/%libname.so
%_pkgconfigdir/%__name.pc

%if_enabled tools
%files tools
%_bindir/%{__name}EncApp
%_bindir/%{__name}DecApp
%_bindir/%{__name}SampleDecoder
%_bindir/%{__name}SampleEncoder
%endif

%changelog
* Thu Mar 13 2025 Yuri N. Sedunov <aris@altlinux.org> 0.9.0-alt1
- first build for Sisyphus (v0.9.0-5-ge0940ac)


