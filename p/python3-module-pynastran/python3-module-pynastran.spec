%define _unpackaged_files_terminate_build 1

%define pypi_name pynastran

%def_with check

Name: python3-module-%pypi_name
Version: 1.4.1
Release: alt2.git20260717.a31c1b3

Summary: A Python-based interface tool for Nastran's file formats
License: BSD-3-Clause
Group: Engineering
URL: https://github.com/SteveDoyle2/pyNastran

BuildRequires(pre): rpm-build-python3

BuildRequires: python3-devel
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel

%if_with check
BuildRequires: python3-module-cpylog
BuildRequires: python3-module-docopt
BuildRequires: python3-module-numpy
BuildRequires: python3-module-qtpy
BuildRequires: python3-module-scipy
BuildRequires: python3-module-contourpy
BuildRequires: python3-module-matplotlib
BuildRequires: python3-module-fonttools
%endif

%filter_from_requires /python3(OCC.Core.BRepPrimAPI)/d
%filter_from_requires /python3(OCC.Display.SimpleGui)/d
%filter_from_requires /python3(PyQt4)/d
%filter_from_requires /python3(PyQt4.QtCore)/d
%filter_from_requires /python3(dynanduril.femap.femap_hash)/d
%filter_from_requires /python3(mymodule)/d
%filter_from_requires /python3(notebook_to_markdown)/d
%filter_from_requires /python3(op2)/d
%filter_from_requires /python3(op4)/d
%filter_from_requires /python3(pyNastran.converters.cart3d.cart3d_reader)/d
%filter_from_requires /python3(pyNastran.converters.panair.panairGridPatch)/d
%filter_from_requires /python3(pyNastran.dev.bdf_vectorized3.cards.aero.spline_methods)/d
%filter_from_requires /python3(pyNastran.dev.bdf_vectorized3.mesh_utils.aero_utils)/d
%filter_from_requires /python3(pyNastran.dev.tools.pressure_map.pressure_map_aero_setup)/d
%filter_from_requires /python3(pyNastran.op2.dev.op2)/d
%filter_from_requires /python3(vtk.numpy_interface)/d
%filter_from_requires /python3(vtk.qt4.QVTKRenderWindowInteractor)/d
%filter_from_requires /python3(vtk.util)/d
%filter_from_requires /python3(vtk.util.vtkAlgorithm)/d

# needs libblosc2.so
Requires: libblosc2-devel

Requires: python3-module-imageio
Requires: python3-module-qscintilla2-qt5

BuildArch: noarch

Source: %pypi_name-%version.tar

Patch: %name-%version-%release.patch

%description
pyNastran is an interface library to the various Nastran file formats
(BDF, OP2, OP4). Using the BDF interface, you can read/edit/write
Nastran geometry without worrying about field formatting. Many checks
are also performed to verify that your model is correct. Using the OP2
interface, you can read large result files quickly and efficiently.
Additionally, you can also extract a subset of the result data and write
OP2/F06 result files.

%prep
%setup -n %pypi_name-%version
%patch -p1
sed -i "s/docopt-ng>=0.9.0/docopt==0.6.2/" pyproject.toml \
                                           requirements_docs.txt
sed -i "s/docopt-ng/docopt/"               pyNastran/gui/menus/about/about.py

# FIX versioning
sed -i "s/'git'/'do-not-use-git-on-non-git-folder'/" pyNastran/__init__.py
sed -i "s/1.5.0/%version/" pyNastran/__init__.py
sed -i "s/no.git.checksum/%(echo %release | awk -F. '{print $NF}')/" pyNastran/__init__.py
date_out=$(echo "%release" | awk -F. '{d=$2; sub(/^git/,"",d); printf "('\''%d'\'','\''%d'\'','\''%d'\'')\n", substr(d,1,4), substr(d,5,2), substr(d,7,2)}')
sed -i "s/date_out = ('2026', '2', 'xx')/date_out = $date_out/" pyNastran/__init__.py

%build
%pyproject_build

%install
%pyproject_install

# prepare desktop file
mkdir -p %buildroot%_desktopdir
cat <<EOF > %buildroot%_desktopdir/pyNastranGUI.desktop
[Desktop Entry]
Name=pyNastranGUI
Comment=pyNastran GUI application
Exec=pyNastranGUI
Icon=/usr/lib/python3/site-packages/pyNastran/gui/icons/logo.png
Type=Application
Encoding=UTF-8
Categories=Science
EOF

%check
#%%tox_create_default_config
%tox_check_pyproject

%files
%doc LICENSE.md README.md
%python3_sitelibdir/pyNastran/
%python3_sitelibdir/pynastran*

%_bindir/abaqus_to_nastran
%_bindir/f06
%_bindir/format_converter
%_bindir/op2

%_bindir/pyNastranGUI
%_desktopdir/pyNastranGUI.desktop

%_bindir/test_bdf
%_bindir/test_bdfv
%_bindir/test_op2
%_bindir/test_op4
%_bindir/test_pynastrangui

# no dynanduril python module
%exclude %_bindir/bdf

%changelog
* Wed Jul 22 2026 Nikolay Strelkov <snk@altlinux.org> 1.4.1-alt2.git20260717.a31c1b3
- Enabled check.

* Sun Jul 19 2026 Nikolay Strelkov <snk@altlinux.org> 1.4.1-alt1.git20260717.a31c1b3
- Initial build for Sisyphus
