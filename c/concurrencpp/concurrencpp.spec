%define soversion 0
%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%set_verify_elf_method strict

Name: concurrencpp
Version: 0.1.7
Release: alt1

Summary: C++ concurrency library based on coroutines
Summary(ru_RU.UTF-8): Библиотека конкурентного программирования на C++ на основе сопрограмм
License: MIT
Group: System/Libraries
Url: https://github.com/David-Haim/concurrencpp
Vcs: https://github.com/David-Haim/concurrencpp.git


Source0: %name-%version.tar
Patch0: %name-%version-alt1-i586-when-all.patch

BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake ctest gcc-c++

%description
concurrencpp is a C++20 concurrency library that provides executors,
coroutines, asynchronous synchronization primitives, timers, and generators.

%description -l ru_RU.UTF-8
concurrencpp — библиотека конкурентного программирования на C++20,
предоставляющая исполнители, сопрограммы, асинхронные примитивы синхронизации,
таймеры и генераторы.

%package -n lib%name%soversion
Summary: Runtime library for concurrencpp
Summary(ru_RU.UTF-8): Разделяемая библиотека времени выполнения concurrencpp
Group: System/Libraries

%description -n lib%name%soversion
This package contains the shared runtime library for concurrencpp.

%description -n lib%name%soversion -l ru_RU.UTF-8
Пакет содержит разделяемую библиотеку времени выполнения concurrencpp.

%package -n lib%name-devel
Summary: Development files for concurrencpp
Summary(ru_RU.UTF-8): Файлы для разработки с concurrencpp
Group: Development/C++
Requires: lib%name%soversion = %EVR

%description -n lib%name-devel
This package contains headers and CMake files needed to develop applications
with concurrencpp.

%description -n lib%name-devel -l ru_RU.UTF-8
Пакет содержит заголовочные файлы и файлы CMake, необходимые для разработки
приложений с использованием concurrencpp.

%prep
%setup
%autopatch -p1

%build
%cmake \
    -DBUILD_SHARED_LIBS:BOOL=ON
%cmake_build

pushd test
%cmake \
    -DBUILD_SHARED_LIBS:BOOL=ON
%cmake_build
popd

%install
%cmake_install

%check
pushd test
%ctest
popd

%files -n lib%name%soversion
%doc LICENSE.txt
%_libdir/lib%name.so.%{soversion}*

%files -n lib%name-devel
%doc README.md
%_includedir/%name-%version
%_libdir/lib%name.so
%_libdir/cmake/%name-%version

%changelog
* Tue Aug 11 2026 Georgij Tsarin <crystarm@altlinux.org> 0.1.7-alt1
- Initial build for Sisyphus.
