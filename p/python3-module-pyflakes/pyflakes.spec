%define _unpackaged_files_terminate_build 1
%define pypi_name pyflakes

Name: python3-module-%pypi_name
Version: 3.0.1
Release: alt1

Summary: A simple program which checks Python source files for errors
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/pyflakes/
BuildArch: noarch

# https://github.com/PyCQA/pyflakes.git
Source: %name-%version.tar
Patch0: %name-%version-alt.patch

BuildRequires(pre): rpm-build-python3

# build backend and its deps
BuildRequires: python3(setuptools)
BuildRequires: python3(wheel)

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
%pyproject_build

%install
%pyproject_install

mv %buildroot%_bindir/{pyflakes,pyflakes-py3}

# don't package tests
rm -r %buildroot%python3_sitelibdir/pyflakes/test

%check
%tox_check_pyproject

%files
%doc AUTHORS LICENSE README.rst
%_bindir/pyflakes-py3
%python3_sitelibdir/pyflakes/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Mon Feb 13 2023 Anton Zhukharev <ancieg@altlinux.org> 3.0.1-alt1
- 2.5.0 -> 3.0.1.

* Mon Aug 15 2022 Stanislav Levin <slev@altlinux.org> 2.5.0-alt1
- 2.4.0 -> 2.5.0.

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

