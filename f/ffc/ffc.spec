# REMOVE ME (I was set for NMU) and uncomment real Release tags:
Release: alt1.dev.git20150430.1
Name:           ffc
Version:        1.6.0
#Release:        alt1.dev.git20150430
Epoch: 1
Summary:        Compiler for finite element variational forms
Group:          Development/Tools
License:        LGPL v3
URL:            http://fenicsproject.org/
# https://bitbucket.org/fenics-project/ffc.git
Source: %name-%version.tar.gz
Source1: http://www.fenics.org/pub/documents/ffc/ffc-user-manual/ffc-user-manual.pdf
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Requires: python-module-%name = %epoch:%version-%release

BuildRequires(pre): rpm-build-python
BuildPreReq: python-devel swig
BuildPreReq: libnumpy-devel python-module-fiat
BuildPreReq: python-module-ferari gcc-c++

Obsoletes: python-module-ufc

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
Requires: python-module-fiat python-module-ferari
%setup_python_module ffc
%py_provides ffc
%py_requires FIAT ferari
Obsoletes: python-module-ufc
#add_python_req_skip reassign

%description -n python-module-%name
FFC is a compiler for finite element variational forms. From a high-level
description of the form, it generates efficient low-level C++ code that
can be used to assemble the corresponding discrete operator (tensor). In
particular, a bilinear form may be assembled into a matrix and a linear
form may be assembled into a vector.

This package contains python module of FFC.

%package -n ufc-devel
Summary: Development files for UFC
Group: Development/Other
Requires: %name = %EVR

%description -n ufc-devel
UFC (Unified Form-assembly Code) is a unified framework for finite
element assembly. More precisely, it defines a fixed interface for
communicating low level routines (functions) for evaluating and
assembling finite element variational forms. The UFC interface
consists of a single header file ufc.h that specifies a C++ interface
that must be implemented by code that complies with the UFC
specification. Examples of form compilers that support the UFC
interface are FFC and SyFi.

This package contains development files for UFC.

%prep
%setup

%build
%python_build

%install
%python_build_install --optimize=2

install -d %buildroot%_docdir/%name
install -p -m644 %SOURCE1 %buildroot%_docdir/%name

%if "%_libexecdir/pkgconfig" != "%_pkgconfigdir"
install -d %buildroot%_pkgconfigdir
mv %buildroot%_libexecdir/pkgconfig/* %buildroot%_pkgconfigdir/
%endif

touch %buildroot%python_sitelibdir/ffc_time_ext/__init__.py

%files
%doc README* AUTHORS ChangeLog COPYING
%_bindir/*
%_man1dir/*

%files doc
%_docdir/%name
%doc demo

%files -n python-module-%name
%python_sitelibdir/*

%files -n ufc-devel
%_includedir/*
%_pkgconfigdir/*
%_datadir/ufc

%changelog
* Tue Jun 07 2016 Ivan Zakharyaschev <imz@altlinux.org> 1:1.6.0-alt1.dev.git20150430.1
- (AUTO) subst_x86_64.

* Sat May 02 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:1.6.0-alt1.dev.git20150430
- Version 1.6.0dev

* Mon Nov 03 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:1.4.0-alt1.git20141022
- Version 1.4.0

* Thu May 08 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:1.3.0-alt2.git20140430
- Obsoletes: python-module-ufc

* Wed May 07 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:1.3.0-alt1.git20140430
- Version 1.3.0

* Thu Oct 24 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:1.2.0-alt2.git20131007
- New snapshot

* Mon Jun 17 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:1.2.0-alt2.git20130429
- Rebuilt with updated NumPy

* Tue May 07 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:1.2.0-alt1.git20130429
- Version 1.2.0

* Thu Jan 31 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:1.1.0-alt1.bzr20130129
- Version 1.1.0

* Mon Oct 15 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:1.0.0-alt1.bzr20120910
- New snapshot

* Mon Aug 13 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:1.0.0-alt1.bzr20120530
- New snapshot

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

