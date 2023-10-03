%define _cmake__builddir BUILD

Name: libkeyfinder
Version: 2.2.8
Release: alt1

Summary: Musical key detection for digital audio
Summary(ru_RU.UTF-8): Обнаружение музыкального ключа для цифрового звука

License: GPL-3.0+
Group: System/Libraries
Url: https://mixxxdj.github.io/libkeyfinder

Source: https://github.com/mixxxdj/libkeyfinder/archive/%version/%name-%version.tar.gz

BuildPreReq: rpm-build-ninja
BuildRequires: gcc-c++
BuildRequires: cmake
BuildRequires: libfftw3-devel
# tests
BuildRequires: catch-devel ctest

%ifnarch i586
%if "3" <= "%{get_version catch-devel}"
%def_enable tests
%else
%def_disable tests
%endif
%else
%def_disable tests
%endif

%description
libkeyfinder is a small C++11 library for estimating the musical key of digital audio.

%description -l ru_RU.UTF-8
libkeyfinder - это небольшая библиотека на c++11 для оценки музыкального ключа цифрового звука.

%package -n libkeyfinder2
Summary: Musical key detection for digital audio
Summary(ru_RU.UTF-8): Обнаружение музыкального ключа для цифрового звука
Group: System/Libraries

%description -n libkeyfinder2
libkeyfinder is a small C++11 library for estimating the musical key of digital audio.

%description -n libkeyfinder2 -l ru_RU.UTF-8
libkeyfinder - это небольшая библиотека на c++11 для оценки музыкального ключа цифрового звука.

%package devel
Summary: Development files for %name
Summary(ru_RU.UTF-8): Файлы для разработки с помощью %name
Group: Development/Other

%description devel
libkeyfinder is a small C++11 library for estimating the musical key of digital audio.

%description devel -l ru_RU.UTF-8
libkeyfinder - это небольшая библиотека на c++11 для оценки музыкального ключа цифрового звука.

%prep
%setup

%build
%cmake \
    -GNinja \
    -DCMAKE_BUILD_TYPE=RelWithDebInfo \
%if_disabled tests
    -DBUILD_TESTING=OFF \
%endif
    -DCMAKE_INSTALL_LIBDIR=%_libdir \
#
cmake --build "%_cmake__builddir" -j%__nprocs

%install
%cmake_install

%if_enabled tests
%check
%cmake_build --target test
%endif

%files -n libkeyfinder2
%doc CHANGELOG.md LICENSE README.md
%_libdir/libkeyfinder.so.2*

%files devel
%dir %_includedir/keyfinder/
%_includedir/keyfinder/*.h
%_libdir/libkeyfinder.so
%_pkgconfigdir/libkeyfinder.pc
%dir %_libdir/cmake/KeyFinder/
%_libdir/cmake/KeyFinder/*

%changelog
* Tue Oct 03 2023 Leontiy Volodin <lvol@altlinux.org> 2.2.8-alt1
- New version.
- Enabled tests.

* Mon Jun 20 2022 Leontiy Volodin <lvol@altlinux.org> 2.2.7-alt1
- New version.
- Upstream:
  + Fix pkgconfig file when CMAKE_INSTALL_{INCLUDE,LIB}DIR
  are absolute paths.

* Mon Jan 17 2022 Leontiy Volodin <lvol@altlinux.org> 2.2.6-alt1
- New version (2.2.6).

* Thu Oct 14 2021 Leontiy Volodin <lvol@altlinux.org> 2.2.5-alt2
- Fixed build with glibc 2.34.
- Built via ninja again.

* Wed Jul 21 2021 Leontiy Volodin <lvol@altlinux.org> 2.2.5-alt1
- New version (2.2.5).
- Built with debuginfo.
- Upstream:
  + Set version for .so library and setup version symlinks.

* Fri Jul 02 2021 Leontiy Volodin <lvol@altlinux.org> 2.2.4-alt1.1
- Adapted build for p9 branch.

* Thu Jul 01 2021 Leontiy Volodin <lvol@altlinux.org> 2.2.4-alt1
- Initial build for ALT Sisyphus.
