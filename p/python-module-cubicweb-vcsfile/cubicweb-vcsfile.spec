%define _unpackaged_files_terminate_build 1
%define oname cubicweb-vcsfile

%def_disable check

Name: python-module-%oname
Version: 2.4.2
Release: alt1
Summary: Component to integrate version control systems data into the CubicWeb framework
License: LGPL
Group: Development/Python
BuildArch: noarch
Url: https://pypi.python.org/pypi/cubicweb-vcsfile/

Source: %oname-%version.tar

BuildRequires: python-module-setuptools-tests cubicweb subversion-python
BuildRequires: python-module-cubicweb-localperms mercurial
BuildRequires: python-module-cubicweb-tag
BuildRequires: python-module-cubicweb-folder
BuildRequires: python-module-logilab-mtconverter
BuildRequires: python-module-logilab-common
BuildRequires: python-module-hglib
BuildRequires: python2.7(tzlocal)

Requires: cubicweb python-module-cubicweb-localperms
Requires: python-module-cubicweb-tag
Requires: python-module-cubicweb-folder
%py_requires logilab.mtconverter logilab.common svn mercurial hglib

%description
This cube stores the data found in a version content manager repository.
It currently works with subversion or mercurial repository.

It doesn't access to the data directly. All the repository's metadata
(eg revision, file names, commit message, date and autor, etc) are
stored as entities, and thus queryable via RQL, while actual files
content is kept in the repository and fetched from there on demand.

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
%_bindir/*
%python_sitelibdir/*
%_datadir/cubicweb/*
%_docdir/%oname

%changelog
* Tue Dec 12 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 2.4.2-alt1
- Updated to upstream version 2.4.2.

* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 2.4.1-alt1
- automated PyPI update

* Wed Feb 18 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.3-alt1
- Version 2.0.3

* Fri Jan 16 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.2-alt1
- Version 2.0.2

* Tue Dec 23 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.0-alt1
- Version 2.0.0

* Thu Nov 27 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.17.0-alt1
- Initial build for Sisyphus

