%define _unpackaged_files_terminate_build 1
%define oname filechunkio

%def_with python3

Name: python-module-%oname
Version: 1.8
Release: alt1
Summary: FileChunkIO represents a chunk of an OS-level file containing bytes data
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/filechunkio/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source0: https://pypi.python.org/packages/10/4d/1789767002fa666fcf486889e8f6a2a90784290be9c0bc28d627efba401e/%{oname}-%{version}.tar.gz
BuildArch: noarch

#BuildPreReq: python-devel python-module-setuptools-tests
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools-tests
%endif

%py_provides %oname

# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: python-base python-modules python-modules-compiler python-modules-email python-modules-encodings python3 python3-base
BuildRequires: python-devel python-modules-unittest rpm-build-python3

%description
FileChunkIO represents a chunk of an OS-level file containing bytes
data. Python 2.6+ is required.

BACKGROUND: I wrote FileChunkIO to upload huge files to Amazon S3 in
multiple parts without having to split them physically upfront (which
requires more time and twice the disk space) or creating in-memory
chunks as StringIO instances.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
FileChunkIO represents a chunk of an OS-level file containing bytes
data. Python 2.6+ is required.

BACKGROUND: I wrote FileChunkIO to upload huge files to Amazon S3 in
multiple parts without having to split them physically upfront (which
requires more time and twice the disk space) or creating in-memory
chunks as StringIO instances.

This package contains tests for %oname.

%package -n python3-module-%oname
Summary: FileChunkIO represents a chunk of an OS-level file containing bytes data
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
FileChunkIO represents a chunk of an OS-level file containing bytes
data. Python 2.6+ is required.

BACKGROUND: I wrote FileChunkIO to upload huge files to Amazon S3 in
multiple parts without having to split them physically upfront (which
requires more time and twice the disk space) or creating in-memory
chunks as StringIO instances.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
FileChunkIO represents a chunk of an OS-level file containing bytes
data. Python 2.6+ is required.

BACKGROUND: I wrote FileChunkIO to upload huge files to Amazon S3 in
multiple parts without having to split them physically upfront (which
requires more time and twice the disk space) or creating in-memory
chunks as StringIO instances.

This package contains tests for %oname.

%prep
%setup -q -n %{oname}-%{version}

%if_with python3
cp -fR . ../python3
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
python %oname/tests.py  -v
%if_with python3
pushd ../python3
python3 %oname/tests.py  -v
popd
%endif

%files
%doc PKG-INFO
%python_sitelibdir/*
%exclude %python_sitelibdir/*/tests.*

%files tests
%python_sitelibdir/*/tests.*

%if_with python3
%files -n python3-module-%oname
%doc PKG-INFO
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests.*
%exclude %python3_sitelibdir/*/*/tests.*

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/tests.*
%python3_sitelibdir/*/*/tests.*
%endif

%changelog
* Tue Jan 17 2017 Igor Vlasenko <viy@altlinux.ru> 1.8-alt1
- automated PyPI update

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.6-alt1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 1.6-alt1.1
- NMU: Use buildreq for BR.

* Sat Jan 17 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.6-alt1
- Initial build for Sisyphus

