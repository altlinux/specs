%define oname ascot
Name: python-module-%oname
Version: 0.8.0
Release: alt1.bzr20120110
Summary: Automated Stability Condition Tester
Group: Development/Python
License:GPL v3
URL: http://www.fenics.org/
# bzr branch lp:ascot
Source: %oname-%version.tar.gz
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

%setup_python_module %oname
BuildPreReq: libdolfin-real-devel libslepc-real-devel
BuildArch: noarch

%description
ASCoT tests the inf-sup stability of a family of finite element
discretizations for a given variational form.

%prep
%setup

%build
%python_build

%install
%python_install

%files
%doc AUTHORS COPYING README demo
%python_sitelibdir/*

%changelog
* Tue Jan 17 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8.0-alt1.bzr20120110
- New snapshot

* Wed Dec 07 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8.0-alt1.bzr20111017
- New snapshot

* Mon Nov 14 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.8.0-alt1.bzr20110310.1
- Rebuild with Python-2.7

* Fri Apr 15 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8.0-alt1.bzr20110310
- New snapshot

* Fri Nov 26 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8.0-alt1.bzr20101025
- Version 0.8.0

* Tue Aug 10 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.0-alt1.bzr20100412
- Version 0.1.0

* Sat Dec 19 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.1-alt1.bzr20091109
- Initial build for Sisyphus

