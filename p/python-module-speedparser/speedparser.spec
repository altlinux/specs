%define oname speedparser

%def_with python3
%def_disable check

Name: python-module-%oname
Version: 0.2.0
Release: alt1.git20140816.1

Summary: feedparser but faster and worse
Group: Development/Python
License: MIT
Url: https://github.com/jmoiron/speedparser
BuildArch: noarch

%py_provides %oname
%py_requires lxml chardet

BuildRequires(pre): rpm-build-python
#BuildPreReq: python-devel python-module-setuptools-tests
#BuildPreReq: python-module-lxml python-module-chardet
#BuildPreReq: python-modules-json python-module-ipdb
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools-tests
#BuildPreReq: python3-module-lxml python3-module-chardet
#BuildPreReq: python3-module-ipdb python-tools-2to3
%endif

# https://github.com/jmoiron/speedparser.git
Source: %name-%version.tar

# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: ipython ipython3 libgpg-error python-base python-devel python-module-PyStemmer python-module-Pygments python-module-babel python-module-cffi python-module-chardet python-module-cryptography python-module-cssselect python-module-docutils python-module-enum34 python-module-functools32 python-module-future python-module-genshi python-module-greenlet python-module-ipykernel python-module-ipyparallel python-module-ipython_genutils python-module-jinja2 python-module-jsonschema python-module-jupyter_client python-module-jupyter_core python-module-lxml python-module-matplotlib python-module-nbconvert python-module-nbformat python-module-ndg-httpsclient python-module-ntlm python-module-numpy python-module-pexpect python-module-ptyprocess python-module-pyasn1 python-module-pycares python-module-pycurl python-module-pygobject3 python-module-pyparsing python-module-pytz python-module-setuptools python-module-snowballstemmer python-module-sphinx python-module-terminado python-module-tornado_xstatic python-module-traitlets python-module-wx3.0 python-module-xstatic python-module-xstatic-term.js python-module-zmq python-module-zope.interface python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-logging python-modules-unittest python-modules-wsgiref python-tools-2to3 python3 python3-base python3-module-Pygments python3-module-babel python3-module-cffi python3-module-chardet python3-module-cssselect python3-module-docutils python3-module-future python3-module-genshi python3-module-greenlet python3-module-ipykernel python3-module-ipyparallel python3-module-ipython_genutils python3-module-jinja2 python3-module-jsonschema python3-module-jupyter_client python3-module-jupyter_core python3-module-lxml python3-module-matplotlib python3-module-nbconvert python3-module-nbformat python3-module-numpy python3-module-pexpect python3-module-ptyprocess python3-module-pycares python3-module-pycparser python3-module-pygobject3 python3-module-pyparsing python3-module-pytest python3-module-pytz python3-module-setuptools python3-module-snowballstemmer python3-module-sphinx python3-module-terminado python3-module-tornado_xstatic python3-module-traitlets python3-module-xstatic python3-module-xstatic-term.js python3-module-yieldfrom.http.client python3-module-yieldfrom.requests python3-module-yieldfrom.urllib3 python3-module-zmq python3-module-zope python3-module-zope.interface
BuildRequires: python-module-html5lib python-module-ipdb python-module-notebook python-module-pytest python3-module-html5lib python3-module-ipdb python3-module-notebook rpm-build-python3 time

%description
Speedparser is a black-box "style" reimplementation of the Universal
Feed Parser. It uses some feedparser code for date and authors, but
mostly re-implements its data normalization algorithms based on
feedparser output. It uses lxml for feed parsing and for optional HTML
cleaning. Its compatibility with feedparser is very good for a strict
subset of fields, but poor for fields outside that subset.
See tests/speedparsertests.py for more information on which fields are
more or less compatible and which are not.

%package -n python3-module-%oname
Summary: feedparser but faster and worse
Group: Development/Python3
%py3_provides %oname
%py3_requires lxml chardet

%description -n python3-module-%oname
Speedparser is a black-box "style" reimplementation of the Universal
Feed Parser. It uses some feedparser code for date and authors, but
mostly re-implements its data normalization algorithms based on
feedparser output. It uses lxml for feed parsing and for optional HTML
cleaning. Its compatibility with feedparser is very good for a strict
subset of fields, but poor for fields outside that subset.
See tests/speedparsertests.py for more information on which fields are
more or less compatible and which are not.

%prep
%setup
tar -xf tests/feeds.tar.bz2

%if_with python3
cp -fR . ../python3
find ../python3 -type f -name '*.py' -exec 2to3 -w -n '{}' +
%endif

%build
%python_build

%if_with python3
pushd ../python3
%python3_build
popd
%endif

%install
%python_install

%if_with python3
pushd ../python3
%python3_install
popd
%endif

%check
PYTHONPATH=%buildroot%python_sitelibdir python setup.py test
%if_with python3
pushd ../python3
PYTHONPATH=%buildroot%python3_sitelibdir python3 setup.py test
popd
%endif

%files
%doc *.rst docs/*.rst
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.rst docs/*.rst
%python3_sitelibdir/*
%endif

%changelog
* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.2.0-alt1.git20140816.1
- NMU: Use buildreq for BR.

* Fri Sep 05 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.0-alt1.git20140816
- Initial build for Sisyphus

