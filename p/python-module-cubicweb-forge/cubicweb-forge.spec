%define _unpackaged_files_terminate_build 1
%define oname cubicweb-forge

%def_disable check

Name: python-module-%oname
Version: 1.13.0
Release: alt2
Summary: Software forge component for the CubicWeb framework
License: LGPL
Group: Development/Python
BuildArch: noarch
Url: https://pypi.python.org/pypi/cubicweb-forge/

Source: %oname-%version.tar

BuildRequires: python-module-setuptools-tests cubicweb
BuildRequires: python-module-Pillow python-module-markdown
BuildRequires: python-module-cubicweb-card
BuildRequires: python-module-cubicweb-comment
BuildRequires: python-module-cubicweb-email
BuildRequires: python-module-cubicweb-file
BuildRequires: python-module-cubicweb-folder
BuildRequires: python-module-cubicweb-mailinglist
BuildRequires: python-module-cubicweb-tag
BuildRequires: python-module-cubicweb-testcard
BuildRequires: python-module-cubicweb-tracker
BuildRequires: python-module-cubicweb-nosylist

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
%setup -n %oname-%version

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
* Tue Dec 12 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 1.13.0-alt2
- Disabled tests.

* Tue Jan 17 2017 Igor Vlasenko <viy@altlinux.ru> 1.13.0-alt1
- automated PyPI update

* Wed Feb 18 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.11.0-alt1
- Version 1.11.0

* Thu Jan 15 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.10.2-alt1
- Initial build for Sisyphus

