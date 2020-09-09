%define _unpackaged_files_terminate_build 1
%define oname pyflakes

%def_without check

Name: python-module-%oname
Version: 2.1.1
Release: alt3

Summary: A simple program which checks Python source files for errors
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/pyflakes

BuildArch: noarch

# https://github.com/PyCQA/pyflakes.git
Source: %name-%version.tar
Source1: pyflakes.1

BuildRequires(pre): rpm-build-python
%if_with check
BuildRequires: python2.7(tox)
BuildRequires: python2.7(json)
%endif

Provides: pyflakes = %EVR
Obsoletes: pyflakes < %EVR


%description
Pyflakes is similar to PyChecker in scope, but differs in that it does\
not execute the modules to check them. This is both safer and faster,\
although it does not perform as many checks. Unlike PyLint, Pyflakes\
checks only for logical errors in programs; it does not perform any\
check on style.

%prep
%setup

%build
%python_build

%install
%python_install

install -Dpm 644 %SOURCE1 %buildroot%_man1dir/pyflakes.1

rm -r %buildroot%python_sitelibdir/pyflakes/test

%check
# we don't want flake8, because pyflakes is its dep
sed -i \
-e "/deps = flake8/d" \
-e "/flake8 pyflakes setup.py/d" \
tox.ini

export PIP_NO_INDEX=YES
export TOXENV=py%{python_version_nodots python}
tox --sitepackages -p auto -o -v

%files
%doc AUTHORS LICENSE README.rst
%_man1dir/pyflakes.1*
%_bindir/pyflakes
%python_sitelibdir/pyflakes/
%python_sitelibdir/pyflakes-*.egg-info/


%changelog
* Wed Sep 09 2020 Stanislav Levin <slev@altlinux.org> 2.1.1-alt3
- Disabled testing.

* Thu Feb 20 2020 Andrey Bychkov <mrdrew@altlinux.org> 2.1.1-alt2
- Rebuild with new setuptools
- python3 support removed (built separately).

* Fri Mar 22 2019 Stanislav Levin <slev@altlinux.org> 2.1.1-alt1
- 2.0.0 -> 2.1.1.

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

