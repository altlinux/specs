%define oname slugify

Name: python-module-%oname
Version: 0.1.0
Release: alt1.git20141016.1.2
Summary: Returns a unicode slugs
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/python-slugify/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/un33k/python-slugify.git
Source: %name-%version.tar
BuildArch: noarch

%py_provides %oname

# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: python-base python-devel python-module-setuptools python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-hotshot python-modules-logging python-modules-multiprocessing python-modules-unittest python-modules-xml python-tools-2to3 python3 python3-base python3-module-pytest python3-module-setuptools xz
BuildRequires: python-module-nose python-module-pytest python-module-unidecode python-tools-pep8 python3-module-nose python3-module-unidecode python3-tools-pep8 rpm-build-python3 time

%description
A Python Slugify application that handles Unicode.

%prep
%setup

%build
%python_build_debug

%install
%python_install

%check
nosetests
./pep8.sh

%files
%doc *.md
%_bindir/*
%python_sitelibdir/*

%changelog
* Thu Feb 08 2018 Mikhail Gordeev <obirvalger@altlinux.org> 0.1.0-alt1.git20141016.1.2
- Split to two packages (for python and python3)

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.1.0-alt1.git20141016.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.1.0-alt1.git20141016.1
- NMU: Use buildreq for BR.

* Thu Oct 30 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.0-alt1.git20141016
- Initial build for Sisyphus

