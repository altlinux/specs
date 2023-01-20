Name: rpi-userland
Version: 20220615
Release: alt1

Summary: ARM side libraries and programs used on Raspberry Pi.
License: BSD License (no advertising)
Group: System/Base
URL: https://github.com/raspberrypi/userland.git
Packager: Dmitry Terekhin <jqt4@altlinux.org>
ExclusiveArch: armh aarch64
Source: %name-%version.tar
BuildRequires: cmake gcc gcc-c++

%description
%summary

%package -n rpi-vcgencmd
Summary: Query the VideoCore for information.
Group: System/Base

%description -n rpi-vcgencmd
vcgencmd is a command line utility
that can get various pieces of information
from the VideoCore GPU on the Raspberry Pi.

%prep
%setup
sed -i 's/add_subdirectory/#add_subdirectory/' CMakeLists.txt
sed -i 's/#add_subdirectory(interface\/vcos)/add_subdirectory(interface\/vcos)/' CMakeLists.txt
sed -i 's/#add_subdirectory(interface\/vchiq_arm)/add_subdirectory(interface\/vchiq_arm)/' CMakeLists.txt
sed -i 's/#add_subdirectory(interface\/vmcs_host)/add_subdirectory(interface\/vmcs_host)/' CMakeLists.txt
sed -i 's/#add_subdirectory(host_applications\/linux)/add_subdirectory(host_applications\/linux)/' CMakeLists.txt
sed -i 's/add_subdirectory/#add_subdirectory/' host_applications/linux/CMakeLists.txt
sed -i 's/#add_subdirectory(apps\/gencmd)/add_subdirectory(apps\/gencmd)/' host_applications/linux/CMakeLists.txt

%build
%ifarch %arm
%cmake -DARM64=OFF
%endif
%ifarch aarch64
%cmake -DARM64=ON
%endif
%cmake -DCMAKE_SKIP_RPATH:BOOL=ON
%cmake_build

%install
install -D build/bin/vcgencmd %buildroot%_bindir/vcgencmd
install -D host_applications/linux/apps/gencmd/vcgencmd.1 %buildroot%_mandir/man1/vcgencmd.1
install -D build/lib/libvchiq_arm.so %buildroot%_libdir/libvchiq_arm.so
install -D build/lib/libvcos.so %buildroot%_libdir/libvcos.so

%files -n rpi-vcgencmd
%_bindir/vcgencmd
%_mandir/man1/vcgencmd.1.xz
%_libdir/libvchiq_arm.so
%_libdir/libvcos.so

%changelog
* Thu Jan 19 2023 Dmitry Terekhin <jqt4@altlinux.org> 20220615-alt1
- Updated

* Thu May 27 2021 Dmitry Terekhin <jqt4@altlinux.org> 20210527-alt1
- Initial build
