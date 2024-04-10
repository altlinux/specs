Name:           gfsview
Version:        20121130
Release:        alt1

Summary:        Graphical viewer for Gerris simulation files

License:        GPLv3
Group:          Sciences/Physics
URL:            http://gfs.sourceforge.net

Source:         %name-%version.tar
Patch:          use_system_gl2ps.patch

BuildRequires: gerris libOSMesa-devel libGLU-devel libgl2ps-devel
BuildRequires: libgtkglext-devel libstartup-notification-devel
BuildRequires: libftgl-devel

%description
%summary.

%prep
%setup
%patch -p1
rm -rv gl2ps

# Comment "undefined symbol: gl2psLineWidth"
sed -i 's/gl2psLineWidth/\/\/gl2psLineWidth/' gl/gfsgl.c

%build
%autoreconf
%configure --disable-static
%make_build

%install
%makeinstall_std

find %buildroot%_libdir -type f -name "*.la" -delete -print

%files
%_bindir/gfsview
%_bindir/gfsview-batch2D
%_bindir/gfsview-batch3D
%_bindir/gfsview2D
%_bindir/gfsview3D

%_libdir/gerris/libgfsview2D-0.0.1.so
%_libdir/gerris/libgfsview2D.so
%_libdir/gerris/libgfsview3D-0.0.1.so
%_libdir/gerris/libgfsview3D.so
%_libdir/libgfsgl2D.so
%_libdir/libgfsgl2D.so.*
%_libdir/libgfsgl3D.so
%_libdir/libgfsgl3D.so.*

%_datadir/%name

%_desktopdir/gfsview.desktop
%_desktopdir/gfsview2D.desktop
%_desktopdir/gfsview3D.desktop
%_iconsdir/hicolor/48x48/mimetypes/*.png
%_datadir/mime/packages/%name.xml

%changelog
* Sat Apr 06 2024 Grigory Ustinov <grenka@altlinux.org> 20121130-alt1
- Initial build for Sisyphus.
