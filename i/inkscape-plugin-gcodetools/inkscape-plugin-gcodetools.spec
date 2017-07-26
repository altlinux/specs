%define oname gcodetools
Name: inkscape-plugin-%oname
Version: 1.7
Release: alt1.20160125
Summary: CAM extension for Inkscape to export paths to Gcode

Group: Engineering
License: GPLv2+
Url: https://github.com/pcb2gcode/pcb2gcode/
Packager: Anton Midyukov <antohami@altlinux.org>
Buildarch: noarch

Source: %oname-%version.tar
Source1: Makefile

BuildRequires: asciidoc-a2x rpm-build-python
%add_python_req_skip bezmisc cubicsuperpath inkex simplepath simplestyle simpletransform
Requires: inkscape

%description
CAM extension for Inkscape to export paths to Gcode.

%prep
%setup -n %oname-%version
find . -type d -exec chmod 755 {} \;
find . -type f -name "*.py" -exec chmod 755 {} \;

%build
pushd doc
cp %SOURCE1 .
make
popd

%install
rm -fr debian
rm -fr doc/Makefile doc/gcodetools-ru.asciidoc
mkdir -p %buildroot%_datadir/inkscape/extensions/gcodetools
cp -r . %buildroot%_datadir/inkscape/extensions/gcodetools/
rm -fr %buildroot%_datadir/inkscape/extensions/gcodetools/README.md
rm -fr %buildroot%_datadir/inkscape/extensions/gcodetools/doc
rm -fr %buildroot%_datadir/inkscape/extensions/gcodetools/examples
%buildroot%_datadir/inkscape/extensions/gcodetools/create_inx.py

%files
%_datadir/inkscape/extensions/gcodetools
%doc README.md doc examples

%changelog
* Tue Jul 25 2017 Anton Midyukov <antohami@altlinux.org> 1.7-alt1.20160125
- Initial build for ALT Sisyphus.
