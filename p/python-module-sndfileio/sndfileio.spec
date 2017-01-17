%define _unpackaged_files_terminate_build 1
%define oname sndfileio

%def_with python3

Name: python-module-%oname
Version: 0.7.1
Release: alt1
Summary: Provides a unified API to read and write sound-files to and from numpy arrays
License: Free
Group: Development/Python
Url: https://pypi.python.org/pypi/sndfileio/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/gesellkammer/sndfileio.git
Source0: https://pypi.python.org/packages/10/a5/b73fbef06657f54b17373972ee4037fae1e1a110ad3d047ebd03c4878da9/%{oname}-%{version}.tar.gz
BuildArch: noarch

#BuildPreReq: python-devel python-module-setuptools-tests
#BuildPreReq: python-module-scikits.audiolab libnumpy-devel
#BuildPreReq: python-module-scikits.samplerate python-module-scipy
#BuildPreReq: python-module-matplotlib
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools-tests
#BuildPreReq: python3-module-scikits.audiolab libnumpy-py3-devel
#BuildPreReq: python3-module-scikits.samplerate python3-module-scipy
#BuildPreReq: python3-module-matplotlib
%endif

%py_provides %oname
%py_requires numpy scikits.audiolab scikits.samplerate scipy matplotlib

# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: python-base python-devel python-module-PyStemmer python-module-Pygments python-module-babel python-module-cssselect python-module-future python-module-genshi python-module-jinja2 python-module-mpmath python-module-numpy python-module-pyparsing python-module-pytest python-module-pytz python-module-scikits.eartho python-module-setuptools python-module-snowballstemmer python-module-sphinx python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-logging python-modules-unittest python-tools-2to3 python3 python3-base python3-module-gdal python3-module-matplotlib python3-module-numpy python3-module-pyparsing python3-module-pytest python3-module-scikits.eartho python3-module-setuptools
BuildRequires: python-module-docutils python-module-html5lib python-module-matplotlib python-module-scikits.samplerate python-module-scipy python-module-setuptools-tests python3-module-scikits.samplerate python3-module-scipy python3-module-setuptools-tests rpm-build-python3 time

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
%setup -q -n %{oname}-%{version}

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
%doc *.rst PKG-INFO
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.rst PKG-INFO
%python3_sitelibdir/*
%endif

%changelog
* Tue Jan 17 2017 Igor Vlasenko <viy@altlinux.ru> 0.7.1-alt1
- automated PyPI update

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.6-alt2.git20141120.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.6-alt2.git20141120.1
- NMU: Use buildreq for BR.

* Tue Apr 28 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6-alt2.git20141120
- Rebuilt with updated NumPy

* Sun Mar 22 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6-alt1.git20141120
- Initial build for Sisyphus

