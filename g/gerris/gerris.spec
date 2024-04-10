%define         optflags_lto %nil
Name:           gerris
Version:        20131206
Release:        alt1

Summary:        Gerris Flow Solver

License:        GPLv3
Group:          Sciences/Physics
URL:            http://gfs.sourceforge.net

Source:         %name-%version.tar
Patch:          Port-to-Python-3.patch

BuildRequires: rpm-build-python3
BuildRequires: libgts-devel

# Simulation files for this project can use gcc, so this dependency is quite necessary
Requires: gcc

%description
Gerris is a system for the solution of the partial differential equations
describing fluid flow.

%prep
%setup
%patch -p1

%build
%autoreconf
%configure --disable-mpi --disable-static
%make_build

%install
%makeinstall_std

find %buildroot%_libdir -type f -name "*.la" -delete -print

# Depends: python3(gfs2tex)
rm -fv %buildroot%_bindir/gfs2doc

%files
%_bindir/bat2gts
%_bindir/darcs2dist
%_bindir/gerris2D
%_bindir/gerris3D
%_bindir/gfs-highlight
%_bindir/gfs2gfs
%_bindir/gfs2oogl2D
%_bindir/gfs2oogl3D
%_bindir/gfscombine2D
%_bindir/gfscombine3D
%_bindir/gfscompare2D
%_bindir/gfscompare3D
%_bindir/gfsjoin
%_bindir/gfsjoin2D
%_bindir/gfsjoin3D
%_bindir/gfsplot
%_bindir/gfsxref
%_bindir/kdt2kdt
%_bindir/kdtquery
%_bindir/ppm2mpeg
%_bindir/ppm2theora
%_bindir/ppm2video
%_bindir/ppmcombine
%_bindir/rsurface2kdt
%_bindir/shapes
%_bindir/streamanime
%_bindir/xyz2kdt

%_datadir/%name
%_man1dir/*.1.xz
%_iconsdir/hicolor/48x48/mimetypes/*.png
%_datadir/mime/packages/%name.xml

%_includedir/gfs.h
%_includedir/%name
%_libdir/pkgconfig/%name?D.pc
%_libdir/%name/*.so
%_libdir/%name/*.so.2*
%_libdir/libgfs?D.so
%_libdir/libgfs?D-1.3.so.2*

%changelog
* Sat Apr 06 2024 Grigory Ustinov <grenka@altlinux.org> 20131206-alt1
- Initial build for Sisyphus (Closes: #49940).
