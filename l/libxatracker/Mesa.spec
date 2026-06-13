%define optflags_lto %nil

Name: libxatracker
Version: 25.1.9
Release: alt4
Epoch: 4
License: MIT
Summary: Mesa XA state tracker
Group: System/Libraries
Url: http://www.mesa3d.org

Source: %name-%version.tar
Patch: %name-%version.patch

#BuildPreReq: /proc
BuildRequires(pre): meson
BuildRequires: gcc-c++ indent flex
BuildRequires: libdrm-devel
BuildRequires: python3-devel
BuildRequires: python3-module-mako
BuildRequires: python3-module-yaml
BuildRequires: python3(packaging)
BuildRequires: zlib-devel
BuildRequires: llvm-devel

%description
Xorg Gallium3D acceleration library.

%package devel
Summary: Mesa XA state tracker development package
Group: Development/C

%description devel
Xorg Gallium3D acceleration development package.

%set_verify_elf_method unresolved=relaxed

%prep
%setup -q
%patch -p1

tar -xf subprojects.tar

%build
%meson \
	-Dplatforms= \
	-Dosmesa=false \
	-Dgallium-drivers=llvmpipe,svga \
	-Dgallium-vdpau=disabled \
	-Dgallium-va=disabled \
	-Dgallium-xa=enabled \
	-Dgallium-nine=false \
	-Dgallium-opencl=disabled \
	-Dgallium-rusticl=false \
	-Dvulkan-drivers= \
	-Dshared-glapi=enabled \
	-Dgles1=disabled \
	-Dgles2=disabled \
	-Dopengl=true \
	-Dgbm=disabled \
	-Dglvnd=disabled \
	-Dglx=disabled \
	-Degl=disabled \
	-Dllvm=enabled \
	-Dshared-llvm=enabled \
	-Dvalgrind=disabled \
	-Dbuild-tests=false \
	-Dmesa-clc=auto \
	-Dmicrosoft-clc=disabled \
	-Dxlib-lease=disabled \
	-Dandroid-libbacktrace=disabled \
	-Dlibunwind=disabled \
	-Dlmsensors=disabled
#

%meson_build

%install
%meson_install

# trim some garbage, the mesa base package handles these
rm -rf %buildroot%_datadir/drirc.d
rm -rf %buildroot%_includedir/GL/gl*.h
rm -rf %buildroot%_includedir/KHR

%files
%_libdir/libxatracker.so.*

%files devel
%_includedir/xa_*.h
%_libdir/libxatracker.so
%_pkgconfigdir/xatracker.pc

%changelog
* Sat Jun 13 2026 Anton Midyukov <antohami@altlinux.org> 4:25.1.9-alt4
- Apply 0001-c11-threads-fix-build-on-fedora-44.patch.

* Sat Feb 28 2026 Anton Midyukov <antohami@altlinux.org> 4:25.1.9-alt3
- add BR on python3(packaging) (fix FTBFS).

* Fri Dec 12 2025 Anton Midyukov <antohami@altlinux.org> 4:25.1.9-alt2
- Initial build from old Mesa.
