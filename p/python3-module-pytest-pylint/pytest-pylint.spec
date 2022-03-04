%define _unpackaged_files_terminate_build 1
%define oname pytest-pylint

%def_with check

Name: python3-module-%oname
Version: 0.18.0
Release: alt3

Summary: pytest plugin to check source code with pylint
License: MIT
Group: Development/Python3
BuildArch: noarch
Url: https://pypi.org/project/pytest-pylint/

# https://github.com/carsongee/pytest-pylint.git
Source: %name-%version.tar
Patch: %name-%version-alt.patch

BuildRequires(pre): rpm-build-python3

%if_with check
BuildRequires: python3(pylint)
BuildRequires: python3(pytest)
BuildRequires: python3(pytest_flake8)
BuildRequires: python3(tox)
%endif

%py3_provides %oname


%description
Run pylint with pytest and have configurable rule types (i.e.
Convention, Warn, and Error) fail the build. You can also specify a
pylintrc file.

%prep
%setup
%patch -p1

%build
%python3_build

%install
%python3_install

%check
export PIP_NO_INDEX=YES
export TOXENV=py%{python_version_nodots python3}
tox.py3 --sitepackages -vvr

%files
%doc *.rst
%python3_sitelibdir/pytest_pylint/
%python3_sitelibdir/pytest_pylint-%version-py%_python3_version.egg-info/

%changelog
* Fri Mar 04 2022 Stanislav Levin <slev@altlinux.org> 0.18.0-alt3
- Fixed FTBFS (Pytest 7).

* Thu Feb 10 2022 Stanislav Levin <slev@altlinux.org> 0.18.0-alt2
- Fixed FTBFS (Pylint 2.12.2).

* Sun Apr 18 2021 Stanislav Levin <slev@altlinux.org> 0.18.0-alt1
- 0.17.0 -> 0.18.0.

* Wed Aug 05 2020 Stanislav Levin <slev@altlinux.org> 0.17.0-alt2
- Fixed FTBFS(new pytest 6.0.1).

* Tue Aug 04 2020 Stanislav Levin <slev@altlinux.org> 0.17.0-alt1
- 0.14.0 -> 0.17.0.

* Tue Nov 26 2019 Andrey Bychkov <mrdrew@altlinux.org> 0.14.0-alt4
- python2 disabled

* Sat Oct 19 2019 Stanislav Levin <slev@altlinux.org> 0.14.0-alt3
- Fixed testing against Pylint 2.4.2+.

* Thu Aug 22 2019 Stanislav Levin <slev@altlinux.org> 0.14.0-alt2
- Fixed testing against Pytest 5.1.

* Thu Jan 17 2019 Stanislav Levin <slev@altlinux.org> 0.14.0-alt1
- 0.12.3 -> 0.14.0.

* Mon Oct 15 2018 Stanislav Levin <slev@altlinux.org> 0.12.3-alt2
- Fixed tests with new pytest-3.8.

* Mon Sep 03 2018 Stanislav Levin <slev@altlinux.org> 0.12.3-alt1
- 0.7.1 -> 0.12.3.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.7.1-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Fri Nov 03 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.7.1-alt1
- Updated to upstream version 0.7.1.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.1.0-alt1.git20150423.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Fri Apr 24 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.0-alt1.git20150423
- Initial build for Sisyphus

