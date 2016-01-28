# vim: set ft=spec: -*- rpm-spec -*-

%define modulename persistent

%def_with python3

%if_with python3
%define py3name python3-module-%modulename
%define py3dir %py3name-%version
%endif

Name: python-module-%modulename
Version: 4.1.1
Release: alt2.1

%setup_python_module %modulename

Summary: Translucent persistent objects
License: ZPL 2.1
Group: Development/Python

Url: http://www.zope.org/Products/ZODB
Packager: Aleksey Avdeev <solo@altlinux.ru>

# git://github.com/zopefoundation/persistent.git
Source: %name-%version.tar

#BuildPreReq: python-module-coverage
#BuildPreReq: python-module-nose
#BuildPreReq: python-module-zope.interface
#BuildPreReq: python-module-setuptools-tests
#BuildPreReq: python-module-sphinx-devel
#BuildPreReq: python-module-repoze.sphinx.autointerface

%if_with python3
#BuildPreReq: rpm-build-python3
#BuildPreReq: python3-devel
#BuildPreReq: python3-module-coverage
#BuildPreReq: python3-module-distribute
#BuildPreReq: python3-module-nose
#BuildPreReq: python3-module-zope.interface
#BuildPreReq: python3-module-setuptools-tests
%endif

BuildRequires(pre): rpm-macros-sphinx
# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: elfutils python-base python-devel python-module-PyStemmer python-module-Pygments python-module-babel python-module-cssselect python-module-genshi python-module-jinja2 python-module-jinja2-tests python-module-markupsafe python-module-pytest python-module-pytz python-module-repoze python-module-repoze.sphinx python-module-setuptools python-module-six python-module-snowballstemmer python-module-sphinx python-module-sphinx_rtd_theme python-module-zope python-module-zope.interface python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-json python-modules-logging python-modules-multiprocessing python-modules-unittest python3 python3-base python3-module-pytest python3-module-setuptools python3-module-zope.interface
BuildRequires: python-module-alabaster python-module-coverage python-module-docutils python-module-html5lib python-module-nose python-module-objects.inv python-module-repoze.sphinx.autointerface python-module-setuptools-tests python3-devel python3-module-coverage python3-module-nose python3-module-setuptools-tests python3-module-zope rpm-build-python3 time

%description
This package contains a generic persistence implementation for Python.
It forms the core protocol for making objects interact "transparently"
with a database such as the ZODB.

%package docs
Summary: Documentation for translucent persistent objects
Group: Development/Documentation
BuildArch: noarch

%description docs
This package contains documentation for persistence implementation for
Python. It forms the core protocol for making objects interact
"transparently" with a database such as the ZODB.

%package tests
Summary: Tests for translucent persistent objects
Group: Development/Python
Requires: %name = %EVR

%description tests
This package contains a generic tests persistence implementation for
Python. It forms the core protocol for making objects interact
"transparently" with a database such as the ZODB.

%if_with python3
%package -n %py3name
Summary: Sample python3 module specfile
Group: Development/Python

%description -n %py3name
This specfile is provided as sample specfile for python3 module
packages. It contains most of usual tags and constructions used in such
specfiles.

%package -n %py3name-tests
Summary: Sample python3 module tests specfile
Group: Development/Python
Requires: %py3name = %EVR

%description -n %py3name-tests
This specfile is provided as sample specfile for python3 module tests
packages. It contains most of usual tags and constructions used in such
specfiles.

%endif

%prep
%setup
%if_with python3
rm -rf ../%py3dir
cp -a . ../%py3dir
%endif

%prepare_sphinx .
ln -s ../objects.inv docs/

%build
%python_build
%if_with python3
pushd ../%py3dir
%python3_build
popd
%endif

%install
%if_with python3
pushd ../%py3dir
%python3_install
install -p -m644 persistent/_compat.h \
	%buildroot%_includedir/python%_python3_version%_python3_abiflags/
popd
%endif

%python_install
install -p -m644 persistent/_compat.h \
	%buildroot%_includedir/python%_python_version/

export PYTHONPATH=%buildroot%python_sitelibdir
%make -C docs html

%check
%__python setup.py test -q
%if_with python3
pushd ../%py3dir
%__python3 setup.py test -q
popd
%endif

%files
%doc *.txt
%_includedir/python%_python_version
%python_sitelibdir/%modulename/
%exclude %python_sitelibdir/%modulename/test*
%python_sitelibdir/*.egg-info

%files tests
%python_sitelibdir/%modulename/test*

%files docs
%doc docs/_build/html/*

%if_with python3
%files -n %py3name
%doc *.txt
%_includedir/python%_python3_version%_python3_abiflags
%python3_sitelibdir/%modulename/
%exclude %python3_sitelibdir/%modulename/test*
%python3_sitelibdir/*.egg-info

%files -n %py3name-tests
%python3_sitelibdir/%modulename/test*
%endif

%changelog
* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 4.1.1-alt2.1
- NMU: Use buildreq for BR.

* Fri Aug 28 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.1.1-alt2
- Really version 4.1.1

* Wed Aug 26 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.1.1-alt1
- Version 4.1.1

* Thu Jul 17 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.8-alt2
- Avoid conflict with ZODB3

* Wed Jul 16 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.8-alt1
- Version 4.0.8

* Thu Nov 28 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.6-alt1.1
- Fixed build

* Wed Mar 13 2013 Aleksey Avdeev <solo@altlinux.ru> 4.0.6-alt1
- Initial build for ALT Linux Sisyphus
