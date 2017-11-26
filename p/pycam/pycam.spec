Name: pycam
Version: 0.6.2
Release: alt1
Summary: Open Source CAM - Toolpath Generation for 3-Axis CNC machining
Group: Engineering
License: GPLv3+
Url: http://sourceforge.net/projects/%name/
BuildArch: noarch

Packager: Anton Midyukov <antohami@altlinux.org>

Source: http://downloads.sourceforge.net/project/%name/%name/%version/%name-%version.tar.gz
Patch: desktop-categories.patch
Buildrequires(pre): rpm-build-python
BuildRequires: python-devel
BuildRequires: ccache
BuildRequires: desktop-file-utils
BuildRequires: help2man
%add_python_req_skip ode
%add_python_req_skip openvoronoi
Requires: python-module-pygtkglext
Requires: inkscape
Requires: pstoedit
%py_requires guppy

# Needed because it owns the icon directories
Requires: icon-theme-hicolor

# Segmentation Fault with libfreeglut!!!
Requires: libGLUT

%description
PyCAM is a toolpath generator for 3-axis CNC machining. It loads 3D
models in STL format or 2D contour models from DXF or SVG files. The
resulting GCode can be used with EMC2 or any other machine controller.

PyCAM supports a wide range of toolpath strategies for 3D models and
2D contour models.

%prep
%setup
%patch -p2

for f in ./*.{txt,TXT} ./Changelog; do
    iconv -f iso-8859-1 -t utf-8 $f |sed 's|\r||g' > $f.utf8
    touch -c -r $f $f.utf8
    mv $f.utf8 $f
done

%build
%python_build
pushd man
make
popd

%install
%python_install

desktop-file-install  --dir=%buildroot%_desktopdir \
    share/desktop/%name.desktop

pushd %buildroot%python_sitelibdir/%name/
# remove shebang lines from top of module files
for lib in `find . -path "*.py"`; do
    echo $lib
    sed '/\/usr\/bin\/env/d' $lib > $lib.new && \
        touch -r $lib $lib.new && \
        mv $lib.new $lib
done
popd

# Install icons
install -pD -m 0644 share/mime/application-sla.svg \
    %buildroot%_iconsdir/hicolor/scalable/apps/pycam.svg
install -pD -m 0644 share/mime/icons/32x32/application-sla.png \
    %buildroot%_iconsdir/hicolor/32x32/apps/pycam.png
install -pD -m 0644 share/mime/icons/64x64/application-sla.png \
    %buildroot%_iconsdir/hicolor/64x64/apps/pycam.png
install -pD -m 0644 share/mime/icons/128x128/application-sla.png \
    %buildroot%_iconsdir/hicolor/128x128/apps/pycam.png

# Install man page
install -pD -m 0644 man/pycam.1 %buildroot%_man1dir/pycam.1

%files
%doc Changelog COPYING.TXT LICENSE.TXT README.md technical_details.txt
%_datadir/%name/
%_bindir/%name
%_desktopdir/pycam.desktop
%_iconsdir/hicolor/*/apps/%name.*
%_man1dir/%name.1.*
%python_sitelibdir/*

%changelog
* Sun Nov 26 2017 Anton Midyukov <antohami@altlinux.org> 0.6.2-alt1
- New version 0.6.2

* Wed Sep 27 2017 Anton Midyukov <antohami@altlinux.org> 0.6.1-alt1
- New version 0.6.1

* Sat Jul 29 2017 Anton Midyukov <antohami@altlinux.org> 0.5.1-alt3
- Fix desktop categories.

* Sat Jul 29 2017 Anton Midyukov <antohami@altlinux.org> 0.5.1-alt2
- Added missing requires: python-module-pygtkglext.

* Wed Jul 26 2017 Anton Midyukov <antohami@altlinux.org> 0.5.1-alt1
- Initial build for ALT Sisyphus.
