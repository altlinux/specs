%define oname encore

%def_without docs

%def_with check

Name: python3-module-%oname
Version: 0.8.0
Release: alt1

Summary: A Collection of core-level utility modules for Enthought projects
License: BSD-3-Clause and Apache-2.0
Group: Development/Python3
Url: https://pypi.org/project/encore

VCS: https://github.com/enthought/encore
Source: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-wheel
%if_with docs
BuildRequires: python3-module-sphinx
%endif

%if_with check
BuildRequires: python3-modules-sqlite3
BuildRequires: python3-module-requests
%endif

%description
This package consists of a collection of core utility packages useful for
building Python applications.  This package is intended to be at the
bottom of the software stack and have zero required external dependencies
aside from the Python Standard Library.

%package docs
Summary: Documentation for encore
Group: Development/Documentation

%description docs
This package consists of a collection of core utility packages useful for
building Python applications.  This package is intended to be at the
bottom of the software stack and have zero required external dependencies
aside from the Python Standard Library.

This package contains documentation for encore.

%package tests
Summary: Tests for encore
Group: Development/Python3
Requires: %name = %EVR

%description tests
This package consists of a collection of core utility packages useful for
building Python applications.  This package is intended to be at the
bottom of the software stack and have zero required external dependencies
aside from the Python Standard Library.

This package contains tests for encore.

%prep
%setup

sed -i 's|sphinx-build|sphinx-build-3|' docs/Makefile

%build
%pyproject_build

%install
%pyproject_install

%if_with docs
export PYTHONPATH=%buildroot%python3_sitelibdir
%make -C docs html

cp -fR docs/build/pickle %buildroot%python3_sitelibdir/%oname/
%endif

%check
%tox_create_default_config
%tox_check_pyproject

%files
%doc LICENSE.txt README.rst
%python3_sitelibdir/%oname
%python3_sitelibdir/%{pyproject_distinfo %oname}
%exclude %python3_sitelibdir/*/testing
%exclude %python3_sitelibdir/*/*/tests
%exclude %python3_sitelibdir/*/*/*/tests

%if_with docs
%files docs
%doc docs/build/html/*
%endif

%files tests
%python3_sitelibdir/*/testing
%python3_sitelibdir/*/*/tests
%python3_sitelibdir/*/*/*/tests


%changelog
* Wed Feb 22 2023 Anton Vyatkin <toni@altlinux.org> 0.8.0-alt1
- new version 0.8.0

* Fri Jan 17 2020 Andrey Bychkov <mrdrew@altlinux.org> 0.7.0-alt1
- Version updated to 0.7.0
- porting on python3.

* Tue Dec 09 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.1-alt1.dev.git20141208
- Version 0.6.1.dev

* Mon Nov 03 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.0-alt2.git20140910
- New snapshot

* Thu May 08 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.0-alt2.git20140422
- Moved tests into tests subpackage

* Wed May 07 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.0-alt1.git20140422
- Version 0.6.0

* Sun Oct 27 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.0-alt1.git20131018
- Version 0.4.0

* Mon May 06 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3-alt1.git20130405
- Version 0.3

* Wed Jan 30 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.1-alt1.git20130115
- New snapshot

* Mon Oct 15 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.1-alt1.git20120822
- Version 0.2.1

* Thu Jan 26 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1-alt1.git20120119
- Initial build for Sisyphus

