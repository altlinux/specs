%define oname fs

%def_with python3
%def_without docs

Name: python-module-%oname
Version: 2.0.17
Release: alt1
Summary: Filesystem abstraction layer
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/fs/

BuildArch: noarch

# https://github.com/PyFilesystem/pyfilesystem2.git
Source: %name-%version.tar
Patch1: fs-alt-tests.patch

BuildRequires(pre): rpm-macros-sphinx
BuildRequires: python-module-chardet python-module-django python-module-ecdsa python-module-html5lib
BuildRequires: python-module-ndg-httpsclient python-module-ntlm python-module-pycrypto python-module-setuptools-tests
BuildRequires: python-module-sphinxcontrib-spelling python-module-wx python-module-nose python-module-mock
BuildRequires: python-module-appdirs python-module-pyftpdlib-tests python2.7(pytz)
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-django python3-module-ecdsa python3-module-pycrypto python3-module-setuptools-tests
BuildRequires: python3-module-nose python3-module-mock
BuildRequires: python3-module-appdirs python3-module-pyftpdlib-tests python3(pytz)
%endif

%py_provides %oname

%description
PyFilesystem is an abstraction layer for filesystems. In the same way
that Python's file-like objects provide a common way of accessing files,
PyFilesystem provides a common way of accessing entire filesystems. You
can write platform-independent code to work with local files, that also
works with any of the supported filesystems (zip, ftp, S3 etc.).

%if_with python3
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
%endif

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
%patch1 -p1

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
%endif

%python_install

%if_with docs
export PYTHONPATH=%buildroot%python_sitelibdir
%make -C docs pickle
%make -C docs html

cp -fR docs/_build/pickle %buildroot%python_sitelibdir/%oname/
%endif

%check
LC_ALL=en_US.UTF-8 python setup.py test
%if_with python3
pushd ../python3
LC_ALL=en_US.UTF-8 python3 setup.py test
popd
%endif

%files
%doc LICENSE README.rst readme.md
%python_sitelibdir/*
%if_with docs
%exclude %python_sitelibdir/*/pickle
%endif

%if_with docs
%files pickles
%python_sitelibdir/*/pickle

%files docs
%doc docs/_build/html/*
%endif

%if_with python3
%files -n python3-module-%oname
%doc LICENSE README.rst readme.md
%python3_sitelibdir/*
%endif

%changelog
* Fri Jan 12 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 2.0.17-alt1
- Updated to upstream release 2.0.17.

* Thu Nov 02 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 2.0.13-alt1
- Updated to upstream release 2.0.13.

* Thu Aug 03 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 2.0.5-alt1
- Updated to upstream release 2.0.5

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.5.2-alt1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.5.2-alt1.1
- NMU: Use buildreq for BR.

* Sun Aug 16 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5.2-alt1
- Version 0.5.2

* Mon Dec 22 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5.0-alt1
- Initial build for Sisyphus

