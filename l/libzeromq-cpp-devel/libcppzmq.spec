# Header-only library.
Name:           libzeromq-cpp-devel
Version:        4.8.1
Release:        alt1

Summary:        Header-only C++ binding for libzmq

License:        MIT
Group: 		Development/C++
URL:            https://zeromq.org
# https://github.com/zeromq/cppzmq
Source0:        %name-%version.tar

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  libzeromq-devel
BuildRequires:  catch2-devel

BuildArch:	noarch

%description
cppzmq is a C++ binding for libzmq.

cppzmq maps the libzmq C API to C++ concepts. In particular, it is type-safe,
provides exception-based error handling, and provides RAII-style classes that
automate resource management. cppzmq is a light-weight, header-only binding.

%prep
%setup

%build
%cmake
%cmake_build

%install
%cmake_install

%files
%doc README.md
%_includedir/zmq*.hpp
%_datadir/cmake/*

%changelog
* Wed Feb 16 2022 Grigory Ustinov <grenka@altlinux.org> 4.8.1-alt1
- Build as separate package (previous version was in zeromq).
