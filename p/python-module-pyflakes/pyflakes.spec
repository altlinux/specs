%define _unpackaged_files_terminate_build 1
%define oname pyflakes

Name: python-module-%oname
Version: 2.0.0
Release: alt1

Summary: A simple program which checks Python source files for errors
License: MIT
Group: Development/Python

Url: https://pypi.python.org/pypi/pyflakes
# https://github.com/PyCQA/pyflakes.git
Source: %name-%version.tar
Source1: pyflakes.1

BuildArch: noarch
BuildRequires(pre): rpm-build-python3

Provides: pyflakes = %EVR
Obsoletes: pyflakes < %EVR

%description
Pyflakes is similar to PyChecker in scope, but differs in that it does\
not execute the modules to check them. This is both safer and faster,\
although it does not perform as many checks. Unlike PyLint, Pyflakes\
checks only for logical errors in programs; it does not perform any\
check on style.

%package -n python3-module-%oname
Summary: A simple program which checks Python source files for errors
Group: Development/Python3
Provides: python3-pyflakes = %EVR
Obsoletes: python3-pyflakes < %EVR

%description -n python3-module-%oname
Pyflakes is similar to PyChecker in scope, but differs in that it does\
not execute the modules to check them. This is both safer and faster,\
although it does not perform as many checks. Unlike PyLint, Pyflakes\
checks only for logical errors in programs; it does not perform any\
check on style.

%prep
%setup

rm -rf ../python3
cp -a . ../python3

%build
%python_build

pushd ../python3
%python3_build
popd

%install
pushd ../python3
install -Dpm 644 %SOURCE1 %buildroot%_man1dir/python3-pyflakes.1
%python3_install

mv %buildroot%_bindir/{pyflakes,python3-pyflakes}
# don't package tests
rm -rf %buildroot%python3_sitelibdir/pyflakes/test
popd

install -Dpm 644 %SOURCE1 %buildroot%_man1dir/pyflakes.1
%python_install
rm -rf %buildroot%python_sitelibdir/pyflakes/test

%check
python setup.py test

pushd ../python3
python3 setup.py test
popd

%files
%doc AUTHORS LICENSE README.rst
%_man1dir/pyflakes.1*
%_bindir/pyflakes
%python_sitelibdir/pyflakes/
%python_sitelibdir/pyflakes-*.egg-info/

%files -n python3-module-%oname
%doc AUTHORS LICENSE README.rst
%_man1dir/python3-pyflakes.1*
%_bindir/python3-pyflakes
%python3_sitelibdir/pyflakes/
%python3_sitelibdir/pyflakes-*.egg-info/

%changelog
* Sat Oct 27 2018 Stanislav Levin <slev@altlinux.org> 2.0.0-alt1
- 1.6.0 -> 2.0.0.

* Fri Dec 01 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 1.6.0-alt1
- Updated to upstream version 1.6.0.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.9.2-alt1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Fri Jul 31 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.2-alt1
- Version 0.9.2

* Fri Aug 01 2014 Lenar Shakirov <snejok@altlinux.ru> 0.8.1-alt1
- First build for ALT (based on Fedora 0.8.1-3.fc21.src)

