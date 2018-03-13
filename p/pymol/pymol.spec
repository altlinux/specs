Name:           pymol
Version:        1.8.6.0
Release:        alt1
Summary:        Python-enhanced molecular graphics tool
Group:          Sciences/Chemistry
License:        CNRI Python License
URL:            http://www.pymol.org/
# https://pymol.svn.sourceforge.net/svnroot/pymol

Source:        %name-%version.tar
Source1:			 http://pymolwiki.org/images/7/77/PymolRef.pdf

Requires: python-module-%name = %version-%release

BuildRequires(pre): rpm-build-python
BuildRequires: libGLU-devel python-module-OpenGL libpng-devel tk-devel gcc-c++
BuildRequires: libnumpy-devel libfreetype-devel libGLUT-devel
BuildRequires: python-devel libGLEW-devel
BuildRequires: libxml2-devel libmsgpack-devel

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
%add_python_req_skip headering

%description devel
Development files for PyMOL.

%package -n python-module-%name
Summary: PyMOL python module
Group: Development/Python
Obsoletes: libpymol
%setup_python_module pymol
%py_provides pymol
Requires: python-module-webpy

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
#PYTHONPATH=%buildroot%python_sitelibdir %__python setup2.py install \
#	--skip-build --root=%buildroot

for i in contrib/champ contrib/mmtf-c \
	contrib/uiuc/plugins/include \
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

%files
%doc ChangeLog AUTHORS README LICENSE COPYING
%_bindir/*

%files devel
%doc DEVELOPERS PACKAGING
%_includedir/pymol
%python_sitelibdir/pymol/pymol_path/test

%files -n python-module-%name
%python_sitelibdir/*.egg-info
%python_sitelibdir/pmg_wx
%python_sitelibdir/pymol
%python_sitelibdir/pymol2
%python_sitelibdir/web/pymolhttpd.py*
%exclude %python_sitelibdir/pymol/pymol_path/test

%files -n python-module-chempy
%python_sitelibdir/chempy

%files -n python-module-pmg_tk
%python_sitelibdir/pmg_tk

%files doc
%_docdir/PyMOL

%changelog
* Tue Mar 13 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 1.8.6.0-alt1
- Updated to upstream version 1.8.6.0.

* Thu Apr 07 2016 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 1.7.2.1-alt2.svn20140819.qa1
- NMU: rebuilt with libGLEW.so.1.13.

* Thu Sep 18 2014 Nazarov Denis <nenderus@altlinux.org> 1.7.2.1-alt2.svn20140819
- Rebuilt with libGLEW 1.11.0

* Fri Aug 29 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.7.2.1-alt1.svn20140819
- Version 1.7.2.1

* Fri Oct 05 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2_b3-alt2.svn20090726.4
- Rebuilt with libpng15

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
