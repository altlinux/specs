%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1

%def_with check

Name: process-cpp
Version: 3.1.0
Release: alt1

Summary: C++11 library for handling processes
License: LGPL-3.0-or-later
Group: Other
Url: https://gitlab.com/ubports/development/core/lib-cpp/process-cpp

Source: %name-%version.tar

# sync with version 3.0.2-2 from Debian unstable
Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-build-cmake

BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: boost-devel
BuildRequires: pkgconfig(properties-cpp)
BuildRequires: pkgconfig(gmock)
BuildRequires: ayatana-cmake-modules
BuildRequires: doxygen
BuildRequires: /usr/bin/dot

%if_with check
BuildRequires: ctest
BuildRequires: /proc
%endif

%description
process-cpp is a simple and straightforward wrapper around process
creation and control. It helps both with handling child processes and
with interacting with the current process. Some of its features include:

- Thread-safe get/set/unset operation on the current process's environment.
- Throwing and non-throwing overloads of functions when system calls are
  involved.
- Seamless redirection of input, output and error streams of child processes.
- Type-safe interaction with the virtual proc filesystem, both for reading &
  writing.

The library's main purpose is to assist in testing and when a software
component needs to carry out process creation/control tasks, e.g., a
graphical shell. To this end, the library is extensively tested and tries
to ensure fail-safe operation as much as possible.

%package -n lib%{name}
Summary: C++11 library for handling processes (runtime libraries)
Group: System/Libraries

%description -n lib%{name}
process-cpp is a simple and straightforward wrapper around process
creation and control. It helps both with handling child processes and
with interacting with the current process. Some of its features include:

- Thread-safe get/set/unset operation on the current process's environment.
- Throwing and non-throwing overloads of functions when system calls are
  involved.
- Seamless redirection of input, output and error streams of child processes.
- Type-safe interaction with the virtual proc filesystem, both for reading &
  writing.

The library's main purpose is to assist in testing and when a software
component needs to carry out process creation/control tasks, e.g., a
graphical shell. To this end, the library is extensively tested and tries
to ensure fail-safe operation as much as possible.

This package includes the process-cpp runtime libraries.

%package -n %{name}-devel
Summary: C++11 library for handling processes (dev headers and libraries)
Group: Development/C
Requires: lib%{name} = %{version}-%{release}

%description -n %{name}-devel
process-cpp is a simple and straightforward wrapper around process
creation and control. It helps both with handling child processes and
with interacting with the current process. Some of its features include:

- Thread-safe get/set/unset operation on the current process's environment.
- Throwing and non-throwing overloads of functions when system calls are
  involved.
- Seamless redirection of input, output and error streams of child processes.
- Type-safe interaction with the virtual proc filesystem, both for reading &
  writing.

The library's main purpose is to assist in testing and when a software
component needs to carry out process creation/control tasks, e.g., a
graphical shell. To this end, the library is extensively tested and tries
to ensure fail-safe operation as much as possible.

This package includes all the development headers and libraries for
process-cpp.

%package doc
Summary: C++11 library for handling processes (documentation)
Group: Documentation

%description doc
process-cpp is a simple and straightforward wrapper around process
creation and control. It helps both with handling child processes and
with interacting with the current process. Some of its features include:

- Thread-safe get/set/unset operation on the current process's environment.
- Throwing and non-throwing overloads of functions when system calls are
  involved.
- Seamless redirection of input, output and error streams of child processes.
- Type-safe interaction with the virtual proc filesystem, both for reading &
  writing.

The library's main purpose is to assist in testing and when a software
component needs to carry out process creation/control tasks, e.g., a
graphical shell. To this end, the library is extensively tested and tries
to ensure fail-safe operation as much as possible.

This package includes documentation files for the libprocess-cpp
development.

%prep
%setup
%patch -p1

%build
%cmake \
       -Wno-dev
%cmake_build

%install
%cmake_install

%check
%ctest -j1 -VV -E linux_process_test

%files
%doc AUTHORS ChangeLog COPYING README.md

%files -n lib%{name}
%_libdir/lib%{name}.so.3*

%files -n %{name}-devel
%_includedir/core/posix
%_includedir/core/testing
%_libdir/lib%{name}.so
%_libdir/pkgconfig/%{name}.pc

%files doc
%dir %_docdir/%name
%_docdir/%name/*

%changelog
* Sun Mar 15 2026 Nikolay Strelkov <snk@altlinux.org> 3.1.0-alt1
- New version 3.1.0.

* Thu Dec 04 2025 Nikolay Strelkov <snk@altlinux.org> 3.0.3-alt1
- New version 3.0.3.

* Wed Jul 16 2025 Nikolay Strelkov <snk@altlinux.org> 3.0.2-alt1
- Initial build for Sisyphus
