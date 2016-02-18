%define oname cvxopt

%def_with python3

Name: python-module-%oname
Version: 1.1.7
Release: alt1.1
Summary: Python Software for Convex Optimization
License: GPL v3 or higher/GPL v2 of higher
Group: Development/Python
Url: http://cvxopt.org/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>
Source: %oname-%version.tar.gz
%setup_python_module %oname
# disable requirements on commertial software
%add_python_req_skip mosekarr pymosek mosek

Patch100: python-module-cvxopt-1.1.5-alt3-armh.patch

BuildRequires(pre): rpm-build-python
#BuildPreReq: python-devel liblapack-devel libgsl-devel
#BuildPreReq: libfftw3-devel libglpk4-devel libdsdp-devel
#BuildPreReq: python-module-sphinx-devel texlive-latex-recommended dvipng
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires(pre): rpm-macros-sphinx
# Automatically added by buildreq on Wed Jan 27 2016 (-bi)
# optimized out: elfutils fontconfig libopenblas-devel python-base python-devel python-module-PyStemmer python-module-Pygments python-module-babel python-module-cssselect python-module-genshi python-module-jinja2 python-module-jinja2-tests python-module-markupsafe python-module-pytz python-module-setuptools python-module-six python-module-snowballstemmer python-module-sphinx python-module-sphinx_rtd_theme python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-json python-modules-multiprocessing python-modules-unittest python3 python3-base t1lib tex-common texlive-base texlive-base-bin texlive-common texlive-generic-recommended texlive-latex-base texlive-latex-recommended
BuildRequires: dvipng libdsdp-devel libfftw3-devel libglpk-devel libgsl-devel liblapack-devel python-module-alabaster python-module-docutils python-module-html5lib python-module-objects.inv python3-devel rpm-build-python3 time

#BuildRequires: python3-devel
%endif

Conflicts: %name-pickles < %version-%release

%description
CVXOPT is a free software package for convex optimization based on the
Python programming language. It can be used with the interactive Python
interpreter, on the command line by executing Python scripts, or
integrated in other software via Python extension modules. Its main
purpose is to make the development of software for convex optimization
applications straightforward by building on Python's extensive standard
library and on the strengths of Python as a high-level programming
language.

%if_with python3
%package -n python3-module-%oname
Summary: Python 3 Software for Convex Optimization
Group: Development/Python3
%add_python3_req_skip mosekarr pymosek mosek

%description -n python3-module-%oname
CVXOPT is a free software package for convex optimization based on the
Python programming language. It can be used with the interactive Python
interpreter, on the command line by executing Python scripts, or
integrated in other software via Python extension modules. Its main
purpose is to make the development of software for convex optimization
applications straightforward by building on Python's extensive standard
library and on the strengths of Python as a high-level programming
language.
%endif

%package doc
Summary: Documentation for CVXOPT
Group: Documentation
BuildArch: noarch

%description doc
CVXOPT is a free software package for convex optimization based on the
Python programming language. It can be used with the interactive Python
interpreter, on the command line by executing Python scripts, or
integrated in other software via Python extension modules. Its main
purpose is to make the development of software for convex optimization
applications straightforward by building on Python's extensive standard
library and on the strengths of Python as a high-level programming
language.

This package contains documentation for CVXOPT.

%package examples
Summary: Examples for CVXOPT
Group: Documentation
BuildArch: noarch

%description examples
CVXOPT is a free software package for convex optimization based on the
Python programming language. It can be used with the interactive Python
interpreter, on the command line by executing Python scripts, or
integrated in other software via Python extension modules. Its main
purpose is to make the development of software for convex optimization
applications straightforward by building on Python's extensive standard
library and on the strengths of Python as a high-level programming
language.

This package contains examples for CVXOPT.

%package pickles
Summary: Pickles for CVXOPT
Group: Development/Python

%description pickles
CVXOPT is a free software package for convex optimization based on the
Python programming language. It can be used with the interactive Python
interpreter, on the command line by executing Python scripts, or
integrated in other software via Python extension modules. Its main
purpose is to make the development of software for convex optimization
applications straightforward by building on Python's extensive standard
library and on the strengths of Python as a high-level programming
language.

This package contains pickles for CVXOPT.

%prep
%setup
%ifarch %arm
%patch100 -p2
%endif

%if_with python3
rm -rf ../python3
cp -a . ../python3
%endif

%prepare_sphinx doc/source

%build
%ifarch x86_64
sed -i 's|@64@|64|g' setup.py
%else
sed -i 's|@64@||g' setup.py
%endif
%add_optflags -fno-strict-aliasing
%python_build_debug

%if_with python3
pushd ../python3
%ifarch x86_64
sed -i 's|@64@|64|g' setup.py
%else
sed -i 's|@64@||g' setup.py
%endif
%add_optflags -fno-strict-aliasing
%python3_build_debug
popd
%endif

%make -C doc html

%install
%if_with python3
pushd ../python3
%python3_install
popd
%endif

%python_install

install -d %buildroot%_docdir/%name
cp -fR doc/build/html examples %buildroot%_docdir/%name/

install -d %buildroot%python_sitelibdir/%oname
cp -fR doc/build/pickle %buildroot%python_sitelibdir/%oname/

%files
%doc LICENSE README.md
%python_sitelibdir/*
%exclude %python_sitelibdir/%oname/pickle

%files doc
%doc %dir %_docdir/%name
%doc %_docdir/%name/html

%files examples
%doc %dir %_docdir/%name
%doc %_docdir/%name/examples

%files pickles
%dir %python_sitelibdir/%oname
%python_sitelibdir/%oname/pickle

%if_with python3
%files -n python3-module-%oname
%doc LICENSE README.md
%python3_sitelibdir/*
%endif

%changelog
* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 1.1.7-alt1.1
- NMU: Use buildreq for BR.

* Fri Jul 11 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.7-alt1
- Verson 1.1.7

* Tue Sep 17 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.6-alt1
- Version 1.1.6

* Fri Mar 22 2013 Aleksey Avdeev <solo@altlinux.ru> 1.1.5-alt4.1
- Rebuild with Python-3.3

* Thu Mar 14 2013 Gleb F-Malinovskiy <glebfm@altlinux.org> 1.1.5-alt4
- on %%arm liblapack is built with libblas, not libopenblas

* Mon Feb 04 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.5-alt3
- Rebuilt with glpk 4.48

* Sun Aug 12 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.5-alt2
- Built with OpenBLAS instead of GotoBLAS2

* Wed May 23 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.5-alt1
- Version 1.1.5
- Added module for Python 3

* Thu Apr 12 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 1.1.4-alt1.1
- Rebuild to remove redundant libpython2.7 dependency

* Fri Dec 23 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.4-alt1
- Version 1.1.4

* Mon Oct 24 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.1.3-alt5.1
- Rebuild with Python-2.7

* Sat Apr 09 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.3-alt5
- Built with GotoBLAS2 instead of ATLAS

* Tue Apr 05 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.3-alt4
- Rebuilt with python-module-sphinx-devel

* Fri Mar 25 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.3-alt3
- Rebuilt for debuginfo

* Mon Oct 18 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.3-alt2
- Fixed underlinking

* Tue Sep 21 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.3-alt1
- Version 1.1.3
- Enabled pickles package

* Fri Sep 10 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.2-alt3
- Added explicit conflict with old pickles package (ALT #24051)

* Mon Aug 02 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.2-alt2
- Rebuilt with Sphinx 1.0.1

* Tue Jul 27 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.2-alt1
- Version 1.1.2
- Added pickles

* Wed Nov 11 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.1-alt3
- Rebuilt with python 2.6

* Fri Sep 04 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.1-alt2
- Rebuilt with shared library of DSDP

* Mon Aug 03 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.1-alt1
- Initial build for Sisyphus
