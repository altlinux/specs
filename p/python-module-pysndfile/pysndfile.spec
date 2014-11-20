%define oname pysndfile

%def_with python3

Name: python-module-%oname
Version: 0.2.10
Release: alt1
Summary: Cython wrapper class for reading/writing soundfiles using libsndfile
License: LGPLv3
Group: Development/Python
Url: https://pypi.python.org/pypi/pysndfile/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: gcc-c++ clang-devel libsndfile-devel
BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-Cython libnumpy-devel
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-Cython libnumpy-py3-devel
%endif

%py_provides %oname

%description
pysndfile is a python package providing PySndfile, a Cython wrapper
class around libsndfile. PySndfile provides methods for reading and
writing a large variety of soundfile formats on a variety of plattforms.
PySndfile provides a rather complete access to the different sound file
manipulation options that are available in libsndfile.

Due to the use of libsndfile nearly all sound file formats, (besides mp3
and derived formats) can be read and written with PySndfile.

%package -n python3-module-%oname
Summary: Cython wrapper class for reading/writing soundfiles using libsndfile
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
pysndfile is a python package providing PySndfile, a Cython wrapper
class around libsndfile. PySndfile provides methods for reading and
writing a large variety of soundfile formats on a variety of plattforms.
PySndfile provides a rather complete access to the different sound file
manipulation options that are available in libsndfile.

Due to the use of libsndfile nearly all sound file formats, (besides mp3
and derived formats) can be read and written with PySndfile.

%prep
%setup

rm -f *.cpp

%if_with python3
cp -fR . ../python3
%endif

%build
export CC=clang
export CXX=clang++
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
python setup.py test
%if_with python3
pushd ../python3
python3 setup.py test
popd
%endif

%files
%doc ChangeLog README.txt
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc ChangeLog README.txt
%python3_sitelibdir/*
%endif

%changelog
* Thu Nov 20 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.10-alt1
- Initial build for Sisyphus

