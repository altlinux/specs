%define oname mathutils

%def_without python2
%def_with python3

Name: python-module-%oname
Version: 2.74
Release: alt1.git20150315.1.1.1
Summary: Library providing Matrix, Vector, Quaternion, Euler and Color classes
License: GPLv2+
Group: Development/Python
Url: https://pypi.python.org/pypi/mathutils/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://gitlab.com/ideasman42/blender-mathutils.git
Source: %name-%version.tar

%if_with python2
#BuildPreReq: python-devel python-module-setuptools cmake gcc-c++
%endif
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools cmake gcc-c++
%endif

%py_provides %oname

# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: cmake-modules elfutils libstdc++-devel python-base python3 python3-base python3-module-pytest python3-module-setuptools
BuildRequires: cmake gcc-c++ python3-devel python3-module-setuptools rpm-build-python3

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
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 2.74-alt1.git20150315.1.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Thu Mar 17 2016 Ivan Zakharyaschev <imz@altlinux.org> 2.74-alt1.git20150315.1.1
- (NMU) rebuild with python3-3.5 & rpm-build-python3-0.1.10
  (for ABI dependence and new python3(*) reqs)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 2.74-alt1.git20150315.1
- NMU: Use buildreq for BR.

* Sun Mar 15 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.74-alt1.git20150315
- Initial build for Sisyphus

