%define oname protobuf3
Name: python3-module-%oname
Version: 0.3.0
Release: alt1.git20141113.1
Summary: Protocol buffers library for Python 3
License: MIT
Group: Development/Python3
Url: https://pypi.python.org/pypi/protobuf3/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/Pr0Ger/protobuf3.git
Source: %name-%version.tar
BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-enum34 protobuf-compiler
BuildPreReq: python-module-sphinx-devel
BuildPreReq: python-module-sphinx_rtd_theme

%py3_provides %oname
%py3_requires enum34

%description
Initial idea of this project was lack of support Python 3 in original
Protocol buffers implementation. Currently Google working on this, but
currently there is no easy way to use it with Python 3.

%prep
%setup

%prepare_sphinx .
ln -s ../objects.inv docs/

%build
%python3_build_debug

%install
%python3_install

%make -C docs html

%check
python3 setup.py test
py.test-%_python3_version

%files
%doc *.rst docs/_build/html
%_bindir/*
%python3_sitelibdir/*

%changelog
* Mon Mar 14 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.3.0-alt1.git20141113.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Nov 13 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.0-alt1.git20141113
- Initial build for Sisyphus

