%define oname cvxopt

%def_with check
%def_with docs

Name: python3-module-%oname
Version: 1.3.2
Release: alt1

Summary: Python Software for Convex Optimization

License: GPL-3.0-or-later
Group: Development/Python3
Url: http://cvxopt.org

Source: %oname-%version.tar.gz

BuildRequires(pre): rpm-build-python3
BuildRequires: dvipng libfftw3-devel libglpk-devel libgsl-devel liblapack-devel
BuildRequires: libblas-devel libsuitesparse-devel

%if_with docs
BuildRequires(pre): rpm-macros-sphinx3
BuildRequires: python3-module-sphinx
BuildRequires: python3-module-sphinx_rtd_theme
%endif

%if_with check
BuildRequires: python3-module-pytest
%endif

# mosek is not packaged and there is no tarball on pypi for it
%add_python3_req_skip mosekarr pymosek mosek mosek.array

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
Group: Development/Python3

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
sed -i 's,^BUILD_DSDP.\+$,BUILD_DSDP = 0,' setup.py

%ifarch %e2k
# openblas not available
sed -i 's,openblas,blas,g' setup.py
%endif

%if_with docs
%prepare_sphinx3 doc/source
%endif

%build
%if "%_lib" != "lib64"
sed -i 's|lib64|lib|g' setup.py
%endif
%if "%_arch" != "x86_64"
sed -i 's|x86_64|%_arch|g' setup.py
%endif
%add_optflags -fno-strict-aliasing
export CC="gcc"
export LDSHARED="gcc -shared $RPM_LD_FLAGS"
%python3_build_debug

%if_with docs
%make SPHINXBUILD="sphinx-build-3" -C doc html
%make SPHINXBUILD="sphinx-build-3" -C doc pickle
%endif

%install
%python3_install

%if_with docs
install -d %buildroot%_docdir/%name
cp -fR doc/build/html examples %buildroot%_docdir/%name/

cp -fR doc/build/pickle %buildroot%python3_sitelibdir/%oname/
%endif

%check
export PYTHONPATH=%buildroot%python3_sitelibdir
%__python3 -m pytest

%files
%doc LICENSE README.md
%python3_sitelibdir/%oname
%python3_sitelibdir/*.egg-info
%if_with docs
%exclude %python3_sitelibdir/%oname/pickle

%files examples
%doc %dir %_docdir/%name
%doc %_docdir/%name/examples

%files doc
%doc %dir %_docdir/%name
%doc %_docdir/%name/html

%files pickles
%dir %python3_sitelibdir/%oname
%python3_sitelibdir/%oname/pickle
%endif

%changelog
* Tue Sep 12 2023 Grigory Ustinov <grenka@altlinux.org> 1.3.2-alt1
- Automatically updated to 1.3.2.

* Mon May 15 2023 Grigory Ustinov <grenka@altlinux.org> 1.3.1-alt1
- Automatically updated to 1.3.1.

* Mon May 23 2022 Grigory Ustinov <grenka@altlinux.org> 1.3.0-alt1
- Automatically updated to 1.3.0.
- Build with check.
- Build with docs.

* Mon Dec 13 2021 Grigory Ustinov <grenka@altlinux.org> 1.2.7-alt1
- Automatically updated to 1.2.7.

* Mon Jul 19 2021 Michael Shigorin <mike@altlinux.org> 1.2.6-alt1.1
- E2K: fix build (SuiteSparse seems unbundled)

* Wed Mar 03 2021 Grigory Ustinov <grenka@altlinux.org> 1.2.6-alt1
- Automatically updated to 1.2.6.

* Wed Jan 27 2021 Grigory Ustinov <grenka@altlinux.org> 1.2.5-alt1
- Automatically updated to 1.2.5.
- Drop python2 support.

* Mon May 27 2019 Michael Shigorin <mike@altlinux.org> 1.1.7-alt3
- fixed build on e2k (use blas instead of openblas)

* Tue May 08 2018 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.1.7-alt2
- fixed packaging on 64bit arches other than x86_64

* Thu Mar 22 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 1.1.7-alt1.1.1.1
- (NMU) Rebuilt with python-3.6.4.

* Thu Mar 17 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.1.7-alt1.1.1
- (NMU) rebuild with python3-3.5 & rpm-build-python3-0.1.10
  (for ABI dependence and new python3(*) reqs)

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
