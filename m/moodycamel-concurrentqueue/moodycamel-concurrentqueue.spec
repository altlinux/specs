%define _unpackaged_files_terminate_build 1

%define project_name concurrentqueue

Name:    moodycamel-%project_name
Version: 1.0.4
Release: alt1

Summary: A fast multi-producer, multi-consumer lock-free concurrent queue for C++11
License: BSD-2-Clause OR BSL-1.0
Group:   Development/C++
Url:     https://github.com/cameron314/concurrentqueue

Source: %name-%version.tar

BuildRequires(pre): cmake
BuildRequires: gcc-c++

%description
An industrial-strength lock-free queue for C++.

Features
  - Knock-your-socks-off blazing fast performance.
  - Single-header implementation. Just drop it in your project.
  - Fully thread-safe lock-free queue.Use concurrently from any
  number of threads.
  - C++11 implementation -- elements are moved (instead of copied)
  where possible.
  - Templated, obviating the need to deal exclusively with pointers -- memory
  is managed for you.
  - No artificial limitations on element types or maximum count.
  - Memory can be allocated once up-front, or dynamically as needed.
  - Fully portable (no assembly; all is done through standard C++11 primitives).
  - Supports super-fast bulk operations.
  - Includes a low-overhead blocking version (BlockingConcurrentQueue).
  - Exception safe.

%package devel
Summary: Development files for %name
Group: Development/C++
Provides: %name = %EVR

%description devel
An industrial-strength lock-free queue for C++.

Features
  - Knock-your-socks-off blazing fast performance.
  - Single-header implementation. Just drop it in your project.
  - Fully thread-safe lock-free queue.Use concurrently from any
  number of threads.
  - C++11 implementation -- elements are moved (instead of copied)
  where possible.
  - Templated, obviating the need to deal exclusively with pointers -- memory
  is managed for you.
  - No artificial limitations on element types or maximum count.
  - Memory can be allocated once up-front, or dynamically as needed.
  - Fully portable (no assembly; all is done through standard C++11 primitives).
  - Supports super-fast bulk operations.
  - Includes a low-overhead blocking version (BlockingConcurrentQueue).
  - Exception safe.

The %name-devel package contains libraries and header files
for developing applications that use %name.

%prep
%setup

%build
%cmake
%cmake_build

%install
%cmakeinstall_std

%files devel
%doc *.md
%_includedir/%project_name
%_cmakedir/%project_name

%changelog
* Fri Nov 28 2025 Nikita Shmatko <nash@altlinux.org> 1.0.4-alt1
- Initial build for Sisyphus.
