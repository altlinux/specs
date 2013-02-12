%define modulename FormEncode

Name: python-module-%modulename
Version: 1.3.0
Release: alt1.git20130201
Epoch: 1

%setup_python_module %modulename

Summary: HTML form validation, generation, and convertion package for Python
License: PSF
Group: Development/Python

URL: http://formencode.org
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>
BuildArch: noarch

# git://github.com/formencode/formencode.git
Source0: %name-%version.tar

BuildPreReq: %py_dependencies setuptools
BuildPreReq: python-module-docutils python-module-sphinx-devel
BuildPreReq: python-module-pydns python-module-pycountry
BuildPreReq: python-module-nose

%description
FormEncode validates and converts nested structures. It allows for
a declarative form of defining the validation, and decoupled processes
for filling and generating forms.

%package doc
Summary: This package contains documentation and examples for FormEncode
Group: Development/Documentation

%description doc
FormEncode validates and converts nested structures. It allows for
a declarative form of defining the validation, and decoupled processes
for filling and generating forms.

%package pickles
Summary: This package contains pickles for FormEncode
Group: Development/Python

%description pickles
FormEncode validates and converts nested structures. It allows for
a declarative form of defining the validation, and decoupled processes
for filling and generating forms.

%prep
%setup

%prepare_sphinx .

%build
%python_build

%install
%python_install

pushd docs
export PYTHONPATH=%buildroot%python_sitelibdir
%make html
%make pickle
cp -fR _build/pickle %buildroot%python_sitelibdir/formencode/
popd

%files
%python_sitelibdir/*
%exclude %python_sitelibdir/*/pickle

%files doc
%doc docs/_build/html examples

%files pickles
%python_sitelibdir/*/pickle

%changelog
* Tue Feb 12 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:1.3.0-alt1.git20130201
- Version 1.3.0

* Fri Sep 21 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:1.2.4-alt1.git20120914
- New snapshot

* Thu Dec 08 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.4-alt1.hg20110930
- Version 1.2.4

* Mon Oct 24 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.2.3-alt2.hg20100922.1
- Rebuild with Python-2.7

* Sat Nov 27 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.3-alt2.hg20100922
- New snapshot (svn -> hg)

* Thu Jul 15 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.3-alt1.svn20100511
- Version 1.2.3

* Thu Nov 19 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.2-alt2
- Rebuilt with python 2.6

* Sat Apr 04 2009 Vladimir V. Kamarzin <vvk@altlinux.org> 1.2.2-alt1
- 1.2.2

* Thu Jan 24 2008 Grigory Batalov <bga@altlinux.ru> 0.4-alt2.1.0.1
- Rebuilt with python-2.5.

* Sun Mar 25 2007 ALT QA Team Robot <qa-robot@altlinux.org> 0.4-alt2.1.0
- Rebuilt with rpm-build-python-0.30-alt3.

* Thu Mar 02 2006 Maxim Bodyansky <maximbo@altlinux.ru> 0.4-alt2.1
- add_python_req_skip dispatch sqlobject pkg_resources

* Thu Nov 24 2005 Maxim Bodyansky <maximbo@altlinux.ru> 0.4-alt2
- new upstream's version

* Sun Nov 06 2005 Maxim Bodyansky <maximbo@altlinux.ru> 0.2.2-alt1
- Initial build for Sisyphus
