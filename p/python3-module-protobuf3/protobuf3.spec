%define oname protobuf3
Name: python3-module-%oname
Epoch: 1
Version: 0.2.1
Release: alt1.1
Summary: Protocol buffers library for Python 3
License: MIT
Group: Development/Python3
Url: https://pypi.python.org/pypi/protobuf3/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/Pr0Ger/protobuf3.git
Source: %name-%version.tar
Patch1: %oname-%version-alt-docs.patch

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools
BuildRequires: python3-module-enum34 protobuf-compiler
BuildRequires: python-module-sphinx-devel
BuildRequires: python-module-sphinx_rtd_theme
BuildRequires: python3-module-pytest

%py3_provides %oname
%py3_requires enum34

%description
Initial idea of this project was lack of support Python 3 in original
Protocol buffers implementation. Currently Google working on this, but
currently there is no easy way to use it with Python 3.

%prep
%setup
%patch1 -p1

%prepare_sphinx .
ln -s ../objects.inv docs/

%build
%python3_build_debug

%install
%python3_install

%make -C docs html

%check
python3 setup.py test
py.test3

%files
%doc *.rst docs/_build/html
%_bindir/*
%python3_sitelibdir/*

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1:0.2.1-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Wed Aug 23 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 1:0.2.1-alt1
- Updated to upstream release version 0.2.1.

* Mon Mar 14 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.3.0-alt1.git20141113.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Nov 13 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.0-alt1.git20141113
- Initial build for Sisyphus

