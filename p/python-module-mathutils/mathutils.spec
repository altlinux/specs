%define oname mathutils

%def_without python2
%def_with python3

Name: python-module-%oname
Version: 2.74
Release: alt1.git20150315
Summary: Library providing Matrix, Vector, Quaternion, Euler and Color classes
License: GPLv2+
Group: Development/Python
Url: https://pypi.python.org/pypi/mathutils/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://gitlab.com/ideasman42/blender-mathutils.git
Source: %name-%version.tar

%if_with python2
BuildPreReq: python-devel python-module-setuptools-tests cmake gcc-c++
%endif
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests cmake gcc-c++
%endif

%py_provides %oname

%description
A general math utilities library providing Matrix, Vector, Quaternion,
Euler and Color classes, written in C for speed.

%if_with python3
%package -n python3-module-%oname
Summary: Library providing Matrix, Vector, Quaternion, Euler and Color classes
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
A general math utilities library providing Matrix, Vector, Quaternion,
Euler and Color classes, written in C for speed.
%endif

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

%build
%add_optflags -fno-strict-aliasing -DNDEBUG=1

%if_with python2
cmake \
%if %_lib == lib64
	-DLIB_SUFFIX=64 \
%endif
	-DCMAKE_INSTALL_PREFIX:PATH=%prefix \
	-DCMAKE_C_FLAGS:STRING="%optflags" \
	-DCMAKE_CXX_FLAGS:STRING="%optflags" \
	-DCMAKE_COMPILER_IS_GNUCC:BOOL=ON \
	-DCMAKE_STRIP:FILEPATH="/bin/echo" \
	.
%make_build VERBOSE=1
%endif

%if_with python3
pushd ../python3
cmake \
%if %_lib == lib64
	-DLIB_SUFFIX=64 \
%endif
	-DCMAKE_INSTALL_PREFIX:PATH=%prefix \
	-DCMAKE_C_FLAGS:STRING="%optflags" \
	-DCMAKE_CXX_FLAGS:STRING="%optflags" \
	-DCMAKE_COMPILER_IS_GNUCC:BOOL=ON \
	.
%make_build VERBOSE=1
popd
%endif

%install
%if_with python2
%makeinstall_std
%endif

%if_with python3
pushd ../python3
%makeinstall_std
popd
%endif

%check
%if_with python2
python setup.py test
%endif
%if_with python3
pushd ../python3
python3 setup.py test
popd
%endif

%if_with python2
%files
%doc *.rst
%python_sitelibdir/*
%endif

%if_with python3
%files -n python3-module-%oname
%doc *.rst
%python3_sitelibdir/*
%endif

%changelog
* Sun Mar 15 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.74-alt1.git20150315
- Initial build for Sisyphus

