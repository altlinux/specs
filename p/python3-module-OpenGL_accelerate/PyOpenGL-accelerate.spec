%define _unpackaged_files_terminate_build 1

%define oname OpenGL_accelerate

Name: python3-module-%oname
Version: 3.1.5
Release: alt3
Summary: Acceleration code for PyOpenGL
License: BSD
Group: Development/Python3
Url: http://pyopengl.sourceforge.net/

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-Cython libnumpy-py3-devel

%description
This set of C (Cython) extensions provides acceleration of common
operations for slow points in PyOpenGL 3.x.

%prep
%setup

# Very quick fix for python3.10
sed -i 's/++Py_REFCNT(o)/Py_SET_REFCNT(o, Py_REFCNT(o) + 1)/' src/vbo.c
sed -i 's/--Py_REFCNT(o)/Py_SET_REFCNT(o, Py_REFCNT(o) - 1)/' src/vbo.c

%build
%add_optflags -fno-strict-aliasing

%python3_build

%install
%python3_install

%files
%doc *.txt
%python3_sitelibdir/*

%changelog
* Fri Dec 24 2021 Grigory Ustinov <grenka@altlinux.org> 3.1.5-alt3
- Quickfix for python3.10.

* Mon Aug 02 2021 Grigory Ustinov <grenka@altlinux.org> 3.1.5-alt2
- Drop python2 support.

* Mon Feb 01 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 3.1.5-alt1
- Updated to upstream version 3.1.5.

* Sun Jun 23 2019 Igor Vlasenko <viy@altlinux.ru> 3.1.3b1-alt2
- NMU: remove rpm-build-ubt from BR:

* Tue Apr 09 2019 Grigory Ustinov <grenka@altlinux.org> 3.1.3b1-alt1
- Build new version for python3.7.

* Fri Nov 23 2018 Leontiy Volodin <lvol@altlinux.org> 3.1.1a1-alt2
- Build fixes (removed %%ubt)

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

