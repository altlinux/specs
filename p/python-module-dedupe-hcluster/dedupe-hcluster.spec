%define mname hcluster
%define oname dedupe-%mname

%def_with python3

Name: python-module-%oname
Version: 0.3.2
Release: alt1.git20150304.1
Summary: Hierarchical Clustering Algorithms (Information Theory)
License: SciPy License (BSD Style)
Group: Development/Python
Url: https://pypi.python.org/pypi/dedupe-hcluster
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/datamade/hcluster.git
Source: %name-%version.tar

#BuildPreReq: python-devel python-module-setuptools-tests
#BuildPreReq: python-module-future libnumpy-devel
#BuildPreReq: python-module-nose python-module-Cython
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools-tests
#BuildPreReq: python3-module-future libnumpy-py3-devel
#BuildPreReq: python3-module-nose python3-module-Cython
%endif

%py_provides %mname
Provides: python-module-%mname = %EVR
Conflicts: python-module-%mname < %EVR
Obsoletes: python-module-%mname < %EVR
%py_requires numpy future

# Automatically added by buildreq on Wed Jan 27 2016 (-bi)
# optimized out: elfutils fontconfig ipython ipython3 python-base python-devel python-module-Pillow python-module-PyStemmer python-module-Pygments python-module-babel python-module-cffi python-module-chardet python-module-coverage python-module-cryptography python-module-cssselect python-module-cycler python-module-dateutil python-module-decorator python-module-docutils python-module-enum34 python-module-functools32 python-module-future python-module-genshi python-module-greenlet python-module-ipykernel python-module-ipython_genutils python-module-jinja2 python-module-jsonschema python-module-jupyter_client python-module-jupyter_core python-module-matplotlib python-module-nbconvert python-module-nbformat python-module-ndg-httpsclient python-module-notebook python-module-ntlm python-module-numpy python-module-path python-module-pexpect python-module-pickleshare python-module-ptyprocess python-module-pyasn1 python-module-pycares python-module-pycurl python-module-pygobject3 python-module-pyparsing python-module-pytest python-module-pytz python-module-setuptools python-module-simplegeneric python-module-six python-module-snowballstemmer python-module-sphinx python-module-terminado python-module-tornado_xstatic python-module-traitlets python-module-wx3.0 python-module-xstatic python-module-xstatic-term.js python-module-zmq python-module-zope.interface python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-hotshot python-modules-json python-modules-logging python-modules-multiprocessing python-modules-sqlite3 python-modules-unittest python-modules-wsgiref python-modules-xml python-tools-2to3 python3 python3-base python3-dev python3-module-Pygments python3-module-babel python3-module-cffi python3-module-chardet python3-module-coverage python3-module-cssselect python3-module-cycler python3-module-dateutil python3-module-decorator python3-module-docutils python3-module-future python3-module-genshi python3-module-greenlet python3-module-ipykernel python3-module-ipyparallel python3-module-ipython_genutils python3-module-jinja2 python3-module-jsonschema python3-module-jupyter_client python3-module-jupyter_core python3-module-matplotlib python3-module-nbconvert python3-module-nbformat python3-module-numpy python3-module-path python3-module-pexpect python3-module-pickleshare python3-module-ptyprocess python3-module-pycares python3-module-pycparser python3-module-pygobject3 python3-module-pyparsing python3-module-pytest python3-module-pytz python3-module-setuptools python3-module-simplegeneric python3-module-six python3-module-snowballstemmer python3-module-sphinx python3-module-terminado python3-module-tornado_xstatic python3-module-traitlets python3-module-xstatic python3-module-xstatic-term.js python3-module-yieldfrom.http.client python3-module-yieldfrom.requests python3-module-yieldfrom.urllib3 python3-module-zmq python3-module-zope python3-module-zope.interface python3-modules-sqlite3 xz
BuildRequires: libnumpy-devel python-module-Cython python-module-html5lib python-module-ipyparallel python-module-nose python-module-numpy-testing python-module-setuptools-tests python3-module-Cython python3-module-html5lib python3-module-nose python3-module-notebook python3-module-numpy-testing python3-module-setuptools-tests rpm-build-python3 time

%description
This library provides Python functions for hierarchical clustering. Its
features include

* generating hierarchical clusters from distance matrices
* computing distance matrices from observation vectors
* computing statistics on clusters
* cutting linkages to generate flat clusters
* and visualizing clusters with dendrograms.

It is a fork of clustering and distance functions from the scipy that
removes all the dependencies on scipy. It preserves the API of hcluster
0.2.

%if_with python3
%package -n python3-module-%oname
Summary: Hierarchical Clustering Algorithms (Information Theory)
Group: Development/Python3
%py3_provides %mname
Provides: python3-module-%mname = %EVR
Conflicts: python3-module-%mname < %EVR
Obsoletes: python3-module-%mname < %EVR
%py3_requires numpy future

%description -n python3-module-%oname
This library provides Python functions for hierarchical clustering. Its
features include

* generating hierarchical clusters from distance matrices
* computing distance matrices from observation vectors
* computing statistics on clusters
* cutting linkages to generate flat clusters
* and visualizing clusters with dendrograms.

It is a fork of clustering and distance functions from the scipy that
removes all the dependencies on scipy. It preserves the API of hcluster
0.2.
%endif

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

%build
%add_optflags -fno-strict-aliasing
%python_build_debug

%if_with python3
pushd ../python3
%python3_build_debug
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
python setup.py test -v
python setup.py build_ext -i
nosetests -vv
%if_with python3
pushd ../python3
python3 setup.py test -v
python3 setup.py build_ext -i
nosetests3 -vv
popd
%endif

%files
%doc LICENSE.txt *.md
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc LICENSE.txt *.md
%python3_sitelibdir/*
%endif

%changelog
* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.3.2-alt1.git20150304.1
- NMU: Use buildreq for BR.

* Wed Aug 26 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.2-alt1.git20150304
- Initial build for Sisyphus

