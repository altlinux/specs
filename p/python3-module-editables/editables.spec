%define _unpackaged_files_terminate_build 1
%define pypi_name editables

%def_with check

Name: python3-module-%pypi_name
Version: 0.2
Release: alt1

Summary: Editable installations
License: MIT
Group: Development/Python3
# Source-git: https://github.com/pfmoore/editables.git
Url: https://pypi.org/project/editables

Source: %name-%version.tar
Patch: %name-%version-alt.patch

BuildRequires(pre): rpm-build-python3

%if_with check
BuildRequires: python3(pytest)
BuildRequires: python3(tox)
BuildRequires: python3(tox_console_scripts)
%endif

BuildArch: noarch

%description
A Python library for creating "editable wheels".
This library supports the building of wheels which, when installed, will expose
packages in a local directory on sys.path in "editable mode". In other words,
changes to the package source will be reflected in the package visible to
Python, without needing a reinstall.

%prep
%setup
%autopatch -p1

%build
%python3_build

%install
%python3_install

%check
# override upstream's tox configuration (requires too many fixes)
cat > tox.ini <<'EOF'
[testenv]
commands =
    {envbindir}/pytest -vra {posargs:tests}
EOF
export PIP_NO_BUILD_ISOLATION=no
export PIP_NO_INDEX=YES
export TOXENV=py3
tox.py3 --sitepackages --console-scripts -vvr --develop

%files
%doc README.md
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/%pypi_name-%version-py%_python3_version.egg-info/

%changelog
* Mon Apr 04 2022 Stanislav Levin <slev@altlinux.org> 0.2-alt1
- Initial build for Sisyphus.
