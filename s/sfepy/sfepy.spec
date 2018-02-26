Name: sfepy
Version: 2011.1
Release: alt2.git20110405
Summary: Simple finite elements in Python (SfePy)
License: New BSD License
Group: Sciences/Mathematics
Url: http://sfepy.kme.zcu.cz/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# git://git.sympy.org/sfepy.git
Source: %name-%version.tar.gz
Source1: README.1st

Requires: python-module-%name = %version-%release
Requires: %name-data = %version-%release

BuildRequires(pre): rpm-build-python
BuildPreReq: python-devel python-module-scikits.umfpack libsuitesparse-devel
BuildPreReq: python-module-pyparsing ipython pytables swig
BuildPreReq: libtetgen-devel libnetgen-devel libnumpy-devel
BuildPreReq: doxygen graphviz texlive-latex-extra dvipng
BuildPreReq: python-module-sphinx-devel python-module-Pygments

%description
A finite element analysis software based primarily on NumPy and SciPy.

NOTE: for executing examples You need copy directory %_datadir/%name
into place, where You can write into it.

%package -n python-module-%name
Summary: Python module of Simple finite elements (SfePy)
Group: Development/Python
%setup_python_module %name
Requires: tetgen gmsh netgen
#py_requires matplotlib.backends.backend_gtkagg
%py_requires matplotlib.backends.backend_wxagg
%py_requires pyparsing scikits.umfpack tables IPython
%if "%__python_version" != "2.5"
%py_requires multiprocessing
%endif

%description -n python-module-%name
A finite element analysis software based primarily on NumPy and SciPy.

This package contains python module of SfePy.

%package data
Summary: Data files for Simple finite elements in Python (SfePy)
Group: Sciences/Mathematics
BuildArch: noarch

%description data
A finite element analysis software based primarily on NumPy and SciPy.

This package contains data files for SfePy.

%package doc
Summary: Documentation for Simple finite elements in Python (SfePy)
Group: Documentation
BuildArch: noarch

%description doc
A finite element analysis software based primarily on NumPy and SciPy.

This package contains documentation for SfePy.

%package -n python-module-%name-pickles
Summary: Pickles for Simple finite elements in Python (SfePy)
Group: Development/Python

%description  -n python-module-%name-pickles
A finite element analysis software based primarily on NumPy and SciPy.

This package contains pickles for SfePy.

%prep
%setup
ln -s types.h sfepy/fem/extmods/types_s.h
install -m644 %SOURCE1 .

%prepare_sphinx .
sed -i 's|@PYVER@|%_python_version|g' doc/Makefile

%build
export PYTHONPATH=$PWD:$PWD/script
%python_build_debug build_ext
pushd sfepy/terms
sed -i "28s|\(terms.i'\)|\1, '*.c'|" extmods/setup.py
%python_build_debug build_ext
popd

%install
export PYTHONPATH=$PWD:$PWD/script
%python_install
pushd sfepy/terms
%python_install
popd

export PYTHONPATH=%buildroot%python_sitelibdir
pushd doc
doxygen doxygen.config
%make_build -C doc/latex
popd
install -p -m644 homogen.py %buildroot%python_sitelibdir

#generate_pickles doc doc %name

install -d %buildroot%_docdir/%name/pdf
install -m644 doc/doc/latex/*.pdf %buildroot%_docdir/%name/pdf
cp -fR doc/doc/html %buildroot%_docdir/%name/
#cp -fR pickle %buildroot%python_sitelibdir/%name/

%files
%doc LICENSE README RELEASE_NOTES.txt doc/txt/*.txt
%_bindir/*

%files -n python-module-%name
%python_sitelibdir/*
#exclude %python_sitelibdir/%name/pickle

%files data
%_datadir/%name
%exclude %_datadir/%name/doc/Makefile*
%exclude %_datadir/%name/doc/conf.py

%files doc
%_docdir/%name

#files -n python-module-%name-pickles
#python_sitelibdir/%name/pickle

%changelog
* Fri Jun 08 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2011.1-alt2.git20110405
- Disabled requirement on matplotlib.backends.backend_gtkagg

* Mon Apr 16 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 2011.1-alt1.git20110405.2.1
- Rebuild to remove redundant libpython2.7 dependency

* Tue Nov 15 2011 Dmitry V. Levin <ldv@altlinux.org> 2011.1-alt1.git20110405.2
- Removed Mayavi from package requirements.

* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 2011.1-alt1.git20110405.1
- Rebuild with Python-2.7

* Tue Apr 05 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2011.1-alt1.git20110405
- Version 2011.1

* Tue Apr 05 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2010.3-alt1.git20101115.2
- Rebuilt with python-module-sphinx-devel

* Tue Mar 22 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2010.3-alt1.git20101115.1
- Rebuilt for debuginfo

* Tue Nov 16 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2010.3-alt1.git20101115
- Version 2010.3

* Mon Oct 18 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2010.2-alt1.git20100715.1
- Fixed underlinking

* Mon Jul 19 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2010.2-alt1.git20100715
- Version 2010.2

* Sat Mar 06 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2010.1-alt1.git20100304
- Version 2010.1
- Added pickles package

* Sat Feb 06 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2009.4-alt1.git20100205.1
- Added extension modules

* Sat Feb 06 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2009.4-alt1.git20100205
- New snapshot
- Rebuilt with reformed NumPy

* Sat Dec 19 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2009.4-alt1.git20091211
- Version 2009.4
- Rebuilt with texlive instead of tetex

* Wed Nov 18 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2009.3-alt1.git20090902.1
- Rebuilt with python 2.6

* Mon Sep 14 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2009.3-alt1.git20090902
- Initial build for Sisyphus

