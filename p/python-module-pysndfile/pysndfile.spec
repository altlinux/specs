%define _unpackaged_files_terminate_build 1
%define oname pysndfile

%def_with python3

Name: python-module-%oname
Version: 1.0.0
Release: alt2
Summary: Cython wrapper class for reading/writing soundfiles using libsndfile
License: LGPLv3
Group: Development/Python
Url: https://pypi.python.org/pypi/pysndfile/

Source: %oname-%version.tar

BuildRequires: clang libstdc++-devel libsndfile-devel
BuildRequires: python-devel python-module-setuptools-tests
BuildRequires: python-module-Cython libnumpy-devel python-module-numpy-testing
BuildRequires: python-module-html5lib python-module-notebook
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools-tests
BuildRequires: python3-module-Cython libnumpy-py3-devel python3-module-numpy-testing
BuildRequires: python3-module-html5lib python3-module-notebook
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

%if_with python3
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
%endif

%prep
%setup -n %oname-%version

rm -f *.cpp

%if_with python3
cp -fR . ../python3
%endif

%build
# Clang doesn't support these options
%remove_optflags -frecord-gcc-switches

export CC=clang
export CXX=clang++
%python_build_debug

%if_with python3
pushd ../python3
%python3_build_debug
popd
%endif

%install
export CC=clang
export CXX=clang++
%python_install

%if_with python3
pushd ../python3
%python3_install
popd
%endif

%check
export CC=clang
export CXX=clang++
python setup.py test
PYTHONPATH=%buildroot%python_sitelibdir python tests/pysndfile_test.py

%if_with python3
pushd ../python3
python3 setup.py test
PYTHONPATH=%buildroot%python3_sitelibdir python3 tests/pysndfile_test.py
popd
%endif

%files
%doc ChangeLog README.*
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc ChangeLog README.*
%python3_sitelibdir/*
%endif

%changelog
* Tue Jan 09 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 1.0.0-alt2
- Fixed build.

* Tue Dec 26 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 1.0.0-alt1
- Updated to upstream version 1.0.0.

* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 0.2.11-alt1
- automated PyPI update

* Thu Mar 17 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.2.10-alt1.1.1
- (NMU) rebuild with python3-3.5 & rpm-build-python3-0.1.10
  (for ABI dependence and new python3(*) reqs)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.2.10-alt1.1
- NMU: Use buildreq for BR.

* Thu Nov 20 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.10-alt1
- Initial build for Sisyphus

