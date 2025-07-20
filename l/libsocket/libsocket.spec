Name: libsocket
Version: 2.5.0
Release: alt1

Summary: The ultimate socket library, supporting TCP, UDP and Unix sockets (DGRAM and STREAM)
License: BSD-2-Clause
Group: System/Libraries

Url: https://github.com/dermesser/libsocket
Vcs: https://github.com/dermesser/libsocket
Source: libsocket-2.5.0.tar

BuildRequires(Pre): rpm-macros-cmake
BuildRequires: gcc-c++ cmake

%description
The ultimate socket library, supporting TCP, UDP and Unix sockets (DGRAM
and STREAM). C/C++ wrappers (fully object-oriented in C++). Recent
features: IPv4/IPv6 multicast support (C/C++) +++ Linux epoll wrapper
(C++).

%package devel
Summary: Development files of libsocket
Group: Development/C++
Requires: libsocket = 2.5.0-alt1
BuildArch: noarch

%description devel
The ultimate socket library, supporting TCP, UDP and Unix sockets (DGRAM
and STREAM). C/C++ wrappers (fully object-oriented in C++). Recent
features: IPv4/IPv6 multicast support (C/C++) +++ Linux epoll wrapper
(C++).

This package contains development files of libsocket.

%prep
%setup

subst 's|"lib"|"%_libdir"|' CMakeLists.txt

%build
%cmake -DCMAKE_POLICY_VERSION_MINIMUM=3.5
%cmake_build

%install
%cmake_install

%files
%doc CONTRIBUTORS *.md doc/*
%_libdir/*.so

%files devel
%_includedir/*

%changelog
* Sun Jul 20 2025 Aleksandr Shamaraev <shad@altlinux.org> 2.5.0-alt1
- returned package
- change license
- added vcs
- 2.4.1 -> 2.5.0 (git.6214af72, thnx ruslandh@)

* Wed Oct 31 2018 Michael Shigorin <mike@altlinux.org> 2.4.1-alt4.git20140508
- just build with gcc

* Tue Jan 09 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 2.4.1-alt3.git20140508
- Removed unsupported compiler flags.

* Wed Aug 23 2017 Michael Shigorin <mike@altlinux.org> 2.4.1-alt2.git20140508
- E2K: avoid clang
- minor spec cleanup

* Fri Sep 05 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.4.1-alt1.git20140508
- Initial build for Sisyphus

