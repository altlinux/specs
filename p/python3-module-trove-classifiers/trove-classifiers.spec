%define _unpackaged_files_terminate_build 1
%define pypi_name trove-classifiers

%def_with check

Name: python3-module-%pypi_name
Version: 2022.3.30
Release: alt1

Summary: Canonical source for classifiers on PyPI
License: Apache-2.0
Group: Development/Python3
# Source-git: https://github.com/pypa/trove-classifiers.git
Url: https://pypi.org/project/trove-classifiers

Source: %name-%version.tar
Patch: %name-%version-alt.patch

BuildRequires(pre): rpm-build-python3

%if_with check
BuildRequires: python3(pytest)
BuildRequires: python3(tox)
BuildRequires: python3(tox_console_scripts)
%endif

BuildArch: noarch

# PEP503 name
%py3_provides %pypi_name

%description
Canonical source for classifiers on PyPI:
https://pypi.org/classifiers/

Classifiers categorize projects per PEP 301. Use this package to validate
classifiers in packages for PyPI upload or download.

%prep
%setup
%autopatch -p1

# calver doesn't provide means for reproducible builds from source tree
echo '%version' > ./calver_version

%build
%python3_build

%install
%python3_install

%check
cat > tox.ini <<'EOF'
[testenv]
commands =
    # keep a synced steps to Makefile:test
    pytest
    python -m tests.lib
EOF
export PIP_NO_BUILD_ISOLATION=no
export PIP_NO_INDEX=YES
export TOXENV=py3
tox.py3 --sitepackages --console-scripts -vvr -s false --develop

%files
%doc README.md
%python3_sitelibdir/trove_classifiers/
%python3_sitelibdir/trove_classifiers-%version-py%_python3_version.egg-info/

%changelog
* Fri Apr 01 2022 Stanislav Levin <slev@altlinux.org> 2022.3.30-alt1
- Initial build for Sisyphus.
