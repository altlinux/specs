Name: flatbuffers1
Version: 1.12.0
Release: alt4

Summary: Memory Efficient Serialization Library
License: APL
Group: System/Legacy libraries
Url: https://google.github.io/flatbuffers/

Source: libflatbuffers-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires:  python3-devel
BuildRequires:  python3-module-setuptools
BuildRequires: cmake ctest gcc-c++

%define desc FlatBuffers is a cross platform serialization library architected \
for maximum memory efficiency. It allows you to directly access serialized data \
without parsing/unpacking it first, while still having great forwards/backwards \
compatibility.

%description
%desc

%package -n libflatbuffers
Summary: Memory Efficient Serialization Library
Group: System/Legacy libraries

%description -n libflatbuffers
%desc

%prep
%setup -n libflatbuffers-%version
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

%files -n libflatbuffers
%_libdir/lib*.so.*

%changelog
* Wed Jul 07 2021 Nazarov Denis <nenderus@altlinux.org> 1.12.0-alt4
- Build as legacy library

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
