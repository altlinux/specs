%def_disable   check
%def_enable    devel
%if_enabled    devel
%define _unpackaged_files_terminate_build 1
%endif
%define        nomen aws-crt-cpp

Name:          lib%nomen
Version:       0.43.9
Release:       alt1
Group:         Development/C++
Summary:       C++ wrapper around the aws-c-* libraries
License:       Apache-2.0
Url:           https://github.com/awslabs/aws-crt-cpp
Vcs:           https://github.com/awslabs/aws-crt-cpp.git

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-cmake
%{?!_disable_check:BuildRequires: ctest}
BuildRequires: /proc
BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: pkgconfig(libssl)
BuildRequires: cmake(aws-c-common)
BuildRequires: cmake(aws-c-sdkutils)
BuildRequires: cmake(aws-c-http)
BuildRequires: cmake(aws-c-mqtt)
BuildRequires: cmake(aws-c-auth)
BuildRequires: cmake(aws-c-s3)
BuildRequires: cmake(aws-checksums)
BuildRequires: cmake(aws-c-event-stream)

%description
C++ wrapper around the aws-c-* libraries. Provides Cross-Platform Transport
Protocols and SSL/TLS implementations for C++.

Currently Included:

* aws-c-common: Cross-platform primitives and data structures.
* aws-c-io: Cross-platform event-loops, non-blocking I/O, and TLS
  implementations.
* aws-c-mqtt: MQTT client.
* aws-c-auth: Auth signers such as Aws-auth sigv4
* aws-c-http: HTTP 1.1 client, and websockets (H2 coming soon)
* aws-checksums: Cross-Platform HW accelerated CRC32c and CRC32 with fallback to
  efficient SW implementations.
* aws-c-event-stream: C99 implementation of the vnd.amazon.event-stream
  content-type.


%package       -n %nomen
Group:         Development/C++
Summary:       C++ wrapper around the aws-c-* libraries

%description   -n %nomen
C++ wrapper around the aws-c-* libraries. Provides Cross-Platform Transport
Protocols and SSL/TLS implementations for C++.

Currently Included:

* aws-c-common: Cross-platform primitives and data structures.
* aws-c-io: Cross-platform event-loops, non-blocking I/O, and TLS
  implementations.
* aws-c-mqtt: MQTT client.
* aws-c-auth: Auth signers such as Aws-auth sigv4
* aws-c-http: HTTP 1.1 client, and websockets (H2 coming soon)
* aws-checksums: Cross-Platform HW accelerated CRC32c and CRC32 with fallback to
  efficient SW implementations.
* aws-c-event-stream: C99 implementation of the vnd.amazon.event-stream
  content-type.


%if_enabled    devel
%package       devel
Group:         Development/C++
Summary:       C++ wrapper around the aws-c-* libraries development files
Requires:      cmake
Requires:      ctest
Requires:      gcc-c++
Requires:      pkgconfig(libssl)
Requires:      cmake(aws-c-common)
Requires:      cmake(aws-c-sdkutils)
Requires:      cmake(aws-c-http)
Requires:      cmake(aws-c-mqtt)
Requires:      cmake(aws-c-auth)
Requires:      cmake(aws-c-s3)
Requires:      cmake(aws-checksums)
Requires:      cmake(aws-c-event-stream)

%description   devel
C++ wrapper around the aws-c-* libraries development files.

C++ wrapper around the aws-c-* libraries. Provides Cross-Platform Transport
Protocols and SSL/TLS implementations for C++.

Currently Included:

* aws-c-common: Cross-platform primitives and data structures.
* aws-c-io: Cross-platform event-loops, non-blocking I/O, and TLS
  implementations.
* aws-c-mqtt: MQTT client.
* aws-c-auth: Auth signers such as Aws-auth sigv4
* aws-c-http: HTTP 1.1 client, and websockets (H2 coming soon)
* aws-checksums: Cross-Platform HW accelerated CRC32c and CRC32 with fallback to
  efficient SW implementations.
* aws-c-event-stream: C99 implementation of the vnd.amazon.event-stream
  content-type.
%endif


%prep
%setup
%autopatch

%build
%cmake \
%{?!_disable_check: -DBUILD_TESTING=ON} \
   -DCMAKE_MODULE_PATH=%_libdir/cmake/ \
   -DBUILD_SHARED_LIBS=ON \
   -DBUILD_DEPS=OFF \
   -DUSE_OPENSSL=ON \
   %nil
%cmake_build

%install
%cmakeinstall_std

%check
%ctest


%files
%doc README*
%_libdir/%name.so.*

%files         -n %nomen
%doc README*
%_bindir/elasticurl_cpp
%_bindir/mqtt5_app
%_bindir/mqtt5_canary

%if_enabled    devel
%files         devel
%doc README*
%_libdir/%name.so
%_libdir/cmake/%nomen
%_includedir/aws/iot
%_includedir/aws/crt
%endif


%changelog
* Sat Oct 10 2026 Pavel Skrylev <majioa@altlinux.org> 0.43.9-alt1
- ^ 0.26.0 -> 0.43.9

* Tue Jan 02 2024 Pavel Skrylev <majioa@altlinux.org> 0.26.0-alt1
- Initial build v0.26.0 for Sisyphus
