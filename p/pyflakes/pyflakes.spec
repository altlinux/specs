%define _unpackaged_files_terminate_build 1

%def_with python3

Name:           pyflakes
Version:        1.6.0
Release:        alt1
Summary:        A simple program which checks Python source files for errors

Group:          Development/Python
License:        MIT
BuildArch:      noarch
URL:            https://pypi.python.org/pypi/pyflakes

# https://github.com/PyCQA/pyflakes.git
Source: %name-%version.tar
Source1: pyflakes.1

BuildRequires: python-module-setuptools
BuildRequires: rpm-build-python3
BuildRequires: python3-module-setuptools

Requires: python-module-setuptools

%description
Pyflakes is similar to PyChecker in scope, but differs in that it does\
not execute the modules to check them. This is both safer and faster,\
although it does not perform as many checks. Unlike PyLint, Pyflakes\
checks only for logical errors in programs; it does not perform any\
check on style.

%if_with python3
%package -n python3-%name
Summary: A simple program which checks Python source files for errors
Group: Development/Python3
Requires: python3-module-setuptools

%description -n python3-%name
Pyflakes is similar to PyChecker in scope, but differs in that it does\
not execute the modules to check them. This is both safer and faster,\
although it does not perform as many checks. Unlike PyLint, Pyflakes\
checks only for logical errors in programs; it does not perform any\
check on style.
%endif

%prep
%setup

%if_with python3
cp -a . ../python3
%endif

%build
%python_build

%if_with python3
pushd ../python3
%python3_build
popd
%endif

%install
%if_with python3
pushd ../python3
install -Dpm 644 %SOURCE1 %buildroot%_man1dir/python3-pyflakes.1
%python3_install
popd
pushd %buildroot%_bindir
for i in $(ls); do
	mv $i python3-$i
done
popd
%endif

install -Dpm 644 %SOURCE1 %buildroot%_man1dir/pyflakes.1
%python_install

%check
python setup.py test
%if_with python3
pushd ../python3
python3 setup.py test
popd
%endif

%files
%doc AUTHORS LICENSE NEWS.txt README.rst
%_bindir/*
%if_with python3
%exclude %_bindir/python3-*
%endif
%python_sitelibdir/pyflakes*
%exclude %python_sitelibdir/pyflakes/test/
%_man1dir/pyflakes.1*

%if_with python3
%files -n python3-%name
%doc AUTHORS LICENSE NEWS.txt README.rst
%_bindir/python3-*
%python3_sitelibdir/pyflakes*
%exclude %python3_sitelibdir/pyflakes/test/
%_man1dir/python3-pyflakes.1*
%endif

%changelog
* Fri Dec 01 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 1.6.0-alt1
- Updated to upstream version 1.6.0.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.9.2-alt1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Fri Jul 31 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.2-alt1
- Version 0.9.2

* Fri Aug 01 2014 Lenar Shakirov <snejok@altlinux.ru> 0.8.1-alt1
- First build for ALT (based on Fedora 0.8.1-3.fc21.src)

