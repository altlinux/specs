%define _unpackaged_files_terminate_build 1

%define oname fs

%def_with check
%def_with docs

Name: python-module-%oname
Version: 2.2.1
Release: alt1
Summary: Filesystem abstraction layer
License: MIT
Group: Development/Python
Url: https://pypi.org/project/fs/

BuildArch: noarch

# https://github.com/PyFilesystem/pyfilesystem2.git
Source: %name-%version.tar
Patch: fs-2.2.1-alt-fix-tests-due-to-girar-environment.patch

BuildRequires(pre): rpm-build-python3
%if_with docs
BuildRequires(pre): rpm-macros-sphinx
BuildRequires: python-module-sphinx_rtd_theme
BuildRequires: python-module-objects.inv
%endif

%if_with check
BuildRequires: /proc
BuildRequires: python-module-appdirs
BuildRequires: python-module-backports.os
BuildRequires: python-module-coverage
BuildRequires: python-module-mock
BuildRequires: python-module-nose
BuildRequires: python-module-pyftpdlib-tests
BuildRequires: python-module-tox
BuildRequires: python3-module-appdirs
BuildRequires: python3-module-coverage
BuildRequires: python3-module-mock
BuildRequires: python3-module-nose
BuildRequires: python3-module-pyftpdlib-tests
BuildRequires: python3-module-pysendfile
BuildRequires: python3-module-tox
%endif

%py_requires backports.os

%description
PyFilesystem is an abstraction layer for filesystems. In the same way
that Python's file-like objects provide a common way of accessing files,
PyFilesystem provides a common way of accessing entire filesystems. You
can write platform-independent code to work with local files, that also
works with any of the supported filesystems (zip, ftp, S3 etc.).

%package -n python3-module-%oname
Summary: Filesystem abstraction layer
Group: Development/Python3

%description -n python3-module-%oname
PyFilesystem is an abstraction layer for filesystems. In the same way
that Python's file-like objects provide a common way of accessing files,
PyFilesystem provides a common way of accessing entire filesystems. You
can write platform-independent code to work with local files, that also
works with any of the supported filesystems (zip, ftp, S3 etc.).

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
%patch -p1

rm -rf ../python3
cp -fR . ../python3
# no need for python3
grep -qs '^[[:space:]]*backports\.os[[:space:]]*$' ../python3/tox.ini || exit 1
sed -i '/backports\.os/d' ../python3/tox.ini

grep -qs '^[[:space:]]*enum34[[:space:]]*$' ../python3/tox.ini || exit 1
sed -i '/enum34/d' ../python3/tox.ini

%if_with docs
%prepare_sphinx .
ln -s ../objects.inv docs/
%endif

%build
%python_build

pushd ../python3
%python3_build
popd

%install
pushd ../python3
%python3_install
popd

%python_install

%if_with docs
export PYTHONPATH=%buildroot%python_sitelibdir
%make -C docs pickle
%make -C docs html

cp -fR docs/build/pickle %buildroot%python_sitelibdir/%oname/
%endif

%check
#LC_ALL=en_US.UTF-8 python setup.py test
export PIP_INDEX_URL=http://host.invalid./
export LC_ALL=C.UTF-8
export TOX_TESTENV_PASSENV='LC_ALL'
# prepare
%_bindir/tox --sitepackages -e py%{python_version_nodots python} --notest
cp -f %_bindir/nosetests .tox/py%{python_version_nodots python}/bin/
sed -i "1c #!$(pwd)/.tox/py%{python_version_nodots python}/bin/python" \
.tox/py%{python_version_nodots python}/bin/nosetests

%_bindir/tox --sitepackages -e py%{python_version_nodots python} -v -- -v

pushd ../python3
# prepare
%_bindir/tox.py3 --sitepackages -e py%{python_version_nodots python3} --notest
cp -f %_bindir/nosetests3 .tox/py%{python_version_nodots python3}/bin/nosetests
sed -i "1c #!$(pwd)/.tox/py%{python_version_nodots python3}/bin/python3" \
.tox/py%{python_version_nodots python3}/bin/nosetests

%_bindir/tox.py3 --sitepackages -e py%{python_version_nodots python3} -v -- -v
popd

%files
%doc LICENSE *.md
%python_sitelibdir/fs/
%python_sitelibdir/fs-*.egg-info/
%if_with docs
%exclude %python_sitelibdir/*/pickle
%endif

%if_with docs
%files pickles
%python_sitelibdir/*/pickle

%files docs
%doc docs/build/html/*
%endif

%files -n python3-module-%oname
%doc LICENSE *.md
%python3_sitelibdir/fs/
%python3_sitelibdir/fs-*.egg-info/

%changelog
* Sat Jan 12 2019 Stanislav Levin <slev@altlinux.org> 2.2.1-alt1
- 2.1.0 -> 2.2.1.
- Fixed build.

* Mon Sep 10 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 2.1.0-alt1
- Updated to upstream version 2.1.0.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 2.0.17-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

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

