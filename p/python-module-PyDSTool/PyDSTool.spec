%define oname PyDSTool
Name: python-module-%oname
Version: 0.88.121202
Release: alt2.bzr20130716
Summary: Integrated simulation, modeling and analysis package for dynamical systems
License: BSD
Group: Development/Python
Url: http://www.ni.gsu.edu/~rclewley/PyDSTool/FrontPage.html
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
rm -fR .gear
install -p -m644 %SOURCE1 .
popd

# There is a file in the package named .DS_Store or .DS_Store.gz, 
# the file name used by Mac OS X to store folder attributes.  
# Such files are generally useless in packages and were usually accidentally 
# included by copying complete directories from the source tarball.
find $RPM_BUILD_ROOT \( -name '*.DS_Store' -o -name '*.DS_Store.gz' \) -print -delete

%files
%python_sitelibdir/*

%changelog
* Sun Dec 01 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.88.121202-alt2.bzr20130716
- Applied repocop patch

* Fri Nov 29 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.88.121202-alt1.bzr20130716
- Version 0.88.121202

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

