%define oname uflacs

Name: python-module-%oname
Version: 0.2.0
Release: alt2.git20130926
Summary: UFL Analyser and Compiler System
Group: Development/Python
License: LGPLv3
URL: https://launchpad.net/uflacs
# https://bitbucket.org/fenics-project/uflacs.git
Source: %name-%version.tar
BuildArch: noarch
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

BuildRequires(pre): rpm-build-python
BuildPreReq: python-devel python-module-distribute

%description
The UFL Analyser and Compiler System - uflacs - is a utility for
processing UFL code in various fashions.

%prep
%setup

%build
%python_build_debug

%install
%python_install

%files
%doc README doc/*
%_bindir/*
%python_sitelibdir/*

%changelog
* Fri Oct 25 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.0-alt2.git20130926
- New snapshot

* Tue May 07 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.0-alt2.git20130322
- New snapshot

* Thu Jan 31 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.0-alt2.bzr20130130
- New snapshot

* Mon Oct 15 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.0-alt2.bzr20120928
- New snapshot

* Mon Aug 13 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.0-alt2.bzr20120622
- Added %_bindir/%oname

* Mon Aug 13 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.0-alt1.bzr20120622
- Initial build for Sisyphus

