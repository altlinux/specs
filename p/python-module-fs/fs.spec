%define oname fs

%def_with python3

Name: python-module-%oname
Version: 0.5.0
Release: alt1
Summary: Filesystem abstraction layer
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/fs/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-wx python-module-dexml
BuildPreReq: python-module-django python-module-paramiko
BuildPreReq: python-module-boto
BuildPreReq: python-module-sphinx-devel libfuse
BuildPreReq: python-module-sphinxcontrib-spelling
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-dexml
BuildPreReq: python3-module-django python3-module-paramiko
BuildPreReq: python3-module-boto
%endif

%py_provides %oname

%description
PyFilesystem is an abstraction layer for filesystems. In the same way
that Python's file-like objects provide a common way of accessing files,
PyFilesystem provides a common way of accessing entire filesystems. You
can write platform-independent code to work with local files, that also
works with any of the supported filesystems (zip, ftp, S3 etc.).

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
PyFilesystem is an abstraction layer for filesystems. In the same way
that Python's file-like objects provide a common way of accessing files,
PyFilesystem provides a common way of accessing entire filesystems. You
can write platform-independent code to work with local files, that also
works with any of the supported filesystems (zip, ftp, S3 etc.).

This package contains tests for %oname.

%package -n python3-module-%oname
Summary: Filesystem abstraction layer
Group: Development/Python3
%py3_provides %oname
%add_python3_req_skip wx libarchive

%description -n python3-module-%oname
PyFilesystem is an abstraction layer for filesystems. In the same way
that Python's file-like objects provide a common way of accessing files,
PyFilesystem provides a common way of accessing entire filesystems. You
can write platform-independent code to work with local files, that also
works with any of the supported filesystems (zip, ftp, S3 etc.).

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
PyFilesystem is an abstraction layer for filesystems. In the same way
that Python's file-like objects provide a common way of accessing files,
PyFilesystem provides a common way of accessing entire filesystems. You
can write platform-independent code to work with local files, that also
works with any of the supported filesystems (zip, ftp, S3 etc.).

This package contains tests for %oname.

%package pickles
Summary: Pickles for %oname
Group: Development/Python

%description pickles
PyFilesystem is an abstraction layer for filesystems. In the same way
that Python's file-like objects provide a common way of accessing files,
PyFilesystem provides a common way of accessing entire filesystems. You
can write platform-independent code to work with local files, that also
works with any of the supported filesystems (zip, ftp, S3 etc.).

This package contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
PyFilesystem is an abstraction layer for filesystems. In the same way
that Python's file-like objects provide a common way of accessing files,
PyFilesystem provides a common way of accessing entire filesystems. You
can write platform-independent code to work with local files, that also
works with any of the supported filesystems (zip, ftp, S3 etc.).

This package contains documentation for %oname.

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

%prepare_sphinx .
ln -s ../objects.inv docs/

%build
%python_build_debug

%if_with python3
pushd ../python3
%python3_build_debug
popd
%endif

%install
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

export PYTHONPATH=%buildroot%python_sitelibdir
%make -C docs pickle
%make -C docs html

cp -fR docs/_build/pickle %buildroot%python_sitelibdir/%oname/

%check
python setup.py test
%if_with python3
pushd ../python3
python3 setup.py test
popd
%endif

%files
%doc AUTHORS *.txt
%_bindir/*
%if_with python3
%exclude %_bindir/*.py3
%endif
%python_sitelibdir/*
%exclude %python_sitelibdir/*/tests
%exclude %python_sitelibdir/*/*/*/test*
%exclude %python_sitelibdir/*/pickle

%files pickles
%python_sitelibdir/*/pickle

%files docs
%doc docs/_build/html/*

%files tests
%python_sitelibdir/*/tests
%python_sitelibdir/*/*/*/test*

%if_with python3
%files -n python3-module-%oname
%doc AUTHORS *.txt
%python3_sitelibdir/*
%_bindir/*.py3
%exclude %python3_sitelibdir/*/tests
%exclude %python3_sitelibdir/*/*/*/test*
%exclude %python3_sitelibdir/*/*/*/*/test*

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/tests
%python3_sitelibdir/*/*/*/test*
%python3_sitelibdir/*/*/*/*/test*
%endif

%changelog
* Mon Dec 22 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5.0-alt1
- Initial build for Sisyphus

