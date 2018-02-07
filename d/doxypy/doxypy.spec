Name: doxypy
Version: 0.4.2
Release: alt1.git20100706.1
Summary: doxypy is an input filter for Doxygen
License: GPLv2
Group: Development/Python
Url: https://pypi.python.org/pypi/doxypy/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/0xCAFEBABE/doxypy.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-module-setuptools
BuildRequires: python-module-pytest

%description
doxypy is an input filter for Doxygen. It reformats python comments to
conform to doxygen documentation blocks. This makes it possible to use
the Doxygen/Javadoc syntax inside of docstrings when writing code
documentation and automatically generate API documentation out of it
instead of being forced to use non-python documentation blocks or to
document code redundantly.

%prep
%setup

%build
pushd src
%python_build_debug
popd

%install
pushd src
%python_install
popd

%check
py.test test/src/test.py

%files
%doc README doc/*
%_bindir/*
%python_sitelibdir/*

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.4.2-alt1.git20100706.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Sat Nov 22 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.2-alt1.git20100706
- Initial build for Sisyphus

