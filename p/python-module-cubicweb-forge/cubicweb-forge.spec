%define oname cubicweb-forge
Name: python-module-%oname
Version: 1.10.2
Release: alt1
Summary: Software forge component for the CubicWeb framework
License: LGPL
Group: Development/Python
Url: https://pypi.python.org/pypi/cubicweb-forge/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-module-setuptools-tests cubicweb
BuildPreReq: python-module-Pillow python-module-markdown
BuildPreReq: python-module-cubicweb-card
BuildPreReq: python-module-cubicweb-comment
BuildPreReq: python-module-cubicweb-email
BuildPreReq: python-module-cubicweb-file
BuildPreReq: python-module-cubicweb-folder
BuildPreReq: python-module-cubicweb-mailinglist
BuildPreReq: python-module-cubicweb-tag
BuildPreReq: python-module-cubicweb-testcard
BuildPreReq: python-module-cubicweb-tracker
BuildPreReq: python-module-cubicweb-nosylist

Requires: cubicweb python-module-cubicweb-card
Requires: python-module-cubicweb-comment
Requires: python-module-cubicweb-email
Requires: python-module-cubicweb-file
Requires: python-module-cubicweb-folder
Requires: python-module-cubicweb-mailinglist
Requires: python-module-cubicweb-tag
Requires: python-module-cubicweb-testcard
Requires: python-module-cubicweb-tracker
Requires: python-module-cubicweb-nosylist
%py_requires PIL

%description
This cube provides a full-featured software to support the process of
collaborative developing software. This is built on the tracker cube and
implements user friendly representation of the project: you can
associate to a projet some screenshots, some attachments, a
documentation page and so on.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
This cube provides a full-featured software to support the process of
collaborative developing software. This is built on the tracker cube and
implements user friendly representation of the project: you can
associate to a projet some screenshots, some attachments, a
documentation page and so on.

This package contains tests for %oname.

%prep
%setup

%build
%python_build_debug

%install
%python_install

%check
python setup.py test

%files
%doc README
%python_sitelibdir/*
%_datadir/cubicweb/*
%exclude %python_sitelibdir/*/test*

%files tests
%python_sitelibdir/*/test*

%changelog
* Thu Jan 15 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.10.2-alt1
- Initial build for Sisyphus

