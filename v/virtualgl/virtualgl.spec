%define _unpackaged_files_terminate_build 1
Name: virtualgl
Version: 3.0
Release: alt1

%define vgl_name vgl

Summary: Runs remote OpenGL applications with full 3D hardware acceleration
License: LGPLv2.1
Group: Graphics

Url: http://virtualgl.org
#Git: https://github.com/VirtualGL/virtualgl

Source: %name-%version.tar
Source1: vglserver
Source2: README.ALT-ru_RU.UTF-8

Patch1: %name-2.5.90-alt-remove-solaris-stuff.patch
Patch2: %name-2.5.2-alt-xauth.patch
Patch3: %name-3.0-alt-nettest.patch
Patch4: %name-2.6.3-alt-fix-linkage.patch
# patch 5: modified RedHat libexec path patch
Patch5: %name-2.5.2-alt-libexec-path-fix.patch

BuildRequires: cmake
BuildRequires: gcc-c++ 
BuildRequires: libXtst-devel
BuildRequires: libXv-devel
BuildRequires: libfltk-devel
BuildRequires: libssl-devel
BuildRequires: libturbojpeg-devel
BuildRequires: boost-devel-headers
BuildRequires: opencl-headers
BuildRequires: ocl-icd-devel
BuildRequires: libxcbutil-keysyms-devel

Provides: VirtualGL = %EVR %name = %EVR
Obsoletes: VirtualGL <= %EVR

%description
With VirtualGL, the OpenGL commands and 3D data are redirected to a 3D
graphics accelerator on the application server, and only the rendered
3D images are sent to the client machine. VirtualGL thus "virtualizes"
3D graphics hardware, allowing it to be co-located in the "cold room"
with compute and storage resources.

%package devel
Summary: VirtualGL development files
Group: Development/Other
Requires: %name = %EVR
BuildArch: noarch
Provides: VirtualGL-devel = %EVR %name-devel = %EVR
Obsoletes: VirtualGL-devel <= %EVR

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

sed -i -e 's,"glx.h",<GL/glx.h>,' server/*.[hc]*
sed -i -e 's,"glxext.h",<GL/glxext.h>,' server/*.[hc]*
# Remove bundled libraries
rm -r server/fltk
rm doc/LICENSE-*.txt

%build
%cmake \
	-DCMAKE_BUILD_TYPE="Release" \
	-DCMAKE_INSTALL_PREFIX:PATH=%_usr \
	-DVGL_LIBDIR:PATH=%_libdir \
	-DVGL_FAKELIBDIR:PATH=%_libdir/%vgl_name \
	-DTJPEG_INCLUDE_DIR=/usr/include \
	-DTJPEG_LIBRARY:PATH=turbojpeg \
	-DCMAKE_INSTALL_DOCDIR=%_defaultdocdir/%name-%version \
	-DX11_XTest_INCLUDE_PATH=%_includedir \
	-DVGL_BUILDSTATIC=OFF \
	-DVGL_USESSL=ON \
	-DVGL_SYSTEMGLX=1 \
	-DVGL_SYSTEMFLTK=1 \
	-DVGL_FAKEOPENCL=1 \
	-DVGL_FAKEXCB=1 ..
%cmake_build

%install
mkdir -p %buildroot%_libdir/%vgl_name
%cmake_install
mkdir -p %buildroot%_sbindir
install -pD -m 755 %SOURCE1 %buildroot%_sbindir
mkdir -p %buildroot%_localstatedir/%vgl_name
pushd %buildroot%_bindir
for file in glreadtest nettest glxinfo glxspheres* cpustat tcbench eglinfo; do
    mv $file vgl_$file
done

mkdir -p %buildroot%_defaultdocdir/%name-%version/utils
install -pD -m 644 %SOURCE2 %buildroot%_defaultdocdir/%name-%version
install -pD -m 644 vglserver_config %buildroot%_defaultdocdir/%name-%version/utils
install -pD -m 644 vglgenkey %buildroot%_defaultdocdir/%name-%version/utils

rm %buildroot%_bindir/vgl_glxinfo
ln -sf %_libdir/libvglfaker.so %buildroot%_libdir/%vgl_name/libGL.so

%if "%_lib" == "lib64"
mkdir %buildroot%_libexecdir
mv %buildroot%_bindir/.vglrun.vars64 %buildroot%_libexecdir/vglrun.vars64
%else 
mv %buildroot%_bindir/.vglrun.vars32 %buildroot%_libexecdir/vglrun.vars32
%endif
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
%_libdir/libvglfaker-opencl.so
%_localstatedir/%vgl_name
%doc %_defaultdocdir/%name-%version

%files devel
%_includedir/*.h

%changelog
* Mon Nov 22 2021 Nikolai Kostrigin <nickel@altlinux.org> 3.0-alt1
- new version
  + pack vgl_eglinfo utility by upstream
  + update alt-nettest patch

* Mon May 31 2021 Arseny Maslennikov <arseny@altlinux.org> 2.6.5-alt1.1
- NMU: spec: adapted to new cmake macros.

* Wed Nov 18 2020 Nikolai Kostrigin <nickel@altlinux.org> 2.6.5-alt1
- new version

* Tue Aug 25 2020 Nikolai Kostrigin <nickel@altlinux.org> 2.6.4-alt2
- spec: remove self-obsoletes
  + switch to strict dependencies
  + fix license ambiguity

* Mon Jun 29 2020 Nikolai Kostrigin <nickel@altlinux.org> 2.6.4-alt1
- new version
  + remove upstream-FTBFS-against-Mesa19.3.0-headers patch
  + add faker with the OpenCL interposer (libglfaker-opencl.so) to the package

* Thu Jun 11 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 2.6.3-alt3
- Rebuilt with boost-1.73.0.

* Wed Feb 26 2020 Nikolai Kostrigin <nickel@altlinux.org> 2.6.3-alt2
- FTBFS against Mesa 19.3.0+ headers
  + add upstream-FTBFS-against-Mesa19.3.0-headers patch

* Fri Oct 25 2019 Nikolai Kostrigin <nickel@altlinux.org> 2.6.3-alt1
- new version
  + update fix-linkage patch
  + remove obsolete system-glx patch
  + spec: add new BR: opencl-headers, ocl-icd-devel, libxcbutil-keysyms-devel

* Thu May 23 2019 Nikolai Kostrigin <nickel@altlinux.org> 2.6.2-alt1
- new version

* Wed Jan 09 2019 Nikolai Kostrigin <nickel@altlinux.org> 2.6.1-alt1
- new version
- remove ubt

* Fri Aug 31 2018 Sergey V Turchin <zerg@altlinux.org> 2.5.90-alt2
- rebuild with new openssl
- fix compile on aarch64

* Thu May 03 2018 Nikolai Kostrigin <nickel@altlinux.org> 2.5.90-alt1
- new version build
- restore previous package spec changelog

* Wed Apr 25 2018 Nikolai Kostrigin <nickel@altlinux.org> 2.5.2-alt1
- new version build from Git src tree with updated ALTLinux patches

* Wed Jun 04 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.3-alt1.1
- Rebuilt with updatet libfltk

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

