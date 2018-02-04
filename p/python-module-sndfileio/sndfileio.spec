%define _unpackaged_files_terminate_build 1
%define oname sndfileio

%def_with python3
%def_disable check

Name: python-module-%oname
Version: 0.7.1
Release: alt2.1
Summary: Provides a unified API to read and write sound-files to and from numpy arrays
License: Free
Group: Development/Python
BuildArch: noarch
Url: https://pypi.python.org/pypi/sndfileio/

# https://github.com/gesellkammer/sndfileio.git
Source: %oname-%version.tar

BuildRequires: python-devel python-module-setuptools
BuildRequires: python-module-scikits.samplerate python-module-scipy
BuildRequires: python-module-matplotlib
BuildRequires: python-module-docutils python-module-html5lib
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools
BuildRequires: python3-module-scikits.samplerate python3-module-scipy
BuildRequires: python3-module-matplotlib
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
%setup -n %oname-%version

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
%doc *.rst
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.rst
%python3_sitelibdir/*
%endif

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.7.1-alt2.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Thu Dec 28 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.7.1-alt2
- Fixed build.

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

