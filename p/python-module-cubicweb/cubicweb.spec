%define oname cubicweb
Name: python-module-%oname
Version: 3.25.3
Release: alt1
Summary: A repository of entities / relations for knowledge management
License: LGPL
Group: Development/Python
BuildArch: noarch
Url: https://pypi.python.org/pypi/cubicweb/

Source: %name-%version.tar
Patch1: %oname-%version-alt-build.patch

BuildRequires: python-dev python-module-setuptools-tests
BuildRequires: python-module-logilab-common python-module-logilab-mtconverter
BuildRequires: python-module-rql python-module-yams
BuildRequires: python-module-lxml python-module-logilab-database
BuildRequires: python-module-passlib python-module-pytz
BuildRequires: python-module-markdown
BuildRequires: python-module-twisted-core
BuildRequires: python-module-twisted-web
BuildRequires: python-module-docutils
BuildRequires: python-module-Pillow
BuildRequires: python-module-pycrypto python-module-fyzz
BuildRequires: python-module-vobject python-module-rdflib
BuildRequires: python-module-logilab-constraint
BuildRequires: python-module-yapps2
BuildRequires: python2.7(wsgicors) python2.7(pyramid.config) python2.7(webtest) python2.7(pyramid_multiauth)
BuildRequires: python2.7(backports.tempfile)

%py_requires twisted.internet twisted.web logilab.common docutils rdflib
%py_requires logilab.mtconverter logilab.database PIL vobject
%py_requires cubicweb.devtools.testlib sqlite3 logilab.constraint
%py_requires markdown

%description
CubicWeb is a entities / relations based knowledge management system
developped at Logilab.

%package -n %oname
Summary: RQL command line client to the repository and data files
Group: Development/Other
Requires: %name = %EVR
%py_provides cubes

%description -n %oname
CubicWeb is a entities / relations based knowledge management system
developped at Logilab.

This package contains RQL command line client to the repository and data
files.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires logilab.common.testlib

%description tests
CubicWeb is a entities / relations based knowledge management system
developped at Logilab.

This package contains tests for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
CubicWeb is a entities / relations based knowledge management system
developped at Logilab.

This package contains documentation for %oname.

%prep
%setup
%patch1 -p1

%build
%python_build_debug

%install
%python_install

install -d %buildroot%_man1dir
install -p -m644 man/* %buildroot%_man1dir/

%check
python setup.py test

%files -n %oname
%doc README
%_bindir/*
%_man1dir/*
%_datadir/%oname

%files
%python_sitelibdir/*
%exclude %python_sitelibdir/*/test
%exclude %python_sitelibdir/*/*/test*

%files tests
%python_sitelibdir/*/test
%python_sitelibdir/*/*/test*

%files docs
%doc doc/*

%changelog
* Mon Dec 11 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 3.25.3-alt1
- Updated to upstream version 3.25.3.

* Mon Oct 16 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 3.25.2-alt1
- Updated to upstream version 3.25.2.

* Wed Feb 18 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.20.4-alt1
- Version 3.20.4

* Fri Jan 16 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.20.1-alt2
- Added requires: markdown

* Thu Jan 15 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.20.1-alt1
- Version 3.20.1

* Tue Dec 09 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.19.6-alt1
- Version 3.19.6

* Thu Nov 27 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.19.5-alt3.hg20141124
- Provides cubes

* Thu Nov 27 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.19.5-alt2.hg20141124
- Added necessary requirements

* Tue Nov 25 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.19.5-alt1.hg20141124
- New snapshot

* Wed Nov 05 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.19.5-alt1.hg20140730
- Initial build for Sisyphus

