%define _unpackaged_files_terminate_build 1
%define oname pytest-pylint

%def_with check

Name: python3-module-%oname
Version: 0.14.0
Release: alt4

Summary: pytest plugin to check source code with pylint
License: MIT
Group: Development/Python3
BuildArch: noarch
Url: https://pypi.org/project/pytest-pylint/

# https://github.com/carsongee/pytest-pylint.git
Source: %name-%version.tar
Patch: %name-%version-alt.patch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-pytest-runner

%if_with check
BuildRequires: pylint
BuildRequires: python3-module-coverage
BuildRequires: python3-module-mock
BuildRequires: python3-module-pylint
BuildRequires: python3-module-pytest
BuildRequires: python3-module-pytest-pep8
BuildRequires: python3-module-tox
%endif

%py3_provides %oname


%description
Run pylint with pytest and have configurable rule types (i.e.
Convention, Warn, and Error) fail the build. You can also specify a
pylintrc file.

%prep
%setup
%patch -p1

sed -i 's|#!/usr/bin/env python|#!/usr/bin/env python3|' \
    $(find ./ -name '*.py')

%build
%python3_build

%install
%python3_install

%check
sed -i '/^\[testenv\]$/a whitelist_externals =\
    \/bin\/cp\
    \/bin\/sed\
setenv =\
    py%{python_version_nodots python3}: _COV_BIN=%_bindir\/coverage3\
commands_pre =\
    \/bin\/cp {env:_COV_BIN:} \{envbindir\}\/coverage\
    \/bin\/sed -i \x271c #!\{envpython\}\x27 \{envbindir\}\/coverage' tox.ini
export PIP_NO_INDEX=YES
export TOXENV=py%{python_version_nodots python3}
tox.py3 --sitepackages -p auto -o -v

%files
%doc *.rst pylintrc
%python3_sitelibdir/pytest_pylint.py
%python3_sitelibdir/pytest_pylint-*.egg-info/
%python3_sitelibdir/__pycache__/


%changelog
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

