Name: libsocket
Version: 2.4.1
Release: alt3.git20140508

Summary: The ultimate socket library, supporting TCP, UDP and Unix sockets (DGRAM and STREAM)
License: BSD
Group: System/Libraries

Url: https://github.com/dermesser/libsocket
Source: %name-%version.tar

BuildRequires: gcc-c++ cmake
%ifnarch e2k
# TODO: is it reasonable on x86 either?
BuildRequires: clang-devel
%endif

%description
The ultimate socket library, supporting TCP, UDP and Unix sockets (DGRAM
and STREAM). C/C++ wrappers (fully object-oriented in C++). Recent
features: IPv4/IPv6 multicast support (C/C++) +++ Linux epoll wrapper
(C++).

%package devel
Summary: Development files of %name
Group: Development/C++
Requires: %name = %EVR
BuildArch: noarch

%description devel
The ultimate socket library, supporting TCP, UDP and Unix sockets (DGRAM
and STREAM). C/C++ wrappers (fully object-oriented in C++). Recent
features: IPv4/IPv6 multicast support (C/C++) +++ Linux epoll wrapper
(C++).

This package contains development files of %name.

%prep
%setup

%build
%ifnarch e2k
# Clang doesn't support these options
%remove_optflags -frecord-gcc-switches
%endif

cmake \
%if %_lib == lib64
	-DLIB_SUFFIX=64 \
%endif
	-DCMAKE_INSTALL_PREFIX:PATH=%prefix \
	-DCMAKE_C_FLAGS:STRING="%optflags" \
	-DCMAKE_CXX_FLAGS:STRING="%optflags" \
	-DCMAKE_Fortran_FLAGS:STRING="%optflags" \
%ifnarch e2k
	-DCMAKE_C_COMPILER=clang \
	-DCMAKE_CXX_COMPILER=clang++ \
%endif
	-DCMAKE_STRIP:FILEPATH="/bin/echo" \
	.

%make_build VERBOSE=1

%install
%makeinstall_std

%files
%doc CONTRIBUTORS *.md doc/*
%_libdir/*.so

%files devel
%_includedir/*

%changelog
* Tue Jan 09 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 2.4.1-alt3.git20140508
- Removed unsupported compiler flags.

* Wed Aug 23 2017 Michael Shigorin <mike@altlinux.org> 2.4.1-alt2.git20140508
- E2K: avoid clang
- minor spec cleanup

* Fri Sep 05 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.4.1-alt1.git20140508
- Initial build for Sisyphus

