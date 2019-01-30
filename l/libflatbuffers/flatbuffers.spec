Name: libflatbuffers
Version: 1.10.0
Release: alt1

Summary: Memory Efficient Serialization Library
License: Apache
Group: System/Libraries
Url: https://google.github.io/flatbuffers/

Source: %name-%version.tar

BuildRequires: cmake ctest gcc-c++

%package devel
Summary: Memory Efficient Serialization Library
Group: Development/C++

%define desc FlatBuffers is a cross platform serialization library architected \
for maximum memory efficiency. It allows you to directly access serialized data \
without parsing/unpacking it first, while still having great forwards/backwards \
compatibility.

%description
%desc

%description devel
%desc
This package contains development part of FlatBuffers.

%prep
%setup

%build
cmake  	-DCMAKE_BUILD_TYPE=Release \
	-DCMAKE_CXX_FLAGS:STRING='%optflags' \
	-DCMAKE_INSTALL_PREFIX=%prefix \
	-DFLATBUFFERS_BUILD_FLATC=ON \
	-DFLATBUFFERS_BUILD_FLATLIB=OFF \
	-DFLATBUFFERS_BUILD_SHAREDLIB=ON \
	-DFLATBUFFERS_BUILD_TESTS=ON \
	.

%make_build

%check
make test

%install
%makeinstall_std

%files
%_libdir/lib*.so.*

%files devel
%_bindir/flatc
%_includedir/flatbuffers
%_libdir/cmake/flatbuffers
%_libdir/*.so

%changelog
* Wed Jan 30 2019 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.10.0-alt1
- initial
