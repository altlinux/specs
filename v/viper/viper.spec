Name: viper
Version: 1.0.0
Release: alt1.bzr20120417
Summary: A simple mesh plotter and run--time visualization module
License: LGPL v3+
Group: Graphics
Url: http://fenicsproject.org/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>
BuildArch: noarch

# bzr branch lp:fenics-viper
Source: %name-%version.tar.gz

Requires: python-module-%name
BuildPreReq: python-devel

%description
Viper is a simple mesh plotter and run--time visualization module. Viper is
part of the FEniCS project.

Originally, Viper was a simple hack to make run-time visualization for PyCC.
The aim of Viper is efficiency and simplicity. Therefore, only default filters
and modules are available, and only very limited configuration is possible.

Recently, Viper has been expanded to provide plotting for Dolfin. The extension
is available through the viper_dolfin sub module, or directly through DOLFIN's
Python interface.

%package -n python-module-%name
Summary: Python module of Viper
Group: Development/Python
# skip requires for bootstrap
%add_python_req_skip dolfin vtk

%description -n python-module-%name
Viper is a simple mesh plotter and run--time visualization module. Viper is
part of the FEniCS project.

Originally, Viper was a simple hack to make run-time visualization for PyCC.
The aim of Viper is efficiency and simplicity. Therefore, only default filters
and modules are available, and only very limited configuration is possible.

Recently, Viper has been expanded to provide plotting for Dolfin. The extension
is available through the viper_dolfin sub module, or directly through DOLFIN's
Python interface.

This package contains Python module of Viper.

%prep
%setup

%build
%python_build

%install
%python_install

%files
%doc AUTHORS COPYING ChangeLog README doc/manual/*.pdf
%_bindir/*
%_man1dir/*

%files -n python-module-%name
%python_sitelibdir/*

%changelog
* Sun May 13 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.0-alt1.bzr20120417
- New snapshot

* Tue Jan 17 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.0-alt1.bzr20120112
- Version 1.0.0

* Tue Dec 06 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0-alt1.beta.bzr20110811
- Version 1.0-beta

* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.4.7-alt1.bzr20110602.1
- Rebuild with Python-2.7

* Wed Aug 03 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.7-alt1.bzr20110602
- New snapshot

* Fri Apr 15 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.7-alt1.bzr20110414
- Version 0.4.7

* Tue Aug 10 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.6-alt1.bzr20100701
- Version 0.4.6

* Wed Jun 16 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.5-alt1.bzr20100114
- New snapshot

* Tue Jun 15 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.5-alt1.bzr20091112.5
- Disabled requirement on dolfin

* Thu Jun 10 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.5-alt1.bzr20091112.4
- Enabled requirement on dolfin

* Thu Jun 10 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.5-alt1.bzr20091112.3
- Disabled requirement on dolfin for rebuild dolfin with NumPy 2.0.0

* Fri Dec 25 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.5-alt1.bzr20091112.2
- Enables requirement on dolfin for reform built without
  python-module-Numeric

* Thu Dec 24 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.5-alt1.bzr20091112.1
- Disabled requirement on dolfin for reform built without
  python-module-Numeric and with SuperLU 4.0

* Wed Dec 09 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.5-alt1.bzr20091112
- Version 0.4.5

* Sun Dec 06 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.3-alt4.hg20090831.2
- Rebuilt with requirement on vtk and dolfin

* Wed Nov 11 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.3-alt4.hg20090831.1
- Rebuilt with python 2.6 (bootstrap)

* Mon Aug 31 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.3-alt4.hg20090831
- Snapshot 20090831

* Sat Aug 29 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.3-alt4.hg20090819.2
- Returned requirement on VTK. Well, now requirement on Dolfin is
  disabled, awaiting pkg-config files in boost and zlib development packages

* Sat Aug 29 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.3-alt4.hg20090819.1
- Bootstrap for moving CHOLMOD and UMFPACK pkg-config files from dolfin
  into SuiteSparse

* Wed Aug 19 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.3-alt4.hg20090819
- New snapshot

* Wed Aug 19 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.3-alt3.1
- Rebuilt with requirement on vtk and dolfin

* Wed Jul 15 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.3-alt2
- Added previously skipped requirement

* Thu Jul 09 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.3-alt1
- Bootstrap

