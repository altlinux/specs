%define oname PyDSTool
Name: python-module-%oname
Version: 0.88
Release: alt1.svn20100720.2.1
Summary: Integrated simulation, modeling and analysis package for dynamical systems
License: BSD
Group: Development/Python
Url: http://www.cam.cornell.edu/~rclewley/cgi-bin/moin.cgi/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# http://jay.cam.cornell.edu/svn/PyDSTool
Source: %oname-%version.tar.gz
Source1: %oname.pth

#Requires: python-module-scipy python-module-matplotlib
#Requires: python-modules-tkinter gcc-fortran python-devel
#Requires: python-devel gcc-fortran swig python-module-numpy
#Requires: libgotoblas-devel liblapack-goto-devel
#Requires: python-module-openopt
#Requires: gnuplot

%add_python_req_skip matplotlib scipy pylab

%description
PyDSTool is an integrated simulation, modeling and analysis package for
dynamical systems, written in Python.

%install
install -d %buildroot%python_sitelibdir
pushd %buildroot%python_sitelibdir
tar -xzf %SOURCE0
install -p -m644 %SOURCE1 .
popd

%files
%python_sitelibdir/*

%changelog
* Sun Oct 30 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.88-alt1.svn20100720.2.1
- Rebuild with Python-2.7

* Fri Apr 08 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.88-alt1.svn20100720.2
- Requires GotoBLAS2 instead of ATLAS

* Tue Mar 15 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.88-alt1.svn20100720.1
- Removed requirement of libfftw3-devel

* Mon Jul 26 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.88-alt1.svn20100720
- Version 0.88

* Thu Nov 19 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.87-alt1.svn20090922.1
- Rebuilt with python 2.6

* Sat Oct 03 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.87-alt1.svn20090922
- Initial build for Sisyphus

