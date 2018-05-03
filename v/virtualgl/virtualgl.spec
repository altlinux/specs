Name: virtualgl
Version: 2.5.2
Release: alt1%ubt

%define vgl_name vgl

Summary: Runs remote OpenGL applications with full 3D hardware acceleration
License: LGPL
Group: Graphics

Url: http://virtualgl.org
#Git: https://github.com/VirtualGL/virtualgl

Source: %name-%version.tar
Source1: vglserver
Source2: README.ALT-ru_RU.UTF-8

Patch1: %name-2.5.2-alt-remove-solaris-stuff.patch
Patch2: %name-2.5.2-alt-xauth.patch
Patch3: %name-2.5.2-alt-nettest.patch
Patch4: %name-2.5.2-alt-fix-linkage.patch
# patch 5: modified RedHat libexec path patch
Patch5: %name-2.5.2-alt-libexec-path-fix.patch
# patch 6: updated Fedora Core system glx patch
Patch6: %name-2.5.2-alt-system-glx.patch

BuildRequires(pre): rpm-build-ubt
BuildRequires: cmake
BuildRequires: gcc-c++ 
BuildRequires: libXv-devel
BuildRequires: libfltk-devel
BuildRequires: libssl-devel
BuildRequires: libturbojpeg-devel

Provides: VirtualGL = %version %name = %version
Obsoletes: VirtualGL <= %version %name < %version

%description
With VirtualGL, the OpenGL commands and 3D data are redirected to a 3D
graphics accelerator on the application server, and only the rendered
3D images are sent to the client machine. VirtualGL thus "virtualizes"
3D graphics hardware, allowing it to be co-located in the "cold room"
with compute and storage resources.

%package devel
Summary: VirtualGL development files
Group: Development/Other
Requires: %name = %version
BuildArch: noarch
Provides: VirtualGL-devel = %version %name-devel = %version
Obsoletes: VirtualGL-devel <= %version %name-devel < %version

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
%patch6 -p1

sed -i -e 's,"glx.h",<GL/glx.h>,' server/*.[hc]*
# Remove bundled libraries
rm -r common/glx* server/fltk
rm doc/LICENSE-*.txt

%build
%cmake \
	-DCMAKE_BUILD_TYPE="Release" \
	-DCMAKE_INSTALL_PREFIX:PATH=%_usr \
	-DVGL_LIBDIR:PATH=%_libdir \
	-DVGL_FAKELIBDIR:PATH=%_libdir/%vgl_name \
	-DTJPEG_INCLUDE_DIR=/usr/include \
	-DTJPEG_LIBRARY:PATH=turbojpeg \
	-DVGL_DOCDIR=%_defaultdocdir/%name-%version \
	-DVGL_BUILDSTATIC=OFF \
	-DVGL_USESSL=ON \
	-DVGL_SYSTEMGLX=1 \
	-DVGL_SYSTEMFLTK=1 \
       	-DVGL_FAKEXCB=1 ..
%cmake_build VERBOSE=1

%install
mkdir -p %buildroot%_libdir/%vgl_name
%cmakeinstall_std
mkdir -p %buildroot%_sbindir
install -pD -m 755 %SOURCE1 %buildroot%_sbindir
mkdir -p %buildroot%_localstatedir/%vgl_name
pushd %buildroot%_bindir
for file in glreadtest nettest glxinfo glxspheres* cpustat tcbench; do
    mv $file vgl_$file
done

mkdir -p %buildroot%_defaultdocdir/%name-%version/utils
install -pD -m 644 %SOURCE2 %buildroot%_defaultdocdir/%name-%version
install -pD -m 644 vglserver_config %buildroot%_defaultdocdir/%name-%version/utils
install -pD -m 644 vglgenkey %buildroot%_defaultdocdir/%name-%version/utils

rm %buildroot%_bindir/vgl_glxinfo
ln -sf %_libdir/libvglfaker.so %buildroot%_libdir/%vgl_name/libGL.so

%ifarch x86_64
mkdir %buildroot%_libexecdir
mv %buildroot%_bindir/.vglrun.vars64 %buildroot%_libexecdir/vglrun.vars64
%else 
mv %buildroot%_bindir/.vglrun.vars32 %buildroot%_libexecdir/vglrun.vars32
%endif

mv %buildroot%_defaultdocdir/VirtualGL/* %buildroot%_defaultdocdir/%name-%version
popd

%pre
groupadd -r -f xgrp

%post
chgrp xgrp %_localstatedir/%vgl_name
chmod 2755 %_localstatedir/%vgl_name

%files
%_libexecdir/vglrun.vars??
%_bindir/vgl*
%_sbindir/vgl*
%_libdir/%vgl_name
%_libdir/lib??faker.so
%_libdir/libvglfaker-nodl.so
%_libdir/libvglfaker.so
%_localstatedir/%vgl_name
%doc %_defaultdocdir/%name-%version

%files devel
%_includedir/*.h

%changelog
* Wed Apr 25 2018 Nikolai Kostrigin <nickel@altlinux.org> 2.5.2-alt1%ubt
- new version build from Git src tree with updated ALTLinux patches
