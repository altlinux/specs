%define _unpackaged_files_terminate_build 1
%define oname pluggy

%def_with check

Name: python3-module-%oname
Version: 1.0.0
Release: alt1

Summary: Plugin and hook calling mechanisms for python
License: MIT
Group: Development/Python3
# Source-git: https://github.com/pytest-dev/pluggy.git
Url: https://pypi.python.org/pypi/pluggy

BuildArch: noarch

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3(setuptools_scm)

%if_with check
BuildRequires: python3(tox)
BuildRequires: python3(tox_no_deps)
BuildRequires: python3(tox_console_scripts)
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

%python3_build

%install
export SETUPTOOLS_SCM_PRETEND_VERSION=%version
%python3_install

%check
export SETUPTOOLS_SCM_PRETEND_VERSION=%version
export PIP_NO_BUILD_ISOLATION=no
export PIP_NO_INDEX=YES
export TOXENV=py3
tox.py3 --sitepackages --no-deps --console-scripts -vvr -s false

%files
%doc LICENSE CHANGELOG.rst README.rst
%python3_sitelibdir/pluggy/
%python3_sitelibdir/pluggy-%version-py%_python3_version.egg-info/

%changelog
* Wed Sep 08 2021 Stanislav Levin <slev@altlinux.org> 1.0.0-alt1
- 0.13.1 -> 1.0.0.

* Sun May 03 2020 Stanislav Levin <slev@altlinux.org> 0.13.1-alt2
- Dropped BR on importlib_metadata.

* Mon Apr 20 2020 Stanislav Levin <slev@altlinux.org> 0.13.1-alt1
- 0.13.0 -> 0.13.1.

* Thu Feb 20 2020 Andrey Bychkov <mrdrew@altlinux.org> 0.13.0-alt2
- Build for python2 disabled.

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

