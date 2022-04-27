%define oname fs

%def_with check
%def_with docs

Name: python3-module-%oname
Version: 2.4.15
Release: alt1

Summary: Filesystem abstraction layer

License: MIT
Group: Development/Python3
Url: https://pypi.org/project/fs

BuildArch: noarch

# https://github.com/PyFilesystem/pyfilesystem2.git
Source: %name-%version.tar

# Fix tests due to girar environment
#
# girar uses non-default(1) hidepid mount option for /proc.
# Python psutil doesn't expect an inaccessibility of non-user
# components of /proc. The 'children' method recursively tries
# to get the parent pid for all the processes using /proc.
# Actually, ftp daemon has been stopped and then check for
# children processes and tcp connections is performed. For now,
# this assertion can be relaxed.
Patch: fs-2.4.11-alt-fix-tests-due-to-girar-environment.patch

BuildRequires(pre): rpm-build-python3
%if_with docs
BuildRequires(pre): rpm-macros-sphinx3
BuildRequires: python3-module-sphinx
BuildRequires: python3-module-sphinx_rtd_theme
BuildRequires: python3-module-recommonmark
%endif

%if_with check
BuildRequires: /proc
BuildRequires: python3-module-pytest
BuildRequires: python3-module-appdirs
BuildRequires: python3-module-pyftpdlib-tests
BuildRequires: python3-module-parameterized
%endif

%description
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

%if_with docs
%prepare_sphinx3 .
ln -s ../objects.inv docs/
%endif

%build
%python3_build

%if_with docs
export PYTHONPATH=%buildroot%python3_sitelibdir
%make SPHINXBUILD="sphinx-build-3" -C docs html
%make SPHINXBUILD="sphinx-build-3" -C docs man
%endif

%install
%python3_install

%if_with docs
mkdir -p %buildroot%_man1dir
cp -fr docs/build/man/*.1 %buildroot%_man1dir
%endif

%check
py.test3 -vv

%files
%doc LICENSE *.md
%python3_sitelibdir/fs/
%python3_sitelibdir/fs-*.egg-info/
%if_with docs
%_man1dir/*
%endif

%if_with docs
%files docs
%doc docs/build/html/*
%endif

%changelog
* Wed Apr 27 2022 Grigory Ustinov <grenka@altlinux.org> 2.4.15-alt1
- Automatically updated to 2.4.15.

* Thu Apr 01 2021 Grigory Ustinov <grenka@altlinux.org> 2.4.13-alt1
- Automatically updated to 2.4.13.

* Fri Mar 26 2021 Grigory Ustinov <grenka@altlinux.org> 2.4.12-alt1
- Automatically updated to 2.4.12.

* Tue Sep 08 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 2.4.11-alt2
- Removed backports.os dependency since it's not needed for python-3.

* Thu Feb 27 2020 Grigory Ustinov <grenka@altlinux.org> 2.4.11-alt1
- Build new version.
- Build without python2 support.
- Build with man page.
- Switch checking to pytest.

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

