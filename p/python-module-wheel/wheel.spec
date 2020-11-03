%define oname wheel

Name: python-module-%oname
Version: 0.34.2
Release: alt2
Summary: A built-package format for Python
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/wheel/
Packager: Python Development Team <python@packages.altlinux.org>

# Source-url: https://bitbucket.org/pypa/wheel/get/%version.tar.gz
Source: %name-%version.tar
BuildArch: noarch
BuildRequires(pre): rpm-build-python
BuildRequires: python-module-keyring python-module-pyxdg python-module-setuptools
%py_provides %oname

%description
A wheel is a ZIP-format archive with a specially formatted filename and
the .whl extension. It is designed to contain all the files for a PEP
376 compatible install in a way that is very close to the on-disk
format. Many packages will be properly installed with only the "Unpack"
step (simply extracting the file onto sys.path), and the unpacked
archive preserves enough information to "Spread" (copy data and scripts
to their final locations) at any later time.

%prep
%setup

%build
%python_build

%install
%python_install
pushd %buildroot%_bindir
for i in $(ls); do
	mv $i $i.py2
done
popd

%check
%__python setup.py test

%files
%doc *.txt
%_bindir/*
%python_sitelibdir/*

%changelog
* Tue Nov 03 2020 Vitaly Lipatov <lav@altlinux.ru> 0.34.2-alt2
- NMU: drop unneeded pytest-cov buildrequires

* Sat Apr 11 2020 Alexey Shabalin <shaba@altlinux.org> 0.34.2-alt1
- 0.34.2
- build python2 module only

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.29.0-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Mon Jan 02 2017 Anton Midyukov <antohami@altlinux.org> 0.29.0-alt1
- New version 0.29.0

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.24.0-alt2.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Tue Feb 02 2016 Sergey Alembekov <rt@altlinux.ru> 0.24.0-alt2
- cleanup buildreq

* Fri Oct 17 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.24.0-alt1
- Initial build for Sisyphus
