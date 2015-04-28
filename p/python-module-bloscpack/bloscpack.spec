%define oname bloscpack

%def_with python3

Name: python-module-%oname
Version: 0.8.0
Release: alt1.dev.git20150325
Summary: Command line interface to and serialization format for Blosc
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/bloscpack/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/Blosc/bloscpack.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-blosc-tests python-module-numpy
BuildPreReq: python-module-nose python-module-cram
BuildPreReq: python-module-mock python-module-coverage
BuildPreReq: python-module-coveralls python-module-requests
BuildPreReq: python-module-docopt
BuildPreReq: python-modules-json
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-blosc-tests python3-module-numpy
BuildPreReq: python3-module-nose python3-module-cram
BuildPreReq: python3-module-mock python3-module-coverage
BuildPreReq: python3-module-coveralls python-tools-2to3
BuildPreReq: python3-module-requests
BuildPreReq: python3-module-docopt
%endif

%py_provides %oname
%py_requires blosc numpy json

%description
Command line interface to and serialization format for Blosc, a high
performance, multi-threaded, blocking and shuffling compressor. Uses
python-blosc bindings to interface with Blosc. Also comes with native
support for efficiently serializing and deserializing Numpy arrays.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
Command line interface to and serialization format for Blosc, a high
performance, multi-threaded, blocking and shuffling compressor. Uses
python-blosc bindings to interface with Blosc. Also comes with native
support for efficiently serializing and deserializing Numpy arrays.

This package contains tests for %oname.

%if_with python3
%package -n python3-module-%oname
Summary: Command line interface to and serialization format for Blosc
Group: Development/Python3
%py3_provides %oname
%py3_requires blosc numpy json

%description -n python3-module-%oname
Command line interface to and serialization format for Blosc, a high
performance, multi-threaded, blocking and shuffling compressor. Uses
python-blosc bindings to interface with Blosc. Also comes with native
support for efficiently serializing and deserializing Numpy arrays.

%package  -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description  -n python3-module-%oname-tests
Command line interface to and serialization format for Blosc, a high
performance, multi-threaded, blocking and shuffling compressor. Uses
python-blosc bindings to interface with Blosc. Also comes with native
support for efficiently serializing and deserializing Numpy arrays.

This package contains tests for %oname.
%endif

%prep
%setup

%if_with python3
cp -fR . ../python3
find ../python3 -type f -name '*.py' -exec 2to3 -w -n '{}' +
%endif

%build
export LC_ALL=en_US.UTF-8
%python_build_debug

%if_with python3
pushd ../python3
%python3_build_debug
popd
%endif

%install
export LC_ALL=en_US.UTF-8
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

%check
export LC_ALL=en_US.UTF-8
python setup.py test
#CRAM=cram NOSETESTS=nosetests ./test.sh
nosetests -v test/test_file_io.py:pack_unpack_hard
nosetests -v test/test_numpy_io.py:huge_arrays
%if_with python3
pushd ../python3
python3 setup.py test
#CRAM=cram.py3 NOSETESTS=nosetests3 ./test.sh
#nosetests3 -v test/test_file_io.py:pack_unpack_hard
nosetests3 -v test/test_numpy_io.py:huge_arrays
popd
%endif

%files
%doc *.rst bench
%_bindir/*
%if_with python3
%exclude %_bindir/*.py3
%endif
%python_sitelibdir/*
%exclude %python_sitelibdir/*/test*

%files tests
%python_sitelibdir/*/test*

%if_with python3
%files -n python3-module-%oname
%doc *.rst bench
%_bindir/*.py3
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/test*
%exclude %python3_sitelibdir/*/*/test*

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/test*
%python3_sitelibdir/*/*/test*
%endif

%changelog
* Tue Apr 28 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8.0-alt1.dev.git20150325
- Initial build for Sisyphus

