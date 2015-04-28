%define oname sndfileio

%def_with python3

Name: python-module-%oname
Version: 0.6
Release: alt2.git20141120
Summary: Provides a unified API to read and write sound-files to and from numpy arrays
License: Free
Group: Development/Python
Url: https://pypi.python.org/pypi/sndfileio/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/gesellkammer/sndfileio.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-scikits.audiolab libnumpy-devel
BuildPreReq: python-module-scikits.samplerate python-module-scipy
BuildPreReq: python-module-matplotlib
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-scikits.audiolab libnumpy-py3-devel
BuildPreReq: python3-module-scikits.samplerate python3-module-scipy
BuildPreReq: python3-module-matplotlib
%endif

%py_provides %oname
%py_requires numpy scikits.audiolab scikits.samplerate scipy matplotlib

%description
Common API for reading and writing soundfiles.

* Uses installed packages if found (scikits.audiolab)
* Implements reading uncompressed formats correctly in any format.
* The data is independent of the encoding. All data is presented as
  float64
* Bitdepth is handled automatically depending on the the actual data.

%if_with python3
%package -n python3-module-%oname
Summary: Provides a unified API to read and write sound-files to and from numpy arrays
Group: Development/Python3
%py3_provides %oname
%py3_requires numpy scikits.audiolab scikits.samplerate scipy matplotlib

%description -n python3-module-%oname
Common API for reading and writing soundfiles.

* Uses installed packages if found (scikits.audiolab)
* Implements reading uncompressed formats correctly in any format.
* The data is independent of the encoding. All data is presented as
  float64
* Bitdepth is handled automatically depending on the the actual data.
%endif

%prep
%setup

%if_with python3
cp -fR . ../python3
find ../python3 -type f -name '*.py' -exec 2to3 -w -n '{}' +
%endif

%build
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
%doc *.md *.rst
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.md *.rst
%python3_sitelibdir/*
%endif

%changelog
* Tue Apr 28 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6-alt2.git20141120
- Rebuilt with updated NumPy

* Sun Mar 22 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6-alt1.git20141120
- Initial build for Sisyphus

