%define _unpackaged_files_terminate_build 1
%define pypi_name autocommand

%def_with check

Name: python3-module-%pypi_name
Version: 2.2.1
Release: alt1

Summary: A library to create a command-line program from a function
License: LGPLv3
Group: Development/Python3
# Source-git: https://github.com/Lucretiel/autocommand.git
Url: https://pypi.org/project/autocommand

Source: %name-%version.tar
Patch0: %name-%version-alt.patch

BuildRequires(pre): rpm-build-python3

%if_with check
BuildRequires: python3(pytest)
BuildRequires: python3(tox)
BuildRequires: python3(tox_console_scripts)
%endif

BuildArch: noarch

%description
A library to automatically generate and run simple argparse parsers from
function signatures.

%prep
%setup
%autopatch -p1

%build
%python3_build

%install
%python3_install

%check
cat > tox.ini <<'EOF'
[testenv]
usedevelop=True
commands =
    {envbindir}/pytest {posargs:-vra}
EOF
export PIP_NO_BUILD_ISOLATION=no
export PIP_NO_INDEX=YES
export TOXENV=py3
tox.py3 --sitepackages --console-scripts -vvr -s false

%files
%doc README.rst
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/%pypi_name-%version-py%_python3_version.egg-info/

%changelog
* Tue Feb 08 2022 Stanislav Levin <slev@altlinux.org> 2.2.1-alt1
- Initial build for Sisyphus.
