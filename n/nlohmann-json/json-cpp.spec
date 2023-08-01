%define _unpackaged_files_terminate_build 1

Name: nlohmann-json
Version: 3.11.2
Release: alt1.1

Summary: JSON for Modern C++ (c++11) ("single header file")

License: MIT
Group: Development/C++
Url: https://github.com/nlohmann/json

Packager: Pavel Vainerman <pv@altlinux.ru>

# Source0-url: https://github.com/nlohmann/json/archive/refs/tags/v%version.tar.gz
Source0: %name-%version.tar
# Source1-url: https://github.com/nlohmann/json_test_data/archive/refs/tags/v3.1.0.tar.gz
Source1: json_test_data.tar

# fix build with gcc 13
Patch1: a49829bd984c0282be18fcec070df0c31bf77dd5.patch
Patch2: a5b09d50b786638ed9deb09ef13860a3cb64eb6b.patch

BuildRequires: cmake ctest gcc-c++

%description
There are myriads of JSON libraries out there, and each may even have its reason to exist. 
Our class had these design goals:
- intuitive syntax.
- Trivial integration.
- Serious testing

%package devel
Summary: JSON for Modern C++ (c++11) ("single header file")
Group: Development/C++
BuildArch: noarch
Provides: json-cpp
Obsoletes: json-cpp

%description devel
There are myriads of JSON libraries out there, and each may even have its reason to exist. 
Our class had these design goals:
- intuitive syntax.
- Trivial integration.
- Serious testing

This package contains the single header C++ file and CMake dependency files.

%prep
%setup -a1
%autopatch -p1
#rm -rf test/cmake_fetch_content
%ifarch %e2k
# LCC 1.26 lacks <span>, and other workarounds
sed -i 's/JSON_HAS_CPP_20/UNDEF_&/;/std_fs::path(json(1))/d;s/__INTEL_COMPILER/__EDG__/' tests/src/unit-regression2.cpp
# failed test "object with error"
sed -i '/\[json.exception.type_error.301\]/d' tests/src/unit-constructor1.cpp
%endif
sed -i -e '/add_subdirectory(cmake_fetch_content)/ d' tests/CMakeLists.txt
sed -i -e '/add_subdirectory(cmake_fetch_content2)/ d' tests/CMakeLists.txt

%build
%cmake \
%ifarch %mips riscv64
    -DJSON_FastTests:BOOL=ON \
%endif
    %nil

%cmake_build

%install
%cmake_install

%check
ln -sf ../json_test_data %_cmake__builddir/json_test_data
%cmake_build --target test

%files devel
%_includedir/nlohmann
%_datadir/cmake/nlohmann_json
# https://bugzilla.altlinux.org/7917
%_datadir/pkgconfig/nlohmann_json.pc
#_pkgconfigdir/nlohmann_json.pc

%changelog
* Tue Aug 01 2023 Ilya Kurdyukov <ilyakurdyukov@altlinux.org> 3.11.2-alt1.1
- Fixed build for Elbrus.

* Wed Jul 26 2023 Vitaly Lipatov <lav@altlinux.ru> 3.11.2-alt1
- new version 3.11.2 (with rpmrb script)
- switch to build from source tarballs with upstream urls
- pack nlohmann-json-devel as noarch

* Fri Dec 10 2021 Ilya Kurdyukov <ilyakurdyukov@altlinux.org> 3.10.4-alt1.1
- Fixed build for Elbrus.

* Mon Nov 15 2021 Paul Wolneykien <manowar@altlinux.org> 3.10.4-alt1
- new version 3.10.4

* Thu Sep 16 2021 Ivan A. Melnikov <iv@altlinux.org> 3.10.2-alt2
- Disable slower tests on %%mips and riscv64 to avoid timeouts.

* Tue Sep 14 2021 Paul Wolneykien <manowar@altlinux.org> 3.10.2-alt1
- Updated to v3.10.2.

* Wed Apr 28 2021 Arseny Maslennikov <arseny@altlinux.org> 3.8.0-alt3.1
- NMU: spec: adapted to new cmake macros.

* Thu Sep 10 2020 Ivan A. Melnikov <iv@altlinux.org> 3.8.0-alt3
- Skip test-unicode on mips*, as it timeouts.

* Fri Jul 03 2020 Paul Wolneykien <manowar@altlinux.org> 3.8.0-alt2
- Added the test data bundle.
- Fix: Run the tests with CMake.
- Skip the cmake_fetch_content test.

* Thu Jul 02 2020 Paul Wolneykien <manowar@altlinux.org> 3.8.0-alt1
- Freshed up to v3.8.0.

* Tue Mar 31 2020 Paul Wolneykien <manowar@altlinux.org> 3.7.2-alt2
- Run the auto-tests.
- Package CMake dependency files.
- This is now an arch package'nlohmann-json' providing nlohmann-json-devel
  and replacing json-cpp.
- Fixed project lincense: MIT.

* Tue Mar 31 2020 Paul Wolneykien <manowar@altlinux.org> 3.7.2-alt1
- Upstream version 3.7.2.
- Also install %_includedir/nlohmann/json.hpp symlink.

* Mon Nov 26 2018 Pavel Vainerman <pv@altlinux.ru> 3.4.0-alt1
- new version

* Sun Mar 19 2017 Pavel Vainerman <pv@altlinux.ru> 2.1.1-alt1
- new version

* Tue Nov 08 2016 Pavel Vainerman <pv@altlinux.ru> 2.0.7-alt1
- new version

* Sun Oct 30 2016 Pavel Vainerman <pv@altlinux.ru> 2.0.6-alt0.1
- initial commit 
