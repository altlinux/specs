%define _unpackaged_files_terminate_build 1

%def_with check

Name: dxf2gcode
Version: 20240509
Release: alt1

Summary: 2D drawings to CNC machine compatible G-Code converter
License: GPL-3.0-or-later
Group: Engineering
URL: https://sourceforge.net/p/dxf2gcode/wiki/Home/
Vcs: https://salsa.debian.org/science-team/dxf2gcode

BuildRequires(pre): rpm-build-python3

BuildRequires: python3-devel
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel
BuildRequires: python3(PyQt5)
BuildRequires: /usr/bin/pyuic5
BuildRequires: /usr/bin/lrelease-qt5

%if_with check
BuildRequires: /usr/bin/inkscape
BuildRequires: /usr/bin/pstoedit
BuildRequires: /usr/bin/gs
BuildRequires: python3(configobj)
%endif

BuildArch: noarch

Source: %name-%version.tar

# sync with version 20240509-2 from Debian unstable
Patch: %name-%version-%release.patch

%description
This program reads 2D mechanical drawings of parts to be fabricated
and produces G-code tool movement instructions for running on automatic
machine tools (CNC machines) such as milling machines and lathes.

This is a graphical CAM (Computer Aided Manufacturing) program.
It accepts input in DXF, PDF, or Postscript format.  It supports milling,
drilling, and turning operations, as well as work-holding tabs.

%prep
%setup
%patch -p1
sed -i "s|Categories=.*|Categories=Graphics;2DGraphics;Engineering;X-CNC;|" dxf2gcode.desktop

%build
%__python3 ./make_tr.py --no-pylupdate
%__python3 ./make_py_uic.py 5
%__python3 ./st-setup.py build
lrelease-qt5 i18n/*.ts

%install
%__python3 ./st-setup.py install \
                                 --root=%buildroot \
                                 --prefix=%_prefix \
                                 --install-lib %python3_sitelibdir \
                                 --install-data=%_prefix \
                                 --install-scripts=%_bindir

%find_lang %name --with-qt

%check
sed -i "s|SVG=/usr/|SVG=%{buildroot}/usr/|" debian/tests/test-dxf2gcode

export AUTOPKGTEST_TMP=%buildroot%_tmppath
export PATH=$PATH:%buildroot%_bindir
export PYTHONPATH=%buildroot%python3_sitelibdir

sh debian/tests/test-dxf2gcode

rm -fv %buildroot%_tmppath/dxf2gcode.log
rm -fv %buildroot%_tmppath/test.dxf
rm -fv %buildroot%_tmppath/test.eps
rm -fv %buildroot%_tmppath/test.ngc

%files -f %{name}.lang
%doc COPYING README.txt
%python3_sitelibdir/%name/
%python3_sitelibdir/*egg-info
%_bindir/dxf2gcode
%python3_sitelibdir/__pycache__
%python3_sitelibdir/dxf2gcode_images5_rc.py
%python3_sitelibdir/dxf2gcode_ui5.py
%_desktopdir/dxf2gcode.desktop
%_iconsdir/hicolor/scalable/apps/dxf2gcode.svg
%_man1dir/dxf2gcode.1.*
%_datadir/metainfo/dxf2gcode.appdata.xml

%changelog
* Thu Dec 25 2025 Nikolay Strelkov <snk@altlinux.org> 20240509-alt1
- Initial build for Sisyphus
