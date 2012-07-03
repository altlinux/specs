%define oname gts
Name: python-module-%oname
Version: 0.3.1
Release: alt1.svn20090606.1
Summary: Pythonic binding for the GNU Triangulated Surface (GTS) Library
License: LGPLv2+
Group: Development/Python
Url: http://pygts.sourceforge.net/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel libgts-devel libnumpy-devel

%description
PyGTS is a python package used to construct, manipulate, and perform
computations on 3D triangulated surfaces. It is a hand-crafted and
pythonic binding for the GNU Triangulated Surface (GTS) Library.

%prep
%setup

%build
%add_optflags -fno-strict-aliasing
%python_build_debug

%install
%python_install

%files
%doc AUTHORS ChangeLog FAQ README* doc/*
%python_sitelibdir/*

%changelog
* Thu Apr 12 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 0.3.1-alt1.svn20090606.1
- Rebuild to remove redundant libpython2.7 dependency

* Mon Dec 19 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.1-alt1.svn20090606
- Initial build for Sisyphus

