%define mname scikits
%define oname %mname.samplerate

%def_with python3

Name: python-module-%oname
Epoch: 1
Version: 0.4.0
Release: alt2.git20090722.1
Summary: A python module for high quality audio resampling
License: GPLv2
Group: Development/Python
Url: https://pypi.python.org/pypi/scikits.samplerate/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# git://github.com/cournape/samplerate.git
Source: %name-%version.tar
Source1: site.cfg

#BuildPreReq: libsamplerate-devel
#BuildPreReq: python-devel python-module-setuptools-tests
#BuildPreReq: python-module-Cython libnumpy-devel
#BuildPreReq: python-module-nose
#BuildPreReq: python-module-sphinx-devel python-module-numpydoc
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools-tests
#BuildPreReq: python3-module-Cython libnumpy-py3-devel
#BuildPreReq: python3-module-nose
%endif

%py_provides %oname
%py_requires %mname numpy

BuildRequires(pre): rpm-macros-sphinx
# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: elfutils ipython ipython3 libnumpy-devel python-base python-devel python-module-Pillow python-module-PyStemmer python-module-Pygments python-module-babel python-module-cffi python-module-chardet python-module-coverage python-module-cryptography python-module-cssselect python-module-docutils python-module-enum34 python-module-functools32 python-module-future python-module-genshi python-module-greenlet python-module-ipykernel python-module-ipyparallel python-module-ipython_genutils python-module-jinja2 python-module-jinja2-tests python-module-jsonschema python-module-jupyter_client python-module-jupyter_core python-module-markupsafe python-module-matplotlib python-module-nbconvert python-module-nbformat python-module-ndg-httpsclient python-module-ntlm python-module-numpy python-module-numpydoc python-module-pexpect python-module-ptyprocess python-module-pyasn1 python-module-pycares python-module-pycurl python-module-pygobject3 python-module-pyparsing python-module-pytz python-module-setuptools python-module-six python-module-snowballstemmer python-module-sphinx python-module-sphinx_rtd_theme python-module-terminado python-module-tornado_xstatic python-module-traitlets python-module-wx3.0 python-module-xstatic python-module-xstatic-term.js python-module-zmq python-module-zope.interface python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-hotshot python-modules-json python-modules-logging python-modules-multiprocessing python-modules-unittest python-modules-wsgiref python-modules-xml python-tools-2to3 python3 python3-base python3-dev python3-module-Pygments python3-module-babel python3-module-cffi python3-module-chardet python3-module-coverage python3-module-cssselect python3-module-docutils python3-module-future python3-module-genshi python3-module-greenlet python3-module-ipykernel python3-module-ipyparallel python3-module-ipython_genutils python3-module-jinja2 python3-module-jsonschema python3-module-jupyter_client python3-module-jupyter_core python3-module-matplotlib python3-module-nbconvert python3-module-nbformat python3-module-numpy python3-module-pexpect python3-module-ptyprocess python3-module-pycares python3-module-pycparser python3-module-pygobject3 python3-module-pyparsing python3-module-pytest python3-module-pytz python3-module-setuptools python3-module-snowballstemmer python3-module-sphinx python3-module-terminado python3-module-tornado_xstatic python3-module-traitlets python3-module-xstatic python3-module-xstatic-term.js python3-module-yieldfrom.http.client python3-module-yieldfrom.requests python3-module-yieldfrom.urllib3 python3-module-zmq python3-module-zope python3-module-zope.interface xz
BuildRequires: libnumpy-py3-devel libsamplerate-devel python-module-Cython python-module-alabaster python-module-html5lib python-module-nose python-module-notebook python-module-numpy-testing python-module-objects.inv python-module-pytest python3-module-Cython python3-module-html5lib python3-module-nose python3-module-notebook python3-module-numpy-testing rpm-build-python3 time

%description
Samplerate is a small python package to do high quality audio resampling
for data in numpy arrays; IOW, it is a matlab resample replacement.

Samplerate is a wrapper around the Secret Rabbit Code from Erik de
Castro Lopo (http://www.mega-nerd.com/SRC/), which has high quality
converters based on the work of J.O Smith from CCRMA (see
http://ccrma.stanford.edu/~jos/resample/optfir.pdf).

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
Samplerate is a small python package to do high quality audio resampling
for data in numpy arrays; IOW, it is a matlab resample replacement.

This package contains tests for %oname.

%package -n python3-module-%oname
Summary: A python module for high quality audio resampling
Group: Development/Python3
%py3_provides %oname
%py3_requires %mname numpy

%description -n python3-module-%oname
Samplerate is a small python package to do high quality audio resampling
for data in numpy arrays; IOW, it is a matlab resample replacement.

Samplerate is a wrapper around the Secret Rabbit Code from Erik de
Castro Lopo (http://www.mega-nerd.com/SRC/), which has high quality
converters based on the work of J.O Smith from CCRMA (see
http://ccrma.stanford.edu/~jos/resample/optfir.pdf).

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
Samplerate is a small python package to do high quality audio resampling
for data in numpy arrays; IOW, it is a matlab resample replacement.

This package contains tests for %oname.

%package pickles
Summary: Pickles for %oname
Group: Development/Python

%description pickles
Samplerate is a small python package to do high quality audio resampling
for data in numpy arrays; IOW, it is a matlab resample replacement.

This package contains pickles for %oname.

%prep
%setup

rm -f scikits/samplerate/_samplerate.c
install -m644 %SOURCE1 .
%ifarch x86_64
sed -i 's|\(library_dirs =\).*|\1 %_libdir|' site.cfg
%endif

%if_with python3
cp -fR . ../python3
mv ../python3/scikits/samplerate/setup.py \
	../python3/scikits/samplerate/setup.py.bak
find ../python3 -type f -name '*.py' -exec 2to3 -w -n '{}' +
mv ../python3/scikits/samplerate/setup.py.bak \
	../python3/scikits/samplerate/setup.py
%endif

%prepare_sphinx docs
ln -s ../objects.inv docs/src/

%build
cython scikits/samplerate/_samplerate.pyx
%python_build_debug

%if_with python3
pushd ../python3
cython3 scikits/samplerate/_samplerate.pyx
sed -i '1a\#define PyString_FromStringAndSize PyUnicode_FromStringAndSize' \
	scikits/samplerate/_samplerate.c
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

python setup.py build_ext -i
export PYTHONPATH=$PWD:$PWD/docs/ext
%make -C docs pickle
%make -C docs html

install -d %buildroot%python_sitelibdir/%oname
cp -fR docs/build/pickle %buildroot%python_sitelibdir/%oname/

%check
pushd ~
export PYTHONPATH=%buildroot%python_sitelibdir
nosetests -v %oname
popd
%if_with python3
pushd ../python3
pushd ~
export PYTHONPATH=%buildroot%python3_sitelibdir
nosetests3 -v %oname
popd
popd
%endif

%files
%doc Changelog README TODO docs/src/examples docs/build/html
%python_sitelibdir/%mname/samplerate
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/%mname/samplerate/tests

%files tests
%python_sitelibdir/%mname/samplerate/tests

%files pickles
%python_sitelibdir/*/pickle

%if_with python3
%files -n python3-module-%oname
%doc Changelog README TODO docs/src/examples
%python3_sitelibdir/%mname/samplerate
%python3_sitelibdir/*.egg-info
%exclude %python3_sitelibdir/%mname/samplerate/tests

%files -n python3-module-%oname-tests
%python3_sitelibdir/%mname/samplerate/tests
%endif

%changelog
* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 1:0.4.0-alt2.git20090722.1
- NMU: Use buildreq for BR.

* Tue Apr 28 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:0.4.0-alt2.git20090722
- Rebuilt with updated NumPy

* Sat Feb 28 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:0.4.0-alt1.git20090722
- Initial build for Sisyphus

