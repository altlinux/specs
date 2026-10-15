%def_disable   check
%def_enable    devel
%{?!_disable_devel:%define _unpackaged_files_terminate_build 1}
%define        nomen aws-c-mqtt

Name:          lib%nomen
Version:       1.0.0
Release:       alt1
Group:         Development/C
Summary:       C99 implementation of the MQTT 3.1.1 specification
License:       Apache-2.0
Url:           https://github.com/awslabs/aws-c-mqtt
Vcs:           https://github.com/awslabs/aws-c-mqtt.git

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-cmake
%{?!_disable_check:BuildRequires: ctest}
BuildRequires: /proc
BuildRequires: cmake
BuildRequires: clang-tools
BuildRequires: cmake(aws-c-http)

%description
C99 implementation of the MQTT 3.1.1 and MQTT 5 specifications.


%if_enabled    devel
%package       devel
Group:         Development/C
Summary:       C99 implementation of the MQTT 3.1.1 specification development files

Requires:      ctest
Requires:      cmake
Requires:      clang-tools
Requires:      cmake(aws-c-http)

%description   devel
Development headers and libraries for %nomen.

C99 implementation of the MQTT 3.1.1 and MQTT 5 specifications.
%endif


%package       -n elastipubsub
Group:         Development/C
Summary:       Aws Crypto Abstraction Layer executables

%description   -n elastipubsub
Aws Crypto Abstraction Layer executables.

Aws Crypto Abstraction Layer: Cross-Platform, C99 wrapper for cryptography
primitives.


%prep
%setup
%autopatch

%build
%cmake \
   -DCMAKE_MODULE_PATH=%_libdir/cmake \
   -DCMAKE_PREFIX_PATH=%_usr \
   -DCMAKE_C_COMPILER=clang \
   -DBUILD_SHARED_LIBS=ON \
   -DASSERT_LOCK_HELD=ON \
   %nil
%cmake_build

%install
%cmakeinstall_std

%check
%ctest


%files
%doc README*
%_libdir/%name.so.*

%if_enabled    devel
%files         devel
%doc README*
%_libdir/%name.so
%_libdir/cmake/%nomen
%_includedir/aws/mqtt
%endif

%files         -n elastipubsub
%_bindir/elastipubsub
%_bindir/elastipubsub5
%_bindir/elastishadow
%_bindir/mqtt5canary


%changelog
* Wed Oct 07 2026 Pavel Skrylev <majioa@altlinux.org> 1.0.0-alt1
- ^ 0.10.1 -> 1.0.0

* Wed Jan 03 2024 Pavel Skrylev <majioa@altlinux.org> 0.10.1-alt1
- Initial build v0.10.1 for Sisyphus
