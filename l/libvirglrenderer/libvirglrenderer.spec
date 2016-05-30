
Name: libvirglrenderer
Version: 0.5.0
Release: alt1

Summary: Virgl Rendering library
Group: System/Libraries
License: MIT

#VCS: git:git://people.freedesktop.org/~airlied/virglrenderer
Source: %name-%version.tar

BuildRequires: pkgconfig(libdrm) >= 2.4.50
BuildRequires: pkgconfig(gbm)
BuildRequires: pkgconfig(epoxy)

%description
The virgil3d rendering library is a library used by
qemu to implement 3D GPU support for the virtio GPU.

%package devel
Summary: Virgil3D renderer development files
Group: Development/C

Requires: %name = %version-%release

%description devel
Virgil3D renderer development files, used by
qemu to build against.

%package test-server
Summary: Virgil3D renderer testing server
Group: Emulators

Requires: %name = %version-%release

%description test-server
Virgil3D renderer testing server is a server
that can be used along with the mesa virgl
driver to test virgl rendering without GL.

%prep
%setup

%build
%autoreconf
%configure --disable-silent-rules
%make_build

%install
%makeinstall_std

%files
%doc COPYING
%_libdir/*.so.*

%files devel
%_includedir/virgl
%_libdir/*.so
%_pkgconfigdir/*.pc

%files test-server
%_bindir/virgl_test_server

%changelog
* Thu May 19 2016 Alexey Shabalin <shaba@altlinux.ru> 0.5.0-alt1
- 0.5.0

* Thu Dec 17 2015 Alexey Shabalin <shaba@altlinux.ru> 0.3.0-alt0.1.git.e9d3c0c27
- initial build

