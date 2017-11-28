%define mname scikits
%define oname %mname.audiolab

%def_with python3

Name: python-module-%oname
Epoch: 1
Version: 0.11.0
Release: alt3.git20130116
Summary: A python module to make noise from numpy arrays
License: LGPLv2.1+
Group: Development/Python
Url: https://pypi.python.org/pypi/scikits.audiolab/

# git://github.com/cournape/audiolab.git
Source: %name-%version.tar
Source1: site.cfg
Patch1: %oname-%version-alt-build.patch

BuildRequires(pre): rpm-macros-sphinx
BuildRequires: libsndfile-devel libvorbis-devel libflac-devel xvfb-run
BuildRequires: python-devel python-module-setuptools-tests
BuildRequires: python-module-pytest python-module-numpy-testing
BuildRequires: python-module-nose libnumpy-devel
BuildRequires: python-module-Cython python-module-html5lib python-module-notebook
BuildRequires: python-module-alabaster python-module-matplotlib-sphinxext python-module-objects.inv
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools-tests
BuildRequires: python3-module-numpy-testing
BuildRequires: python3-module-nose libnumpy-py3-devel
BuildRequires: python3-module-Cython python3-module-html5lib python3-module-notebook
BuildRequires: python3-module-pycairo
%endif

%py_provides audiolab %oname
%py_requires numpy

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
%patch1 -p1

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
* Tue Nov 28 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 1:0.11.0-alt3.git20130116
- Fixed build.

* Thu Mar 17 2016 Ivan Zakharyaschev <imz@altlinux.org> 1:0.11.0-alt2.git20130116.1.1
- (NMU) rebuild with python3-3.5 & rpm-build-python3-0.1.10
  (for ABI dependence and new python3(*) reqs)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 1:0.11.0-alt2.git20130116.1
- NMU: Use buildreq for BR.

* Sun Apr 26 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:0.11.0-alt2.git20130116
- Rebuilt with updated NumPy

* Sat Feb 28 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:0.11.0-alt1.git20130116
- Initial build for Sisyphus

