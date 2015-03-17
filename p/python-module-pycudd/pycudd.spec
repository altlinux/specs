%define oname pycudd

%def_with python3

Name: python-module-%oname
Version: 2.0.2
Release: alt2
Summary: Enhanced Python interface to the Colorado University BDD package, CUDD
License: Free
Group: Development/Python
Url: http://bears.ece.ucsb.edu/pycudd.html
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel swig libcudd-devel gcc-c++
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python-tools-2to3
%endif

%py_provides %oname

%description
PyCUDD is an enhanced Python interface to the Colorado University BDD
package, CUDD.

%if_with python3
%package -n python3-module-%oname
Summary: Enhanced Python interface to the Colorado University BDD package, CUDD
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
PyCUDD is an enhanced Python interface to the Colorado University BDD
package, CUDD.
%endif

%prep
%setup

%if_with python3
cp -fR . ../python3
find ../python3 -type f -name '*.py' -exec 2to3 -w -n '{}' +
%endif

%build
%ifarch x86_64
LIB_SUFFIX=64
%endif
%add_optflags %optflags_shared -I%_includedir/cudd
%add_optflags -DFALSE=false -DTRUE=true

%make LIB_SUFFIX=$LIB_SUFFIX FLAGS="%optflags"

%if_with python3
pushd ../python3
%make LIB_SUFFIX=$LIB_SUFFIX FLAGS="%optflags" \
	PYTHON_VER=python%_python3_version%_python3_abiflags SWIG="swig -py3"
2to3 -w -n %oname.py
sed -i 's|\t|        |g' %oname.py
popd
%endif

%install
install -d %buildroot%python_sitelibdir
install -m644 %oname.py *.so %buildroot%python_sitelibdir/

%if_with python3
pushd ../python3
install -d %buildroot%python3_sitelibdir
install -m644 %oname.py *.so %buildroot%python3_sitelibdir/
popd
%endif

%check
export PYTHONPATH=$PWD
python example1.py
python example2.py
%if_with python3
pushd ../python3
export PYTHONPATH=$PWD
python3 example1.py
python3 example2.py
popd
%endif

%files
%doc README UNIMPLEMENTED example?.py doc/*
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc README UNIMPLEMENTED ../python3/example?.py doc/*
%python3_sitelibdir/*
%endif

%changelog
* Tue Mar 17 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.2-alt2
- Applied patch from https://github.com/pysmt/pysmt/tree/master/patches

* Mon Mar 16 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.2-alt1
- Initial build for Sisyphus

