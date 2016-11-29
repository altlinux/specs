%define oname gunicorn

%def_with python3

Name: python-module-%oname
Version: 19.6.0
Release: alt1
Summary: WSGI HTTP Server for UNIX
License: Mit
Group: Development/Python
Url: http://pypi.python.org/pypi/gunicorn
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/benoitc/gunicorn.git
Source: %name-%version.tar
BuildArch: noarch

#BuildPreReq: python-devel python-module-setuptools-tests
#BuildPreReq: python-module-sphinx-devel python-module-jinja2
#BuildPreReq: python-module-docutils python-module-pytest-cov
#BuildPreReq: python-module-mock
#BuildPreReq: python-modules-logging python-modules-multiprocessing
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools-tests
#BuildPreReq: python3-module-jinja2 python3-module-asyncio
#BuildPreReq: python3-module-docutils python3-module-pytest-cov
#BuildPreReq: python3-module-mock
%endif

%py_provides %oname
%py_requires logging

BuildRequires(pre): rpm-macros-sphinx
# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: python-base python-devel python-module-PyStemmer python-module-Pygments python-module-babel python-module-coverage python-module-cssselect python-module-funcsigs python-module-genshi python-module-jinja2 python-module-jinja2-tests python-module-linecache2 python-module-markupsafe python-module-pbr python-module-pluggy python-module-py python-module-pytest python-module-pytz python-module-setuptools python-module-six python-module-snowballstemmer python-module-sphinx python-module-sphinx_rtd_theme python-module-traceback2 python-module-unittest2 python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-json python-modules-logging python-modules-multiprocessing python-modules-unittest python-modules-xml python3 python3-base python3-module-Pygments python3-module-babel python3-module-cffi python3-module-coverage python3-module-cryptography python3-module-cssselect python3-module-docutils python3-module-enum34 python3-module-genshi python3-module-jinja2 python3-module-linecache2 python3-module-ntlm python3-module-pip python3-module-pluggy python3-module-py python3-module-pycparser python3-module-pytest python3-module-pytz python3-module-setuptools python3-module-six python3-module-snowballstemmer python3-module-traceback2
BuildRequires: python-module-alabaster python-module-docutils python-module-html5lib python-module-mock python-module-objects.inv python-module-pytest-cov python-module-setuptools-tests python3-module-html5lib python3-module-pbr python3-module-pytest-cov python3-module-setuptools-tests python3-module-sphinx python3-module-unittest2 rpm-build-python3 time

%description
Gunicorn 'Green Unicorn' is a Python WSGI HTTP Server for UNIX. It's a
pre-fork worker model ported from Ruby's Unicorn project. The Gunicorn
server is broadly compatible with various web frameworks, simply
implemented, light on server resource usage, and fairly speedy.

%package -n python3-module-%oname
Summary: WSGI HTTP Server for UNIX
Group: Development/Python3
%py3_provides %oname
%py3_requires asyncio

%description -n python3-module-%oname
Gunicorn 'Green Unicorn' is a Python WSGI HTTP Server for UNIX. It's a
pre-fork worker model ported from Ruby's Unicorn project. The Gunicorn
server is broadly compatible with various web frameworks, simply
implemented, light on server resource usage, and fairly speedy.

%package docs
Summary: Documentation for gunicorn
Group: Development/Documentation
BuildArch: noarch

%description docs
Gunicorn 'Green Unicorn' is a Python WSGI HTTP Server for UNIX. It's a
pre-fork worker model ported from Ruby's Unicorn project. The Gunicorn
server is broadly compatible with various web frameworks, simply
implemented, light on server resource usage, and fairly speedy.

This package contains documentation for gunicorn.

%package pickles
Summary: Pickles for gunicorn
Group: Development/Python

%description pickles
Gunicorn 'Green Unicorn' is a Python WSGI HTTP Server for UNIX. It's a
pre-fork worker model ported from Ruby's Unicorn project. The Gunicorn
server is broadly compatible with various web frameworks, simply
implemented, light on server resource usage, and fairly speedy.

This package contains pickles for gunicorn.

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

%prepare_sphinx docs
ln -s ../objects.inv docs/source/

%build
%python_build

%if_with python3
pushd ../python3
%python3_build
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

export PYTHONPATH=%buildroot%python_sitelibdir
%make -C docs html
%make -C docs pickle

cp -fR docs/build/pickle %buildroot%python_sitelibdir/%oname/

%check
python setup.py test
%if_with python3
pushd ../python3
python3 setup.py test
popd
%endif

%files
%doc NOTICE THANKS *.rst *.md
%_bindir/*
%if_with python3
%exclude %_bindir/*.py3
%endif
%python_sitelibdir/*
%exclude %python_sitelibdir/*/pickle
%exclude %python_sitelibdir/gunicorn/workers/_gaiohttp.py

%files docs
%doc docs/build/html examples

%files pickles
%python_sitelibdir/*/pickle

%if_with python3
%files -n python3-module-%oname
%doc NOTICE THANKS *.rst *.md
%_bindir/*.py3
%python3_sitelibdir/*
%endif

%changelog
* Tue Nov 29 2016 Alexey Shabalin <shaba@altlinux.ru> 19.6.0-alt1
- 19.6.0

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 19.2.1-alt1.git20150206.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 19.2.1-alt1.git20150206.1
- NMU: Use buildreq for BR.

* Tue Feb 17 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 19.2.1-alt1.git20150206
- Version 19.2.1

* Sun Jan 04 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 19.2.0-alt1.git20141222
- Version 19.2.0

* Mon Aug 04 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 19.1.0-alt1.git20140730
- New snapshot

* Fri Jul 11 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 19.1.0-alt1.git20140703
- Version 19.1.0

* Fri Nov 29 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 18.1-alt1.git20131125
- Version 18.1

* Tue Sep 17 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 18.0-alt1.git20130831
- Version 18.0

* Thu Feb 14 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.17.2-alt1.git20130210
- Version 0.17.2
- Added pickles

* Tue Jun 05 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.14.4-alt1.git20120604
- Initial build for Sisyphus

