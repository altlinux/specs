Name:           pymol
Version:        1.2_b3
Release:        alt2.svn20090726.3.1.1
Summary:        Python-enhanced molecular graphics tool
Group:          Sciences/Chemistry
License:        CNRI Python License
URL:            http://www.pymol.org/
# https://pymol.svn.sourceforge.net/svnroot/pymol
Source:        %name-%version.tar.bz2
Source1:			 http://pymolwiki.org/images/7/77/PymolRef.pdf
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>
Requires: python-module-%name = %version-%release

BuildRequires(pre): rpm-build-python
BuildPreReq: libGLU-devel python-module-OpenGL libpng-devel tk-devel gcc-c++
BuildPreReq: python-module-numpy libfreetype-devel libfreeglut-devel
BuildPreReq: python-devel

%description
PyMOL is a Python-enhanced molecular graphics tool. It excels at 3D
visualization of proteins, small molecules, density, surfaces, and trajectories.
It also includes molecular editing, ray tracing, and movies.

%package devel
Summary: Development files for PyMOL
Group: System/Libraries
Obsoletes: libpymol-devel
Requires: python-module-%name = %version-%release
%py_requires pymol

%description devel
Development files for PyMOL.

%package -n python-module-%name
Summary: PyMOL python module
Group: Development/Python
Obsoletes: libpymol
%setup_python_module pymol
%py_provides pymol

%description -n python-module-%name
PyMOL python module.

%package -n python-module-chempy
Summary: Application in Python which is meant to help in learning chemistry
Group: Development/Python
Requires: python-module-%name = %version-%release
%setup_python_module chempy
%py_provides chempy
%py_requires pymol

%description -n python-module-chempy
Chemistry in Python - application in Python which is meant to help in learning
chemistry.

%package -n python-module-pmg_tk
Summary: GUI on Tk for PyMOL
Group: Development/Python
Requires: python-module-%name = %version-%release
%setup_python_module pmg_tk
%py_provides pmg_tk
%py_requires pymol

%description -n python-module-pmg_tk
GUI on Tk for PyMOL.

%package doc
Summary: Documentation for PyMOL
Group: Documentation
BuildArch: noarch

%description doc
Documentation for PyMOL.

%prep
%setup
cp %SOURCE1 ./

%build
%python_build

%install
%python_install
PYTHONPATH=%buildroot%python_sitelibdir %__python setup2.py install \
	--skip-build --root=%buildroot

for i in contrib/champ contrib/modules contrib/pyopengl \
	contrib/sglite contrib/uiuc/plugins/include \
	contrib/uiuc/plugins/molfile_plugin/src layer0 layer1 \
	layer2 layer3 layer4 layer5 ov/src
do
	mkdir -p "%buildroot%_includedir/%name/$i"
	install -pm644 "$i"/*.h "%buildroot%_includedir/%name/$i/"
done

mkdir -p %buildroot%_bindir
cat <<EOF >%buildroot%_bindir/pymol
#!/bin/sh

%__python %python_sitelibdir/pymol/__init__.py "\$@"
EOF
chmod +x %buildroot%_bindir/pymol

mkdir -pv %buildroot%_docdir/PyMOL
cp PymolRef.pdf %buildroot%_docdir/PyMOL/
bzip2 ChangeLog

%files
%doc ChangeLog.bz2 AUTHORS README LICENSE COPYING
%_bindir/*

%files devel
%doc DEVELOPERS PACKAGING
%_includedir/pymol
%python_sitelibdir/pymol/pymol_path/test

%files -n python-module-%name
%python_sitelibdir/*.egg-info
%python_sitelibdir/pmg_wx
%python_sitelibdir/pymol
%exclude %python_sitelibdir/pymol/pymol_path/test

%files -n python-module-chempy
%python_sitelibdir/chempy

%files -n python-module-pmg_tk
%python_sitelibdir/pmg_tk

%files doc
%_docdir/PyMOL

%changelog
* Thu Apr 12 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 1.2_b3-alt2.svn20090726.3.1.1
- Rebuild to remove redundant libpython2.7 dependency

* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.2_b3-alt2.svn20090726.3.1
- Rebuild with Python-2.7

* Sat Jan 02 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2_b3-alt2.svn20090726.3
- Rebuilt without python-module-Numeric

* Mon Nov 16 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2_b3-alt2.svn20090726.2
- Rebuilt with python 2.6

* Sun Jul 26 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2_b3-alt2.svn20090726.1
- Snapshot 20090726

* Tue Jun 23 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2_b3-alt2.svn20090321
- Rebuild with changed libnpg12

* Sat Mar 21 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2_b3-alt1.svn20090321
- new snapshot from upstream
- don't need building shared libraries

* Tue Mar 03 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2_b3-alt1
- Initial build for Sisyphus
