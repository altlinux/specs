Name:           ffc
Version:        1.0.0
Release:        alt1.bzr20120507
Epoch: 1
Summary:        Compiler for finite element variational forms
Group:          Development/Tools
License:        LGPL v3
URL:            http://www.fenics.org/
# bzr branch lp:ffc
Source: %name-%version.tar.gz
Source1: http://www.fenics.org/pub/documents/ffc/ffc-user-manual/ffc-user-manual.pdf
BuildArch: noarch
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Requires: python-module-%name = %epoch:%version-%release

BuildRequires(pre): rpm-build-python
BuildPreReq: python-devel
BuildPreReq: libnumpy-devel python-module-fiat python-module-ufc
BuildPreReq: python-module-ferari

%description
FFC is a compiler for finite element variational forms. From a high-level
description of the form, it generates efficient low-level C++ code that
can be used to assemble the corresponding discrete operator (tensor). In
particular, a bilinear form may be assembled into a matrix and a linear
form may be assembled into a vector.

FFC may be used either from the command line (by invoking the 'ffc' command)
or as a Python module ('import ffc').

FFC is part of the FEniCS project (www.fenics.org) and functions as a
just-in-time (JIT) compiler for DOLFIN.

%package doc
Summary: User manual for FFC
Group: Development/Documentation
BuildArch: noarch

%description doc
FFC is a compiler for finite element variational forms. From a high-level
description of the form, it generates efficient low-level C++ code that
can be used to assemble the corresponding discrete operator (tensor). In
particular, a bilinear form may be assembled into a matrix and a linear
form may be assembled into a vector.

This package contains user manual for UFL (Unified Form Language).

%package -n python-module-%name
Summary: Python module of FFC
Group: Development/Python
BuildArch: noarch
Requires: python-module-fiat python-module-ufc python-module-ferari
%setup_python_module ffc
%py_provides ffc
%py_requires FIAT ufc ferari
#add_python_req_skip reassign

%description -n python-module-%name
FFC is a compiler for finite element variational forms. From a high-level
description of the form, it generates efficient low-level C++ code that
can be used to assemble the corresponding discrete operator (tensor). In
particular, a bilinear form may be assembled into a matrix and a linear
form may be assembled into a vector.

This package contains python module of FFC.

%prep
%setup

%build
%python_build

%install
%python_build_install --optimize=2

install -d %buildroot%_docdir/%name
install -p -m644 %SOURCE1 %buildroot%_docdir/%name

%files
%doc README TODO AUTHORS ChangeLog COPYING
%_bindir/*
%_man1dir/*

%files doc
%_docdir/%name
%doc demo

%files -n python-module-%name
%python_sitelibdir_noarch/*

%changelog
* Sun May 13 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:1.0.0-alt1.bzr20120507
- New snapshot

* Tue Jan 17 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:1.0.0-alt1.bzr20111207
- Version 1.0.0

* Tue Dec 06 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.rc1-alt1.bzr20111130
- Version 1.0.rc1

* Thu Oct 27 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.9.10-alt1.bzr20110708.2
- Rebuild with Python-2.7

* Thu Oct 27 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.10-alt1.bzr20110708.1
- Rebuilt with updated NumPy

* Wed Aug 03 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.10-alt1.bzr20110708
- Version 0.9.10

* Fri Apr 15 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.9-alt1.bzr20110404
- Version 0.9.9

* Tue Nov 23 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.4-alt1.bzr20101122
- Version 0.9.4

* Tue Aug 10 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.3-alt1.bzr20100724
- Version 0.9.3

* Wed Jun 16 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.2-alt1.bzr20100615
- Version 0.9.2

* Wed Dec 09 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7.1-alt3.bzr20091204
- Version 0.7.1

* Tue Nov 10 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.2-alt2.hg20090831.1
- Rebuilt with python 2.6

* Mon Aug 31 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.2-alt2.hg20090831
- Snapshot 20090831

* Tue Jul 21 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.2-alt2.hg20090819
- New snapshot

* Fri Apr 24 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.2-alt1
- Initial build for Sisyphus

