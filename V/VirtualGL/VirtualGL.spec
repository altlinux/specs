Name: VirtualGL
Version: 2.3
Release: alt1

%define vgl_name vgl

Summary: Runs remote OpenGL applications with full 3D hardware acceleration.
License: LGPL
#Group: System/Libraries
Group: Graphics

Url: http://virtualgl.org
Packager: Dmitry Derjavin <dd@altlinux.org>

Source: %name-%version.tar
Source1: vglserver
Source2: README.ALT-ru_RU.UTF-8

Patch1: VirtualGL-2.2.90-alt-remove-solaris-stuff.patch
Patch2: VirtualGL-2.2.90-alt-xauth.patch
Patch3: VirtualGL-2.2.90-alt-nettest.patch
Patch4: VirtualGL-2.2.90-alt-fix-linkage.patch
Patch5: VirtualGL-2.2.90-alt-system-fltk.patch

BuildRequires: cmake gcc-c++ libGL-devel libGLU-devel libXv-devel libssl-devel libturbojpeg-devel libjpeg-devel libfltk-devel

%description
With VirtualGL, the OpenGL commands and 3D data are redirected to a 3D
graphics accelerator on the application server, and only the rendered
3D images are sent to the client machine. VirtualGL thus "virtualizes"
3D graphics hardware, allowing it to be co-located in the "cold room"
with compute and storage resources.

%package devel
Summary: VirtualGL development files
Group: Development/Other
Requires: %name

%description devel
With VirtualGL, the OpenGL commands and 3D data are redirected to a 3D
graphics accelerator on the application server, and only the rendered
3D images are sent to the client machine. VirtualGL thus "virtualizes"
3D graphics hardware, allowing it to be co-located in the "cold room"
with compute and storage resources.

This package contains VirtualGL development libraries.

%prep
%setup

%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1

%build
mkdir BUILD
pushd BUILD
cmake -DCMAKE_BUILD_TYPE="Release" -DCMAKE_INSTALL_PREFIX:PATH=%_usr \
-DVGL_LIBDIR:PATH=%_libdir -DVGL_FAKELIBDIR:PATH=%_libdir/%vgl_name \
-DTJPEG_INCLUDE_DIR=/usr/include -DTJPEG_LIBRARY:PATH=turbojpeg \
-DVGL_DOCDIR=%_datadir/doc/%name-%version -DVGL_BUILDSTATIC=OFF -DVGL_USESSL=ON ..
%make_build VERBOSE=1
popd

%install
pushd BUILD
%makeinstall_std
popd
mkdir -p %buildroot%_sbindir
install -pD -m 755 %SOURCE1 %buildroot%_sbindir
mkdir -p %buildroot%_localstatedir/%vgl_name
pushd %buildroot%_bindir
for file in nettest glxinfo glxspheres cpustat tcbench; do
    mv $file vgl_$file
done
mkdir -p %buildroot%_datadir/doc/%name-%version/utils
install -pD -m 644 %SOURCE2 %buildroot%_datadir/doc/%name-%version
install -pD -m 644 vglserver_config %buildroot%_datadir/doc/%name-%version/utils
install -pD -m 644 vglgenkey %buildroot%_datadir/doc/%name-%version/utils
popd

%pre
groupadd -r -f xgrp

%post
chgrp xgrp %_localstatedir/%vgl_name
chmod 2755 %_localstatedir/%vgl_name

%files
%_bindir/vgl*
%_sbindir/vgl*
%_libdir/%vgl_name
%_libdir/lib??faker.so
%_localstatedir/%vgl_name
%doc %_datadir/doc/%name-%version

%files devel
%_includedir/*.h

%changelog
* Mon Dec 26 2011 Dmitry Derjavin <dd@altlinux.org> 2.3-alt1
- [2.3] (closes: 26707)

* Thu Nov 17 2011 Ivan A. Melnikov <iv@altlinux.org> 2.2.90-alt5
- use system fltk.

* Thu Nov 17 2011 Dmitry Derjavin <dd@altlinux.org> 2.2.90-alt4
- rrfaker linkage fixed, thanks to iv@;
- minor cleanup.

* Thu Nov 17 2011 Dmitry Derjavin <dd@altlinux.org> 2.2.90-alt3
- minor patch for vglconnect to fit our paths changes;
- README update.

* Wed Nov 16 2011 Dmitry Derjavin <dd@altlinux.org> 2.2.90-alt2
- vglserver_config and vglgenkey moved to documentation -> utils;
- vglserver added to run 3D-enabled X-server from inittab;
- vglrun patched to interact with vglserver smoothly;
- ALT cpecific README added.

* Mon Nov 14 2011 Dmitry Derjavin <dd@altlinux.org> 2.2.90-alt1
- Initial ALT Linux build.

