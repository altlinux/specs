%global pypi_name pycollada
%global oname collada

%global descr pycollada is a python module for creating, editing and loading COLLADA,\
which is a COLLAborative Design Activity for establishing an interchange\
file format for interactive 3D applications.\
\
The library allows you to load a COLLADA file and interact with it as a\
python object. In addition, it supports creating a collada python object\
from scratch, as well as in-place editing.

Name: python3-module-%pypi_name
Version: 0.9.3
Release: alt1

Summary: A python COLLADA library. Can be used to create, edit and load COLLADA documents
License: BSD-3-Clause
Group: Development/Python3
URL: https://github.com/pycollada/pycollada
VCS: https://pycollada.readthedocs.io

Source: %pypi_name-%version.tar

BuildRequires(pre): rpm-macros-python3
BuildRequires: rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-numpy
BuildRequires: python3-module-dateutil
BuildRequires: python3-module-lxml

BuildArch: noarch

%description
%descr

%package tests
Summary: Tests for pycollada
Group: Development/Python3
Requires: %name

%description tests
This package contains tests for pycollada

%descr

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%files
%doc AUTHORS.md CHANGELOG.rst COPYING README.markdown
%python3_sitelibdir_noarch/%oname
%exclude %python3_sitelibdir_noarch/%oname/tests
%python3_sitelibdir_noarch/%{pyproject_distinfo %pypi_name}

%files tests
%python3_sitelibdir_noarch/%oname/tests

%changelog
* Mon Nov 02 2026 Ulysses Apokin <ulysses@altlinux.org> 0.9.3-alt1
- New version.

* Mon Feb 03 2020 Andrey Bychkov <mrdrew@altlinux.org> 0.4.1-alt3
- Build for python2 disabled.

* Wed May 16 2018 Andrey Bychkov <mrdrew@altlinux.org> 0.4.1-alt2.git20140411.2
- (NMU) rebuild with python3.6

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.4.1-alt2.git20140411.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Sat Aug 16 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.1-alt2.git20140411
- Added module for Python 3

* Mon Jul 14 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.1-alt1.git20140411
- Version 0.4.1

* Tue Apr 02 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4-alt1.git20130302
- Version 0.4

* Mon Dec 12 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3-alt1.git20111115
- New snapshot

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.3-alt1.git20110831.1
- Rebuild with Python-2.7

* Thu Sep 01 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3-alt1.git20110831
- Initial build for Sisyphus

