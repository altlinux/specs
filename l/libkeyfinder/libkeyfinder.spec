Name: libkeyfinder
Version: 2.2.4
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
BuildRequires: catch2-devel

%description
libkeyfinder is a small C++11 library for estimating the musical key of digital audio.

%description -l ru_RU.UTF-8
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
sed -i 's|lib/cmake/KeyFinder|%_lib/cmake/KeyFinder|' CMakeLists.txt

%build
%cmake \
    -GNinja \
    -DCMAKE_INSTALL_LIBDIR=%_libdir \
#
%cmake_build

%install
%cmake_install

%files devel
%doc CHANGELOG.md LICENSE README.md
%dir %_includedir/keyfinder/
%_includedir/keyfinder/*.h
%_libdir/libkeyfinder.so
%_pkgconfigdir/libkeyfinder.pc
%dir %_libdir/cmake/KeyFinder/
%_libdir/cmake/KeyFinder/*

%changelog
* Thu Jul 01 2021 Leontiy Volodin <lvol@altlinux.org> 2.2.4-alt1
- Initial build for ALT Sisyphus.
