%define modulename FormEncode

%def_with python3

%if_with python3
%define py3name python3-module-%modulename
%define py3dir %py3name-%version
%endif

Name: python-module-%modulename
Version: 1.3.0
Release: alt1.git20150207.1
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

#BuildPreReq: %py_dependencies setuptools
#BuildPreReq: python-module-docutils python-module-sphinx-devel
#BuildPreReq: python-module-pycountry
#BuildPreReq: python-module-nose
#BuildPreReq: python-module-dns

%if_with python3
#BuildPreReq: rpm-build-python3
#BuildPreReq: python-tools-2to3
#BuildPreReq: python3-devel
#BuildPreReq: python3-module-distribute
#BuildPreReq: python3-module-docutils
#BuildPreReq: python3-module-nose
#BuildPreReq: python3-module-pycountry
#BuildPreReq: python3-module-dns
%endif

BuildRequires(pre): rpm-macros-sphinx
# Automatically added by buildreq on Wed Jan 27 2016 (-bi)
# optimized out: python-base python-devel python-module-PyStemmer python-module-Pygments python-module-babel python-module-cssselect python-module-genshi python-module-jinja2 python-module-jinja2-tests python-module-markupsafe python-module-pytz python-module-setuptools python-module-six python-module-snowballstemmer python-module-sphinx python-module-sphinx_rtd_theme python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-json python-modules-logging python-modules-multiprocessing python-modules-unittest python-modules-xml python3 python3-base python3-module-Pygments python3-module-babel python3-module-cssselect python3-module-docutils python3-module-genshi python3-module-jinja2 python3-module-pytz python3-module-setuptools python3-module-snowballstemmer
BuildRequires: python-module-alabaster python-module-dns python-module-docutils python-module-html5lib python-module-nose python-module-objects.inv python-module-pycountry python3-module-dns python3-module-html5lib python3-module-nose python3-module-sphinx rpm-build-python3 time

%description
FormEncode validates and converts nested structures. It allows for
a declarative form of defining the validation, and decoupled processes
for filling and generating forms.

%if_with python3
%package -n %py3name
Summary: HTML form validation, generation, and convertion package for Python 3
Group: Development/Python3
BuildArch: noarch

%description -n %py3name
FormEncode validates and converts nested structures. It allows for
a declarative form of defining the validation, and decoupled processes
for filling and generating forms.

%endif

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
%if_with python3
rm -rf ../%py3dir
cp -a . ../%py3dir
%endif

%prepare_sphinx .

%build
%python_build
%if_with python3
pushd ../%py3dir
%python3_build
popd
%endif

%install
%python_install
rm -rf %buildroot%python_sitelibdir/docs
%if_with python3
pushd ../%py3dir
%python3_install
rm -rf %buildroot%python3_sitelibdir/docs
popd
%endif

pushd docs
export PYTHONPATH=%buildroot%python_sitelibdir
%make html
%make pickle
cp -fR _build/pickle %buildroot%python_sitelibdir/formencode/
popd

%files
%doc docs/*.txt
%python_sitelibdir/*
%exclude %python_sitelibdir/*/pickle

%if_with python3
%files -n %py3name
%doc ../%py3dir/docs/*.txt
%python3_sitelibdir/*
%endif

%files doc
%doc docs/_build/html examples

%files pickles
%python_sitelibdir/*/pickle

%changelog
* Wed Jan 27 2016 Mikhail Efremov <sem@altlinux.org> 1:1.3.0-alt1.git20150207.1
- NMU: Use buildreq for BR.

* Wed Feb 25 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:1.3.0-alt1.git20150207
- 1.3.0 released

* Thu Mar 21 2013 Aleksey Avdeev <solo@altlinux.ru> 1:1.3.0-alt1.git20130312
- New snapshot
- Added module for Python 3

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
