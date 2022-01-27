%define _unpackaged_files_terminate_build 1
%define oname pyflakes

%def_with check

Name: python3-module-%oname
Version: 2.4.0
Release: alt1

Summary: A simple program which checks Python source files for errors
License: MIT
Group: Development/Python3
Url: https://pypi.python.org/pypi/pyflakes
BuildArch: noarch

# https://github.com/PyCQA/pyflakes.git
Source: %name-%version.tar
Source1: pyflakes.1
Patch0: %name-%version-alt.patch

BuildRequires(pre): rpm-build-python3

%if_with check
BuildRequires: python3(tox)
%endif

Provides: python3-pyflakes = %EVR
Obsoletes: python3-pyflakes < %EVR


%description
Pyflakes is similar to PyChecker in scope, but differs in that it does\
not execute the modules to check them. This is both safer and faster,\
although it does not perform as many checks. Unlike PyLint, Pyflakes\
checks only for logical errors in programs; it does not perform any\
check on style.

%prep
%setup
%autopatch -p1

%build
%python3_build

%install
%python3_install

install -Dpm 644 %SOURCE1 %buildroot%_man1dir/python3-pyflakes.1

mv %buildroot%_bindir/{pyflakes,pyflakes-py3}

# don't package tests
rm -r %buildroot%python3_sitelibdir/pyflakes/test

%check
export PIP_NO_INDEX=YES
export TOXENV=py3
tox.py3 --sitepackages -vvr

%files
%doc AUTHORS LICENSE README.rst
%_man1dir/python3-pyflakes.1*
%_bindir/pyflakes-py3
%python3_sitelibdir/%oname/
%python3_sitelibdir/%oname-%version-py%_python3_version.egg-info/

%changelog
* Wed Jan 26 2022 Stanislav Levin <slev@altlinux.org> 2.4.0-alt1
- 2.3.1 -> 2.4.0.

* Mon Apr 19 2021 Grigory Ustinov <grenka@altlinux.org> 2.3.1-alt1
- 2.2.0 -> 2.3.1.

* Mon Oct 19 2020 Stanislav Levin <slev@altlinux.org> 2.2.0-alt1
- 2.1.1 -> 2.2.0.

* Thu Feb 20 2020 Andrey Bychkov <mrdrew@altlinux.org> 2.1.1-alt2
- Build for python2 disabled.

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

