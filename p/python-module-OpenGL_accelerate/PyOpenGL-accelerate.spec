%define oname OpenGL_accelerate

%def_with python3

Name: python-module-%oname
Version: 3.1.0
Release: alt1
Summary: Acceleration code for PyOpenGL
License: BSD
Group: Development/Python
Url: http://pyopengl.sourceforge.net/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-Cython
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-Cython
%endif

%description
This set of C (Cython) extensions provides acceleration of common
operations for slow points in PyOpenGL 3.x.

%package -n python3-module-%oname
Summary: Acceleration code for PyOpenGL
Group: Development/Python3

%description -n python3-module-%oname
This set of C (Cython) extensions provides acceleration of common
operations for slow points in PyOpenGL 3.x.

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

%build
%add_optflags -fno-strict-aliasing

%python_build_debug

%if_with python3
pushd ../python3
%python3_build_debug
popd
%endif

%install
%python_install

%if_with python3
pushd ../python3
%python3_install
popd
%endif

%files
%doc *.txt
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.txt
%python3_sitelibdir/*
%endif

%changelog
* Sun Aug 24 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.1.0-alt1
- Initial build for Sisyphus

