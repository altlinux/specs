%define oname fs

%def_with python3
%def_without docs

Name: python-module-%oname
Version: 0.5.2
Release: alt1.1.1
Summary: Filesystem abstraction layer
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/fs/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

#BuildPreReq: python-devel python-module-setuptools-tests
#BuildPreReq: python-module-wx python-module-dexml
#BuildPreReq: python-module-django python-module-paramiko
#BuildPreReq: python-module-boto
#BuildPreReq: python-module-sphinx-devel libfuse
#BuildPreReq: python-module-sphinxcontrib-spelling
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools-tests
#BuildPreReq: python3-module-dexml
#BuildPreReq: python3-module-django python3-module-paramiko
#BuildPreReq: python3-module-boto
%endif

%py_provides %oname

BuildRequires(pre): rpm-macros-sphinx
# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: python-base python-devel python-module-PyStemmer python-module-Pygments python-module-babel python-module-cffi python-module-cryptography python-module-cssselect python-module-docutils python-module-enum34 python-module-genshi python-module-jinja2 python-module-numpy python-module-psycopg2 python-module-pyasn1 python-module-pytest python-module-pytz python-module-setuptools python-module-snowballstemmer python-module-sphinx python-module-yaml python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-unittest python-modules-wsgiref python3 python3-base python3-module-chardet python3-module-psycopg2 python3-module-pytest python3-module-setuptools python3-module-yaml python3-module-yieldfrom.http.client python3-module-yieldfrom.urllib3
BuildRequires: python-module-chardet python-module-django python-module-ecdsa python-module-html5lib python-module-ndg-httpsclient python-module-ntlm python-module-pycrypto python-module-setuptools-tests python-module-sphinxcontrib-spelling python-module-wx python3-module-django python3-module-ecdsa python3-module-pycrypto python3-module-setuptools-tests python3-module-yieldfrom.requests rpm-build-python3

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

%if_with docs
%prepare_sphinx .
ln -s ../objects.inv docs/
%endif

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

%if_with docs
export PYTHONPATH=%buildroot%python_sitelibdir
%make -C docs pickle
%make -C docs html

cp -fR docs/_build/pickle %buildroot%python_sitelibdir/%oname/
%endif

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
%if_with docs
%exclude %python_sitelibdir/*/pickle
%endif

%if_with docs
%files pickles
%python_sitelibdir/*/pickle

%files docs
%doc docs/_build/html/*
%endif

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
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.5.2-alt1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.5.2-alt1.1
- NMU: Use buildreq for BR.

* Sun Aug 16 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5.2-alt1
- Version 0.5.2

* Mon Dec 22 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5.0-alt1
- Initial build for Sisyphus

