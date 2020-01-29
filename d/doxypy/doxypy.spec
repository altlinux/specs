Name: doxypy
Version: 0.4.2
Release: alt2

Summary: doxypy is an input filter for Doxygen
License: GPLv2
Group: Development/Python3
Url: https://pypi.python.org/pypi/doxypy/
BuildArch: noarch

# https://github.com/0xCAFEBABE/doxypy.git
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-pytest python-tools-2to3


%description
doxypy is an input filter for Doxygen. It reformats python comments to
conform to doxygen documentation blocks. This makes it possible to use
the Doxygen/Javadoc syntax inside of docstrings when writing code
documentation and automatically generate API documentation out of it
instead of being forced to use non-python documentation blocks or to
document code redundantly.

%prep
%setup

find -type f -name '*.py' -exec 2to3 -w -n '{}' +

%build
pushd src
%python3_build_debug
popd

%install
pushd src
%python3_install
popd

%check
py.test3 test/src/test.py

%files
%doc README doc/*
%_bindir/*
%python3_sitelibdir/*


%changelog
* Wed Jan 29 2020 Andrey Bychkov <mrdrew@altlinux.org> 0.4.2-alt2
- Porting on Python3.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.4.2-alt1.git20100706.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Sat Nov 22 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.2-alt1.git20100706
- Initial build for Sisyphus

