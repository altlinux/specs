%define _unpackaged_files_terminate_build 1
%define oname pluggy

%def_without check

Name: python-module-%oname
Version: 0.13.0
Release: alt3

Summary: Plugin and hook calling mechanisms for python
License: MIT
Group: Development/Python
# Source-git: https://github.com/pytest-dev/pluggy.git
Url: https://pypi.python.org/pypi/pluggy

BuildArch: noarch

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python
BuildRequires: python2.7(setuptools_scm)

%py_requires importlib_metadata

%if_with check
BuildRequires: python2.7(importlib_metadata)
BuildRequires: python2.7(pytest)
BuildRequires: python2.7(tox)
%endif


%description
This is the plugin manager as used by pytest but stripped of pytest
specific details.

%prep
%setup

# there is a file with name CHANGELOG.rst, not CHANGELOG
# a wrong reference leads to broken install via pip
sed -i '/^include CHANGELOG$/{s/$/.rst/}' MANIFEST.in

%build
# SETUPTOOLS_SCM_PRETEND_VERSION: when defined and not empty,
# its used as the primary source for the version number in which
# case it will be a unparsed string
export SETUPTOOLS_SCM_PRETEND_VERSION=%version

%python_build

%install
export SETUPTOOLS_SCM_PRETEND_VERSION=%version
%python_install

%check
export SETUPTOOLS_SCM_PRETEND_VERSION=%version
export PIP_NO_INDEX=YES
export TOXENV=py%{python_version_nodots python}
sed -i -e '/^\[testenv\]$/a whitelist_externals =\
    \/bin\/cp\
    \/bin\/sed\
commands_pre =\
    \/bin\/cp {env:_PYTEST_BIN:} \{envbindir\}\/pytest\
    \/bin\/sed -i \x271c #!\{envpython\}\x27 \{envbindir\}\/pytest' \
-e '/^setenv[ ]*=/a\
    py%{python_version_nodots python}: _PYTEST_BIN=%_bindir\/py.test' \
tox.ini
tox --sitepackages -p auto -o -v -r


%files
%doc LICENSE CHANGELOG.rst README.rst
%python_sitelibdir/pluggy/
%python_sitelibdir/pluggy-*.egg-info/


%changelog
* Wed Sep 09 2020 Stanislav Levin <slev@altlinux.org> 0.13.0-alt3
- Disabled testing.

* Thu Feb 20 2020 Andrey Bychkov <mrdrew@altlinux.org> 0.13.0-alt2
- python3 support removed (built separately).

* Wed Oct 16 2019 Stanislav Levin <slev@altlinux.org> 0.13.0-alt1
- 0.12.0 -> 0.13.0.

* Fri Aug 09 2019 Stanislav Levin <slev@altlinux.org> 0.12.0-alt2
- Fixed testing against Pytest 5.

* Thu Jun 06 2019 Stanislav Levin <slev@altlinux.org> 0.12.0-alt1
- 0.11.0 -> 0.12.0.

* Wed May 08 2019 Stanislav Levin <slev@altlinux.org> 0.11.0-alt1
- 0.9.0 -> 0.11.0.

* Sun Mar 17 2019 Stanislav Levin <slev@altlinux.org> 0.9.0-alt1
- 0.8.1 -> 0.9.0.

* Mon Jan 14 2019 Stanislav Levin <slev@altlinux.org> 0.8.1-alt1
- 0.8.0 -> 0.8.1.

* Sat Oct 20 2018 Stanislav Levin <slev@altlinux.org> 0.8.0-alt1
- 0.7.1 -> 0.8.0.

* Mon Aug 20 2018 Stanislav Levin <slev@altlinux.org> 0.7.1-alt1
- 0.6.0 -> 0.7.1.

* Tue Mar 20 2018 Stanislav Levin <slev@altlinux.org> 0.6.0-alt1
- 0.3.0 -> 0.6.0

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.3.0-alt1.git20150528.2.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Thu Jul 13 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.3.0-alt1.git20150528.2
- Fixed build spec with py.test3

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.3.0-alt1.git20150528.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Tue Jul 28 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.0-alt1.git20150528
- Initial build for Sisyphus

