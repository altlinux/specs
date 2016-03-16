%define oname uranium

%def_with python3
%def_disable check

Name: python-module-%oname
Version: 0.0.52
Release: alt1.git20150209.1.1
Summary: A build system for python
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/uranium/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/toumorokoshi/uranium.git
Source: %name-%version.tar
BuildArch: noarch

#BuildPreReq: python-devel python-module-setuptools-tests
#BuildPreReq: python-module-docopt python-module-jinja2
#BuildPreReq: python-module-pip python-module-yaml
#BuildPreReq: python-module-requests python-module-six
#BuildPreReq: python-module-virtualenv python-module-zc.buildout
#BuildPreReq: python-module-httpretty python-module-nose
#BuildPreReq: python-module-mock python-module-tornado
#BuildPreReq: python-module-sphinx-devel python-module-sphinx_rtd_theme
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools-tests
#BuildPreReq: python3-module-docopt python3-module-jinja2
#BuildPreReq: python3-module-pip python3-module-yaml
#BuildPreReq: python3-module-requests python3-module-six
#BuildPreReq: python3-module-virtualenv python3-module-zc.buildout
#BuildPreReq: python3-module-httpretty python3-module-nose
#BuildPreReq: python3-module-mock python3-module-tornado
%endif

%py_provides %oname
%py_requires docopt jinja2 pip yaml requests six virtualenv zc.buildout

BuildRequires(pre): rpm-macros-sphinx
# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: python-base python-devel python-module-BTrees python-module-PyStemmer python-module-Pygments python-module-ZODB python-module-babel python-module-cffi python-module-cryptography python-module-cssselect python-module-enum34 python-module-genshi python-module-jinja2 python-module-jinja2-tests python-module-markupsafe python-module-ntlm python-module-persistent python-module-pyasn1 python-module-pytz python-module-setuptools python-module-six python-module-snowballstemmer python-module-sphinx python-module-sphinx_rtd_theme python-module-transaction python-module-zc.buildout python-module-zc.lockfile python-module-zc.zlibstorage python-module-zdaemon python-module-zope.event python-module-zope.interface python-module-zope.proxy python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-json python-modules-multiprocessing python-modules-unittest python3 python3-base python3-module-BTrees python3-module-ZODB python3-module-cffi python3-module-cryptography python3-module-cssselect python3-module-enum34 python3-module-genshi python3-module-jinja2 python3-module-ndg-httpsclient python3-module-ntlm python3-module-persistent python3-module-pip python3-module-pycparser python3-module-setuptools python3-module-transaction python3-module-zc.buildout python3-module-zc.lockfile python3-module-zc.zlibstorage python3-module-zdaemon python3-module-zope python3-module-zope.event python3-module-zope.interface python3-module-zope.proxy
BuildRequires: python-module-alabaster python-module-chardet python-module-docutils python-module-html5lib python-module-ndg-httpsclient python-module-nose python-module-objects.inv python-module-pbr python-module-pip python-module-pycares python-module-pycurl python-module-pytest python-module-unittest2 python-module-virtualenv python-module-yaml python-module-zc.recipe.egg python-modules-wsgiref python3-module-chardet python3-module-html5lib python3-module-mimeparse python3-module-nose python3-module-pbr python3-module-pycares python3-module-pytest python3-module-unittest2 python3-module-urllib3 python3-module-virtualenv python3-module-yaml python3-module-zc.recipe.egg rpm-build-python3 time

%description
uranium is a build system that allows for compilation of python-based
services and tools.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires httpretty nose mock

%description tests
uranium is a build system that allows for compilation of python-based
services and tools.

This package contains tests for %oname.

%package -n python3-module-%oname
Summary: A build system for python
Group: Development/Python3
%py3_provides %oname
%py3_requires docopt jinja2 pip yaml requests six virtualenv zc.buildout

%description -n python3-module-%oname
uranium is a build system that allows for compilation of python-based
services and tools.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR
%py3_requires httpretty nose mock

%description -n python3-module-%oname-tests
uranium is a build system that allows for compilation of python-based
services and tools.

This package contains tests for %oname.

%package pickles
Summary: Pickles for %oname
Group: Development/Python

%description pickles
uranium is a build system that allows for compilation of python-based
services and tools.

This package contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
uranium is a build system that allows for compilation of python-based
services and tools.

This package contains documentation for %oname.

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

%prepare_sphinx .
ln -s ../objects.inv docs/

%build
%python_build_debug

%if_with python3
pushd ../python3
%python3_build_debug
popd
%endif

%install
%if_with python3
pushd ../python3
%python3_install
popd
pushd %buildroot%_bindir
for i in $(ls); do
	mv $i $i.py3
done
popd
%endif

%python_install

%make -C docs pickle
%make -C docs html

cp -fR docs/_build/pickle %buildroot%python_sitelibdir/%oname/

%check
python setup.py test
%if_with python3
pushd ../python3
python3 setup.py test
popd
%endif

%files
%doc *.md examples
%_bindir/*
%if_with python3
%exclude %_bindir/*.py3
%endif
%python_sitelibdir/*
%exclude %python_sitelibdir/*/pickle
%exclude %python_sitelibdir/*/tests
%exclude %python_sitelibdir/*/example*

%files tests
%python_sitelibdir/*/tests
%python_sitelibdir/*/example*

%files pickles
%python_sitelibdir/*/pickle

%files docs
%doc docs/_build/html/*

%if_with python3
%files -n python3-module-%oname
%doc *.md examples
%_bindir/*.py3
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests
%exclude %python3_sitelibdir/*/example*
%exclude %python3_sitelibdir/*/*/example*

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/tests
%python3_sitelibdir/*/example*
%python3_sitelibdir/*/*/example*
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.0.52-alt1.git20150209.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.0.52-alt1.git20150209.1
- NMU: Use buildreq for BR.

* Tue Feb 10 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.52-alt1.git20150209
- Version 0.0.52

* Wed Feb 04 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.49-alt1.git20150203
- Version 0.0.49

* Wed Jan 28 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.39-alt1.git20150126
- Version 0.0.39

* Mon Jan 26 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.37-alt1.git20150125
- Version 0.0.37

* Tue Jan 20 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.26-alt1.git20150119
- New snapshot

* Mon Jan 19 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.26-alt1.git20150118
- Initial build for Sisyphus

