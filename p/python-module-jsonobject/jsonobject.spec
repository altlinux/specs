%define _unpackaged_files_terminate_build 1
%define oname jsonobject

Name: python-module-%oname
Version: 0.9.8
Release: alt2
Summary: A library for dealing with JSON as python objects

License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/jsonobject/
# https://github.com/dimagi/jsonobject.git

Source: %name-%version.tar

BuildRequires: python-devel python-module-setuptools
BuildRequires: python-module-couchdbkit python-module-unittest2
BuildRequires: python-module-six
BuildRequires: python-module-Cython

BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python3-module-couchdbkit python3-module-unittest2
BuildPreReq: python3-module-six
BuildPreReq: python3-module-Cython

%py_provides %oname


%description
A python library for handling deeply nested JSON objects as
well-schema'd python objects.

%package -n python3-module-%oname
Summary: A library for dealing with JSON as python objects
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
A python library for handling deeply nested JSON objects as
well-schema'd python objects.

%prep
%setup

cp -fR . ../python3

%build
export LC_ALL=en_US.UTF-8
%python_build_debug

pushd ../python3
%python3_build_debug
popd

%install
export LC_ALL=en_US.UTF-8
%python_install

pushd ../python3
%python3_install
popd

%check
export LC_ALL=en_US.UTF-8
python setup.py test
python -m unittest test.test_couchdbkit

pushd ../python3
python3 setup.py test
python3 -m unittest test.test_couchdbkit
popd

%files
%doc *.md
%python_sitelibdir/*

%files -n python3-module-%oname
%doc *.md
%python3_sitelibdir/*


%changelog
* Tue Jan 29 2019 Stanislav Levin <slev@altlinux.org> 0.9.8-alt2
- Dropped BR on argparse.

* Wed Dec 26 2018 Andrey Bychkov <mrdrew@altlinux.org> 0.9.8-alt1
- Version updated to 0.9.8

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.6.1-alt1.git20150130.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Tue Mar 03 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.1-alt1.git20150130
- New snapshot

* Thu Nov 27 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.1-alt1.git20141126
- Initial build for Sisyphus

