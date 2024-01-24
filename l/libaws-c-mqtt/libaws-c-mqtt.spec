%define        _unpackaged_files_terminate_build 1
%define        oname aws-c-mqtt

Name:          lib%oname
Version:       0.10.1
Release:       alt1
Group:         Development/C
Summary:       C99 implementation of the MQTT 3.1.1 specification
License:       Apache-2.0
Url:           https://github.com/awslabs/aws-c-mqtt
Vcs:           https://github.com/awslabs/aws-c-mqtt.git

Source:        %name-%version.tar
Patch:         path.patch
BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake
BuildRequires: libaws-c-http-devel

%description
C99 implementation of the MQTT 3.1.1 and MQTT 5 specifications.


%package       devel
Group:         Development/C
Summary:       C99 implementation of the MQTT 3.1.1 specification development files

%description   devel
Development headers and libraries for %oname.

C99 implementation of the MQTT 3.1.1 and MQTT 5 specifications.


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
%cmake_insource \
   -DCMAKE_MODULE_PATH=%_libdir/cmake \
   -DBUILD_SHARED_LIBS=ON


%install
%cmakeinstall_std

%check
%make test


%files
%doc README*
%_libdir/%name.so.*

%files         devel
%doc README*
%_libdir/%name.so
%_libdir/cmake/%oname
%_includedir/aws/mqtt

%files         -n elastipubsub
%_bindir/elastipubsub
%_bindir/elastipubsub5
%_bindir/mqtt5canary


%changelog
* Wed Jan 03 2024 Pavel Skrylev <majioa@altlinux.org> 0.10.1-alt1
- Initial build v0.10.1 for Sisyphus
