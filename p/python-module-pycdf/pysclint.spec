%define cdfdir %_libexecdir/hdf5-seq

%define oname pycdf
Name: python-module-pycdf
Version: 0.6_0
Release: alt6.1.1
Summary: Python wrapper around the Unidata netCDF library
License: Public
Group: Sciences/Other
Url: http://sourceforge.net/projects/pysclint/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://pysclint.svn.sourceforge.net/svnroot/pysclint
Source: %oname-%version.tar.gz

BuildRequires(pre): rpm-build-python
BuildPreReq: python-devel python-module-Pyrex swig libnumpy-devel
BuildPreReq: zlib-devel libjpeg-devel libnetcdf-devel
%setup_python_module %oname

%description
The pycdf package wraps the complete functionality of the Unidata netcdf
library inside a Python OOP framework. Variables are read/written
through arrays defined by the Numeric or numarray packages.

%package examples
Summary: Examples for Python wrapper around the Unidata netCDF library
Group: Development/Documentation
Requires: %name = %version-%release

%description examples
The pycdf package wraps the complete functionality of the Unidata netcdf
library inside a Python OOP framework. Variables are read/written
through arrays defined by the Numeric or numarray packages.

This package contains examples for pycdf.

%prep
%setup

%build
pushd pycdf
sed -i "s|@INCDIRS@|%cdfdir/include|g" setup.py
sed -i "s|@LIBDIRS@|%cdfdir/lib|g" setup.py
%python_build_debug
popd

%install
pushd pycdf
%python_install
popd

cp -fR doc/pycdf/examples %buildroot%python_sitelibdir/pycdf/

%files
%doc pycdf/CHANGES pycdf/PKG-INFO pycdf/README pycdf/doc/pycdf.html
%python_sitelibdir/*
%exclude %python_sitelibdir/%oname/examples

%files examples
%python_sitelibdir/%oname/examples

%changelog
* Thu Apr 12 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 0.6_0-alt6.1.1
- Rebuild to remove redundant libpython2.7 dependency

* Mon Oct 24 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.6_0-alt6.1
- Rebuild with Python-2.7

* Sun Apr 24 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6_0-alt6
- Rebuilt with libnetcdf7

* Sat Mar 26 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6_0-alt5
- Rebuilt for debuginfo

* Thu Oct 28 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6_0-alt4
- Rebuilt for soname set-versions

* Sat Mar 06 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6_0-alt3
- Rebuilt with reformed NumPy

* Thu Nov 19 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6_0-alt2
- Rebuilt with python 2.6

* Fri Sep 18 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6_0-alt1
- Initial build for Sisyphus

