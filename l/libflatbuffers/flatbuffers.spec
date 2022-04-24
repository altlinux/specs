%define sover 2
%define desc FlatBuffers is a cross platform serialization library architected \
for maximum memory efficiency. It allows you to directly access serialized data \
without parsing/unpacking it first, while still having great forwards/backwards \
compatibility.

Name: libflatbuffers
Version: 2.0.6
Release: alt1

Summary: Memory Efficient Serialization Library
License: APL
Group: System/Libraries
Url: https://google.github.io/flatbuffers/

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires:  python3-devel
BuildRequires:  python3-module-setuptools
BuildRequires: cmake ctest gcc-c++

%description
%desc

%package -n %name%sover
Summary: Memory Efficient Serialization Library
Group: System/Libraries

%description -n %name%sover
%desc

%package devel
Summary: Memory Efficient Serialization Library
Group: Development/C++

%description devel
%desc
This package contains development part of FlatBuffers.

%package -n python3-module-flatbuffers
Summary: Python3 files for %name
Group: Development/Python3
Requires: %name%sover = %EVR

%description -n python3-module-flatbuffers
This package contains python files for %name.

%prep
%setup
%add_optflags -Wno-class-memaccess -Wno-stringop-overflow
%ifarch %e2k
sed -i 's,-Werror -Wextra -Werror=shadow,,' CMakeLists.txt
%endif

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

pushd python
%python3_build
popd

%check
make test

%install
%makeinstall_std
pushd python
%python3_install
popd
[ %python3_sitelibdir = %python3_sitelibdir_noarch ] ||
  (
    mkdir -p %buildroot%python3_sitelibdir
    mv %buildroot%python3_sitelibdir_noarch/* %buildroot%python3_sitelibdir
  )

%files -n %name%sover
%_libdir/%name.so.*

%files devel
%_bindir/flatc
%_includedir/flatbuffers
%_libdir/cmake/flatbuffers
%_libdir/%name.so
%_pkgconfigdir/flatbuffers.pc

%files -n python3-module-flatbuffers
%python3_sitelibdir/*

%changelog
* Sun Apr 24 2022 Nazarov Denis <nenderus@altlinux.org> 2.0.6-alt1
- 2.0.6 released

* Wed Jul 07 2021 Nazarov Denis <nenderus@altlinux.org> 2.0.0-alt1
- 2.0.0 released

* Thu May 20 2021 Anton Midyukov <antohami@altlinux.org> 1.12.0-alt3
- build python3-module-flatbuffers

* Sat Apr 17 2021 Michael Shigorin <mike@altlinux.org> 1.12.0-alt2
- E2K: workaround ftbfs with (stricter) lcc

* Tue Jan 26 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.12.0-alt1
- 1.12.0 released

* Tue Dec 03 2019 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.11.0-alt1
- 1.11.0 released

* Fri Jun 07 2019 Michael Shigorin <mike@altlinux.org> 1.10.0-alt1.1
- E2K: explicit -std=c++11; avoid -Werror for now

* Wed Jan 30 2019 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.10.0-alt1
- initial
