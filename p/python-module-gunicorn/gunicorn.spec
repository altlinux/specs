%define oname gunicorn

%def_with python3

Name: python-module-%oname
Version: 19.7.1
Release: alt2.1
Summary: WSGI HTTP Server for UNIX
License: Mit
Group: Development/Python
Url: http://pypi.python.org/pypi/gunicorn

# https://github.com/benoitc/gunicorn.git
Source: %name-%version.tar
Patch: deprecate-gaiohttp-worker.patch
BuildArch: noarch

BuildRequires(pre): rpm-macros-sphinx
BuildRequires: python-module-alabaster python-module-docutils python-module-html5lib python-module-mock python-module-objects.inv python-module-pytest-cov python-module-setuptools time
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-html5lib python3-module-pbr python3-module-pytest-cov python3-module-setuptools python3-module-sphinx python3-module-unittest2
%endif

%py_provides %oname
%py_requires logging

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
# python3-module-aiohtt >= 2.0 not provides aiohttp.wsgi
%add_python3_req_skip aiohttp.wsgi 

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
%patch -p1

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
PYTHONPATH=$(pwd) py.test
%if_with python3
pushd ../python3
PYTHONPATH=$(pwd) py.test3
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
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 19.7.1-alt2.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Sun Nov 19 2017 Anton Midyukov <antohami@altlinux.org> 19.7.1-alt2
- Skip pyrequires aiohttp.wsgi
- Added deprecate gaiohttp worker patch.

* Fri Aug 11 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 19.7.1-alt1
- Updated to upstream version 19.7.1.

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

