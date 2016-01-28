%define oname fiona

%def_with python3
%def_disable check

Name: python-module-%oname
Version: 1.6.0
Release: alt1.git20150810.1
Summary: Fiona reads and writes spatial data files
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/Fiona/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/Toblerity/Fiona.git
Source: %name-%version.tar

#BuildPreReq: libgdal-devel libproj-devel gcc-c++
#BuildPreReq: python-devel python-module-setuptools-tests
#BuildPreReq: python-module-Cython python-module-cligj
#BuildPreReq: python-module-six python-module-nose
#BuildPreReq: python-module-click-tests python-module-click-plugins
#BuildPreReq: python-modules-logging python-modules-json
#BuildPreReq: python-module-sphinx-devel
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools-tests
#BuildPreReq: python3-module-Cython python3-module-cligj
#BuildPreReq: python3-module-six python3-module-nose
#BuildPreReq: python3-module-click-tests python3-module-click-plugins
%endif

Conflicts: fio
%py_provides %oname
%py_requires logging json cligj six click click_plugins

BuildRequires(pre): rpm-macros-sphinx
# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: elfutils ipython ipython3 libhdf5-8-seq libnetcdf7-seq libsasl2-3 libstdc++-devel python-base python-devel python-module-Pillow python-module-PyStemmer python-module-Pygments python-module-babel python-module-cffi python-module-chardet python-module-coverage python-module-cryptography python-module-cssselect python-module-docutils python-module-enum34 python-module-functools32 python-module-future python-module-genshi python-module-greenlet python-module-ipykernel python-module-ipyparallel python-module-ipython_genutils python-module-jinja2 python-module-jinja2-tests python-module-jsonschema python-module-jupyter_client python-module-jupyter_core python-module-markupsafe python-module-matplotlib python-module-nbconvert python-module-nbformat python-module-ndg-httpsclient python-module-ntlm python-module-numpy python-module-pexpect python-module-ptyprocess python-module-pyasn1 python-module-pycares python-module-pycurl python-module-pygobject3 python-module-pyparsing python-module-pytz python-module-setuptools python-module-six python-module-snowballstemmer python-module-sphinx python-module-sphinx_rtd_theme python-module-terminado python-module-tornado_xstatic python-module-traitlets python-module-wx3.0 python-module-xstatic python-module-xstatic-term.js python-module-zmq python-module-zope.interface python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-json python-modules-logging python-modules-multiprocessing python-modules-unittest python-modules-wsgiref python-modules-xml python3 python3-base python3-dev python3-module-Pygments python3-module-babel python3-module-cffi python3-module-chardet python3-module-coverage python3-module-cssselect python3-module-docutils python3-module-future python3-module-genshi python3-module-greenlet python3-module-ipykernel python3-module-ipyparallel python3-module-ipython_genutils python3-module-jinja2 python3-module-jsonschema python3-module-jupyter_client python3-module-jupyter_core python3-module-matplotlib python3-module-nbconvert python3-module-nbformat python3-module-numpy python3-module-pexpect python3-module-ptyprocess python3-module-pycares python3-module-pycparser python3-module-pygobject3 python3-module-pyparsing python3-module-pytest python3-module-pytz python3-module-setuptools python3-module-snowballstemmer python3-module-sphinx python3-module-terminado python3-module-tornado_xstatic python3-module-traitlets python3-module-xstatic python3-module-xstatic-term.js python3-module-yieldfrom.http.client python3-module-yieldfrom.requests python3-module-yieldfrom.urllib3 python3-module-zmq python3-module-zope python3-module-zope.interface
BuildRequires: gcc-c++ libgdal-devel python-module-Cython python-module-alabaster python-module-html5lib python-module-nose python-module-notebook python-module-objects.inv python-module-pytest python3-module-Cython python3-module-html5lib python3-module-nose python3-module-notebook rpm-build-python3 time

%description
Fiona is OGR's neat, nimble, no-nonsense API for Python programmers.

Fiona is designed to be simple and dependable. It focuses on reading and
writing data in standard Python IO style and relies upon familiar Python
types and protocols such as files, dictionaries, mappings, and iterators
instead of classes specific to OGR. Fiona can read and write real-world
data using multi-layered GIS formats and zipped virtual file systems and
integrates readily with other Python GIS packages such as pyproj, Rtree,
and Shapely.

%package -n python3-module-%oname
Summary: Fiona reads and writes spatial data files
Group: Development/Python3
%py3_provides %oname
%py3_requires logging json cligj six click click_plugins

%description -n python3-module-%oname
Fiona is OGR's neat, nimble, no-nonsense API for Python programmers.

Fiona is designed to be simple and dependable. It focuses on reading and
writing data in standard Python IO style and relies upon familiar Python
types and protocols such as files, dictionaries, mappings, and iterators
instead of classes specific to OGR. Fiona can read and write real-world
data using multi-layered GIS formats and zipped virtual file systems and
integrates readily with other Python GIS packages such as pyproj, Rtree,
and Shapely.

%package pickles
Summary: Pickles for %oname
Group: Development/Python

%description pickles
Fiona is OGR's neat, nimble, no-nonsense API for Python programmers.

Fiona is designed to be simple and dependable. It focuses on reading and
writing data in standard Python IO style and relies upon familiar Python
types and protocols such as files, dictionaries, mappings, and iterators
instead of classes specific to OGR. Fiona can read and write real-world
data using multi-layered GIS formats and zipped virtual file systems and
integrates readily with other Python GIS packages such as pyproj, Rtree,
and Shapely.

This package contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
Fiona is OGR's neat, nimble, no-nonsense API for Python programmers.

Fiona is designed to be simple and dependable. It focuses on reading and
writing data in standard Python IO style and relies upon familiar Python
types and protocols such as files, dictionaries, mappings, and iterators
instead of classes specific to OGR. Fiona can read and write real-world
data using multi-layered GIS formats and zipped virtual file systems and
integrates readily with other Python GIS packages such as pyproj, Rtree,
and Shapely.

This package contains documentation for %oname.

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

%prepare_sphinx .
ln -s ../objects.inv docs/

%build
%add_optflags -fno-strict-aliasing
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

python setup.py build_ext -i
export PYTHONPATH=$PWD
%make -C docs pickle
%make -C docs html

cp -fR docs/_build/pickle %buildroot%python_sitelibdir/%oname/

%check
export LC_ALL=en_US.UTF-8
python setup.py test
%if_with python3
pushd ../python3
python3 setup.py test
popd
%endif

%files
%doc CHANGES.txt CREDITS.txt *.rst examples
%_bindir/*
%if_with python3
%exclude %_bindir/*.py3
%endif
%python_sitelibdir/*
%exclude %python_sitelibdir/*/pickle

%files pickles
%python_sitelibdir/*/pickle

%files docs
%doc docs/_build/html docs/*.txt

%if_with python3
%files -n python3-module-%oname
%doc CHANGES.txt CREDITS.txt *.rst examples
%_bindir/*.py3
%python3_sitelibdir/*
%endif

%changelog
* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 1.6.0-alt1.git20150810.1
- NMU: Use buildreq for BR.

* Wed Aug 12 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.6.0-alt1.git20150810
- Version 1.6.0

* Mon Mar 02 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.5.0-alt1.git20150301
- New snapshot

* Thu Feb 19 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.5.0-alt1.git20150204
- Initial build for Sisyphus

