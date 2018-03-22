%define oname OpenGL_accelerate

%def_with python3

Name: python-module-%oname
Version: 3.1.1a1
Release: alt1%ubt.1
Summary: Acceleration code for PyOpenGL
License: BSD
Group: Development/Python
Url: http://pyopengl.sourceforge.net/

Source: %name-%version.tar

BuildRequires(pre): rpm-build-ubt
BuildRequires: python-devel python-module-Cython libnumpy-devel
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-Cython libnumpy-py3-devel
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
* Thu Mar 22 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 3.1.1a1-alt1%ubt.1
- (NMU) Rebuilt with python-3.6.4.

* Sat Jan 27 2018 Anton Midyukov <antohami@altlinux.org> 3.1.1a1-alt1%ubt
- New version 3.1.1a1

* Fri Aug 18 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 3.1.0-alt3
- Updated build dependencies.

* Thu Mar 17 2016 Ivan Zakharyaschev <imz@altlinux.org> 3.1.0-alt2.1.1
- (NMU) rebuild with python3-3.5 & rpm-build-python3-0.1.10
  (for ABI dependence and new python3(*) reqs)

* Wed Jan 27 2016 Mikhail Efremov <sem@altlinux.org> 3.1.0-alt2.1
- NMU: Use buildreq for BR.

* Sun Mar 01 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.1.0-alt2
- Fixed build

* Sun Aug 24 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.1.0-alt1
- Initial build for Sisyphus

