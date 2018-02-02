%def_with python3

Name: nuitka
Version: 0.5.11
Release: alt1.git20150318.1.1
Summary: Python compiler with full language support and CPython compatibility
License: ASLv2.0
Group: Development/Python
Url: https://pypi.python.org/pypi/Nuitka/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# http://git.nuitka.net/Nuitka.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools gcc-c++
BuildPreReq: python-module-lxml
BuildPreReq: python-modules-json python-modules-logging
BuildPreReq: python-modules-multiprocessing
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python3-module-lxml
BuildPreReq: python-tools-2to3
%endif

%py_provides %name
%py_requires json logging multiprocessing lxml
%add_python_req_skip builtins

%description
Nuitka is **the** Python compiler. It is a seamless replacement or
extension to the Python interpreter and compiles **every** construct
that CPython 2.6, 2.7, 3.2, 3.3, and 3.4 have. It then executed
uncompiled code, and compiled code together in an extremely compatible
manner.

You can use all Python library modules or and all extension modules
freely. It translates the Python into a C level program that then uses
"libpython" to execute in the same way as CPython does. All optimization
is aimed at avoiding overhead, where it's unnecessary. None is aimed at
removing compatibility, although there is an "improved" mode, where not
every bug of standard Python is emulated, e.g. more complete error
messages are given.

%if_with python3
%package py3
Summary: Python compiler with full language support and CPython compatibility
Group: Development/Python3
%py3_provides %name
%py3_requires json logging multiprocessing lxml
%add_python3_req_skip exceptions md5

%description py3
Nuitka is **the** Python compiler. It is a seamless replacement or
extension to the Python interpreter and compiles **every** construct
that CPython 2.6, 2.7, 3.2, 3.3, and 3.4 have. It then executed
uncompiled code, and compiled code together in an extremely compatible
manner.

You can use all Python library modules or and all extension modules
freely. It translates the Python into a C level program that then uses
"libpython" to execute in the same way as CPython does. All optimization
is aimed at avoiding overhead, where it's unnecessary. None is aimed at
removing compatibility, although there is an "improved" mode, where not
every bug of standard Python is emulated, e.g. more complete error
messages are given.
%endif

%prep
%setup

%if_with python3
cp -fR . ../python3
#find ../python3 -type f -name '*.py' -exec 2to3 -w -n '{}' +
for i in $(find ../python3 -type f -name '*.py'); do
	2to3 -w -n $i ||:
done
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

%files
%doc *.rst
%_bindir/*
%if_with python3
%exclude %_bindir/*.py3
%endif
%python_sitelibdir/*

%if_with python3
%files py3
%doc *.rst
%_bindir/*.py3
%python3_sitelibdir/*
%endif

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.5.11-alt1.git20150318.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.5.11-alt1.git20150318.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Wed Mar 18 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5.11-alt1.git20150318
- Initial build for Sisyphus

