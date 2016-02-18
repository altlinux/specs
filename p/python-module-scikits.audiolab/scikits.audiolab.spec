%define mname scikits
%define oname %mname.audiolab

%def_with python3

Name: python-module-%oname
Epoch: 1
Version: 0.11.0
Release: alt2.git20130116.1
Summary: A python module to make noise from numpy arrays
License: LGPLv2.1+
Group: Development/Python
Url: https://pypi.python.org/pypi/scikits.audiolab/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# git://github.com/cournape/audiolab.git
Source: %name-%version.tar
Source1: site.cfg

#BuildPreReq: libsndfile-devel libvorbis-devel libflac-devel xvfb-run
#BuildPreReq: libogg-devel libalsa-devel
#BuildPreReq: python-devel python-module-setuptools-tests
#BuildPreReq: python-module-nose libnumpy-devel
#BuildPreReq: python-module-Cython python-test
#BuildPreReq: python-module-sphinx-devel python-module-numpydoc
#BuildPreReq: python-module-matplotlib-sphinxext
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools-tests
#BuildPreReq: python3-module-nose libnumpy-py3-devel
#BuildPreReq: python3-module-Cython python3-test
#BuildPreReq: python3-module-pycairo
%endif

%py_provides audiolab %oname
%py_requires numpy

BuildRequires(pre): rpm-macros-sphinx
# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: at-spi2-atk at-spi2-core colord dbus dbus-tools-gui elfutils fakeroot fontconfig fonts-bitmap-misc glib-networking gobject-introspection gobject-introspection-x11 ipython ipython3 libat-spi2-core libatk-gir libcairo-gobject libcap-ng libgdk-pixbuf libgdk-pixbuf-gir libgpg-error libgtk+3-gir libnumpy-devel libogg-devel libpango-gir libwayland-client libwayland-cursor libwayland-egl libwayland-server python-base python-devel python-module-Pillow python-module-PyStemmer python-module-Pygments python-module-babel python-module-cffi python-module-chardet python-module-coverage python-module-cryptography python-module-cssselect python-module-cycler python-module-dateutil python-module-decorator python-module-docutils python-module-enum34 python-module-functools32 python-module-future python-module-genshi python-module-greenlet python-module-ipykernel python-module-ipyparallel python-module-ipython_genutils python-module-jinja2 python-module-jinja2-tests python-module-jsonschema python-module-jupyter_client python-module-jupyter_core python-module-markupsafe python-module-matplotlib python-module-matplotlib-gtk3 python-module-nbconvert python-module-nbformat python-module-ndg-httpsclient python-module-ntlm python-module-numpy python-module-numpydoc python-module-path python-module-pexpect python-module-pickleshare python-module-ptyprocess python-module-pyasn1 python-module-pycairo python-module-pycares python-module-pycurl python-module-pygobject3 python-module-pyparsing python-module-pytz python-module-setuptools python-module-simplegeneric python-module-six python-module-snowballstemmer python-module-sphinx python-module-sphinx_rtd_theme python-module-terminado python-module-tornado_xstatic python-module-traitlets python-module-wx3.0 python-module-xstatic python-module-xstatic-term.js python-module-zmq python-module-zope.interface python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-hotshot python-modules-json python-modules-logging python-modules-multiprocessing python-modules-sqlite3 python-modules-unittest python-modules-wsgiref python-modules-xml python-tools-2to3 python3 python3-base python3-dev python3-module-Pygments python3-module-babel python3-module-cffi python3-module-chardet python3-module-coverage python3-module-cssselect python3-module-cycler python3-module-dateutil python3-module-decorator python3-module-docutils python3-module-future python3-module-genshi python3-module-greenlet python3-module-ipykernel python3-module-ipyparallel python3-module-ipython_genutils python3-module-jinja2 python3-module-jsonschema python3-module-jupyter_client python3-module-jupyter_core python3-module-matplotlib python3-module-matplotlib-gtk3 python3-module-nbconvert python3-module-nbformat python3-module-numpy python3-module-path python3-module-pexpect python3-module-pickleshare python3-module-ptyprocess python3-module-pycares python3-module-pycparser python3-module-pygobject3 python3-module-pyparsing python3-module-pytest python3-module-pytz python3-module-setuptools python3-module-simplegeneric python3-module-six python3-module-snowballstemmer python3-module-sphinx python3-module-terminado python3-module-tornado_xstatic python3-module-traitlets python3-module-xstatic python3-module-xstatic-term.js python3-module-yieldfrom.http.client python3-module-yieldfrom.requests python3-module-yieldfrom.urllib3 python3-module-zmq python3-module-zope python3-module-zope.interface python3-modules-sqlite3 shared-mime-info xauth xkbcomp xkeyboard-config xorg-server-common xorg-xvfb xz
BuildRequires: libflac-devel libnumpy-py3-devel libsndfile-devel libvorbis-devel python-module-Cython python-module-alabaster python-module-html5lib python-module-matplotlib-sphinxext python-module-nose python-module-notebook python-module-numpy-testing python-module-objects.inv python-module-pytest python3-module-Cython python3-module-html5lib python3-module-nose python3-module-notebook python3-module-numpy-testing python3-module-pycairo rpm-build-python3 time xvfb-run

%description
Audiolab is a python package for audio file IO using numpy arrays. It
supports many different audio formats, including wav, aiff, au, flac,
ogg, htk. It also supports output to audio device.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
Audiolab is a python package for audio file IO using numpy arrays. It
supports many different audio formats, including wav, aiff, au, flac,
ogg, htk. It also supports output to audio device.

This package contains tests for %oname.

%package pickles
Summary: Pickles for %oname
Group: Development/Python

%description pickles
Audiolab is a python package for audio file IO using numpy arrays. It
supports many different audio formats, including wav, aiff, au, flac,
ogg, htk. It also supports output to audio device.

This package contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
Audiolab is a python package for audio file IO using numpy arrays. It
supports many different audio formats, including wav, aiff, au, flac,
ogg, htk. It also supports output to audio device.

This package contains documentation for %oname.

%package -n python3-module-%oname
Summary: A python module to make noise from numpy arrays
Group: Development/Python3
%py3_provides audiolab %oname
%py3_requires numpy

%description -n python3-module-%oname
Audiolab is a python package for audio file IO using numpy arrays. It
supports many different audio formats, including wav, aiff, au, flac,
ogg, htk. It also supports output to audio device.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
Audiolab is a python package for audio file IO using numpy arrays. It
supports many different audio formats, including wav, aiff, au, flac,
ogg, htk. It also supports output to audio device.

This package contains tests for %oname.

%prep
%setup

install -m644 %SOURCE1 .
%ifarch x86_64
sed -i 's|\(library_dirs\).*|\1 = %_libdir|' site.cfg
%endif
ln -s ../../site.cfg audiolab/soundio/
rm -f audiolab/pysndfile/_sndfile.c \
	audiolab/soundio/alsa/_alsa_backend.c

%if_with python3
cp -fR . ../python3
sed -i 's|@PY3@||' ../python3/audiolab/pysndfile/_sndfile.pyx
sed -i '/@PY2@/d' ../python3/audiolab/pysndfile/_sndfile.pyx
mv ../python3/audiolab/pysndfile/setup.py \
	../python3/audiolab/pysndfile/setup.py.bak
mv ../python3/audiolab/soundio/setup.py \
	../python3/audiolab/soundio/setup.py.bak
find ../python3 -type f -name '*.py' -exec 2to3 -w -n '{}' +
mv ../python3/audiolab/pysndfile/setup.py.bak \
	../python3/audiolab/pysndfile/setup.py
mv ../python3/audiolab/soundio/setup.py.bak \
	../python3/audiolab/soundio/setup.py
%endif

sed -i '/@PY3@/d' audiolab/pysndfile/_sndfile.pyx
sed -i 's|@PY2@||' audiolab/pysndfile/_sndfile.pyx

%prepare_sphinx docs
ln -s ../objects.inv docs/src/

%build
%add_optflags -fno-strict-aliasing
cython audiolab/pysndfile/_sndfile.pyx
cython audiolab/soundio/alsa/_alsa_backend.pyx
%python_build_debug

%if_with python3
pushd ../python3
cython3 audiolab/pysndfile/_sndfile.pyx
cython3 audiolab/soundio/alsa/_alsa_backend.pyx
sed -i '1a\#define PyString_FromStringAndSize PyUnicode_FromStringAndSize' \
	audiolab/pysndfile/_sndfile.c \
	audiolab/soundio/alsa/_alsa_backend.c
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
%make -C docs pickle
%make -C docs html

install -d %buildroot%python_sitelibdir/%oname
cp -fR docs/build/pickle %buildroot%python_sitelibdir/%oname/

%check
export PYTHONPATH=$PWD
mkdir tmp
%make tests
%if_with python3
pushd ../python3
python3 setup.py build_ext -i
export PYTHONPATH=$PWD
mkdir tmp
%make tests PYTHON=python3 NOSETESTS=nosetests3
popd
%endif

%files
%doc Changelog NEWS TODO *.txt docs/src/examples
%python_sitelibdir/*
%exclude %python_sitelibdir/*/test*
%exclude %python_sitelibdir/*/pickle

%files pickles
%python_sitelibdir/*/pickle

%files docs
%doc docs/build/html/*

%files tests
%python_sitelibdir/*/test*

%if_with python3
%files -n python3-module-%oname
%doc Changelog NEWS TODO *.txt docs/src/examples
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/test*

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/test*
%endif

%changelog
* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 1:0.11.0-alt2.git20130116.1
- NMU: Use buildreq for BR.

* Sun Apr 26 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:0.11.0-alt2.git20130116
- Rebuilt with updated NumPy

* Sat Feb 28 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:0.11.0-alt1.git20130116
- Initial build for Sisyphus

