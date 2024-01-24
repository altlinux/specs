%define        _unpackaged_files_terminate_build 1

Name:          aws-crt-cpp
Version:       0.26.0
Release:       alt1
Group:         Development/C++
Summary:       C++ wrapper around the aws-c-* libraries
License:       Apache-2.0
Url:           https://github.com/aws/aws-sdk-cpp
Vcs:           https://github.com/aws/aws-sdk-cpp.git

Source:        %name-%version.tar
Patch:         path.patch
BuildRequires(pre): rpm-macros-cmake
BuildRequires: /proc
BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: libssl-devel
BuildRequires: libaws-c-common-devel
BuildRequires: libaws-c-sdkutils-devel
BuildRequires: libaws-c-http-devel
BuildRequires: libaws-c-mqtt-devel
BuildRequires: libaws-c-auth-devel
BuildRequires: libaws-c-s3-devel
BuildRequires: libaws-checksums-devel
BuildRequires: libaws-c-event-stream-devel

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


%package       -n lib%name
Group:         Development/C++
Summary:       C++ wrapper around the aws-c-* libraries

%description   -n lib%name
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


%package       -n lib%name-devel
Group:         Development/C++
Summary:       C++ wrapper around the aws-c-* libraries development files
Requires:      lib%name = %EVR
Requires:      /proc
Requires:      cmake
Requires:      gcc-c++
Requires:      libssl-devel
Requires:      libaws-c-common-devel
Requires:      libaws-c-sdkutils-devel
Requires:      libaws-c-http-devel
Requires:      libaws-c-mqtt-devel
Requires:      libaws-c-auth-devel
Requires:      libaws-c-s3-devel
Requires:      libaws-checksums-devel
Requires:      libaws-c-event-stream-devel

%description   -n lib%name-devel
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


%prep
%setup
%autopatch

%build
%cmake_insource \
   -DCMAKE_MODULE_PATH=%_libdir/cmake/ \
   -DBUILD_SHARED_LIBS=ON \
   -DBUILD_DEPS=OFF \
   -DBUILD_TESTING=ON \
   -DUSE_OPENSSL=ON

%cmake_build

%install
%cmakeinstall_std

%check
#%make test

%files
%doc README*
%_bindir/*

%files         -n lib%name
%doc README*
%_libdir/lib%name.so

%files         -n lib%name-devel
%doc README*
%_libdir/cmake/%name
%_includedir/aws/iot
%_includedir/aws/crt


%changelog
* Tue Jan 02 2024 Pavel Skrylev <majioa@altlinux.org> 0.26.0-alt1
- Initial build v0.26.0 for Sisyphus
