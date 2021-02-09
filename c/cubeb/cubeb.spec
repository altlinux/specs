%set_verify_elf_method unresolved=relaxed

%define sover 0
%define cubeb_commit 8d53747d4adc3b0b03ebf79b05f1fff08c5ae8ef
%define sanitizers_cmake_commit aab6948fa863bc1cbe5d0850bc46b9ef02ed4c1a

Name: cubeb
Version: 0.2
Release: alt1.git8d53747

Summary: A cross platform audio library
License: ISC
Group: System/Libraries

Url: https://github.com/mozilla/%name
Packager: Nazarov Denis <nenderus@altlinux.org>

# https://github.com/mozilla/cubeb/archive/%cubeb_commit/%name-%cubeb_commit.tar.gz
Source0: %name-%cubeb_commit.tar
# https://github.com/arsenm/sanitizers-cmake/archive/%sanitizers_cmake_commit/sanitizers-cmake-%sanitizers_cmake_commit.tar.gz
Source1: sanitizers-cmake-%sanitizers_cmake_commit.tar

Patch0: %name-alt-pthread.patch
Patch1: %name-alt-soname.patch

BuildRequires: cmake
BuildRequires: doxygen
BuildRequires: gcc-c++
BuildRequires: graphviz

%description
Cubeb is a cross-platform library, written in C/C++, that was created and has
been maintained by the Firefox Media Team.
The role of the library is to communicate with audio devices and to provide
audio input and/or output.

%package -n lib%name%sover
Summary: A cross platform audio library
Group: System/Libraries

%description -n lib%name%sover
Cubeb is a cross-platform library, written in C/C++, that was created and has
been maintained by the Firefox Media Team.
The role of the library is to communicate with audio devices and to provide
audio input and/or output.

%package -n lib%name-devel
Summary: Development files for %name
Group: Development/C++

%description -n lib%name-devel
Development files for %name

%prep
%setup -n %name-%cubeb_commit -b 1

%patch0 -p1
%patch1 -p1

%__mv -Tf ../sanitizers-cmake-%sanitizers_cmake_commit cmake/sanitizers-cmake

%build
%__mkdir_p %_target_platform
pushd %_target_platform

cmake .. \
	-DCMAKE_INSTALL_PREFIX:PATH=%prefix \
	-DCMAKE_C_FLAGS:STRING='%optflags' \
	-DCMAKE_CXX_FLAGS:STRING='%optflags' \
	-DCMAKE_BUILD_TYPE:STRING=Release \
	-DBUILD_SHARED_LIBS:BOOL=TRUE \
	-DBUILD_TESTS:BOOL=FALSE \
	-Wno-dev
popd

%make_build -C %_target_platform

%install
%makeinstall_std -C %_target_platform

%files
%doc AUTHORS LICENSE
%_bindir/%name-test

%files -n lib%name%sover
%_libdir/lib%name.so.*

%files -n lib%name-devel
%_libdir/lib%name.so
%dir %_libdir/cmake/%name
%_libdir/cmake/%name/%{name}*.cmake
%dir %_includedir/%name
%_includedir/%name/%{name}*.h

%changelog
* Wed Feb 10 2021 Nazarov Denis <nenderus@altlinux.org> 0.2-alt1.git8d53747
- Initial build for ALT Linux
